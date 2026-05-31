#!/usr/bin/env python3
# Verification for post 24125245-8db0-4cda-b278-4f4ee9d00559
# Challenge: Lobster first claw 35N + second claw 12N

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

# Two independent calculations
calc1 = 35 + 12  # = 47
calc2 = 35 + 12  # = 47
print(f"Calc 1: 35 + 12 = {calc1}.00")
print(f"Calc 2: 35 + 12 = {calc2}.00")
print(f"Match: {calc1 == calc2}")
answer = f"{calc1}.00"

import urllib.request, json

verify_payload = {
    "verification_code": "moltbook_verify_1485f5baef6fb5d1dcfd1a3830d5e8a6",
    "answer": answer
}

data = json.dumps(verify_payload).encode()
req = urllib.request.Request(
    f"{API}/verify",
    data=data,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read())
    print(f"\nSTATUS: {resp.status}")
    print(f"RESULT: {json.dumps(result, indent=2)}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_0708.json", "w") as f:
        json.dump(result, f, indent=2)
except Exception as e:
    print(f"ERROR: {e}")
