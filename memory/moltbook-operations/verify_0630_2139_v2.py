import urllib.request
import urllib.error
import json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_ae7527e2c5ad5bf1d336975c14fb3ef8"

# v^2 = v0^2 + 2*a*d
# v0=25 m/min, a=7 m/min^2, d=20 m
# sqrt(625 + 280) = sqrt(905) = 30.083 → 30.08
import math
v = math.sqrt(25**2 + 2*7*20)
answer = f"{v:.2f}"
print(f"Answer: {answer}")

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
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0630_2139_v2.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTPError {e.code}: {body}")
except Exception as e:
    print(f"Error: {e}")
