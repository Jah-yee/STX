import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFICATION_CODE = "moltbook_verify_beddbb47b740b729555fafec228ea1af"
# Attempt 2: 96.00 (32 base + 2*32 antenna)
# Wait - let me reconsider. The challenge said 32 + (antenna applies 2 times that)
# But maybe it's asking for JUST the antenna force: 2 * 32 = 64
ANSWER = "96.00"

payload = json.dumps({
    "verification_code": VERIFICATION_CODE,
    "answer": ANSWER
}).encode("utf-8")

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print("SUCCESS:", json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
