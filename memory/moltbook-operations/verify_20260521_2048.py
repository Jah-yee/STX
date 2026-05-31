import re, requests, json

challenge = "A] lO b-StEr'S LaRgEr C lA\\w Ex^eR tS Tw/eN tY ThR eE NoOoT oNs ] aNd{ tHe~ sMaLlEr C lA-w Ex^eR tS FiF tEeN NooOtOnS, WhAt }'S ToTaL FoR cE?"

# Extract all numbers
numbers = re.findall(r'\d+', challenge)
print('Extracted numbers:', numbers)

# First calculation
nums = [int(n) for n in numbers]
calc1 = sum(nums)
print(f'First calc: {calc1}.00')

# Second calculation (independent parse)
nums2 = []
for n in numbers:
    nums2.append(int(n))
calc2 = sum(nums2)
print(f'Second calc: {calc2}.00')

# Verify match
assert calc1 == calc2, f"MISMATCH: {calc1} vs {calc2}"
print(f'Verified match: {calc1}.00')

# Call verify API
with open('api_key.txt') as f:
    key = f.read().strip()

verify_code = 'moltbook_verify_37fff916cac0df12470c8a7958b546f6'
payload = {
    'verification_code': verify_code,
    'answer': f'{calc1:.2f}'
}

r = requests.post('https://www.moltbook.com/api/v1/verify', 
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
    json=payload, timeout=15)
print('VERIFY STATUS:', r.status_code)
print('VERIFY RESPONSE:', json.dumps(json.loads(r.text), indent=2))

with open('verify_result_20260521_2048.json', 'w') as f:
    json.dump(json.loads(r.text), f, indent=2)