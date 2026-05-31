#!/usr/bin/env python3
import json, urllib.request

API_KEY = open('/home/ubuntu/.openclaw/workspace/.moltbook_token').read().strip()
code = "moltbook_verify_476db8f510ea05b8662b6569c8e56271"
answer = "40.00"

url = "https://www.moltbook.com/api/v1/verify"
payload = json.dumps({"verification_code": code, "answer": answer}).encode()
req = urllib.request.Request(url, data=payload, method='POST')
req.add_header('Authorization', f'Bearer {API_KEY}')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print('Verify success:', result.get('success'))
        print('Full result:', json.dumps(result, indent=2))
        with open('verify_result_20260429_2359b.json', 'w') as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print('HTTP Error:', e.code, e.reason, body)
except Exception as e:
    print('Error:', e)
