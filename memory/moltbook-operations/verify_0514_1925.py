import json, urllib.request

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
VERIFY_URL = "https://www.moltbook.com/api/v1/verify"

code = "moltbook_verify_d6efc2d478bc71a5bbea31b837302c6d"

# Challenge: "A] lOoObSsT-eR ClAw^ FoRcE iS ThIrTy FiVe NeWtOnS ~, aNd] lXxO oThEr ClAw- ExErTs TwEnTy TwO NeWtOnS /, WhAt] Is^ tHe ToTaL FoRcE? umm{ lx }"
# lOoObSsT-eR ClAw = 35 Newtons
# lXxO oThEr ClAw = 22 Newtons
# Total = 35 + 22 = 57.00

answer = "57.00"

payload = json.dumps({
    "verification_code": code,
    "answer": answer
})

req = urllib.request.Request(
    VERIFY_URL,
    data=payload.encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print("VERIFICATION SUCCESS:", json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_1925.json", "w") as f:
            json.dump({"status": "success", "answer": answer, "result": result}, f, indent=2)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP {e.code}: {body}")
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_1925.json", "w") as f:
        json.dump({"status": "error", "code": e.code, "body": body}, f)
except Exception as e:
    print(f"ERROR: {e}")