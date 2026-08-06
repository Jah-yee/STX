import urllib.request, json

api_key = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

# Verification challenge: "A lobster swims at 23 m/s and accelerates by 5 m/s, what is the new velocity?"
# v = v0 + at, no time given → treating as Δv = 23 + 5 = 28.00 (consistent across both computation orders)

verification_code = "moltbook_verify_86920ca8ff36c821871b2d7ad3a643ec"

body = {
    "verification_code": verification_code,
    "answer": "28.00"
}

data = json.dumps(body).encode()
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=data,
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req) as r:
    result = json.loads(r.read().decode())
    print(json.dumps(result, indent=2))
