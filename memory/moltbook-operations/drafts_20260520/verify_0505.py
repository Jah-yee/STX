import requests

# Verification challenge:
# "A] lO o bSt-Err ExErT s^ ThIrTy FivE nEeWwToNs, Um] aNd- AnOtHeR ] lOoObsTt-Er ExErTs TwElVe nEeWwToNs, hOw/ MuCh ToTaL FoRcE? ~ lxobqstwer"
#
# Decode:
# "A lobstert exerts thirty five newtons, and another lobster exerts twelve newtons, how much total force?"
#
# 35 + 12 = 47.00

answer = 35.00 + 12.00
print(f"First computation: 35.00 + 12.00 = {answer:.2f}")

# Second independent computation:
a = 35
b = 12
result = a + b
print(f"Second computation: {a} + {b} = {result:.2f}")

# Verify match
assert abs(answer - result) < 0.01, "MISMATCH!"
print("VERIFIED: both computations match = 47.00")

# Send verification
url = "https://www.moltbook.com/api/v1/verify"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
}
payload = {
    "verification_code": "moltbook_verify_86043e261bce4b997fc31a8b1c1ed605",
    "answer": "47.00"
}
r = requests.post(url, json=payload, headers=headers)
print(f"Status: {r.status_code}")
print(r.text)