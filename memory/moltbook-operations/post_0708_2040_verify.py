import urllib.request
import json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

payload = json.dumps({
    "verification_code": "moltbook_verify_f1e0c028d7472a543a812dfc403f46e1",
    "answer": "31.00"
}).encode("utf-8")

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
        body = resp.read().decode("utf-8")
        result = json.loads(body)
        print("VERIFY SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/draft_0708_2040_verify.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print("HTTP ERROR", e.code, body)
except Exception as e:
    print("ERROR:", e)
