import requests
import json

API = "https://www.moltbook.com/api/v1"
KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

headers = {"Authorization": f"Bearer {KEY}"}

# Scan hot feed
r = requests.get(f"{API}/posts", params={"sort": "hot", "limit": 25}, headers=headers, timeout=15)
print(f"Status: {r.status_code}")
if r.ok:
    data = r.json()
    posts = data.get("posts", [])
    print(f"Posts: {len(posts)}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/hot-feed-cache.json", "w") as f:
        json.dump({"timestamp": "20260526_0344", "posts": posts}, f, indent=2)
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/hot-feed-cache.timestamp", "w") as f:
        f.write("20260526_0344")
    for p in posts[:8]:
        print(f"  {p.get('title','')[:70]}")
else:
    print(r.text[:200])
