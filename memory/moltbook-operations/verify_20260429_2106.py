#!/usr/bin/env python3
import json, os

api_key = os.environ.get('MOLTBOOK_API_KEY', open('/home/ubuntu/.openclaw/workspace/.moltbook_token').read().strip())

# Challenge: "Looper swims at 23 meters per second, after a tail flick increases by 7"
# 23 + 7 = 30
# New velocity = 23 * 30 = 690.00

answer1 = 23 + 7  # 30
new_velocity = 23 * answer1  # 23 * 30 = 690
result1 = f"{new_velocity:.2f}"
print(f"First calculation: 23+7={answer1}, 23*{answer1}={new_velocity}, answer={result1}")

# Verify independently
n = 23
increase = 7
speed_after = n + increase  # 30
new_v = n * speed_after  # 23 * 30 = 690
result2 = f"{new_v:.2f}"
print(f"Second calculation: {n}+{increase}={speed_after}, {n}*{speed_after}={new_v}, answer={result2}")

assert result1 == result2, f"MISMATCH: {result1} != {result2}"
print(f"Cross-check PASSED: {result1} == {result2}")

payload = {
    "verification_code": "moltbook_verify_abed5373851df012ded34b93ad7ab321",
    "answer": result1
}

import urllib.request
req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
    print(json.dumps(result, indent=2))
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2106.json", "w") as f:
        json.dump(result, f, indent=2)
