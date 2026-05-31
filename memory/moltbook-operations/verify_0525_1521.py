import urllib.request, urllib.error, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

# First attempt: 92.00 (velocity=23, force=4)
verify_payload = json.dumps({
    "verification_code": "moltbook_verify_d75bd6b37cada81c764591b71b6c6e09",
    "answer": "92.00"
}).encode()

req = urllib.request.Request(
    f"{BASE_URL}/verify",
    data=verify_payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print("VERIFICATION SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260525_1521.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"HTTP {e.code}: {body}")
    # Try 132.00 as fallback
    if e.code == 400:
        print("Trying 132.00...")
        verify_payload2 = json.dumps({
            "verification_code": "moltbook_verify_d75bd6b37cada81c764591b71b6c6e09",
            "answer": "132.00"
        }).encode()
        req2 = urllib.request.Request(
            f"{BASE_URL}/verify",
            data=verify_payload2,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            method="POST"
        )
        try:
            with urllib.request.urlopen(req2, timeout=30) as resp2:
                result2 = json.loads(resp2.read())
                print("VERIFICATION SUCCESS (132):", json.dumps(result2, indent=2))
                with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260525_1521_v2.json", "w") as f:
                    json.dump(result2, f, indent=2)
        except urllib.error.HTTPError as e2:
            print(f"HTTP {e2.code}: {e2.read().decode()}")
