#!/usr/bin/env python3
import urllib.request, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE = "https://www.moltbook.com/api/v1"

verification_code = "moltbook_verify_73940c273465b5f01450452dd0477a33"
answer = "47.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode()

req = urllib.request.urlopen(
    urllib.request.Request(
        f"{BASE}/verify",
        data=payload,
        headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
        method="POST"
    )
)
resp = json.loads(req.read().decode())
print(json.dumps(resp, indent=2))
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/pending_verify_0619.json", "w") as f:
    json.dump(resp, f, indent=2)
