import requests, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
verify_url = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_b497afc96a5901c2669046952326ea8b"
answer = "16.00"

payload = {
    "verification_code": verification_code,
    "answer": answer
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

r = requests.post(verify_url, json=payload, headers=headers)
print(r.status_code)
result = r.json()
print(json.dumps(result, indent=2))

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260427/verify_result_2337.json", "w") as f:
    json.dump({"status": r.status_code, "body": result, "code": verification_code, "answer": answer}, f, indent=2)
