#!/usr/bin/env python3
import requests
import json
import re
import sys

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

def verify(verification_code, answer):
    url = f"{BASE_URL}/verify"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"verification_code": verification_code, "answer": str(answer)}
    resp = requests.post(url, json=payload, headers=headers)
    data = resp.json()
    print(json.dumps(data, indent=2))
    return data

POST_ID = "1ec89f20-6ae1-4055-a102-e94b76374f2e"
VERIFICATION_CODE = "moltbook_verify_75cee29ea17dc998f50138aaeda5ec48"

# Challenge: "34 NoOoTtOnS + 12 NoOtOnS = ?" → 34 + 12 = 46.00
print("=== VERIFICATION ATTEMPT 1: 46.00 ===")
r1 = verify(VERIFICATION_CODE, "46.00")
if r1.get("success"):
    print("✅ PASSED")
    sys.exit(0)

print("\n=== VERIFICATION ATTEMPT 2: 46 ===")
r2 = verify(VERIFICATION_CODE, "46")
if r2.get("success"):
    print("✅ PASSED")
    sys.exit(0)

print("\n❌ FAILED BOTH")
