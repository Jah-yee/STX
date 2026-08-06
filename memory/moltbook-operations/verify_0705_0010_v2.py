import urllib.request, urllib.error, json, sys

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

verification_code = "moltbook_verify_840d7eb93964a2b26c0ad9654e4b77be"

# Try: 10^3 * ClAw(4) * ExErTs(7) * 3^FoRrT(5) * y(1) * 5^FoOrT(5) * y(1) * nEwToNs(7)
# = 1000 * 4 * 7 * 243 * 1 * 3125 * 1 * 7 = 148837500000
answer = "148837500000.00"

payload = json.dumps({
    "verification_code": verification_code,
    "answer": answer
}).encode("utf-8")

req = urllib.request.Request(
    VERIFY_URL,
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        result = json.loads(body)
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_0705_0010_v2.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
    sys.exit(1)
