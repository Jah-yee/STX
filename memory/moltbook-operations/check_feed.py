import urllib.request, json, sys

token = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
url = "https://www.moltbook.com/api/v1/feed?sort=hot&limit=8"

req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        raw = r.read().decode()
        d = json.loads(raw)
        posts = d.get("data", []) if isinstance(d, dict) else d
        for p in posts[:8]:
            print(p.get("title","")[:80], "|", p.get("id",""))
except Exception as e:
    print("ERR", e, file=sys.stderr)
