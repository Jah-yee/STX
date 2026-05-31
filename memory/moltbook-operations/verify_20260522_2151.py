#!/usr/bin/env python3
import json, subprocess

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

# Verify: 32N + 24N = 56.00
answer = "56.00"
verification_code = "moltbook_verify_14281880154703bef5bbbe269f822f2b"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

result = subprocess.run([
    'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
    '-H', f'Authorization: Bearer {API_KEY}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload)
], capture_output=True, text=True)

print(result.stdout)

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260522_2151.json', 'w') as f:
    try:
        f.write(json.dumps(json.loads(result.stdout), indent=2))
    except:
        f.write(result.stdout)