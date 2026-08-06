import requests, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE = "https://www.moltbook.com/api/v1"

verify_code = "moltbook_verify_1ab68926383e689b95f4566e20679ec9"
answer = "75.00"

payload = {
    "verification_code": verify_code,
    "answer": answer
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.post(f"{BASE}/verify", json=payload, headers=headers, timeout=30)
print(resp.text)

# Save result
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0607_2332.json", "w") as f:
    json.dump({"verify_payload": payload, "response": resp.json()}, f, indent=2)
