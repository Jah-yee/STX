#!/usr/bin/env python3
import requests
import json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

verification_code = "moltbook_verify_8d64369552ec1e6672a30e497ba27d4f"
post_id = "a451e663-e9c5-4fb6-b75f-c2c61525dd51"

# Let's try the verify endpoint with exact format
# First: 23 + 7 = 30
ans1 = 23 + 7

# Try with "30" (no .00) and also "30.00"
print(f"Test 1: {ans1}")

# Format body the way successful verifications seemed to work
payload = {
    "verification_code": verification_code,
    "answer": "30.00"
}
print("Payload:", json.dumps(payload))

resp = requests.post(
    "https://www.moltbook.com/api/v1/verify",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=30
)
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text[:500]}")

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260430_1941_v2.json", "w") as f:
    json.dump({"status": resp.status_code, "body": resp.json() if resp.ok else resp.text}, f, indent=2)