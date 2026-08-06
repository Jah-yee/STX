#!/usr/bin/env python3
"""Robust Moltbook poster with improved challenge parsing."""
import urllib.request, json, re, sys

API_KEY = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()
BASE = 'https://www.moltbook.com/api/v1'

def do_post(data):
    req = urllib.request.Request(
        BASE + '/posts',
        data=json.dumps(data).encode(),
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {'error': e.code, 'body': json.loads(e.read())}

def do_verify(code, answer):
    req = urllib.request.Request(
        BASE + '/verify',
        data=json.dumps({'verification_code': code, 'answer': answer}).encode(),
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {'error': e.code, 'body': json.loads(e.read())}

def extract_numbers(challenge_text):
    """Extract ALL possible numbers from garbled challenge text.
    
    Approach: For each known number word, try to find it as a contiguous
    substring in the lowercased, symbol-stripped text. This handles
    interleaved-case words like 'tHiRrTy'.
    """
    text_lower = challenge_text.lower()
    # Remove non-alphanumeric
    cleaned = re.sub(r'[^a-z0-9]', '', text_lower)
    
    word_map = {
        'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
        'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
        'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
        'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,
        'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100
    }
    
    tens = {'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
    ones = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    
    found = set()
    
    # Find all number words as substrings (not just whole-word)
    for word, val in word_map.items():
        if word in cleaned:
            found.add(val)
    
    # Compound numbers: try all tens+ones combinations
    for tw, tv in tens.items():
        for ow, ov in ones.items():
            compound = tw + ow
            if compound in cleaned:
                found.add(tv + ov)
            # Also try ones tens
            compound2 = ow + tw
            if compound2 in cleaned:
                found.add(ov + tv)
    
    # Digit patterns
    for d in re.findall(r'\d+', challenge_text):
        found.add(int(d))
    
    return sorted(found)

def generate_candidates(nums):
    """Generate candidate answers from extracted numbers."""
    candidates = set()
    for n in nums:
        candidates.add(round(n, 2))
        candidates.add(float(n))
    
    for i, n1 in enumerate(nums):
        for n2 in nums[i+1:]:
            ops = [
                n1 + n2,
                abs(n1 - n2),
                abs(n2 - n1),
                n1 * n2,
            ]
            # Try division if reasonable
            if n2 != 0:
                ops.append(n1 / n2)
            if n1 != 0:
                ops.append(n2 / n1)
            for op in ops:
                candidates.add(round(op, 2))
                candidates.add(float(op))
    
    if len(nums) >= 3:
        n1, n2, n3 = nums[0], nums[1], nums[2]
        candidates.add(round(n1 + n2 + n3, 2))
        candidates.add(round(n1 * n2 * n3, 2))
        candidates.add(round(n1 + n2 - n3, 2))
        candidates.add(round(n1 - n2 + n3, 2))
    
    # Format all as 2 decimal places
    return sorted(set(f"{c:.2f}" for c in candidates))

def try_verify(code, challenge_text):
    """Try to solve and verify a challenge."""
    nums = extract_numbers(challenge_text)
    print(f"  Numbers: {nums}")
    candidates = generate_candidates(nums)
    print(f"  Candidates ({len(candidates)}): {candidates[:15]}")
    
    for ans in candidates[:10]:
        vr = do_verify(code, ans)
        if vr.get('success'):
            print(f"  VERIFIED: {ans}")
            return True, ans
        hint = vr.get('message', 'fail')
        print(f"  {ans}: {hint}")
    return False, None

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: post_robust.py <title> <body>")
        sys.exit(1)
    
    title = sys.argv[1]
    body = sys.argv[2]
    
    post_data = {
        "title": title,
        "content": body,
        "submolt": "general"
    }
    
    print(f"Posting: {title[:60]}...")
    result = do_post(post_data)
    
    if 'error' in result:
        print(f"HTTP {result['error']}: {result['body']}")
        sys.exit(1)
    
    post = result.get('post', {})
    post_id = post.get('id', '')
    print(f"Post ID: {post_id}")
    
    v = post.get('verification', {})
    code = v.get('verification_code', '')
    challenge = v.get('challenge_text', '')
    
    if not code:
        print(f"NO VERIFY NEEDED! https://www.moltbook.com/post/{post_id}")
        sys.exit(0)
    
    print(f"Challenge: {challenge}")
    success, ans = try_verify(code, challenge)
    
    if success:
        print(f"SUCCESS! https://www.moltbook.com/post/{post_id}")
    else:
        print(f"VERIFICATION FAILED. Post: https://www.moltbook.com/post/{post_id}")
        sys.exit(1)
