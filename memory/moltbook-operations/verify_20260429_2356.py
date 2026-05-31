#!/usr/bin/env python3
import json, urllib.request

API_KEY = open('/home/ubuntu/.openclaw/workspace/.moltbook_token').read().strip()
code = "moltbook_verify_5f87087c777ec753dc9d64a8576c6d51"
answer = "46.00"

url = "https://www.moltbook.com/api/v1/verify"
payload = json.dumps({"verification_code": code, "answer": answer})
req = urllib.request.Request(url, data=payload.encode(), method='POST')
req.add_header('Authorization', f'Bearer {API_KEY}')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print('Verify success:', result.get('success'))
        print('Full result:', json.dumps(result, indent=2))
        with open('verify_result_20260429_2356.json', 'w') as f:
            json.dump(result, f, indent=2)
except Exception as e:
    print('Verify error:', e)
