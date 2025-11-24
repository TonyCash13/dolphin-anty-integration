import requests

payload = null

resp = requests.delete(
    "https://dolphin-anty-api.com/api/v2/proxy/{id}",
    json=payload,
    headers={
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }
)

print(resp.status_code)
print(resp.text)