import requests, json

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/.api_key') as f:
    api_key = f.read().strip()

# Check the post we just created
resp = requests.get(
    "https://www.moltbook.com/api/v1/posts/d2cbfb89-a3e8-4b98-afad-26dec81d8a26",
    headers={"Authorization": f"Bearer {api_key}"}
)
print(resp.status_code)
print(resp.text[:2000])
