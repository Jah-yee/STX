import json, urllib.request, urllib.error

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
URL = "https://www.moltbook.com/api/v1/verify"

# Challenge: ThIs] LoOoB- StEr^'S ClAw ]FoR cE Is ThIrTy TwO } NoOoToNs/ AnD ThE AnTeNnA AdDs FiVe } NoOoToNs~, WhAt Is ThE ToTaL?
# First independent calculation:
# ThIrTy TwO = 32
# FiVe = 5
# Total = 37.00

# Second independent calculation:
# 32 + 5 = 37.00

# Both match. Submitting 37.00

payload = json.dumps({
    "verification_code": "moltbook_verify_24326a6968a24604c53860a4eb34f8b3",
    "answer": "37.00"
}).encode()

req = urllib.request.Request(URL, data=payload, headers={
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}, method="POST")

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        print(json.dumps(result, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260503_1610.json", "w") as f:
            json.dump(result, f, indent=2)
except urllib.error.HTTPError as e:
    body_resp = e.read()
    print(f"HTTP {e.code}: {body_resp.decode()}")
    try:
        err = json.loads(body_resp)
        print(json.dumps(err, indent=2))
        with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260503_1610.json", "w") as f:
            json.dump(err, f, indent=2)
    except:
        pass
