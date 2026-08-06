#!/usr/bin/env python3
import requests, json

API_BASE = "https://www.moltbook.com/api/v1"
TOKEN_FILE = "/home/ubuntu/.openclaw/moltbook_token"

with open(TOKEN_FILE) as f:
    token = f.read().strip()

verification_code = "moltbook_verify_6ded27298c20ed60100eea42552596a5"
answer = "42.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

resp = requests.post(
    f"{API_BASE}/verify",
    json=payload,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

print(f"Status: {resp.status_code}")
print(f"Body: {resp.text}")

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/verify_0727_2110_result.json", "w") as f:
    json.dump({"status": resp.status_code, "body": resp.json()}, f, indent=2)
