import json, subprocess, time, os

api_key = open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/api_key.txt').read().strip()

# Scan hot feed
result = subprocess.run([
    'curl', '-s', '-X', 'GET',
    'https://www.moltbook.com/api/v1/feed?sort=hot&limit=50',
    '-H', 'Content-Type: application/json',
    '-H', f'Authorization: Bearer {api_key}'
], capture_output=True, text=True, timeout=20)

try:
    data = json.loads(result.stdout)
except:
    print(f"Failed to parse response: {result.stdout[:200]}")
    exit(1)

posts = data.get('posts', data.get('data', []))
candidates = []
for p in posts:
    if isinstance(p, dict) and p.get('title'):
        candidates.append({
            'title': p['title'],
            'upvotes': p.get('upvotes', 0),
            'comments': p.get('comments', 0),
            'id': p.get('id', '')
        })

# Filter AI/agent/system relevant
ai_keywords = ['agent', 'llm', 'model', 'ai', 'automation', 'tool', 'workflow', 'eval', 'benchmark', 'inference', 'prompt', 'system', 'orchestrat', 'delegation', 'verification', 'trust', 'confidence', 'postmortem', 'failure']
def is_ai_relevant(t):
    t_lower = t.lower()
    return any(k in t_lower for k in ai_keywords)

candidates = [c for c in candidates if is_ai_relevant(c['title'])]
candidates.sort(key=lambda x: -x['upvotes'])

# Save cache
cache = {'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'), 'candidates': candidates[:30], 'source': 'feed_hot'}
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/hot-feed-cache.json', 'w') as f:
    json.dump(cache, f, indent=2)

print(f'Scanned {len(candidates)} AI-relevant posts from hot feed')
for c in candidates[:10]:
    print(f"  [{c['upvotes']} upvotes {c['comments']} comments] {c['title'][:80]}")

print(f"\nCache saved. Total candidates: {len(candidates)}")