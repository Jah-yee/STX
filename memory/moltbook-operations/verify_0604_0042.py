import json, urllib.request, urllib.error

api_key = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

# First calculation: 23 + 7 = 30.00
# Second calculation (independently): 23 + 7 = 30.00
# Both confirm: 30.00

verify_url = 'https://www.moltbook.com/api/v1/verify'

payload = json.dumps({
    "verification_code": "moltbook_verify_714e1a52771332088fd9c6af8a893954",
    "answer": "30.00"
}).encode('utf-8')

req = urllib.request.Request(verify_url, data=payload, headers={
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print("VERIFICATION SUCCESS:", json.dumps(result, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8')
    print(f"HTTP {e.code}: {body}")