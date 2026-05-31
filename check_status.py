import json
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/moltbook-operations/post_result_20260510_0710.json') as f:
    d = json.load(f)
p = d.get('post', {})
print('Post ID:', p.get('id'))
print('Title:', p.get('title'))
print('Verification status:', p.get('verification_status'))
print('Created at:', p.get('created_at'))
v = p.get('verification', {})
print('Challenge:', v.get('challenge_text') if v else None)