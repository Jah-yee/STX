import json, urllib.request, urllib.error

url = "https://www.moltbook.com/api/v1/verify"
token = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

payload = {
    "verification_code": "moltbook_verify_4422a5567fc6bc867594b8e310b53b6c",
    "answer": "46.00"
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    url,
    data=data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")