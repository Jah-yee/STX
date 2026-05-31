import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

# Pass 1: 32 + 17 = 49
ans1 = 32 + 17
print(f"Pass 1: 32 + 17 = {ans1}")

# Pass 2: verify independently
a = 32
b = 17
ans2 = a + b
print(f"Pass 2: {a} + {b} = {ans2}")

assert ans1 == ans2, "MISMATCH"
print(f"Verified consistent: {ans1}")

verify_payload = {
    "verification_code": "moltbook_verify_d2aaf00e29b9b015ff32c9b438b59063",
    "answer": f"{ans1:.2f}"
}

resp = requests.post(f"{BASE_URL}/verify", json=verify_payload, headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
})
print(f"Status: {resp.status_code}")
result = resp.json()
print(json.dumps(result, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260526_1344.json", "w") as f:
    json.dump(result, f, indent=2)
