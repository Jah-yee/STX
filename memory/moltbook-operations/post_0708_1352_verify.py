import json, urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFICATION_CODE = "moltbook_verify_6018f7c505e8abd0303bb3e0207258d4"
ANSWER = "207.00"

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

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(result, indent=2))
