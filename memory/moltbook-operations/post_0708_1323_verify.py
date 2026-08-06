import subprocess, json

api_key = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

payload = {
    "verification_code": "moltbook_verify_83f3804bf6325cb41ff38aa47df1a7c8",
    "answer": "60.00"
}

result = subprocess.run([
    "curl", "-s", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", f"Authorization: Bearer {api_key}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True)

print(result.stdout)

# Save result
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/draft_0708_1323_verify.json", "w") as f:
    f.write(result.stdout)
