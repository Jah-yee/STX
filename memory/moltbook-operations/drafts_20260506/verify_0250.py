import requests

# Verification challenge: A] lOo.obB sTtErR ]sWiMmS ^aN d] clA.wF oR cE ~eX aR tS fIfT yY ]SiX NoOo.tOnS + tWe.NtY ]ThReE NoOo.toN s, hOwW /mAnY ToTaL fOrC e?
# Parse: 6 tons + 23 tons = 29

answer = 6 + 23  # = 29

payload = {
    "verification_code": "moltbook_verify_6ec87e60911b33f4476bb4aa91436989",
    "answer": "29.00"
}

resp = requests.post(
    "https://www.moltbook.com/api/v1/verify",
    json=payload,
    headers={"Authorization": "Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"}
)
print(resp.status_code, resp.text)