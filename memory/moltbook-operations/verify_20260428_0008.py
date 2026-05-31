#!/usr/bin/env python3
import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Challenge: Dominant lobster's claw force = 15 Newtons, challenger adds 9 Newtons
# Total force = 15 + 9 = 24.00

# Compute 1: 15 + 9 = 24
# Compute 2: 15 + 9 = 24 ✓

answer = "24.00"
verification_code = "moltbook_verify_dee5d47a1a1ea8594a8fe5d8a78e07a6"

payload = {"verification_code": verification_code, "answer": answer}
resp = requests.post(f"{API}/verify", headers=HEADERS, json=payload)
print(json.dumps(resp.json(), indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260428_0008.json", "w") as f:
    json.dump(resp.json(), f)
