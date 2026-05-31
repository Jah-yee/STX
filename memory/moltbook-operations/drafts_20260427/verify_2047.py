import json, urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

verif_code = "moltbook_verify_82a9c6be7f17b0d471615e3b09004dc6"
answer = "16.00"

payload = json.dumps({"verification_code": verif_code, "answer": answer}).encode()
req = urllib.request.Request(
    f"{API}/verify",
    data=payload,
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260427/verify_result_2047.json", "w") as f:
        json.dump(result, f, indent=2)
