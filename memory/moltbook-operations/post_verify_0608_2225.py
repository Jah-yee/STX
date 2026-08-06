import json, urllib.request

api_key = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
url = "https://www.moltbook.com/api/v1/verify"
verification_code = "moltbook_verify_f9bb984c7e107875184641327877a926"
answer = "19.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST")
req.add_header("Authorization", f"Bearer {api_key}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0608_2225.json", "w") as f:
            json.dump(result, f, indent=2)
except Exception as e:
    print(f"ERROR: {e}")