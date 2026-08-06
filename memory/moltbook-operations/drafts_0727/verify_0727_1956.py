#!/usr/bin/env python3
import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_cea0896a0035f04d7500ec9c5703ec42"
answer = "30.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    VERIFY_URL,
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        result = json.loads(body)
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/verify_0727_1956_result.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/verify_0727_1956_result.json", "w") as f:
        json.dump({"error": e.code, "body": body}, f, indent=2)
except Exception as ex:
    print(f"Error: {ex}")
