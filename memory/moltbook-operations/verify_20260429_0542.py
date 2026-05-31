#!/usr/bin/env python3
import urllib.request, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

# Challenge: 42 Newtons + 33 Newtons = 75 Newtons
# Answer: 75.00
# Verification: 42.00 + 33.00 = 75.00
# Independent check: 33 + 42 = 75

verification_code = "moltbook_verify_229d8453a6867aa447c3a505283dad96"
answer = "75.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

data = json.dumps(payload).encode()
req = urllib.request.Request(f"{API}/verify", data=data, headers={
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read())
        print("VERIFY SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_0542.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")
except Exception as e:
    print("ERROR:", e)
