#!/usr/bin/env python3
import json
import sys

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt') as f:
    api_key = f.read().strip()

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260526/editor_1422.md') as f:
    content = f.read()

# Extract title from content (first line after # Editor Version — lobster-math captcha)
lines = content.strip().split('\n')
title = lines[0].replace('**Title:**', '').strip()
body = content

payload = {
    "title": title,
    "content": body,
    "submolt": "general",
    "type": "text"
}

print(f"Title: {title}", file=sys.stderr)
print(f"Body preview: {body[:100]}", file=sys.stderr)

import urllib.request
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/posts",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print("RESULT:", json.dumps(result), file=sys.stderr)
        if result.get("success"):
            print(f"POST_ID={result.get('post_id')}")
        elif result.get("verification_challenge"):
            print(f"VERIFICATION_REQUIRED={json.dumps(result['verification_challenge'])}", file=sys.stderr)
        else:
            print(f"ERROR={json.dumps(result)}", file=sys.stderr)
except Exception as e:
    print(f"EXCEPTION={e}", file=sys.stderr)
