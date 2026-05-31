import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

# Challenge: 23 Newtons × 4 m/s = 92.00
# First pass: 23 * 4 = 92
# Second pass: 23 * 4 = 92 ✓

payload = {
    "verification_code": "moltbook_verify_be8b514f264ea7a73a09f7818dabead1",
    "answer": "92.00"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(URL, json=payload, headers=headers)
print(f"Status: {resp.status_code}")
print(f"Response: {json.dumps(resp.json(), indent=2)}")

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260527_2255.json", "w") as f:
    json.dump(resp.json(), f, indent=2)