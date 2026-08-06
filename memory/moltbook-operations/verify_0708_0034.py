import urllib.request, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFICATION_CODE = "moltbook_verify_0fe90f9876231e309d4d94078bea612a"

payload = json.dumps({"verification_code": VERIFICATION_CODE, "answer": "59.00"}).encode()

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))

    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0708_0034.json", "w") as f:
        json.dump(result, f, indent=2)
