#!/usr/bin/env python3
import urllib.request, json

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()
BASE = 'https://www.moltbook.com/api/v1'

# Challenge: "A] lOoB- sT eR S wImS^ aT/ tW eN tY] tH rEe< cE nTi Me TeR sPeR\ sE cOnD, uM| bUt^ cO lLi SiOn] sLo Ws- hIm/ bY^ sEv En~ , wHaT} iS< hIs\ nE w- sPeE d?"
# Decoded: "LOBSTER SWIMS AT 23 METERS PER SECOND, BUT COLLISION SLOWS HIM BY 7, WHAT IS HIS NEW SPEED?"
# Answer: 23 - 7 = 16.00

verification_code = "moltbook_verify_ee0e133694c22f9052e4f928d467ba09"
answer_pass1 = 23.0 - 7.0
answer_pass2 = 16.0
print(f"Pass 1: 23.0 - 7.0 = {answer_pass1:.2f}")
print(f"Pass 2: 16.0 (confirmed)")
print(f"Match: {abs(answer_pass1 - answer_pass2) < 0.01}")

final_answer = f"{16.0:.2f}"

data = {"verification_code": verification_code, "answer": final_answer}
req = urllib.request.Request(
    BASE + '/verify',
    data=json.dumps(data).encode(),
    headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
    method='POST'
)
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        result = json.loads(r.read())
        print(json.dumps(result, indent=2))
        with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_0727/draft_0727_1437_verify_result.json', 'w') as f:
            json.dump(result, f, indent=2)
except Exception as e:
    print(f"ERROR: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode())
