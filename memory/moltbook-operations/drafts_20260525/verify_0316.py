#!/usr/bin/env python3
import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_f3ab8995155f58dedc2f97f28117d468"
answer = "13.00"

payload = json.dumps({"verification_code": verification_code, "answer": answer})
cmd = ['curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
       '-H', f'Authorization: Bearer {API_KEY}',
       '-H', 'Content-Type: application/json',
       '-d', payload]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stdout)