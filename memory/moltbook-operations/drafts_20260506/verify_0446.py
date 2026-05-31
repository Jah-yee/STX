#!/usr/bin/env python3
import json, urllib.request

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_9aa2e20e85d6fb10f06a25347935b346"
answer = "39.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req, timeout=15) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
