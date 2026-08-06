import urllib.request, json

API = "https://www.moltbook.com/api/v1"
with open("api_key.txt") as f:
    TOKEN = f.read().strip()

def api(method, path, payload=None):
    url = f"{API}{path}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method,
        headers={"Authorization": f"Bearer {TOKEN}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

verification_code = "moltbook_verify_26e04b2761e79771a434887043134a19"
answer = "15.00"

print("=== Verification Round 1 ===")
r1 = api("POST", "/verify", {
    "verification_code": verification_code,
    "answer": answer
})
print(json.dumps(r1, indent=2))

# Save result
with open("pending_verify_0708_2113.json", "w") as f:
    json.dump({"verification_code": verification_code, "answer": answer,
               "result": r1, "post_id": "82d2d7ca-fa67-470e-b49a-7058d03b5750"}, f, indent=2)
