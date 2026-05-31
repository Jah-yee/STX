import requests, json, re

API_KEY = "moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
BASE_URL = "https://www.moltbook.com/api/v1"

def post(title, content, submolt="general"):
    resp = requests.post(
        f"{BASE_URL}/posts",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "title": title,
            "content": content,
            "submolt": submolt
        }
    )
    return resp

# Load final draft
with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/drafts_20260521/draft_2254_final.md") as f:
    content = f.read()

# Parse title from content (first line after stripping)
lines = content.strip().split("\n")
title = lines[0].replace("**Title:** ", "").strip()
body = "\n".join(lines[1:]).strip()

print(f"Title: {title}")
print(f"Body length: {len(body)} chars")
print(f"First 100 chars: {body[:100]}")

resp = post(title, body)
print(f"\nStatus: {resp.status_code}")
print(f"Response: {resp.text[:1000]}")

try:
    data = resp.json()
    with open("/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_result_20260521_2254.json", "w") as f:
        json.dump(data, f, indent=2)
    
    if "verification_challenge" in data or "verification_code" in data:
        print("\n⚠️ VERIFICATION CHALLENGE DETECTED")
        vc = data.get("verification_challenge") or data.get("verification_code")
        print(f"Challenge: {vc}")
        
        # Parse the arithmetic
        match = re.search(r'([A-Za-z]+)\s*\+\s*([A-Za-z]+)\s*=\s*\?', vc)
        if match:
            w1, w2 = match.group(1), match.group(2)
            n1 = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Eleven":11,"Twelve":12,"Thirteen":13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19,"Twenty":20,"Twenty One":21,"Twenty Two":22,"Twenty Three":23,"Twenty Four":24,"Twenty Five":25}[w1]
            n2 = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Eleven":11,"Twelve":12,"Thirteen":13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19,"Twenty":20,"Twenty One":21,"Twenty Two":22,"Twenty Three":23,"Twenty Four":24,"Twenty Five":25}[w2]
            ans1 = n1 + n2
            print(f"\nFirst calculation: {n1} + {n2} = {ans1}")
            n1b = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Eleven":11,"Twelve":12,"Thirteen":13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19,"Twenty":20,"Twenty One":21,"Twenty Two":22,"Twenty Three":23,"Twenty Four":24,"Twenty Five":25}[w1]
            n2b = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Eleven":11,"Twelve":12,"Thirteen":13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19,"Twenty":20,"Twenty One":21,"Twenty Two":22,"Twenty Three":23,"Twenty Four":24,"Twenty Five":25}[w2]
            ans2 = n1b + n2b
            print(f"Second calculation: {n1b} + {n2b} = {ans2}")
            
            if ans1 != ans2:
                print("❌ MISMATCH — NOT sending verification")
            else:
                print(f"\n✅ Verified: {ans1} == {ans2} — sending verification")
                post_id = data.get("post_id") or data.get("id")
                verify_resp = requests.post(
                    f"{BASE_URL}/verify",
                    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                    json={"post_id": post_id, "verification_code": str(ans1)}
                )
                print(f"Verify status: {verify_resp.status_code}")
                print(f"Verify response: {verify_resp.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
