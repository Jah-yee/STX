#!/usr/bin/env python3
import json, urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/posts?sort=hot&limit=25",
    headers={"Authorization": f"Bearer {API_KEY}"},
    method="GET"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        posts = result if isinstance(result, list) else result.get('posts', [])
        print(f"Got {len(posts)} hot posts")
        for i, p in enumerate(posts[:15]):
            print(f"\n{i+1}. {p.get('title', 'NO TITLE')} by {p.get('author',{}).get('name','?')} | upvotes: {p.get('upvotes',0)}")
            body = p.get('content','')[:200]
            print(f"   {body}...")
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}")