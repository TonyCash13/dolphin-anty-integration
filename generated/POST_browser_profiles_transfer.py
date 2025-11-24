from typing import Any
from src.types.dolphin_models import browser_profile_transfer

payload: browser_profile_transfer = {
    "ids": [
        0
    ],
    "username": "",
    "withProxy": false
}

import requests

resp = requests.post("https://dolphin-anty-api.com/api/v2/browser_profiles/transfer",
    json=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer <TOKEN>"
    })

print(resp.status_code)
print(resp.text)
