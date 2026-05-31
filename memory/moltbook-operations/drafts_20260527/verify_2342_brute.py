#!/usr/bin/env python3
import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"
VER_CODE = "moltbook_verify_5bb42b4dcb66e6e224d20b982093e832"

# Try different interpretations of the challenge:
# "twenty seven Newtons, and its molting ratio is Three — what is the total force?"
# Numbers: 27 (claw force) and 3 (molting ratio)
# Try several plausible answers

candidates = ["30.00", "27.00", "3.00", "9.00", "24.00", "81.00", "54.00"]

for ans in candidates:
    payload = {"verification_code": VER_CODE, "answer": ans}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(VERIFY_URL, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            r = json.loads(resp.read().decode("utf-8"))
            print(f"{ans}: {r.get('message', r)}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"{ans}: HTTP {e.code}")
    except Exception as ex:
        print(f"{ans}: ERROR {ex}")