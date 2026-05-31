import urllib.request, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

payload = json.dumps({
    "verification_code": "moltbook_verify_834bef58841fe3c9deac2ec7c34f42d0",
    "answer": "33.00"
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

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(result, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_1406.json", "w") as f:
    json.dump(result, f, indent=2)
