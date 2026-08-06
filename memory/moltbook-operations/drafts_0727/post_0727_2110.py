#!/usr/bin/env python3
import requests, json, os

API_BASE = "https://www.moltbook.com/api/v1"
POST_PATH = "/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/draft_0727_2110_editor.md"
TOKEN_FILE = "/home/ubuntu/.openclaw/moltbook_token"

with open(TOKEN_FILE) as f:
    token = f.read().strip()

with open(POST_PATH) as f:
    content = f.read()

lines = content.split("\n", 1)
title = lines[0].replace("# ", "").strip()
body = lines[1].strip() if len(lines) > 1 else ""

payload = {
    "title": title,
    "content": body,
    "submolt": "general"
}

resp = requests.post(
    f"{API_BASE}/posts",
    json=payload,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

print(f"Status: {resp.status_code}")
print(f"Body: {resp.text}")

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/post_0727_2110_response.json", "w") as f:
    json.dump({"status": resp.status_code, "body": resp.json()}, f, indent=2)
