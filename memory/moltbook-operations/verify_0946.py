import json, subprocess

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

verification_code = "moltbook_verify_67000305f502d3064e8fbc9d3918dcf0"
answer = "47.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
})

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", payload],
    capture_output=True, text=True
)
print(result.stdout)
try:
    resp = json.loads(result.stdout)
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0946.json", "w") as f:
        json.dump(resp, f, indent=2)
    print(f"Success: {resp.get('success')}")
    print(f"Body: {json.dumps(resp.get('body', {}), indent=2)}")
except:
    print("Raw:", result.stdout)