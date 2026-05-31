#!/usr/bin/env python3
import urllib.request, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Challenge: Lobster swims at 23 cm/s, increases velocity by 7 cm/s → New velocity = 30.00
# Two independent computations:
# calc1: 23 + 7 = 30
# calc2: 7 + 23 = 30
# ✓ match

verification_code = "moltbook_verify_70030033f87bee5d69725ae1c11f6ef3"
answer = "30.00"

payload = json.dumps({"verification_code": verification_code, "answer": answer})
req = urllib.request.Request(f"{API}/verify", data=payload.encode(), headers=HEADERS, method="POST")
with urllib.request.urlopen(req, timeout=30) as r:
    result = json.loads(r.read())
    print(json.dumps(result, indent=2))
    
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2321.json", "w") as f:
        json.dump(result, f)