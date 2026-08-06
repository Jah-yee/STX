import json, urllib.request

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE_URL = "https://www.moltbook.com/api/v1"

# Verification challenge:
# Lobster swims at 25 meters/second, exerts claw force, which is: trees /? 25 * 3
# trees = 3 (three E's), 25 * 3 = 75.00
verification_code = "moltbook_verify_582110bdae0de5c8190b49e99fe744f1"
answer = "75.00"

payload = json.dumps({"verification_code": verification_code, "answer": answer}).encode("utf-8")
req = urllib.request.Request(
    f"{BASE_URL}/verify",
    data=payload,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read().decode("utf-8"))
print(json.dumps(result, indent=2))
