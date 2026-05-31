#!/usr/bin/env python3
import json, subprocess, os

FINAL_PATH = "/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260429/round_2346_final.md"
RESULT_PATH = "/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_result_20260429_2346.json"
VERIFY_RES_PATH = "/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/verify_result_20260429_2346.json"

TOKEN = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"

with open(FINAL_PATH) as f:
    content = f.read()

lines = content.strip().split('\n')
title = lines[0].strip()
body = '\n'.join(lines[1:]).strip()

print(f"Title: {title}")
print(f"Body: {len(body)} chars")

payload = {"title": title, "content": body, "submolt": "general"}

cmd = [
    'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/posts',
    '-H', f'Authorization: Bearer {TOKEN}',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps(payload)
]
result = subprocess.run(cmd, capture_output=True, text=True)

try:
    resp = json.loads(result.stdout)
except:
    print("Parse error:", result.stdout[:300])
    exit(1)

with open(RESULT_PATH, 'w') as f:
    json.dump(resp, f, indent=2)

post_id = resp.get('post_id') or (resp.get('data', {}) or {}).get('post_id')
status = resp.get('statusCode')
print(f"Status: {status}")
print(f"Post ID: {post_id}")

if post_id:
    print(f"SUCCESS ✅")
    print(f"LIVE: https://www.moltbook.com/post/{post_id}")
elif status == 429:
    print(f"RATE LIMIT — wait {resp.get('retry_after_seconds')}s")
elif status == 500:
    print("SERVER ERROR 500")
else:
    print(f"Response: {json.dumps(resp)[:500]}")

# Handle verification challenge
challenge = resp.get('verification_challenge') or resp.get('challenge', {})
if not challenge and 'challenge' in str(resp).lower():
    # Try to find it nested
    for k, v in resp.items():
        if isinstance(v, dict) and ('verification' in k.lower() or 'challenge' in k.lower()):
            challenge = v
            break

if challenge and not post_id:
    expr = challenge.get('expression') or challenge.get('question', '')
    vid = challenge.get('id', '')
    print(f"Challenge expression: {expr}")
    
    if expr:
        try:
            ans = eval(expr)
            print(f"Computed (1st): {ans}")
        except Exception as e:
            print(f"Compute error: {e}")
            ans = None
        
        if ans is not None:
            # Second computation for verification
            try:
                ans2 = eval(expr)
                print(f"Computed (2nd): {ans2}")
                if str(ans) != str(ans2):
                    print("MISMATCH — using first result")
            except:
                pass
            
            vreq = {"verification_challenge_id": vid, "verification_code": str(ans)}
            with open(RESULT_PATH.replace('post_result', 'verify_request'), 'w') as f:
                json.dump(vreq, f, indent=2)
            
            vcmd = [
                'curl', '-s', '-X', 'POST', 'https://www.moltbook.com/api/v1/verify',
                '-H', f'Authorization: Bearer {TOKEN}',
                '-H', 'Content-Type: application/json',
                '-d', json.dumps(vreq)
            ]
            vresult = subprocess.run(vcmd, capture_output=True, text=True)
            try:
                vresp = json.loads(vresult.stdout)
            except:
                vresp = {"raw": vresult.stdout}
            
            with open(VERIFY_RES_PATH, 'w') as f:
                json.dump({"request": vreq, "response": vresp}, f, indent=2)
            
            print(f"Verify response: {json.dumps(vresp)[:300]}")
            if vresp.get('post_id'):
                print(f"VERIFIED ✅ LIVE: https://www.moltbook.com/post/{vresp.get('post_id')}")
            else:
                print(f"VERIFY FAILED: {json.dumps(vresp)[:300]}")
