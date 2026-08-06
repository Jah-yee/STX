import json

with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/hot-feed-cache.json', 'r') as f:
    content = f.read()

# Find the start of JSON object
json_start = content.find('{')
json_str = content[json_start:]

# Try to find and fix invalid control chars
import re
# Replace invalid control chars that aren't \n, \r, \t
def fix_json(s):
    # Find control characters (0x00-0x1F except \n, \r, \t)
    result = []
    for i, c in enumerate(s):
        code = ord(c)
        if code < 0x20 and code not in (0x09, 0x0a, 0x0d):
            result.append(' ')
        else:
            result.append(c)
    return ''.join(result)

fixed = fix_json(json_str)
d = json.loads(fixed)
posts = d.get('posts', [])
print(f'total posts: {len(posts)}')
for i, p in enumerate(posts[:20]):
    t = p.get('title','?')[:80]
    s = p.get('submolt','?')
    v = p.get('votes_up', p.get('score','?'))
    c = p.get('num_comments','?')
    content_preview = (p.get('content') or '')[:100].replace('\n',' ')
    print(f'{i+1}. [{s}] votes={v} comments={c}')
    print(f'   title: {t}')
    print(f'   content: {content_preview}')
    print()
