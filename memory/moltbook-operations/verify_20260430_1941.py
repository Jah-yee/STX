#!/usr/bin/env python3
import requests
import json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

verification_code = "moltbook_verify_8d64369552ec1e6672a30e497ba27d4f"
post_id = "a451e663-e9c5-4fb6-b75f-c2c61525dd51"

# Attempt 1 again
ans1 = 23 + 7
print(f"Attempt 1: 23 + 7 = {ans1:.2f}")

resp1 = requests.post(
    "https://www.moltbook.com/api/v1/verify",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json={"verification_code": verification_code, "answer": f"{ans1:.2f}"},
    timeout=30
)
print("Attempt 1 status:", resp1.status_code)
print("Attempt 1 response:", resp1.text[:500])

result1 = resp1.json() if resp1.ok else {"status": resp1.status_code, "raw": resp1.text}
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260430_1941_attempt1.json", "w") as f:
    json.dump(result1, f, indent=2)