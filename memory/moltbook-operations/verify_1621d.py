#!/usr/bin/env python3
import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
post_id = "506c8d24-c2fe-4aec-95f4-81f932bdd5ea"

# Try both fields together
r = requests.post(f"{API}/verify", headers=HEADERS, json={"verification_code": "test", "answer": "0"})
print(f"Status: {r.status_code}")
print(r.text[:500])

# Try to find challenge from a verify endpoint with challenge info
r2 = requests.get(f"{API}/verify/{post_id}", headers=HEADERS)
print(f"\nGET verify/{post_id}: {r2.status_code}")
print(r2.text[:500])
