import json, urllib.request, urllib.error

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

payload = {
    "verification_code": "moltbook_verify_187d97df64bac86f10f8344ae035cc6a",
    "answer": "30.00"
}

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260527_2230.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260527_2230_error.json", "w") as f:
        json.dump({"error": str(e.code), "body": body}, f)