import urllib.request, json

url = "https://www.moltbook.com/api/v1/verify"
# Try with plain number string
payload = {
    "verification_code": "moltbook_verify_edda010ac39091b2feb79bb6e4fa527c",
    "answer": "17"
}
data = json.dumps(payload).encode()
req = urllib.request.Request(url, data=data)
req.add_header("Authorization", "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh")
req.add_header("Content-Type", "application/json")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(r.read().decode())
except Exception as e:
    # Read error body
    import urllib.error
    if hasattr(e, 'read'):
        print("Error body:", e.read().decode())
    print("ERROR:", e)
