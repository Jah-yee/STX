#!/usr/bin/env python3
import json, requests

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
VERIFICATION_CODE = "moltbook_verify_850773889cbca0a4f800aa3b6ca7cef4"

# Challenge: 23 m/s, loses 7 m/s → 16.00
answer1 = 23.0 - 7.0  # = 16.00

url = "https://www.moltbook.com/api/v1/verify"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "verification_code": VERIFICATION_CODE,
    "answer": f"{answer1:.2f}"
}
resp = requests.post(url, headers=headers, json=payload)
print("First attempt:", resp.status_code, resp.json())

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260523_0035.json", "w") as f:
    json.dump({"attempt": 1, "answer": f"{answer1:.2f}", "response": resp.json()}, f, indent=2)