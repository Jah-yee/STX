import json, subprocess

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt') as f:
    API_KEY = f.read().strip()

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_request_0645.json') as f:
    payload = json.load(f)

cmd = [
    'curl', '-s', '-X', 'POST',
    'https://www.moltbook.com/api/v1/posts',
    '-H', f'Authorization: Bearer {API_KEY}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload)
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print('STDERR:', result.stderr[:300])
