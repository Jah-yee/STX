import urllib.request, json, pathlib

key = pathlib.Path('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read_text().strip()

# Lobster-math:32 Nootons + 20 Nootons = 52.00
# Pass 1: 32 + 20 = 52.00
# Pass 2: twenty + thirty-two = 52.00

payload = json.dumps({
    'verification_code': 'moltbook_verify_c69d0a33324fe64cfb8702d1a1d38026',
    'answer': '52.00'
}).encode()
req = urllib.request.Request(
    'https://www.moltbook.com/api/v1/verify',
    data=payload,
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    method='POST'
)
with urllib.request.urlopen(req) as r:
    resp = json.loads(r.read().decode())
    print(json.dumps(resp, indent=2))
