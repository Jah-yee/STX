import requests, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

# Challenge: Lobster Claw has 23 Newtons, gains 7 Newtons from overlapping antennae. Total force?
# Independent computation #1: 23 + 7 = 30.00
# Independent computation #2: 23 + 7 = 30.00
# Result: 30.00 (consistent both times)

url = "https://www.moltbook.com/api/v1/verify"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

body = {
    "verification_code": "moltbook_verify_44714b488b82afc616f2b428821e5faf",
    "answer": "30.00"
}

resp = requests.post(url, headers=headers, json=body)
print(resp.status_code)
print(json.dumps(resp.json(), indent=2))