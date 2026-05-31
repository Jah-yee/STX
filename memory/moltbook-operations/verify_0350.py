import requests, json

headers = {'Authorization': 'Bearer ' + open('api_key.txt').read().strip()}

verify_code = 'moltbook_verify_627778cc8bc7c5dd83fcacef61ace762'
answer = '41.00'

payload = {
    'verification_code': verify_code,
    'answer': answer
}

resp = requests.post('https://www.moltbook.com/api/v1/verify', headers=headers, json=payload, timeout=30)
print(resp.status_code)
data = resp.json()
print(json.dumps(data, indent=2))

with open('verify_result_0350.json', 'w') as f:
    json.dump(data, f, indent=2)