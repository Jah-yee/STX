import urllib.request, json, sys

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_581b6fb81ffd66628d704df90845f216"
answer = "28.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(URL, data=payload, method="POST")
req.add_header("Authorization", f"Bearer {API_KEY}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print("SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0606_0909.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.request.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
except Exception as e:
    print("ERROR:", e)
    sys.exit(1)
