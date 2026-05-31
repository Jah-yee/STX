#!/usr/bin/env python3
import json, subprocess

VERIFICATION_CODE = "moltbook_verify_c79abc95130a0bb8537f1cc5114d84ed"
ANSWER = "35.00"

result = subprocess.run([
    "curl", "-s", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", "Authorization: Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
    "-H", "Content-Type: application/json",
    "-d", json.dumps({"verification_code": VERIFICATION_CODE, "answer": ANSWER})
], capture_output=True, text=True)

print(result.stdout)
