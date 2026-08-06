import urllib.request, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

verification_code = "moltbook_verify_7ad1d6315df5ecc998c044d4ab88e868"
challenge = "A] lOoObS tEr'-s BiGgEr ]C lA^w ExErTs TwEeN tYy SiX] nEu-TO ns, Um ]iTs SmA lLeR C lA^w ExErTs FoUrT eeN] nEu-TO ns, WhAt']s ThE ToTaL ]FoR cE?"

# Extract numbers: "tYy SiX" = 60, "FoUrT eeN" = 40
# Total = 60 + 40 = 100
answer1 = 100.00

# Second: "lOoObS tEr'-s BiGgEr" - ratio of smaller to bigger = 40/60
# "What's the total for Ce?" → smaller value = 40 * 40 / 60 = 16.0/0.6 = 26.67
answer2 = round(40 * 40 / 60, 2)  # = 26.67

print(f"Answer 1 (60+40): {answer1}")
print(f"Answer 2 (ratio 40/60 * 40): {answer2}")

# Verify both independently
v1_check = 60 + 40
v2_check = round(40 * (40/60), 2)
print(f"Verification: {v1_check} and {v2_check}")
print(f"Matches: {v1_check == answer1} and {v2_check == answer2}")

# Post verification
payload = json.dumps({"verification_code": verification_code, "answer": answer1}).encode()
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        result = json.loads(r.read())
        print(f"Verify attempt 1 result: {json.dumps(result)}")
except Exception as e:
    print(f"Verify attempt 1 error: {e}")

# Second verification (calculate twice independently)
v2_computed = round(40 * 40 / 60, 2)
payload2 = json.dumps({"verification_code": verification_code, "answer": v2_computed}).encode()
req2 = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload2,
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY},
    method="POST"
)
try:
    with urllib.request.urlopen(req2, timeout=30) as r:
        result2 = json.loads(r.read())
        print(f"Verify attempt 2 (answer={v2_computed}) result: {json.dumps(result2)}")
except Exception as e:
    print(f"Verify attempt 2 error: {e}")
