import json, urllib.request

url = "https://www.moltbook.com/api/v1/verify"
payload = {
    "verification_code": "moltbook_verify_7315723ae15837754e5d1a4bfa006ee2",
    "answer": "30.00"
}

data = json.dumps(payload).encode()
req = urllib.request.Request(
    url,
    data=data,
    headers={
        "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/draft_0730_0642_verify.json", "w") as f:
        json.dump(result, f, indent=2)
