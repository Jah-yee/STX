import json, urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_0f159b62de13159a71658d01331cd077"
answer = "47.00"

# Independent calculation 1: 35 + 12 = 47
calc1 = 35 + 12
print(f"Calc 1: 35 + 12 = {calc1}")

# Independent calculation 2: 35 + 12
calc2 = 35 + 12
print(f"Calc 2: 35 + 12 = {calc2}")

assert calc1 == calc2 == 47, f"Mismatch: {calc1} vs {calc2}"
print(f"✓ Both calculations agree: {calc1}")

payload = json.dumps({"verification_code": verification_code, "answer": answer}).encode()
req = urllib.request.Request(VERIFY_URL, data=payload, headers={"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY}, method="POST")
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read().decode())
    print(json.dumps(result, indent=2))
