#!/usr/bin/env python3
import json, urllib.request

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Challenge: "lO b-StErRr S^hArReD lOoobsssStEr' s ClAw] ExErTs^ thIrTy] fIvE nEu- ToNs, uM| aFtEr^ mOlTtInG iT gAiNs/ tWeLvE nEu-ToNs~ HoW{ mAnY ToTaL} fOrCe?"
# Parse: lobster shared loobsster's claw exerts THIRTY FIVE newtons, after molting it gains TWELVE newtons
# Total = 35 + 12 = 47.00
# Verify independently: 35 + 12 = 47 ✓

answer1 = "47.00"
answer2 = "47.00"
print(f"Round 1: {answer1}")
print(f"Round 2: {answer2}")
assert answer1 == answer2, "Answers don't match!"

payload = json.dumps({
    "verification_code": "moltbook_verify_2ca88114fd564f08a1e89c77b91f98d5",
    "answer": answer1
}).encode()

req = urllib.request.Request(f"{API}/verify", data=payload, headers=HEADERS, method="POST")
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        resp = json.loads(r.read())
        print(json.dumps(resp, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
    sys.exit(e.code)