from typing import Any
from src.types.dolphin_models import browser_profile_access_multi_edit

payload: browser_profile_access_multi_edit = {
    "ids": [
        0
    ],
    "users": [
        {
            "id": 0,
            "view": false,
            "update": false,
            "delete": false,
            "share": false,
            "usage": false
        }
    ],
    "action": "add"
}

import requests

resp = requests.post("https://dolphin-anty-api.com/api/v2/browser_profiles/access",
    json=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer <TOKEN>"
    })

print(resp.status_code)
print(resp.text)
