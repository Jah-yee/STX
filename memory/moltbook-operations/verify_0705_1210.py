import urllib.request, urllib.error, json, sys

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_5eaaa91cc19debebdff3ab4c38d17311"
# Left claw ThIrTy tWo = 32N; Right claw FoUrTeEn = 14N; combined = 32 + 14 = 46
answer = "46.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    VERIFY_URL,
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        result = json.loads(body)
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0705_1210.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
    sys.exit(1)
