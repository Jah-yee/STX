#!/usr/bin/env python3
import json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_f2b78a2d0f742e052a8fddca42214d23"

# Challenge: 35 Newtons + 12 Newtons = 47 Newtons
answer = "47.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

import urllib.request
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read())
        print(json.dumps(body, indent=2))
except urllib.error.HTTPError as e:
    body = json.loads(e.read())
    print(json.dumps(body, indent=2))
