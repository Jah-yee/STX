#!/usr/bin/env python3
import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_7bfebb7ad830daf98b09439352a2a207"
answer = "47.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode()

req = urllib.request.Request(
    URL,
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode()
        result = json.loads(body)
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/verify_0727_1936_result.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTPError {e.code}: {body}")
except Exception as e:
    print(f"Error: {e}")
