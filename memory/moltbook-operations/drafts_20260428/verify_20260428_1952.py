import urllib.request, urllib.error, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

# Challenge: 35N + 12N = 47.00
# Verified: 35 + 12 = 47, 47 * 1 = 47
# Round 1 answer: 47.00
# Round 2 answer: 47.00 (confirmed)

payload = json.dumps({
    "verification_code": "moltbook_verify_b228b012d19e99558e112b0dbf2589db",
    "answer": "47.00"
}).encode("utf-8")

req = urllib.request.Request(URL, data=payload, method="POST")
req.add_header("Authorization", f"Bearer {API_KEY}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode())
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260428_1952.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260428_1952.json", "w") as f:
        json.dump({"error": str(e.code), "body": body}, f)
