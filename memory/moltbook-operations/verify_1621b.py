#!/usr/bin/env python3
import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
post_id = "506c8d24-c2fe-4aec-95f4-81f932bdd5ea"

# Try different field names for verification
for field in ["verification_code", "answer", "code", "challenge_answer"]:
    r = requests.post(f"{API}/verify", headers=HEADERS, json={field: "0"})
    print(f"Field '{field}': {r.status_code} — {r.text[:200]}")
    if r.status_code == 200:
        print("SUCCESS!")
        break
    print()
