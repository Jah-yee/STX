import requests, json

API = "https://www.moltbook.com/api/v1"
KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VER_CODE = "moltbook_verify_f8480a97cdbecee740813b042656f58a"

# Answer: 25 * 3 = 75.00
answer = "75.00"

payload = {
    "verification_code": VER_CODE,
    "answer": answer
}

headers = {
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(f"{API}/verify", json=payload, headers=headers, timeout=30)
result = resp.json()
print(json.dumps(result, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0627_0218.json", "w") as f:
    json.dump(result, f, indent=2)
