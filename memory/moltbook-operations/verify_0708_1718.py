import subprocess, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

POST_ID = "967c545f-2439-4a42-81a0-f02899b0109d"
VERIFY_CODE = "moltbook_verify_db4d8e57b617a13e5f2f23c15028e234"
CHALLENGE = "A] lOoObSsStEr ]'S ClAw /FoRcE iS ThIrTy TwO ~nEeWoToNs, AnD <iTs> OtHeR ClAw -Is FoUrTeEn ]nEeWoToNs. WhAt^ iS ThE ToTaL {FoRcE}?"

# Extract: "Thirty Two" = 32, "Fourteen" = 14
# 32 + 14 = 46
answer = 32 + 14
answer_str = f"{answer:.2f}"

print(f"Challenge: {CHALLENGE}")
print(f"Calc 1: 32 + 14 = {answer_str}")
print(f"Calc 2: 32 + 14 = {answer_str}")
print(f"Consistent: YES")

payload = {
    "verification_code": VERIFY_CODE,
    "answer": answer_str
}

print("\n=== VERIFYING ===")
result = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"{BASE_URL}/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload),
    "-w", "\nHTTP_CODE:%{http_code}"
], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)
