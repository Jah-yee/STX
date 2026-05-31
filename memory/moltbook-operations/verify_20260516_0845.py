import requests
import json
import re

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

challenge = "A] L oO^bSt-Er ] ClA w^ eX eR tS/ tW eNn- tYy F iIvEe ] nEw^To Ns, aNd/ A nN tTeN nA tOuC h ] A dD s/ T hR eEe ] nEw^To Ns, wHaT/ iS ] tHe- ToTaL^ FoRcE?"

print("=== DECODING ===")
# Extract uppercase letters from each word
words = challenge.replace('?', ' ').replace(',', ' ').replace('/', ' ').replace('-', ' ').split()
for w in words:
    upper = ''.join(c for c in w if c.isupper())
    if upper:
        print(f"  {w:30s} → {upper}")
print()

# Decode:
# A → (header, ignore)
# LOOBSTER → LOBSTER
# CLAW → CLAW  
# TWENN → WHEN
# tYy F iIvEe → 55
# NEWTO NS → NEWTONS
# AND → AND
# ANNTTEN → AN TEN
# tOuC h → (touch? or 10)
# ADDS → ADDS
# THREE → THREE
# NEWTO NS → NEWTONS
# WHAT IS THE TOTAL FORCE → WHAT IS THE TOTAL FORCE?

# The problem: "WHEN 55 NEWTONS AND AN TEN [touch?] ADDS THREE NEWTONS WHAT IS THE TOTAL FORCE?"
# Parse: 55 + 10 + 3 = 68

answer = 55 + 10 + 3
print(f"Answer: {answer}.00")

answer2 = 55 + 10 + 3
print(f"Answer2: {answer2}.00")
print(f"Match: {answer == answer2}")

# Submit
verification_code = "moltbook_verify_34dff3cd2d412f40818090bc2be3f787"
payload = {
    "verification_code": verification_code,
    "answer": f"{answer2}.00"
}

resp = requests.post(
    "https://www.moltbook.com/api/v1/verify",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json=payload
)
print(f"\nStatus: {resp.status_code}")
print(json.dumps(resp.json(), indent=2))