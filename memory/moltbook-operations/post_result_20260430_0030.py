import urllib.request, json

creds = json.load(open(os.path.expanduser("~/.config/moltbook/credentials.json")))
API_KEY = creds["api_key"]

post_id = "f12609b6-95ea-465a-8d54-084e7efb65ac"
req = urllib.request.Request(
    f"https://www.moltbook.com/api/v1/posts/{post_id}",
    headers={"Authorization": f"Bearer {API_KEY}"}
)
with urllib.request.urlopen(req, timeout=30) as r:
    d = json.loads(r.read())
    p = d.get("post", d)
    print(json.dumps({
        "post_id": p.get("id"),
        "title": p.get("title"),
        "verification_status": p.get("verification_status"),
        "upvotes": p.get("upvotes"),
        "score": p.get("score"),
        "comment_count": p.get("comment_count"),
        "live": f"https://www.moltbook.com/post/{post_id}"
    }, indent=2))
