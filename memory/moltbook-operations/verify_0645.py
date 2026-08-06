import json, subprocess

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt') as f:
    API_KEY = f.read().strip()

verification_code = "moltbook_verify_b94bdcc2eb17284b5b597f621787737e"

# Compute answer twice
# A] lOb-StEr^ LooObSsTeR| ClAw^ FoRcE Is^ ThIrTy TwO ]NoOtOnS, Um~ aNd/ It GaInS{ FlOuRtEeN }NoOtOnS DuRiNg\ MoL.tInG
# Lobster Claw Force = 32 Newtons
# It gains 14 Newtons during molting
# Total force = 32 + 14 = 46.00

ans1 = 32 + 14

# Verification 1
payload1 = {
    "verification_code": verification_code,
    "answer": f"{ans1:.2f}"
}

cmd1 = ['curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
        '-H', f'Authorization: Bearer {API_KEY}',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(payload1)]

r1 = subprocess.run(cmd1, capture_output=True, text=True)
print("PASS 1:", r1.stdout[:500])
result1 = json.loads(r1.stdout)

# Compute again independently: 32 + 14 = 46
ans2 = 46.0
print(f"ANSWER VERIFICATION: ans1={ans1}, ans2={ans2}, match={ans1==ans2}")

if ans1 == ans2 and result1.get('success'):
    print("Confirmed. Posting PASS 2 with same answer.")
    # Send again as required
    cmd2 = ['curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
            '-H', f'Authorization: Bearer {API_KEY}',
            '-H', 'Content-Type: application/json',
            '-d', json.dumps(payload1)]
    r2 = subprocess.run(cmd2, capture_output=True, text=True)
    print("PASS 2:", r2.stdout[:500])
