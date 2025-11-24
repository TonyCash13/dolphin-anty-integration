from src.types.dolphin_models import BrowserProfileCreateRequest
import requests

requests.post(
    "https://dolphin-anty-api.com/browser_profiles",
    headers={
      "Content-Type": "application/json",
      "Authorization": "Bearer YOUR_SECRET_TOKEN"
    },
)

payload: BrowserProfileCreateRequest = {


}
