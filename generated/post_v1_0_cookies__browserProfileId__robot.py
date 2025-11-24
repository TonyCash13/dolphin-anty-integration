import requests

payload = {
    "data": [
        ""
    ],
    "headless": false,
    "imageless": false,
    "plan": null,
    "browserProfilePassword": null
}

resp = requests.post(
    "https://dolphin-anty-api.com/api/v2/v1.0/cookies/{browserProfileId}/robot",
    json=payload,
    headers={
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }
)

print(resp.status_code)
print(resp.text)