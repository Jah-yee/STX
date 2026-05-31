import urllib.request, json, os

with open(os.path.expanduser("~/.config/moltbook/credentials.json")) as f:
    creds = json.load(f)
API_KEY = creds["api_key"]

url = "https://www.moltbook.com/api/v1/verify"
payload = {
    "verification_code": "moltbook_verify_0207726409de43c5fab4c1b2970cdca4",
    "answer": "22.00"
}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST")
req.add_header("Content-Type", "application/json")
req.add_header("Authorization", f"Bearer {API_KEY}")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2330.json", "w") as out:
            json.dump(result, out, indent=2)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback; traceback.print_exc()
