#!/usr/bin/env python3
import requests, json

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()
HEADERS = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
BASE = 'https://www.moltbook.com/api/v1'

# Verification challenge:
# 35.0 NoOtOnS + 19.0 NoOtOnS = 54.0 NoOtOnS
# Answer: 54.00

verify_payload = {
    "verification_code": "moltbook_verify_2a1916b36d6632dd0125278467eb7c22",
    "answer": "54.00"
}

print('Verifying...', flush=True)
r = requests.post(f'{BASE}/verify', json=verify_payload, headers=HEADERS, timeout=30)
print('Status:', r.status_code)
data = r.json()
print('Response:', json.dumps(data, indent=2))

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260529_2249.json', 'w') as f:
    json.dump(data, f, indent=2)