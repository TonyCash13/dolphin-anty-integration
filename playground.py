#!/usr/bin/env python3
"""
Interactive OpenAPI Playground

Features:
- Loads OpenAPI from local `openapi_temp.json` (if present) or fetches it from known Dolphin URLs
- Lets you input an endpoint path (e.g. /browser_profiles) and choose HTTP method
- Finds requestBody schema (application/json) or parameters and builds an example payload
- Generates a ready-to-run Python `requests` snippet
- Automatically saves generated snippet to `generated/{method}_{sanitized_path}.py`

Usage:
    python playground.py

No dependencies beyond `pyyaml` and `requests` (requests used only when fetching schema).
"""

from __future__ import annotations
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

try:
    import requests
    import yaml
except Exception as e:
    print("Please install dependencies: pip install requests pyyaml")
    raise

# Candidate URLs (same as generator)
CANDIDATE_URLS = [
    "https://docs.dolphin-anty-cdn.com/openapi.yaml"
]
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; OpenAPI-Playground/1.0)"}
LOCAL_JSON = "openapi_temp.json"
GENERATED_DIR = "generated"


def log(msg: str) -> None:
    print(msg)


def load_openapi() -> Dict[str, Any]:
    """Try local JSON first, then try to fetch and parse YAML from candidate URLs."""
    # 1) local file
    if os.path.exists(LOCAL_JSON):
        log(f"🔁 Загружаю OpenAPI из локального файла: {LOCAL_JSON}")
        with open(LOCAL_JSON, "r", encoding="utf-8") as f:
            return json.load(f)

    # 2) try to fetch YAML from candidate URLs
    last_err = None
    for url in CANDIDATE_URLS:
        log(f"📥 Пытаюсь скачать OpenAPI с {url} ...")
        try:
            r = requests.get(url, timeout=20, headers=HEADERS)
        except Exception as e:
            last_err = e
            log(f"⚠️ Ошибка сети: {e}")
            continue

        if r.status_code != 200:
            last_err = f"HTTP {r.status_code}"
            log(f"⚠️ Не 200: {r.status_code}")
            continue

        text = r.text
        # avoid HTML
        if re.search(r"<\/?html|<!doctype", text[:200], re.I):
            last_err = "Получен HTML"
            log("⚠️ Получен HTML, пропускаю")
            continue

        try:
            data = yaml.safe_load(text)
            if not isinstance(data, dict):
                last_err = "YAML распарсен, но не dict"
                log("⚠️ YAML не является объектом")
                continue
            # save local copy
            with open(LOCAL_JSON, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log("✅ OpenAPI загружен и сохранён локально")
            return data
        except Exception as e:
            last_err = e
            log(f"⚠️ Ошибка парсинга YAML: {e}")
            continue

    log("❌ Не удалось получить OpenAPI. Последняя ошибка: %s" % str(last_err))
    sys.exit(1)


# --- Простая развёртка $ref внутри components ---

def resolve_ref(ref: str, root: Dict[str, Any]) -> Dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Внешние $ref не поддерживаются: {ref}")
    parts = ref.lstrip("#/").split("/")
    node = root
    for p in parts:
        if p not in node:
            raise KeyError(f"$ref не найден: {ref}")
        node = node[p]
    if not isinstance(node, dict):
        return {}
    return node.copy()


def dereference(schema: Any, root: Dict[str, Any]) -> Any:
    """Recursive dereference minimal support for $ref / allOf / oneOf / anyOf"""
    if isinstance(schema, dict):
        if "$ref" in schema:
            return dereference(resolve_ref(schema["$ref"], root), root)
        if "allOf" in schema:
            merged = {}
            for part in schema["allOf"]:
                pr = dereference(part, root)
                if isinstance(pr, dict):
                    # shallow merge
                    merged_props = merged.get("properties", {})
                    merged_props.update(pr.get("properties", {}))
                    merged["properties"] = merged_props
                    if "required" in pr:
                        merged_required = set(merged.get("required", [])) | set(pr.get("required", []))
                        merged["required"] = list(merged_required)
            return merged
        if "oneOf" in schema or "anyOf" in schema:
            key = "oneOf" if "oneOf" in schema else "anyOf"
            return {key: [dereference(p, root) for p in schema[key]]}
        out = {}
        for k, v in schema.items():
            if k == "properties":
                out[k] = {pn: dereference(ps, root) for pn, ps in v.items()}
            elif k == "items":
                out[k] = dereference(v, root)
            else:
                out[k] = dereference(v, root)
        return out
    elif isinstance(schema, list):
        return [dereference(x, root) for x in schema]
    else:
        return schema


# --- Helpers to generate example payload ---

def example_value_for_schema(s: Any, root: Dict[str, Any]) -> Any:
    if not isinstance(s, dict):
        return None
    s = dereference(s, root)
    if "oneOf" in s or "anyOf" in s:
        key = "oneOf" if "oneOf" in s else "anyOf"
        variants = s[key]
        # choose first variant
        return example_value_for_schema(variants[0], root)
    t = s.get("type")
    if t == "string":
        ex = s.get("example")
        if ex is not None:
            return ex
        enum = s.get("enum")
        if enum:
            return enum[0]
        fmt = s.get("format")
        if fmt == "date-time":
            return "2025-01-01T00:00:00Z"
        return ""
    if t == "integer":
        return s.get("example", 0)
    if t == "number":
        return s.get("example", 0.0)
    if t == "boolean":
        return s.get("example", False)
    if t == "array":
        items = s.get("items", {})
        return [example_value_for_schema(items, root)]
    if t == "object":
        props = s.get("properties", {})
        obj = {}
        for pn, ps in props.items():
            obj[pn] = example_value_for_schema(ps, root)
        return obj
    # fallback
    return None


def sanitize_filename(s: str) -> str:
    s = s.strip("/\n ")
    s = s.replace("/", "_")
    s = re.sub(r"[^0-9A-Za-z_\-]", "_", s)
    if not s:
        return "root"
    return s


def find_path_item(openapi: Dict[str, Any], user_path: str) -> Optional[Dict[str, Any]]:
    """Find best matching path (exact or templated). Returns tuple (path_template, path_item)"""
    paths = openapi.get("paths", {})
    # exact match
    if user_path in paths:
        return user_path, paths[user_path]
    # try to match templated paths (like /profiles/{id})
    for template, item in paths.items():
        # convert template to regex
        pattern = "^" + re.sub(r"\{[^/]+\}", "[^/]+", template) + "$"
        if re.match(pattern, user_path):
            return template, item
    return None


def build_python_snippet(base_url: str, path_template: str, method: str, openapi: Dict[str, Any]) -> str:
    method_item = openapi.get("paths", {}).get(path_template, {}).get(method.lower())
    if not method_item:
        return "# Метод не найден в OpenAPI"

    # determine full url
    servers = openapi.get("servers", [])
    if servers and isinstance(servers, list):
        server_url = servers[0].get("url", "")
    else:
        server_url = base_url or "https://dolphin-anty-api.com"

    url = server_url.rstrip("/") + path_template

    # request body
    rb = method_item.get("requestBody") or {}
    content = rb.get("content", {})
    schema = None
    if "application/json" in content:
        schema = content["application/json"].get("schema")
    elif content:
        # pick first content type
        first = next(iter(content.values()))
        schema = first.get("schema")

    payload_example = None
    typedict_name = None
    if schema:
        # if $ref to components -> prefer referencing TypedDict
        if isinstance(schema, dict) and "$ref" in schema:
            ref_name = schema["$ref"].split("/")[-1]
            typedict_name = ref_name
        payload_example = example_value_for_schema(schema, openapi)

    # build snippet
    lines: List[str] = []
    lines.append("from typing import Any")
    if typedict_name:
        # assume models are in src/types/dolphin_models.py
        lines.append(f"from src.types.dolphin_models import {typedict_name}")
        lines.append("")
        lines.append(f"payload: {typedict_name} = {json.dumps(payload_example, ensure_ascii=False, indent=4)}")
    else:
        lines.append("")
        lines.append("payload = ")
        lines.append(json.dumps(payload_example or {}, ensure_ascii=False, indent=4))

    lines.append("")
    lines.append("import requests")
    lines.append("")
    lines.append("resp = requests.%s(\"%s\"%s)" % (
        method.lower(),
        url,
        ",\n    json=payload,\n    headers={\n        \"Content-Type\": \"application/json\",\n        \"Authorization\": \"Bearer <TOKEN>\"\n    }" if payload_example is not None else ",\n    headers={\n        \"Authorization\": \"Bearer <TOKEN>\"\n    }"
    ))
    lines.append("")
    lines.append("print(resp.status_code)")
    lines.append("print(resp.text)")

    return "\n".join(lines)


def main():
    openapi = load_openapi()

    print("\n=== OpenAPI Playground ===\n")
    user_path = input("Введите endpoint path (пример: /browser_profiles or /browser_profiles/123): ").strip()
    if not user_path.startswith("/"):
        user_path = "/" + user_path

    found = find_path_item(openapi, user_path)
    if not found:
        print("❌ Путь не найден в OpenAPI")
        sys.exit(1)

    path_template, path_item = found
    print(f"Найден путь: {path_template}")
    methods = [m.upper() for m in path_item.keys()]
    print("Доступные методы:", ", ".join(methods))
    method = input("Выберите метод: ").strip().upper()
    if method not in methods:
        print("❌ Неверный метод")
        sys.exit(1)

    # ask base url (optional)
    base_url = input("(опционально) Если нужно переопределить server URL, введите его или Enter: ").strip()

    snippet = build_python_snippet(base_url, path_template, method, openapi)

    # ensure generated dir
    os.makedirs(GENERATED_DIR, exist_ok=True)
    fname = f"{method}_{sanitize_filename(path_template)}.py"
    outpath = os.path.join(GENERATED_DIR, fname)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(snippet)

    print('\n✅ Сгенерирован файл:', outpath)
    print('\n--- Сниппет (preview) ---\n')
    print(snippet)
    print('\n--- Конец ---\n')


if __name__ == '__main__':
    main()
