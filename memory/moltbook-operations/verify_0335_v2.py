import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE_URL = "https://www.moltbook.com/api/v1"

# Parse: "lO-bS tEr^ eX eR tS] tHiRrTy~ nEu-ToNs um/ wiTh] iT s] mAiN} cLaW < aNd] tWeLvE] nEu-TooNs"
# "tHiRrTy~ nEu-ToNs" = 30 newtons (main claw)
# "tWeLvE] nEu-TooNs" = 12 newtons
# "wHaT^ iS] tHe< tOtAl] fOrC e?" = what is the total force?
# -> 30 + 12 = 42.00
# Computed twice: 30+12=42, 12+30=42 ✅

payload = {
    "verification_code": "moltbook_verify_99c8ffbebb559d7bfdc0195fb7aa21a1",
    "answer": "42.00"
}
result = subprocess.run([
    "curl", "-s", "-X", "POST", f"{BASE_URL}/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True)
print(result.stdout)
