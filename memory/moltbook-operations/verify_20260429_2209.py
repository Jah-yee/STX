import json, urllib.request

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# verification_code from post response
verification_code = "moltbook_verify_92cbbf576f3c1226f8e0f6e08f8721a4"

# Challenge: Lobster applies 23 newtons + another claw adds 7 → 23 + 7 = 30.00
# Compute twice for verification:
# Pass 1: 23 + 7 = 30
# Pass 2: 23 + 7 = 30
# Both match: 30.00

answer_1 = 23 + 7
answer_2 = 23 + 7

print(f"Pass 1: 23 + 7 = {answer_1}")
print(f"Pass 2: 23 + 7 = {answer_2}")
print(f"Consistent: {answer_1 == answer_2}")

answer = f"{answer_1:.2f}"
print(f"Answer to submit: {answer}")

body = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode()

req = urllib.request.Request(
    f"{API}/verify",
    data=body,
    headers=HEADERS,
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))

    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_request_20260429_2209.json", "w") as f:
        json.dump({"verification_code": verification_code, "answer": answer}, f)

    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2209.json", "w") as f:
        json.dump(result, f)