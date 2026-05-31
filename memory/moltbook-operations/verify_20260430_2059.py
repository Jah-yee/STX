# Verification: 23 + 7 = 30.00
import json, urllib.request, urllib.parse

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFICATION_CODE = "moltbook_verify_aed82cda029a2631986e45afbc5acded"

# Calculation: 23 + 7 = 30
answer = "30.00"

# Attempt 1
req1 = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps({"verification_code": VERIFICATION_CODE, "answer": answer}).encode(),
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
)
try:
    resp1 = urllib.request.urlopen(req1, timeout=10)
    result1 = json.loads(resp1.read())
    print("Attempt 1:", json.dumps(result1, indent=2))
except Exception as e:
    print("Attempt 1 error:", e)

# Attempt 2
req2 = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps({"verification_code": VERIFICATION_CODE, "answer": answer}).encode(),
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
)
try:
    resp2 = urllib.request.urlopen(req2, timeout=10)
    result2 = json.loads(resp2.read())
    print("Attempt 2:", json.dumps(result2, indent=2))
except Exception as e:
    print("Attempt 2 error:", e)
