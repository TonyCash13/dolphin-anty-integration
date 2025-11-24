#!/usr/bin/env python3
"""
Скрипт для генерации типов Dolphin Anty API
"""
import requests
import yaml
import json
import subprocess
import os
import sys
from pathlib import Path

def generate_dolphin_types():
    print("🔄 Генерирую типы Dolphin Anty API...")

    openapi_url = "https://docs.dolphin-anty-cdn.com/openapi.yaml"

    try:
        # Скачиваем OpenAPI спецификацию
        print(f"📥 Загружаю OpenAPI спецификацию из {openapi_url}...")
        response = requests.get(openapi_url, timeout=30)
        response.raise_for_status()

        print(f"✅ Статус: {response.status_code}")
        print(f"📄 Content-Type: {response.headers.get('content-type')}")

        # Проверяем что это действительно YAML
        content = response.text
        print(f"🔍 Первые 100 символов: {content[:100]}...")

        # Пробуем разные варианты парсинга
        openapi_spec = None

        # Вариант 1: Пробуем парсить как YAML
        try:
            openapi_spec = yaml.safe_load(content)
            print("✅ Успешно распарсено как YAML")
        except yaml.YAMLError as e:
            print(f"❌ Не YAML: {e}")

            # Вариант 2: Может быть это JSON?
            try:
                openapi_spec = json.loads(content)
                print("✅ Успешно распарсено как JSON")
            except json.JSONDecodeError as e2:
                print(f"❌ Не JSON: {e2}")
                print("📝 Создаю базовые типы...")
                return create_basic_types()

        # Сохраняем временный файл в JSON
        temp_file = "openapi_temp.json"
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(openapi_spec, f, indent=2)

        # Генерируем TypeScript типы
        print("⚙️ Генерирую TypeScript типы...")
        result = subprocess.run([
            "npx", "--yes", "openapi-typescript",
            temp_file,
            "-o", "src/types/dolphin-api.ts"
        ], capture_output=True, text=True, timeout=60)

        # Удаляем временный файл
        if os.path.exists(temp_file):
            os.remove(temp_file)

        if result.returncode == 0:
            print("✅ Типы Dolphin Anty API успешно сгенерированы!")
            subprocess.run(["git", "add", "src/types/dolphin-api.ts"], check=False)
            return True
        else:
            print(f"❌ Ошибка генерации типов: {result.stderr}")
            return create_basic_types()

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка загрузки: {e}")
        return create_basic_types()
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return create_basic_types()

def create_basic_types():
    """Создает базовые типы вручную"""
    basic_types = """/**
 * Базовые типы Dolphin Anty API
 * Сгенерировано автоматически
 */

export interface Profile {
  id?: number;
  name?: string;
  browser?: string;
  os?: string;
  userAgent?: string;
}

export interface CreateProfileRequest {
  name: string;
  browser: string;
  os?: string;
}

export interface APIResponse<T = any> {
  data?: T;
  error?: string;
  success: boolean;
}
"""

    os.makedirs("src/types", exist_ok=True)
    with open("src/types/dolphin-api.ts", "w", encoding="utf-8") as f:
        f.write(basic_types)

    print("✅ Базовые типы созданы вручную")
    subprocess.run(["git", "add", "src/types/dolphin-api.ts"], check=False)
    return True

if __name__ == "__main__":
    success = generate_dolphin_types()
    sys.exit(0 if success else 1)
