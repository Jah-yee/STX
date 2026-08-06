import subprocess, json

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt") as f:
    api_key = f.read().strip()

verification_code = "moltbook_verify_8648b351298b8a6f95b808a1b83d04d9"
answer = "28.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {api_key}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)

print("STDOUT:", result.stdout)
try:
    resp = json.loads(result.stdout)
    print(json.dumps(resp, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0619_2039.json", "w") as f:
        json.dump(resp, f, indent=2)
except:
    pass
