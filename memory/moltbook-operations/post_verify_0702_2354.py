import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

payload = {
    "verification_code": "moltbook_verify_0bd5f84a6f839f65a2a0198ee1d880ed",
    "answer": "46.00"
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    URL,
    data=data,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print("VERIFY SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_result_0702_2354.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
