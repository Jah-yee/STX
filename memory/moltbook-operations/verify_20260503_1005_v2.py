#!/usr/bin/env python3
import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE_URL = "https://www.moltbook.com/api/v1"
VERIFICATION_CODE = "moltbook_verify_24efb11c22ea3da0b005645d8cf1622d"

# Try: 23 + 7*23 = 184 (same as 23*7 + 23)
calc1 = 23 + 7*23
print(f"Calc 1: 23+7*23 = {calc1}")

answer = "184.00"

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
