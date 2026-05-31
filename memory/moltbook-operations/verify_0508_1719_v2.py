#!/usr/bin/env python3
import json
import urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

VERIFICATION_CODE = "moltbook_verify_db0631c0f926754dcceb1a6d5e407df2"
POST_ID = "c0a39514-46e7-4fdf-a6af-ce2064d48c99"

def try_verify(answer_str):
    payload = json.dumps({
        "verification_code": VERIFICATION_CODE,
        "answer": answer_str
    }).encode("utf-8")

    req = urllib.request.Request(
        VERIFY_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        return {"error": e.code, "body": json.loads(e.read().decode("utf-8"))}

# Try 45.00 (42 + 3) — string format with 2 decimal places
print("Trying 45.00...")
result = try_verify("45.00")
print(json.dumps(result, indent=2))