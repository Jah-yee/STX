import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE = "https://www.moltbook.com/api/v1"

# Lobster-math: Twenty-three + Seven = 30
answer = "30.00"
verification_code = "moltbook_verify_3fa5ed73bd3adbb63b9951f93382fdf3"

payload = json.dumps({"verification_code": verification_code, "answer": answer})
req = urllib.request.Request(
    f"{BASE}/verify",
    data=payload.encode(),
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print(json.dumps(result, indent=2))
        with open("verify_result_0627_1842.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"Error: {e}")
