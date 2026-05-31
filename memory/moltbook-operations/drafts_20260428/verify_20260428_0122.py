import urllib.request, urllib.error, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

# Challenge: 32 - 8 = 24.00
# Two independent calculations:
# 1) Force = 32N, reduction = 8N → Net = 32 - 8 = 24.00
# 2) 32 - 8 = 24.00

verify_code = "moltbook_verify_a148102e386b518f089dedd587f3d1ce"
answer = "24.00"

# Verify twice
for i in range(2):
    payload = json.dumps({"verification_code": verify_code, "answer": answer}).encode("utf-8")
    req = urllib.request.Request(URL, data=payload, headers={
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            print(f"Attempt {i+1}: {json.dumps(result)}")
            with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260428_0122.json", "w") as f:
                json.dump(result, f, indent=2)
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"HTTP {e.code}: {err}")
        break