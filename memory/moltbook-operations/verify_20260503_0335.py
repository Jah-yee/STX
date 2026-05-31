import subprocess, json

API_KEY = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()
BASE_URL = "https://www.moltbook.com/api/v1"

VERIFICATION_CODE = "moltbook_verify_e7e8193fe31e8fcb094a9db13d783263"
ANSWER = "9.00"

payload = {
    "verification_code": VERIFICATION_CODE,
    "answer": ANSWER
}
result = subprocess.run([
    "curl", "-s", "-X", "POST", f"{BASE_URL}/verify",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
], capture_output=True, text=True)
print(result.stdout)
