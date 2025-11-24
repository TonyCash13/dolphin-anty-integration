payload: browser_profile_create = {
    "name": "",
    "tags": [
        ""
    ],
    "tabs": [
        ""
    ],
    "platform": "windows",
    "platformVersion": "10.15.7",
    "browserType": "anty",
    "mainWebsite": null,
    "statusId": null,
    "proxy": null,
    "args": [
        null
    ],
    "notes": [
        {}
    ],
    "login": null,
    "password": null,
    "fingerprint": {},
    "uaFullVersion": null,
    "folderId": null,
    "folder": null,
    "homepages": [
        {
            "id": 0,
            "name": "",
            "order": 0
        }
    ],
    "newHomepages": [
        {
            "url": "",
            "name": "",
            "mainWebsite": null,
            "order": 0
        }
    ],
    "fontsMode": "auto",
    "fonts": [
        ""
    ],
    "macAddress": {
        "mode": "manual",
        "value": ""
    },
    "deviceName": {
        "mode": "manual",
        "value": "",
        "valueNew": ""
    },
    "audio": {
        "mode": "noise",
        "noise": 0.0
    },
    "isHiddenProfileName": false,
    "disableLoadWebCameraAndCookies": null,
    "enableArgIsChromeIcon": null,
    "doNotTrack": false,
    "useragent": {
        "mode": "auto",
        "value": ""
    },
    "webrtc": {
        "mode": "off",
        "ipAddress": ""
    },
    "canvas": {
        "mode": "off",
        "value": ""
    },
    "webgl": {
        "mode": "off",
        "noise": [
            0.0
        ],
        "value": ""
    },
    "webgpu": {
        "mode": "off",
        "value": ""
    },
    "webgl2Maximum": {},
    "webglInfo": {
        "mode": "real",
        "vendor": "",
        "renderer": ""
    },
    "clientRect": {
        "mode": "auto",
        "noise": [
            0.0
        ]
    },
    "timezone": {
        "mode": "auto",
        "value": ""
    },
    "locale": {
        "mode": "auto",
        "value": ""
    },
    "geolocation": {
        "mode": "auto",
        "latitude": 0.0,
        "longitude": 0.0
    },
    "cpu": {
        "mode": "real",
        "value": 0
    },
    "memory": {
        "mode": "real",
        "value": 0
    },
    "screen": {
        "mode": null,
        "resolution": null
    },
    "connectionDownlink": null,
    "connectionEffectiveType": null,
    "connectionRtt": null,
    "connectionSaveData": 0,
    "platformName": null,
    "cpuArchitecture": null,
    "osVersion": null,
    "screenWidth": null,
    "screenHeight": null,
    "vendorSub": null,
    "productSub": null,
    "vendor": null,
    "product": null,
    "appCodeName": null,
    "mediaDevices": null,
    "userFields": [
        {}
    ],
    "ports": {
        "mode": "protect",
        "blacklist": ""
    }
}

import requests

resp = requests.post("https://dolphin-anty-api.com/api/v2/browser_profiles",
    json=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": ""
    })

print(resp.status_code)
print(resp.text)
