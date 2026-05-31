import requests, json

API = "https://www.moltbook.com/api/v1"
KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
headers = {"Authorization": f"Bearer {KEY}"}

# Verification: PASS1=18.00, PASS2=18.00 — consistent
code = "moltbook_verify_fd9abd4e1a02eca970f565f188c3e48f"
answer_p1 = "18.00"
answer_p2 = "18.00"

print(f"Pass 1: {answer_p1}, Pass 2: {answer_p2}")
assert answer_p1 == answer_p2, f"MISMATCH: {answer_p1} vs {answer_p2}"

payload = {"verification_code": code, "answer": answer_p1}
r = requests.post(f"{API}/verify", json=payload, headers=headers, timeout=20)
print(f"Status: {r.status_code}")
data = r.json()
print(json.dumps(data, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260526/verify_result_0526_0344.json","w") as f:
    json.dump(data, f, indent=2)
