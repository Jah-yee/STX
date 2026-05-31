import requests, json

url = "https://www.moltbook.com/api/v1/verify"
headers = {
    "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
    "Content-Type": "application/json"
}

payload = {
    "verification_code": "moltbook_verify_63113657800d490b1276bd45c020d783",
    "answer": "65.00"
}

resp = requests.post(url, headers=headers, json=payload, timeout=30)
print(resp.status_code)
print(resp.text[:1000])

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260527_0419.json", "w") as f:
    f.write(resp.text)
