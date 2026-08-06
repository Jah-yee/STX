import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verify_payload = {
    "verification_code": "moltbook_verify_63c0468befb9e626cdfaae0de1f13205",
    "answer": "59.00"
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(verify_payload)],
    capture_output=True, text=True
)

print("STDOUT:", result.stdout)

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0608_2049.json", "w") as f:
    f.write(result.stdout)