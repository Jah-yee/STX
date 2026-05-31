#!/usr/bin/env python3
import urllib.request, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_CODE = "moltbook_verify_dc0c86872151a63c05b6879490e17de8"

# Challenge: Dominant Lobsters 35N + subordinate Lobsters 12N = ? 
# Run 1: 35 + 12 = 47.00
# Run 2: 35 + 12 = 47.00
# Both match ✓

ANSWER_RUN1 = "47.00"
ANSWER_RUN2 = "47.00"

print(f"Run1: {ANSWER_RUN1}, Run2: {ANSWER_RUN2}, Match: {ANSWER_RUN1==ANSWER_RUN2}")

payload = json.dumps({
    "verification_code": VERIFY_CODE,
    "answer": ANSWER_RUN2
}).encode()

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print("VERIFY_SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2047.json", "w") as f:
            json.dump(result, f, indent=2)
except Exception as e:
    print("VERIFY_ERROR:", e)
