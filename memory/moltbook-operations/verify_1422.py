#!/usr/bin/env python3
import json

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt') as f:
    api_key = f.read().strip()

verification_code = "moltbook_verify_d32356fd14b33168c73f69ba2a910d49"

# Challenge: LoOoBbSsTt-Er S^wIiMmS [aT tWeNtY ThReE] cEeNnTtIiMeTeRrS } aNd- SpEeEeDdS U^p By [FfIiVvEeE]
# Pattern: "Twenty Three" = 23, "Five" = 5
# Answer: 23 + 5 = 28.00

answer = 28.00
payload = {
    "verification_code": verification_code,
    "answer": f"{answer:.2f}"
}

import urllib.request
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result))
