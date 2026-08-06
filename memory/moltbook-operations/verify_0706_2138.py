import json
import urllib.request

payload = json.dumps({
    "verification_code": "moltbook_verify_44ed4076d9b018984fe05e6c52fa81a7",
    "answer": "39.00"
}).encode("utf-8")

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={
        "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0706_2138.json", "w") as f:
        json.dump(result, f, indent=2)
