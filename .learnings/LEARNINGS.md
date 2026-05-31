# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260531-001] best_practice

**Logged**: 2026-05-31T11:15:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
GitHub search API (`gh search repos`) returns 99 for repos with 30+ open PRs, not actual count

### Details
When using `gh search repos`, repos with >= 30 open PRs show "99" in the output, not the actual count. This means Gate-2 checks with `gh api repos/OWNER/REPO/pulls --jq 'length'` give accurate counts (30), while search results give a ceiling value (99). Always use the direct API for PR count checks, not search results.

### Suggested Action
For Gate-2 checks, always use: `gh api repos/OWNER/REPO/pulls --jq 'length'` (direct API) instead of relying on search result counts.

### Metadata
- Source: conversation | error
- Related Files: PR攻关 workflow
- Tags: github-api, gate-check, search
- See Also: -

---

## [LRN-20260531-002] insight

**Logged**: 2026-05-31T11:15:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
Most major repos (huggingface, pytorch, numpy, etc.) are permanently Gate-2 blocked at 30 open PRs

### Details
In the current GitHub ecosystem, popular repos frequently hit the 30 PR limit. This means Gate-2 (limit < 2 open PRs) blocks almost all opportunities in large projects. Strategy must focus on: (1) smaller niche repos, (2) repos coming out of cooldown with low PR counts, (3) repos in topic:good-first-issue that have low activity.

### Suggested Action
Adjust PR攻关 strategy: prioritize finding smaller repos (stars 50-5000, PRs < 10) with good-first-issues. Large repos are effectively never available.

### Metadata
- Source: conversation
- Related Files: PR攻关 workflow
- Tags: github-api, gate-check, strategy
- See Also: -

---

## [LRN-20260531-003] knowledge_gap

**Logged**: 2026-05-31T11:15:00Z
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
pallets/click BytesWarning bug (#3533) was officially fixed by PR #3534 (merged 05-30 20:23 UTC)

### Details
Issue #3533 (BytesWarning in Path.convert) was tracked as a potential PR opportunity. However, while we were working on it, the upstream maintainer kdeldycke officially fixed it via PR #3534 which was merged on 2026-05-30 at 20:23 UTC. This demonstrates that for active projects like click, fixes can come from multiple sources quickly.

### Resolution
- **Resolved**: 2026-05-31
- **Outcome**: Opportunity expired. Official fix merged first.
- **Notes**: Jah-yee's attempt blocked by gh pr create 422 + gh repo fork 403 anyway.

### Metadata
- Source: conversation
- Related Files: submitted-repos.json (pallets/click entry)
- Tags: github-api, competition, official-fix
- See Also: -

---
