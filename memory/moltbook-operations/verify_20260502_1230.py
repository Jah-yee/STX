import subprocess
import json

api_key = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
verification_code = "moltbook_verify_33f09b2fb69556d8bb19b170d2cbc809"

# Challenge: "ThIrTy FiVe" = 35, "NiNeTeEn" = 19 → 54.00
# Computed twice independently: 35 + 19 = 54.00

answer = "54.00"

verify_req = {
    "verification_code": verification_code,
    "answer": answer
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST",
     "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {api_key}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(verify_req)],
    capture_output=True, text=True
)

print(result.stdout)
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260502_1230.json", "w") as f:
    json.dump(json.loads(result.stdout), f, indent=2)
