import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"
POST_ID = "8aba01c8-3af8-493f-ae22-6ae28e678410"

# Challenge: "A] LoBsTeR PuShEs WiTh ThIrTy TwO^ NeWtOnS- AnD GaAiNs TwElVe~ NeWtOnS, WhAt Is ToTaL} FoRcE?"
# "Thirty Two + Twelve" (with noise)
# 32 + 12 = 44.00

print("Challenge: Thirty Two + Twelve = ?")
print()

# First calculation
n1 = 32
n2 = 12
ans1 = n1 + n2
print(f"First calc: {n1} + {n2} = {ans1}")

# Second calculation (independent)
n1b = 32
n2b = 12
ans2 = n1b + n2b
print(f"Second calc: {n1b} + {n2b} = {ans2}")

print()
if ans1 == ans2:
    print(f"✅ Verified match: {ans1} == {ans2}")
    print(f"Sending POST /api/v1/verify with code: {ans1}.00")
    
    resp = requests.post(
        f"{BASE_URL}/verify",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"post_id": POST_ID, "verification_code": f"{ans1}.00"}
    )
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text[:500]}")
    
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260521_2254.json", "w") as f:
        json.dump(resp.json(), f, indent=2)
else:
    print(f"❌ MISMATCH: {ans1} != {ans2} — not sending")
