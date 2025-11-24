#!/usr/bin/env python3
"""
Улучшенный генератор TypedDict типов из OpenAPI (Dolphin Anty)

Что делает:
- Корректно скачивает OpenAPI YAML (несколько варинтов URL + User-Agent)
- Проверяет, что получен YAML, а не HTML
- Простая развёртка внутренних $ref (components/schemas)
- Базовая поддержка allOf/oneOf/anyOf (слияние/Union)
- Генерирует TypeScript через `npx openapi-typescript`
- Генерирует Python TypedDict классы в `src/types/dolphin_models.py`
- Логирование и информативные ошибки

Зависимости (локально):
- Python: requests, pyyaml
- Node.js: npx openapi-typescript

Запуск: python3 dolphin_openapi_typedict_generator.py
"""

from __future__ import annotations
import requests
import yaml
import json
import subprocess
import os
import re
import sys
from typing import Any, Dict, List, Tuple, Optional

# --- Конфиг ---
CANDIDATE_URLS = [
    "https://dolphin-anty.com/api/docs/openapi.yaml",
    "https://dolphin-anty.com/api/docs/v1/openapi.yaml",
    "https://docs.dolphin-anty-cdn.com/openapi.yaml",
]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; TypedDict-Generator/1.0)"
}
TEMP_JSON = "openapi_temp.json"
OUT_TS = "src/types/dolphin_api.ts"
OUT_PY = "src/types/dolphin_models.py"

# --- Утилиты ---

def log(msg: str) -> None:
    print(msg)


def fetch_openapi_yaml() -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    """Пытается загрузить OpenAPI YAML с нескольких URL, возвращает текст и распарсенный dict"""
    last_text = None
    for url in CANDIDATE_URLS:
        log(f"📥 Попытка загрузить {url} ...")
        try:
            r = requests.get(url, timeout=20, headers=HEADERS)
        except requests.RequestException as e:
            log(f"⚠️ Сетевой сбой при {url}: {e}")
            continue

        log(f"🔍 Статус: {r.status_code}")
        content_type = r.headers.get("content-type", "")
        log(f"🔍 Content-Type: {content_type}")

        text = r.text
        last_text = text[:1000]

        # Если 404 или HTML — пропускаем
        if r.status_code != 200:
            log(f"❌ Ошибка HTTP: {r.status_code} для {url}")
            continue

        # простая проверка: html vs yaml/json
        if bool(re.search(r"<\/?html|<!doctype", text[:200], re.I)):
            log("❌ Получен HTML, это не OpenAPI YAML — пропускаю")
            continue

        # Пытаемся распарсить YAML
        try:
            data = yaml.safe_load(text)
            if not isinstance(data, dict):
                log("❌ YAML распарсен, но не является объектом (ожидался dict)")
                continue
            log("✅ OpenAPI YAML успешно загружен и распарсен")
            return text, data
        except yaml.YAMLError as e:
            log(f"❌ Ошибка парсинга YAML: {e}")
            continue

    log("❌ Не удалось загрузить корректный OpenAPI YAML. Последняя часть ответа:\n" + (last_text or "<пусто>"))
    return None, None


# --- Простая развёртка $ref ---

def resolve_ref(ref: str, root: Dict[str, Any]) -> Dict[str, Any]:
    """Поддерживаем только внутренние refs вида #/components/schemas/Name"""
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


def merge_schemas(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """Простое глубокое merge: свойства объединяются, required объединяются"""
    out = dict(a)
    if "properties" in a or "properties" in b:
        props = {}
        props.update(a.get("properties", {}))
        props.update(b.get("properties", {}))
        out["properties"] = props
    if "required" in a or "required" in b:
        req = set(a.get("required", [])) | set(b.get("required", []))
        out["required"] = list(req)
    # копируем прочие ключи аккуратно
    for k, v in b.items():
        if k in ("properties", "required"):
            continue
        out[k] = v
    return out


def dereference_schema(schema: Any, root: Dict[str, Any]) -> Any:
    """Развёртывает $ref/ allOf / anyOf / oneOf рекурсивно в пределах components/schemas"""
    if isinstance(schema, dict):
        if "$ref" in schema:
            referred = resolve_ref(schema["$ref"], root)
            return dereference_schema(referred, root)

        if "allOf" in schema:
            merged = {}
            for part in schema["allOf"]:
                part_res = dereference_schema(part, root)
                if isinstance(part_res, dict):
                    merged = merge_schemas(merged, part_res)
            return merged

        if "oneOf" in schema or "anyOf" in schema:
            key = "oneOf" if "oneOf" in schema else "anyOf"
            # представим как union — вернём список вариантов
            variants = []
            for part in schema[key]:
                variants.append(dereference_schema(part, root))
            return {key: variants}

        # рекурсивно обрабатываем свойства и items
        out = {}
        for k, v in schema.items():
            if k in ("properties",):
                out[k] = {pn: dereference_schema(ps, root) for pn, ps in v.items()}
            elif k == "items":
                out[k] = dereference_schema(v, root)
            else:
                out[k] = dereference_schema(v, root)
        return out

    elif isinstance(schema, list):
        return [dereference_schema(x, root) for x in schema]
    else:
        return schema


# --- Генерация Python TypedDict ---

def sanitize_name(name: str) -> str:
    name = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if re.match(r"^[0-9]", name):
        name = "N_" + name
    return name


def openapi_type_to_py(t: Dict[str, Any]) -> str:
    """Простая конвертация одного объекта schema -> Python type (строка)"""
    if not isinstance(t, dict):
        return "Any"

    if "$ref" in t:
        return sanitize_name(t["$ref"].split('/')[-1])

    if "oneOf" in t or "anyOf" in t:
        key = "oneOf" if "oneOf" in t else "anyOf"
        parts = t[key]
        py_parts = [openapi_type_to_py(p) for p in parts]
        # union
        return "Union[" + ", ".join(py_parts) + "]"

    typ = t.get("type")
    fmt = t.get("format")
    if typ == "string":
        return "str"
    if typ == "integer":
        return "int"
    if typ == "number":
        return "float"
    if typ == "boolean":
        return "bool"
    if typ == "array":
        items = t.get("items", {})
        return f"List[{openapi_type_to_py(items)}]"
    if typ == "object":
        # если есть properties — ссылаемся на вложенный TypedDict анонимно -> Dict[str, Any]
        if "properties" in t:
            return "Dict[str, Any]"
        return "Dict[str, Any]"
    return "Any"


def generate_typedicts(openapi: Dict[str, Any]) -> str:
    """Генерирует текст Python файла с TypedDict для схем в components/schemas"""
    lines: List[str] = []
    lines.append('"""')
    lines.append("Автогенерируемые TypedDict типы для Dolphin Anty API")
    lines.append('"""')
    lines.append("from typing import TypedDict, Optional, List, Dict, Any, Union")
    lines.append("")

    comps = openapi.get("components", {})
    schemas = comps.get("schemas", {})
    if not schemas:
        lines.append("# В openapi не найдено components.schemas")
        return "\n".join(lines)

    # Сначала делаем развёрнутые версии схем
    deref_cache: Dict[str, Dict[str, Any]] = {}
    for name, schema in schemas.items():
        try:
            deref = dereference_schema(schema, openapi)
            deref_cache[name] = deref if isinstance(deref, dict) else schema
        except Exception as e:
            log(f"⚠️ Нельзя полностью развернуть {name}: {e}")
            deref_cache[name] = schema

    # Генерация классов
    for name, schema in deref_cache.items():
        class_name = sanitize_name(name)
        lines.append("")
        lines.append(f"class {class_name}(TypedDict, total=False):")
        desc = schema.get("description") if isinstance(schema, dict) else None
        if desc:
            # короткая docstring
            lines.append(f'    """{desc}"""')
        props = schema.get("properties", {}) if isinstance(schema, dict) else {}
        required = set(schema.get("required", [])) if isinstance(schema, dict) else set()
        if not props:
            lines.append("    pass")
            continue
        for prop_name, prop_schema in props.items():
            py_type = openapi_type_to_py(prop_schema)
            if prop_name not in required:
                py_type = f"Optional[{py_type}]"
            # sanitize prop name if needed
            safe_prop = prop_name if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", prop_name) else f'"{prop_name}"'
            desc = prop_schema.get("description") if isinstance(prop_schema, dict) else None
            if desc:
                lines.append(f"    {safe_prop}: {py_type}  # {desc}")
            else:
                lines.append(f"    {safe_prop}: {py_type}")

    return "\n".join(lines)


# --- Основной процесс ---

def generate_all():
    text, openapi = fetch_openapi_yaml()
    if openapi is None:
        log("❌ Остановка: не удалось получить OpenAPI")
        sys.exit(1)

    # Сохраняем временный JSON для openapi-typescript
    try:
        with open(TEMP_JSON, "w", encoding="utf-8") as f:
            json.dump(openapi, f, ensure_ascii=False, indent=2)
    except Exception as e:
        log(f"❌ Не удалось сохранить временный JSON: {e}")
        sys.exit(1)

    # Генерируем TypeScript через npx
    os.makedirs(os.path.dirname(OUT_TS), exist_ok=True)
    log("⚙️ Генерируем TypeScript типы через openapi-typescript...")
    try:
        res = subprocess.run([
            "npx", "--yes", "openapi-typescript", TEMP_JSON, "-o", OUT_TS
        ], capture_output=True, text=True, timeout=120)
    except Exception as e:
        log(f"❌ Ошибка при вызове npx: {e}")
        res = None

    if res is None or res.returncode != 0:
        log("❗ TypeScript генерация не удалась.")
        if res is not None:
            log(res.stderr or res.stdout)
        # продолжаем — но предупредим
    else:
        log("✅ TypeScript типы сгенерированы: " + OUT_TS)

    # Удаляем временный JSON
    try:
        if os.path.exists(TEMP_JSON):
            os.remove(TEMP_JSON)
    except Exception:
        pass

    # Генерируем Python TypedDict
    os.makedirs(os.path.dirname(OUT_PY), exist_ok=True)
    py_text = generate_typedicts(openapi)
    try:
        with open(OUT_PY, "w", encoding="utf-8") as f:
            f.write(py_text)
        log("✅ Python TypedDicts сгенерированы: " + OUT_PY)
    except Exception as e:
        log(f"❌ Не удалось записать Python файл: {e}")

    # Опционально добавляем в git
    try:
        subprocess.run(["git", "add", OUT_TS, OUT_PY], check=False)
        log("ℹ️ Добавлено в git (git add)")
    except Exception:
        pass


if __name__ == '__main__':
    generate_all()
