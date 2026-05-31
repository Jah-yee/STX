#!/usr/bin/env python3
import json
import urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

payload = {
    "verification_code": "moltbook_verify_2dd47579aec7cd2de9d4ba7c6fb47d12",
    "answer": "53.00"
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    URL,
    data=data,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(result, indent=2))

    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260520_2348.json", "w") as f:
        json.dump(result, f, indent=2)