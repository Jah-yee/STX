#!/usr/bin/env python3
"""Batch promote CLEAN PRs for R324 - parallel version."""
import subprocess, json, time, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

def gh(args, timeout=8):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, '', 'TIMEOUT'

def get_all_prs():
    prs = []
    for page in range(1, 6):
        ret, out, err = gh(['gh', 'api', '--header', 'Accept: application/vnd.github+json',
                  f'https://api.github.com/search/issues?q=is%3Apr+is%3Aopen+author%3A%40me&per_page=100&page={page}'])
        if ret != 0 or not out:
            break
        try:
            data = json.loads(out)
        except:
            break
        items = data.get('items', [])
        if not items:
            break
        for item in items:
            repo_url = item['repository_url']
            parts = repo_url.split('/')
            owner, name = parts[-2], parts[-1]
            prs.append({'repo': f"{owner}/{name}", 'number': item['number'],
                       'comments': item['comments'],
                       'mergeable_state': item.get('mergeable_state', '').lower()})
        if len(items) < 100:
            break
    return prs

print("R324 Starting...")
prs = get_all_prs()
print(f"Total OPEN PRs: {len(prs)}")

# Load submitted repos to check cooldown
try:
    with open('/home/ubuntu/.openclaw/workspace-taizi/memory/PR-fast/submitted-repos.json') as f:
        submitted = json.load(f)
except:
    submitted = {}

AT_MAX = 30
SKIP_STATES = {'blocked', 'dirty', 'unstable', 'behind', 'unknown'}
SKIP_REPOS = {
    'Jah-yee/hermes-agent', 'Jah-yee/ruff', 'Jah-yee/ten-framework', 'Jah-yee/tracing',
    'huggingface/smolagents', 'openai/grok', 'facebookresearch/fairseq',
    'facebookresearch/detectron2', 'langchain-ai/langgraph', 'excalidraw/excalidraw',
    'golang/website', 'golang/sys', 'numpy/numpy', 'indico/indico',
    'react/react', 'kubernetes/minikube', 'microsoft/vscode-python',
    'anthropics/prompt-eng-interactive-tutorial',
}

# Also skip repos in cooldown
now = time.time()
cooldown_repos = set()
for repo_name, info in submitted.items():
    if repo_name == 'Submitted PRs' or repo_name == 'Remaining repos' or repo_name == 'Scanned-2026-07-01-fork-test':
        continue
    if isinstance(info, dict) and 'cooldown_until' in info:
        from email.utils import parsedate_to_datetime
        try:
            from datetime import datetime, timezone
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(info['cooldown_until'])
            if dt.timestamp() > now:
                cooldown_repos.add(repo_name)
        except:
            pass

print(f"Cooldown repos: {len(cooldown_repos)}")

to_promote = []
skipped = {'at_max': [], 'blocked': [], 'cooldown': [], 'locked': []}

for pr in prs:
    repo = pr['repo']
    num = pr['number']
    comments = pr['comments']
    ms = pr.get('mergeable_state', '')
    
    if comments >= AT_MAX:
        skipped['at_max'].append(f"{repo}#{num}({comments}c)")
        continue
    if repo in SKIP_REPOS:
        skipped['blocked'].append(f"{repo}#{num}(BLOCKED_REPO)")
        continue
    if repo in cooldown_repos:
        skipped['cooldown'].append(f"{repo}#{num}")
        continue
    if ms in SKIP_STATES:
        skipped['blocked'].append(f"{repo}#{num}({ms})")
        continue
    
    to_promote.append(pr)

print(f"CLEAN to promote: {len(to_promote)}")
for k, v in skipped.items():
    if v:
        print(f"  {k}: {len(v)}")

msg = "Hi @all, gentle reminder that this PR is waiting for review. Happy to make any changes — just let me know! 🙏"

def promote_one(pr):
    repo, num = pr['repo'], pr['number']
    ret, out, err = gh(['gh', 'pr', 'comment', '--repo', repo, str(num), '--body', msg])
    if ret == 0 and 'comment-' in out:
        return ('ok', f"{repo}#{num}", out.split('comment-')[1].split(')')[0] if 'comment-' in out else 'ok')
    elif 'locked' in err.lower() or 'Unable to create comment' in err:
        return ('locked', f"{repo}#{num}", err[:80])
    else:
        return ('fail', f"{repo}#{num}", err[:80])

results = {'ok': [], 'locked': [], 'fail': []}
done = 0
total = len(to_promote)

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(promote_one, pr): pr for pr in to_promote}
    for future in as_completed(futures):
        status, key, detail = future.result()
        results[status].append((key, detail))
        done += 1
        if status == 'ok':
            print(f"✅ {key} ({done}/{total})")
        elif status == 'locked':
            print(f"🔒 {key} locked ({done}/{total})")
        else:
            print(f"❌ {key} fail: {detail} ({done}/{total})")

print(f"\n=== RESULTS ===")
print(f"Promoted: {len(results['ok'])}")
print(f"Locked: {len(results['locked'])}")
print(f"Failed: {len(results['fail'])}")

# Write results for PRs.md
with open('/home/ubuntu/.openclaw/workspace-taizi/memory/PR-fast/r324_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Done! Results saved to r324_results.json")