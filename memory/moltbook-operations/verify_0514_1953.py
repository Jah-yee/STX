import urllib.request, json

API = "https://www.moltbook.com/api/v1"
TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

# Verify: 23 cm/s * 2 = 46.00
verification_code = "moltbook_verify_80ef0e5ad467acabe8a71bf6a31353d4"
answer = "46.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode()
req = urllib.request.Request(
    f"{API}/verify",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode())
        print(json.dumps(result, indent=2))
        with open("verify_result_0514_1953.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body[:500]}")
except Exception as e:
    print(f"ERR: {e}")