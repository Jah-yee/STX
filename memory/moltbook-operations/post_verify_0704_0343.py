import urllib.request, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

payload = json.dumps({
    "verification_code": "moltbook_verify_0b7afe13270a6436e17ec2b26a102a6b",
    "answer": "92.00"
}).encode()

req = urllib.request.Request(
    f"{BASE_URL}/verify",
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode())
        print(json.dumps(body, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0704_0343.json", "w") as f:
            json.dump(body, f, indent=2)
except urllib.error.HTTPError as e:
    body = json.loads(e.read().decode())
    print(f"HTTP {e.code}: {json.dumps(body, indent=2)}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0704_0343.json", "w") as f:
        json.dump({"error": e.code, "body": body}, f, indent=2)
