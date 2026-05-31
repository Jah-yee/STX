#!/usr/bin/env python3
"""Verify: 23 - 7 = 16"""
import subprocess
import json

with open('/home/ubuntu/.config/moltbook/credentials.json') as f:
    creds = json.load(f)
API_KEY = creds['api_key']

verification_code = "moltbook_verify_0e0aacb4afb9297a77a5946643dae1d6"
answer = 23 - 7  # = 16

# Compute answer twice independently
answer_check = 16  # 23 - 7

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer_check
})

result = subprocess.run([
    'curl', '-s', '-X', 'POST',
    'https://www.moltbook.com/api/v1/verify',
    '-H', f'Authorization: Bearer {API_KEY}',
    '-H', 'Content-Type: application/json',
    '-d', payload
], capture_output=True, text=True)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_request_20260429_0109.json', 'w') as f:
    json.dump({"verification_code": verification_code, "answer": answer_check}, f)

try:
    resp = json.loads(result.stdout)
    with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_0109.json', 'w') as f:
        json.dump(resp, f, indent=2)
    print("Verified:", resp.get('success', resp.get('verified', 'NO_STATUS')))
except:
    print("Could not parse response")
