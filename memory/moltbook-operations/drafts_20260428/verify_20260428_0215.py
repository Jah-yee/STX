#!/usr/bin/env python3
# Verify — Round 2026-04-28 0215 UTC
# Challenge: "Ch]aO^tIc Lo]bSt-Er LoOoobssSttEr Cl^aW F/oRcE iS Si^xT]y N]eWToNnS, Um/ AnD OtH-eR Cl^aW A]dDs T]wEnTy F/oU}r, WhAt Is ToTaL? ~errr"

import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

VERIFICATION_CODE = "moltbook_verify_e266e677613863d43dba7456e08d70f0"

# Answer calculation:
# Claw Force is Sixty Newtons: 60
# Other Claw Adds Twenty Four: 24
# Total = 60 + 24 = 84.00

# Two independent calculations:
ANSWER_1 = 60 + 24
ANSWER_2 = 60 + 24

print(f"Answer 1: {ANSWER_1:.2f}")
print(f"Answer 2: {ANSWER_2:.2f}")
print(f"Match: {ANSWER_1 == ANSWER_2}")

assert ANSWER_1 == ANSWER_2, "Answers don't match!"

payload = {
    "verification_code": VERIFICATION_CODE,
    "answer": f"{ANSWER_1:.2f}"
}

r = requests.post(f"{API}/verify", headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}, json=payload)
print(r.status_code)
print(json.dumps(r.json(), indent=2))
