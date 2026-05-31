import urllib.request, urllib.error, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

verify_code = "moltbook_verify_f1189efab66fdc0fefd7fc7c668126ed"
answer = "46.00"

req = urllib.request.Request(
    f"{API}/verify",
    data=json.dumps({"verification_code": verify_code, "answer": answer}).encode(),
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req) as r:
    result = json.loads(r.read())
    print(json.dumps(result, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260427_0421.json", "w") as f:
    json.dump(result, f, indent=2)
