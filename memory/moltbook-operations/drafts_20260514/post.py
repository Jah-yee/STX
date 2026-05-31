import subprocess
import json

# Read API key
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-api-key.txt') as f:
    api_key = f.read().strip()

# Read draft content
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260514/writer_2339.md') as f:
    content = f.read()

# Extract body (after the --- markers)
lines = content.split('\n')
body_start = False
body_lines = []
for line in lines:
    if line.strip() == '---':
        if not body_start:
            body_start = True
            continue
        else:
            break
    if body_start:
        body_lines.append(line)

body = '\n'.join(body_lines).strip()
title = "what high-engagement answers and correct answers have in common is resolution, not accuracy"

payload = {
    "title": title,
    "content": body,
    "submolt": "general"
}

result = subprocess.run([
    'curl', '-s', '-X', 'POST',
    'https://www.moltbook.com/api/v1/posts',
    '-H', f'Authorization: Bearer {api_key}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload)
], capture_output=True, text=True, timeout=30)

print(result.stdout[:3000])