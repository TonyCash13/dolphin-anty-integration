#!/usr/bin/env python3
"""
Интерактивный Playground для Dolphin Anty API
- Генерация Python snippet с payload
- Сохраняет код в папку generated/
- Показывает только доступные методы для выбранного пути
"""

import json
import os
import re
import sys
from typing import Any, Dict, List

# Импортируем генератор OpenAPI (файл должен быть рядом)
from generate_dolphin_types import fetch_openapi_yaml, dereference_schema

# -------------------
# Генерация примера payload
# -------------------
def example_value_for_schema(schema: Dict[str, Any], root: Dict[str, Any]) -> Any:
    if not isinstance(schema, dict):
        return None
    if "$ref" in schema:
        ref_schema = dereference_schema(schema, root)
        return example_value_for_schema(ref_schema, root)

    t = schema.get("type")
    if t == "object":
        props = schema.get("properties", {})
        if not props:
            return {}
        return {k: example_value_for_schema(v, root) for k, v in props.items()}
    if t == "array":
        items = schema.get("items", {})
        return [example_value_for_schema(items, root)]
    if t == "string":
        return ""
    if t == "integer":
        return 0
    if t == "number":
        return 0.0
    if t == "boolean":
        return False
    return None

# -------------------
# Генерация Python snippet
# -------------------
def build_python_snippet(base_url: str, path_template: str, method: str, openapi: Dict[str, Any]) -> str:
    method_item = openapi.get("paths", {}).get(path_template, {}).get(method.lower())
    if not method_item:
        return "# Метод не найден в OpenAPI"

    servers = openapi.get("servers", [])
    server_url = servers[0].get("url") if servers else base_url or "https://dolphin-anty-api.com"
    url = server_url.rstrip("/") + path_template

    # Определяем requestBody schema
    rb = method_item.get("requestBody") or {}
    content = rb.get("content", {})
    schema = None
    if "application/json" in content:
        schema = content["application/json"].get("schema")
    elif content:
        first = next(iter(content.values()))
        schema = first.get("schema")

    payload_example = None
    if schema:
        payload_example = example_value_for_schema(schema, openapi)
        if payload_example is None:
            payload_example = {}

    lines: List[str] = []
    lines.append("import requests")
    lines.append("")
    lines.append("payload = " + json.dumps(payload_example, ensure_ascii=False, indent=4))
    lines.append("")
    lines.append(
        f"resp = requests.{method.lower()}(\n"
        f"    \"{url}\",\n"
        f"    json=payload,\n"
        f"    headers={{\n"
        f"        \"Authorization\": \"Bearer <TOKEN>\",\n"
        f"        \"Content-Type\": \"application/json\"\n"
        f"    }}\n"
        f")"
    )
    lines.append("")
    lines.append("print(resp.status_code)")
    lines.append("print(resp.text)")

    return "\n".join(lines)

# -------------------
# Сохраняем snippet в папку generated
# -------------------
def save_snippet(snippet: str, method: str, path_template: str) -> str:
    os.makedirs("generated", exist_ok=True)
    safe_path = re.sub(r"[^0-9a-zA-Z_]", "_", path_template.strip("/"))
    if not safe_path:
        safe_path = "root"
    filename = f"{method.lower()}_{safe_path}.py"
    filepath = os.path.join("generated", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(snippet)
    return filepath

# -------------------
# CLI Playground
# -------------------
def main():
    print("📌 Dolphin Anty Playground")
    print("Загрузка OpenAPI спецификации...")
    _, openapi = fetch_openapi_yaml()
    if openapi is None:
        print("❌ Не удалось загрузить OpenAPI")
        sys.exit(1)

    base_url = input("Базовый URL (по умолчанию https://dolphin-anty-api.com): ").strip() or "https://dolphin-anty-api.com"
    path_template = input("Путь эндпоинта (например /browser_profiles): ").strip()

    # Показываем только доступные методы
    path_item = openapi.get("paths", {}).get(path_template, {})
    available_methods = [m.upper() for m in path_item.keys()]
    if not available_methods:
        print(f"❌ Для пути {path_template} нет методов в OpenAPI")
        sys.exit(1)

    print(f"Доступные методы для {path_template}: {', '.join(available_methods)}")
    method = input(f"Выберите метод [{available_methods[0]}]: ").strip().upper() or available_methods[0]
    if method not in available_methods:
        print(f"❌ Метод {method} недоступен для {path_template}")
        sys.exit(1)

    snippet = build_python_snippet(base_url, path_template, method, openapi)

    # print("\n📝 Сгенерированный код:\n")
    # print(snippet)

    filepath = save_snippet(snippet, method, path_template)
    print(f"\n✅ Код сохранён в: {filepath}")

if __name__ == "__main__":
    main()
