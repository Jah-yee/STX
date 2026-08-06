#!/usr/bin/env python3
import json, urllib.request, urllib.error

API_BASE = "https://www.moltbook.com/api/v1"
TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

verify_code = "moltbook_verify_6a29f6b0ed6f2cd345ac77e5185e0dfe"
answer = "30.00"

payload = json.dumps({
    "verification_code": verify_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    f"{API_BASE}/verify",
    data=payload,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print("VERIFICATION RESULT:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260630_0621.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260630_0621.json", "w") as f:
        json.dump({"error": f"HTTP {e.code}", "body": body}, f, indent=2)
