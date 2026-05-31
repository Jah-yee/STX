import requests, json

url = "https://www.moltbook.com/api/v1/verify"
token = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

payload = {
    "verification_code": "moltbook_verify_24526548c55fd7dd1d1d0ba2d2bd8f64",
    "answer": "30.00"
}

resp = requests.post(url, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, json=payload)
print(json.dumps(resp.json(), indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260511_1248.json", "w") as f:
    json.dump(resp.json(), f, indent=2)