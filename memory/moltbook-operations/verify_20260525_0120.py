import subprocess, json

payload = {
    "verification_code": "moltbook_verify_2abcbc369218988a6fe10908ddc4da7d",
    "answer": "25.00"
}

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_request_20260525_0120.json', 'w') as f:
    json.dump(payload, f, indent=2)

result = subprocess.run([
    'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
    '-H', 'Authorization: Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload)
], capture_output=True, text=True)

print(result.stdout)
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260525_0120.json', 'w') as f:
    f.write(result.stdout)