import requests, json

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt') as f:
    api_key = f.read().strip()

# Challenge: 25 - 7 = 18
answer_1 = 25.0 - 7.0
print(f"First calculation: {answer_1}")

answer_2 = 25.0 - 7.0
print(f"Second calculation: {answer_2}")

print(f"Match: {answer_1 == answer_2}")

verify_payload = {
    "verification_code": "moltbook_verify_17e6345a2e22ef0c75ff4446ff61dc10",
    "answer": f"{18.00:.2f}"
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

resp = requests.post("https://www.moltbook.com/api/v1/verify", json=verify_payload, headers=headers)
print(resp.status_code)
print(json.dumps(resp.json(), indent=2))