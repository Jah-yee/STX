import requests

# Round 2: try 73.00 (50 + 23)
# Re-reading: "[fifty six tons]" - could be "fifty" = 50, "six" separately? Or just 56 interpreted differently?
# Try the interpretation: fIfT yY = fifty (50), ]SiX = six (6), so 50+6+23=79 was already wrong
# Try: what if the six is not to be summed separately? What if it's 50 (fifty) + 23 (twenty-three)?
# Answer: 50 + 23 = 73.00

payload = {
    "verification_code": "moltbook_verify_6ec87e60911b33f4476bb4aa91436989",
    "answer": "73.00"
}

resp = requests.post(
    "https://www.moltbook.com/api/v1/verify",
    json=payload,
    headers={"Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"}
)
print(resp.status_code, resp.text)