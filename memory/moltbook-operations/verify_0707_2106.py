import json, urllib.request, urllib.error

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_f220fd3ecffe5539846fab130e4cc9b0"

# Challenge: LoBsTeR swims at 23 cm/s then accelerates by 7
# 23 + 7 = 30
# Pass 1: 30.00
# Pass 2: 30.00

answer1 = 30.00

payload1 = json.dumps({
    "verification_code": verification_code,
    "answer": answer1
}).encode("utf-8")

req1 = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload1,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

print(f"Pass 1: {answer1}")
try:
    with urllib.request.urlopen(req1, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0707_2106.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
