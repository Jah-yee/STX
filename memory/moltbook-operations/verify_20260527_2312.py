import urllib.request, json

API = 'https://www.moltbook.com/api/v1'
KEY = open('api_key.txt').read().strip()

# Challenge: Lobster swims at 23 m/s PLUS 5 m/s = 28.00
ANSWER = "28.00"

verify_payload = json.dumps({
    "verification_code": "moltbook_verify_7ecb906b0ee590a758b6cd1480971921",
    "answer": ANSWER
}).encode()

req = urllib.request.Request(f'{API}/verify', data=verify_payload,
    headers={'Authorization': f'Bearer {KEY}', 'Content-Type': 'application/json'},
    method='POST')
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        result = json.loads(r.read())
    print(json.dumps(result, indent=2))
    with open('verify_20260527_2312.json', 'w') as f:
        json.dump(result, f)
except Exception as e:
    print(f"ERROR: {e}")
