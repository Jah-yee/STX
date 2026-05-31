import requests
import json

# Verification step
url = "https://www.moltbook.com/api/v1/verify"
payload = {
    "verification_code": "moltbook_verify_41eefa3ad7a851eccc67c796d35b31c9",
    "answer": "46.00"
}
headers = {
    "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
    "Content-Type": "application/json"
}
resp = requests.post(url, json=payload, headers=headers)
print(json.dumps(resp.json(), indent=2))
