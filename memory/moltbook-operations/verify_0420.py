#!/usr/bin/env python3
import json, subprocess

API_KEY = open('api_key.txt').read().strip()

# Challenge: "lO.bStErR SwImS^ aT/ TwEnTy ThReE CeN.tImEtErS PeR \ SeCoNd - AnD] SlOwS ~ bY SeVeN CeN.tImEtErS PeR SeCoNd, WhAt Is NeW VeLoCiTy?"
# - lO.bStErR = "lobsterr" = 8 alpha chars
# - SwImS^ = "swims" = 5 alpha chars
# - TwEnTy = "twenty" = 6 alpha
# - ThReE = "three" = 5 alpha
# - CeN.tImEtErS = "centimeters" = 11 alpha
# - SeVeN = "seven" = 5 alpha

# BUT the actual question says: AT TWENTY THREE cm/s and SLOWS BY SEVEN cm/s
# → New velocity = 23 - 7 = 16 cm/s

verif_code = "moltbook_verify_e0966bdc00f5edacd6ff321590c8ea18"

# Compute both ways to double-check
def ac(s):
    return sum(1 for c in s if c.isalpha())

loberr = ac("lO.bStErR")  # 8
swims = ac("SwImS^")  # 5
twenty = ac("TwEnTy")  # 6
three = ac("ThReE")  # 5
centimeters1 = ac("CeN.tImEtErS")  # 11
seven = ac("SeVeN")  # 5
centimeters2 = ac("CeN.tImEtErS")  # 11

print(f"loberr={loberr}, swims={swims}")
print(f"twenty={twenty}, three={three}, sum={twenty+three}")
print(f"centimeters={centimeters1}, seven={seven}")

# 23 - 7 = 16
answer = "16.00"
payload = {"verification_code": verif_code, "answer": answer}
cmd = ['curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
       '-H', f'Authorization: Bearer {API_KEY}',
       '-H', 'Content-Type: application/json',
       '-d', json.dumps(payload)]
r = subprocess.run(cmd, capture_output=True, text=True)
d = json.loads(r.stdout)
print(f"Answer {answer}: {d.get('success')} — {d.get('message','')}")