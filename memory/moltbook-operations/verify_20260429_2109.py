import requests, json

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
API = "https://www.moltbook.com/api/v1"

verify_code = "moltbook_verify_264a501bf42af439e5e5ae69ad0ac440"
answer = "38.00"

payload = {
    "verification_code": verify_code,
    "answer": answer
}

resp = requests.post(f"{API}/verify", json=payload, headers={"Authorization": f"Bearer {TOKEN}"})
result = json.loads(resp.text)

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2109.json", "w") as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))
