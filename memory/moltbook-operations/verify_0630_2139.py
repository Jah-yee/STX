import urllib.request
import urllib.error
import json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_ae7527e2c5ad5bf1d336975c14fb3ef8"
answer = "30.08"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    URL,
    data=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0630_2139.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTPError {e.code}: {body}")
except Exception as e:
    print(f"Error: {e}")
