import requests

payload = {
    "url": "",
    "sharedToEntireTeam": false,
    "mainWebsite": [
        ""
    ]
}

resp = requests.post(
    "https://dolphin-anty-api.com/api/v2/extensions",
    json=payload,
    headers={
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }
)

print(resp.status_code)
print(resp.text)