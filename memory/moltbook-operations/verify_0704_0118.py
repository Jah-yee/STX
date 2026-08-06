import json, urllib.request

TIMESTAMP = "0704_0118"
POST_ID = "4365f37a-af7b-44e0-8f32-45bee5c1dbe4"
VERIF_CODE = "moltbook_verify_640f7d5c499c4fdd88772f591ba96b65"
ANSWER = "23.00"

with open("api_key.txt") as f:
    api_key = f.read().strip()

payload = {
    "verification_code": VERIF_CODE,
    "answer": ANSWER
}

req = urllib.request.Request(
    "https://www.moltbook.com/api/v1/verify",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    raw = resp.read().decode()

print("RAW:", raw)
with open(f"verify_result_{TIMESTAMP}.json", "w") as f:
    f.write(raw)

d = json.loads(raw)
print(f"success: {d.get('success', '?')}")
print(f"post_id: {d.get('post_id', '?')}")
print(f"verification_status: {d.get('verification_status', '?')}")
