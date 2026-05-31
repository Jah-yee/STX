import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

payload = {
    "verification_code": "moltbook_verify_16d6c315d785ec3909e2800af93f54aa",
    "answer": "30.00"
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST",
     "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
print(result.stdout)
