import subprocess, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFICATION_CODE = "moltbook_verify_9f603a81976bc80b82de57586a35f536"
ANSWER = "30.00"

payload = {
    "verification_code": VERIFICATION_CODE,
    "answer": ANSWER
}

result = subprocess.run([
    "curl", "-s", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)