import requests

payload = {
    "type": "",
    "host": "",
    "port": 0,
    "login": "",
    "password": "",
    "name": "",
    "changeIpUrl": "",
    "provider": ""
}

resp = requests.patch(
    "https://dolphin-anty-api.com/api/v2/proxy/{id}",
    json=payload,
    headers={
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }
)

print(resp.status_code)
print(resp.text)