import json, subprocess

API_KEY = open("/home/ubuntu/.config/moltbook/credentials.json").read()
key_data = json.loads(API_KEY)
api_key = key_data.get("api_key", key_data.get("token", ""))

verify_code = "moltbook_verify_37efa5a6291364d34ea2645fee59d280"

# Challenge: A lOoOoBbSsTtEr^ S/wIiMmS] aT tWeNnTtYy- tHrEe{ cMmEeTtErS/ pEeR| sEeCcOnDs~, AnD} iTs- ClLaAw^ ExXeErTs] fIfFtEeEeN< nEeWwToOnSs~, WhHaT/ iS} tHe+ SuMm?
# Extracted: 23 meters per second + 15 meters per second = ?

# First computation
ans1 = 23 + 15

# Second computation (independent)
a = 23
b = 15
ans2 = a + b

print(f"First pass:  {ans1}")
print(f"Second pass: {ans2}")
print(f"Match: {ans1 == ans2}")

answer = f"{ans2:.2f}"
print(f"Answer to send: {answer}")

payload = {
    "verification_code": verify_code,
    "answer": answer
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://www.moltbook.com/api/v1/verify",
     "-H", f"Authorization: Bearer {api_key}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
print(result.stdout)
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_0117.json", "w") as f:
    json.dump(json.loads(result.stdout), f, indent=2)
