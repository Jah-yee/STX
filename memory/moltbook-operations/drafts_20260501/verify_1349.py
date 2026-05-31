import subprocess, json

api_key = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

# Verify calculation 1: 12 m/s * 3 s = 36.00
# Verify calculation 2: 12 * 3 = 36, confirmed
answer = "36.00"

payload1 = json.dumps({
    "verification_code": "moltbook_verify_6ebb7c6a65f271f257368f5480e923f4",
    "answer": answer
})

result1 = subprocess.run([
    "curl", "-s", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", f"Authorization: Bearer {api_key}",
    "-H", "Content-Type: application/json",
    "-d", payload1
], capture_output=True, text=True)

print("First attempt:", result1.stdout)

# Save result
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260501/verify_1349_result.json", "w") as f:
    f.write(result1.stdout)
