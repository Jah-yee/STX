#!/usr/bin/env python3
import requests, json, re

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
post_id = "63098301-6502-4bf8-addc-378ea0d2501c"

# Get post to see verification field
r = requests.get(f"{API}/posts/{post_id}", headers=HEADERS)
data = r.json()
post_obj = data.get("post", {})
print(f"verification_status: {post_obj.get('verification_status')}")
print(f"verificationStatus: {post_obj.get('verificationStatus')}")
print(f"verification field: {json.dumps(post_obj.get('verification'), indent=2)}")

# Try calling verify with empty/placeholder to see expected format
r2 = requests.post(f"{API}/verify", headers=HEADERS, json={"verification_code": "", "answer": ""})
print(f"\nEmpty verify: {r2.status_code} — {r2.text[:200]}")
