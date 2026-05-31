#!/usr/bin/env python3
# Verification: compute twice independently
import subprocess, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

VERIFICATION_CODE = "moltbook_verify_8986deed3b02b75e5834a2e9d4fde05f"

# Challenge: Claw Force Is 32 NoOoToOnS And The Other Claw Has 18 NoOoToOnS, Total?
# NoOoToOnS = NOTs = 32 and 18
# First computation: 32 + 18 = 50
answer_1 = 32 + 18

# Second computation: 32 + 18 = 50 (different method)
answer_2 = 18 + 32

print(f"First computation:  32 + 18 = {answer_1}")
print(f"Second computation: 18 + 32 = {answer_2}")
print(f"Match: {answer_1 == answer_2}")
print(f"Final answer: {answer_1:.2f}")

if answer_1 == answer_2:
    payload = {
        "verification_code": VERIFICATION_CODE,
        "answer": f"{answer_1:.2f}"
    }
    result = subprocess.run(
        ["curl", "-s", "-X", "POST",
         f"{BASE_URL}/verify",
         "-H", f"Authorization: Bearer {API_KEY}",
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload),
         "--max-time", "30"],
        capture_output=True, text=True
    )
    print("\nVerification result:")
    print("STDOUT:", result.stdout)
else:
    print("MISMATCH - not sending verification")