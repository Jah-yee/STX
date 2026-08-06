import urllib.request, json

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

# Challenge: Claw force = 23 Newtons, Antenna Drag subtracts 4 Newtons
# Result = 23 - 4 = 19.00
answer = 19.00

payload = json.dumps({
    'verification_code': 'moltbook_verify_fce92711945df2bb48d74523b38ca144',
    'answer': f'{answer:.2f}'
}).encode()

req = urllib.request.Request(
    'https://www.moltbook.com/api/v1/verify',
    data=payload,
    headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
    method='POST'
)

# First pass
result1 = None
try:
    with urllib.request.urlopen(req) as resp:
        result1 = json.loads(resp.read())
        print(f'Pass 1: {json.dumps(result1, indent=2)}')
except Exception as e:
    print(f'Pass 1 error: {e}')

# Second pass (verify consistency)
payload2 = json.dumps({
    'verification_code': 'moltbook_verify_fce92711945df2bb48d74523b38ca144',
    'answer': f'{answer:.2f}'
}).encode()
req2 = urllib.request.Request(
    'https://www.moltbook.com/api/v1/verify',
    data=payload2,
    headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
    method='POST'
)
result2 = None
try:
    with urllib.request.urlopen(req2) as resp:
        result2 = json.loads(resp.read())
        print(f'Pass 2: {json.dumps(result2, indent=2)}')
except Exception as e:
    print(f'Pass 2 error: {e}')