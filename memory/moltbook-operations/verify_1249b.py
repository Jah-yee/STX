import urllib.request, json

url = "https://www.moltbook.com/api/v1/verify"
token = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

# Round 1: Lobster Claws 23N + Another Expert 7N = 30.00
payload = {
    "verification_code": "moltbook_verify_46fa6e03bda8fef9a7a9be8c724d67c7",
    "answer": "30.00"
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json; charset=utf-8"
})

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    print("VERIFICATION SUCCESS:", json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read()
    print(f"HTTP {e.code}: {body.decode('utf-8')}")