#!/usr/bin/env python3
import requests, json, re, time

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
post_id = "63098301-6502-4bf8-addc-378ea0d2501c"

# Try answer without verification_code
r = requests.post(f"{API}/verify", headers=HEADERS, json={"answer": "0.00"})
print(f"Ans only: {r.status_code} — {r.text[:200]}")

# Try with the post_id as verification_code
r2 = requests.post(f"{API}/verify", headers=HEADERS, json={"verification_code": post_id, "answer": "0.00"})
print(f"PostID as code: {r2.status_code} — {r2.text[:200]}")

# Check what fields the /verify endpoint accepts
r3 = requests.post(f"{API}/verify", headers=HEADERS, json={})
print(f"Empty: {r3.status_code} — {r3.text[:200]}")
