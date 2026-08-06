import urllib.request, json

payload = {
    "verification_code": "moltbook_verify_31e944be8e21b800e97d7d602d5f9690",
    "answer": "46.00"
}

data = json.dumps(payload).encode()
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=data,
    headers={
        "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
        "Content-Type": "application/json"
    },
    method="POST"
)
with urllib.request.urlopen(req, timeout=30) as r:
    print(r.read().decode())
