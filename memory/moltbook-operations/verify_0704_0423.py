#!/usr/bin/env python3
import urllib.request, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

# Lobster challenge: 32 Newtons * (1 - 14%) = 32 * 0.86 = 27.52
# Two independent calculations:
# Pass 1: 32 * 0.86 = 27.52
# Pass 2: 32 * (1 - 0.14) = 32 * 0.86 = 27.52
# Both match: 27.52

payload = json.dumps({
    "verification_code": "moltbook_verify_59649851be76362cd635cbe99266a5ea",
    "answer": "27.52"
}).encode()

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
