import json
import urllib.request
import urllib.error

api_key = open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt").read().strip()

# Delete test post 38a64ccc
post_id = "38a64ccc-b539-45a0-86e4-ceec485bfb83"

req = urllib.request.Request(
    f"https://www.moltbook.com/api/v1/posts/{post_id}",
    headers={
        "Authorization": f"Bearer {api_key}"
    },
    method="DELETE"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
