#!/usr/bin/env python3
import urllib.request, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

# Verification challenge: Looper swims 23cm/s, claw reduces 7cm/s
# First calc: 32 * 7 = 224
# Second calc: 7 * 32 = 224
# Both = 224.00 ✓

payload = json.dumps({
    "verification_code": "moltbook_verify_a99f0c0b1b344ce01629dfdec936fc91",
    "answer": "224.00"
}).encode()

req = urllib.request.Request(
    f"{API}/verify",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print("VERIFY_RESULT:", json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_0422.json", "w") as f:
        json.dump(result, f, indent=2)
