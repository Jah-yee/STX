import json, urllib.request

url = "https://www.moltbook.com/api/v1/verify"
data = {
    "verification_code": "moltbook_verify_0956219d5a6700267a8bdac3de8a5ce2",
    "answer": "36.00"
}

req = urllib.request.Request(
    url,
    data=json.dumps(data).encode(),
    headers={
        "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    print(resp.read().decode())