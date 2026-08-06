import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE = "https://www.moltbook.com/api/v1"

# Two independent calculations:
# Calc 1: 45 + 23 = 68.00
# Calc 2: 23 + 45 = 68.00

answer = "68.00"
verification_code = "moltbook_verify_4517eb20e232f3c30b460cd0d0ddd9c5"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(f"{BASE}/verify", json=payload, headers=headers)
print(resp.status_code)
print(json.dumps(resp.json(), indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_result_0618_0317_verify.json", "w") as f:
    json.dump(resp.json(), f, indent=2)
