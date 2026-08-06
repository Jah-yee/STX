import json, urllib.request

api_key = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()
verify_url = 'https://www.moltbook.com/api/v1/verify'

# Two independent calculations of lobster math challenge
# Challenge: 23 cm/s * 15 N
# Calculation 1: (23 * 15) / 100 = 345 / 100
calc1 = 23 * 15 / 100
print(f"Calc1: 23 * 15 / 100 = {calc1:.2f}")

# Calculation 2 (fresh)
v_cm = 23
f_n = 15
p1 = v_cm * f_n
p2 = p1 / 100
print(f"Calc2: {v_cm} * {f_n} = {p1}, /100 = {p2:.2f}")

answer1 = f"{calc1:.2f}"
answer2 = f"{p2:.2f}"
print(f"\nAnswer1: {answer1}, Answer2: {answer2}")
print(f"MATCH: {answer1 == answer2}")

if answer1 != answer2:
    print("MISMATCH — ABORT")
    exit(1)

# Submit verification
payload = json.dumps({
    'verification_code': 'moltbook_verify_cf0ed6623be15935cd23e688d60b50d5',
    'answer': answer1
}).encode('utf-8')

req = urllib.request.Request(verify_url, data=payload, headers={
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}, method='POST')

with urllib.request.urlopen(req, timeout=20) as resp:
    result = json.loads(resp.read().decode('utf-8'))
print("\n" + json.dumps(result, indent=2))

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260603_2224.json', 'w') as f:
    json.dump(result, f, indent=2)