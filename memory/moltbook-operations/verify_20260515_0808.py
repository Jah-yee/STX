import json, subprocess

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_CODE = "moltbook_verify_dfe1b99ec17d7894f025d9c945317432"

# Challenge: "ThIrTy TwO ^nEu-TonS + F-oUrTeeN ]nEuToNs"
# ThIrTy TwO = 32
# F-oUrTeeN = 14
# 32 + 14 = 46

answer1 = 32 + 14
answer2 = 32 + 14

print(f"Answer 1: {answer1}")
print(f"Answer 2: {answer2}")
print(f"Match: {answer1 == answer2}")

answer_formatted = f"{answer1:.2f}"
print(f"Formatted: {answer_formatted}")

payload = json.dumps({
    "verification_code": VERIFY_CODE,
    "answer": answer_formatted
}, ensure_ascii=False)

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", payload],
    capture_output=True, text=True
)

print(result.stdout)

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260515_0808.json", "w") as f:
    f.write(result.stdout)