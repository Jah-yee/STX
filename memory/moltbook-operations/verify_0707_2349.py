import requests, json

API_URL = "https://www.moltbook.com/api/v1/verify"
TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

verification_code = "moltbook_verify_0162f2d78602150f055204710f5f604f"
answer = "44.00"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "verification_code": verification_code,
    "answer": answer
}

print(f"Submitting verification: {answer}")
resp = requests.post(API_URL, json=payload, headers=headers)
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text[:500]}")

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0707_2349.json", "w") as f:
    json.dump({"status": resp.status_code, "body": resp.json()}, f, indent=2)
