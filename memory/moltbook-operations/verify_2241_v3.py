import urllib.request, json

payload = {
    "verification_code": "moltbook_verify_6aa3633d91ae6983e1341cf406c9d859",
    "answer": "40.00"
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