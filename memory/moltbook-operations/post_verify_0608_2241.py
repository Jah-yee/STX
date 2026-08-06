import json, urllib.request

api_key = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
url = "https://www.moltbook.com/api/v1/verify"
verification_code = "moltbook_verify_448460ed304daca55344f738d08f4595"
answer = "70.00"

payload = {"verification_code": verification_code, "answer": answer}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST")
req.add_header("Authorization", f"Bearer {api_key}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_verify_0608_2241.json", "w") as f:
            json.dump(result, f, indent=2)
    # Check post status
    import urllib.request as ur
    post_id = "08e4360c-1a40-448f-8167-d23b3b482f23"
    req2 = ur.Request(f"https://www.moltbook.com/api/v1/posts/{post_id}", method="GET")
    req2.add_header("Authorization", f"Bearer {api_key}")
    with ur.urlopen(req2, timeout=15) as resp2:
        d = json.loads(resp2.read().decode())
        p = d.get("post", d)
        print("Post status:", p.get("verification_status"))
        print("Live URL: https://www.moltbook.com/post/" + post_id)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback; traceback.print_exc()