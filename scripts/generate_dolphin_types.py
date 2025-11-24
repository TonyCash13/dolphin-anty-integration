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

        # Детальная диагностика
        print(f"🔍 Статус ответа: {response.status_code}")
        print(f"🔍 Content-Type: {response.headers.get('content-type')}")
        print(f"🔍 Размер ответа: {len(response.text)} символов")

        response.raise_for_status()

        # Проверяем что это YAML
        content = response.text
        if not content.strip():
            print("❌ Пустой ответ от сервера")
            return False

        print(f"🔍 Первые 200 символов: {content[:200]}...")

        # Парсим YAML
        openapi_spec = yaml.safe_load(content)

        if not openapi_spec:
            print("❌ Не удалось распарсить YAML")
            return False

        print("✅ OpenAPI спецификация успешно загружена и распарсена")

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
            print("✅ Типы Dolphin Anty API успешно сгенерированы из OpenAPI!")

            # Добавляем сгенерированные файлы в git
            subprocess.run(["git", "add", "src/types/dolphin-api.ts"], check=False)
            subprocess.run(["git", "add", "src/types/python_types.py"], check=False)

            return True
        else:
            print(f"❌ Ошибка генерации TypeScript типов: {result.stderr}")
            return False

    except yaml.YAMLError as e:
        print(f"❌ Ошибка парсинга YAML: {e}")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Таймаут генерации типов")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False
