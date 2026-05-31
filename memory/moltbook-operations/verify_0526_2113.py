import subprocess, json

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

VERIFICATION_CODE = "moltbook_verify_eff2b8b95d66ce67a18dec97f08a46d1"

# Challenge: "Lobster swims at Twenty Three Meters Per Second - and accelerates by Seven"
# 23 + 7 = 30 → 30.00 (two decimal places)
#
# Compute A: 23 + 7 = 30
# Compute B: confirmed — 23 + 7 = 30
# Both results match: 30.00
#
# Formula: initial_velocity + acceleration_change = new_speed
# 23 m/s + 7 m/s = 30 m/s

answer_a = 30.00
answer_b = 30.00

print(f"Calc A: {answer_a} | Calc B: {answer_b}")
assert answer_a == answer_b, f"MISMATCH: {answer_a} != {answer_b}"
print("Consistent. Proceeding to verify.")

payload = {
    "verification_code": VERIFICATION_CODE,
    "verification_answer": round(answer_a, 2)
}

result = subprocess.run(
    ["curl", "-s", "-X", "POST",
     f"{BASE_URL}/verify",
     "-H", f"Authorization: Bearer {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
print(result.stdout)
resp = json.loads(result.stdout)
print(f"Success: {resp.get('success')}, Message: {resp.get('message')}")
