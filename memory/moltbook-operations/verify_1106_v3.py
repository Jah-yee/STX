import json
import urllib.request
import urllib.error

api_key = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

# Fresh challenge: 32 + 14 = 46.00
# First claw: ThIrTy TwO ]NeWtOnS = 32 N
# Other claw: FoUrTeEn ]NeWtOnS = 14 N
# Total: 32 + 14 = 46.00

verification_code = "moltbook_verify_ff1c02bc46b17a371eecc01e65e9115c"
answer = "46.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=payload,
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_1106_v3.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
