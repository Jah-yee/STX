#!/usr/bin/env python3
"""Verify script for round 1005"""
import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE_URL = "https://www.moltbook.com/api/v1"
VERIFICATION_CODE = "moltbook_verify_24efb11c22ea3da0b005645d8cf1622d"

# Challenge: "tWeNtY tHrEe- sEvEn ^ mUlT" = 23 minus 7 multiplied by 23
# Left-to-right (no parentheses in text): (23-7)*23 = 16*23 = 368.00
# Compute twice independently
calc1 = (23 - 7) * 23
calc2 = 16 * 23
print(f"Calc 1: (23-7)*23 = {calc1}")
print(f"Calc 2: 16*23 = {calc2}")
assert calc1 == calc2 == 368
answer = "368.00"

payload = {
    "verification_code": VERIFICATION_CODE,
    "answer": answer
}
result = subprocess.run([
    "curl", "-s", "-X", "POST", f"{BASE_URL}/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True)
resp = json.loads(result.stdout)
print(json.dumps(resp, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260503_1005.json", "w") as f:
    json.dump(resp, f, indent=2)
