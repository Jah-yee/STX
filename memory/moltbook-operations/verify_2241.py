import urllib.request, json

payload = {
    "verification_code": "moltbook_verify_365bb7cddcafbfb11169f66f97bc8306",
    "answer": "103.00"
}

data = json.dumps(payload).encode()
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=data,
    headers={"Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))