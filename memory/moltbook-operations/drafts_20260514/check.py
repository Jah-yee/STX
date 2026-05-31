import subprocess
import json

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-api-key.txt') as f:
    api_key = f.read().strip()

# Get post to check verification status
result = subprocess.run([
    'curl', '-s', '-X', 'GET',
    'https://www.moltbook.com/api/v1/posts/b342d331-a9d9-454d-abe7-7b2f2ecb64c5',
    '-H', f'Authorization: Bearer {api_key}',
], capture_output=True, text=True, timeout=30)

print(result.stdout[:2000])