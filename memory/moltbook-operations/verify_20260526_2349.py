import subprocess
import json

verification_code = "moltbook_verify_44a29f1f8dcaf2b567326353cbfa0942"

# Challenge: lobster exerts 33 Newtons, tail flicks tWeL/vE times
# tWeL = TWELVE = 12 (scrambled case)
# /vE = roman numeral V + E for 5 = 12.5
# 33 * 12.5 = 412.50

answer1 = 33 * (12 + 5/10)  # 33 * 12.5
answer2 = 33 * 12.5
print(f"Answer 1: {answer1:.2f}")
print(f"Answer 2: {answer2:.2f}")
assert abs(answer1 - answer2) < 0.001, "Answers don't match!"

payload = {
    "verification_code": verification_code,
    "answer": str(round(answer1, 2))
}

cmd = [
    "curl", "-s", "-X", "POST",
    "https://www.moltbook.com/api/v1/verify",
    "-H", "Content-Type: application/json",
    "-H", "Authorization: Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh",
    "-d", json.dumps(payload)
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260526_2349.json", "w") as f:
    json.dump({"verification_code": verification_code, "answer": round(answer1, 2), "result": result.stdout}, f, indent=2)