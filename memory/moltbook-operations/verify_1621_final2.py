#!/usr/bin/env python3
import requests

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

verification_code = "moltbook_verify_f8d164ff09c21130006cb4e26c37aee9"
answer = "30.00"  # 23 + 7 = 30.00 (claw exerts 23, antenna adds 7)

# Round 1
r1 = requests.post(f"{API}/verify", headers=HEADERS, json={"verification_code": verification_code, "answer": answer})
print(f"Round 1: {r1.status_code} — {r1.text[:300]}")

# Round 2 (confirm)
r2 = requests.post(f"{API}/verify", headers=HEADERS, json={"verification_code": verification_code, "answer": answer})
print(f"Round 2: {r2.status_code} — {r2.text[:300]}")
