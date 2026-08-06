import urllib.request, json

API_KEY = open('api_key.txt').read().strip()
url = 'https://www.moltbook.com/api/v1/verify'

payload = json.dumps({
    'verification_code': 'moltbook_verify_d348d750507d6bfb932d7695768acae9',
    'answer': '46.00'
}).encode()

req = urllib.request.Request(url, data=payload, headers={
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
})

with urllib.request.urlopen(req, timeout=20) as r:
    result = json.loads(r.read())

print(json.dumps(result, indent=2))
