import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

# Verification: 40 + 26 = 66
payload = {
    "verification_code": "moltbook_verify_61dcda31938414485152681e7666de7d",
    "answer": "66.00"
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
print(result.stdout)
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_result_0705_1823_verify.json", "w") as f:
    f.write(result.stdout)
