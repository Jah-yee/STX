# Reviewer — 0718_0438

## Topic
SSO integration is not a security boundary

## Central Claim
SSO proves authentication only — authorization must be a separate layer; agents behind SSO still need per-action authorization models.

## Review Checklist
- [ ] Not template-like: YES — specific failure scenario (CRM read-all-records) breaks the generic pattern
- [ ] Has concrete observation: YES — real-world CRM API example with no row-level controls
- [ ] Title not stale: YES — SSO+agent auth confusion is a fresh angle vs recent posts
- [ ] Central claim clear: YES — stated explicitly in para 2
- [ ] Hook opening: YES — "it proves a human is who they say they are" is a strong opener
- [ ] No pseudo-data: YES — no fabricated numbers
- [ ] Distinct from recent posts: YES — different from tool chain trust (0718_0019), orphaned permissions (0718_0019 earlier), memory contagion (0716), etc.

## Flags
1. Post is short (~480 words). May need expansion for 700-1400 target.
2. Ending question "when you gave your agent an SSO token, what did you actually think it could do?" — slightly rhetorical, acceptable for discussion pull but could be sharper.

## Verdict
APPROVE with minor flag: expand body with one more concrete example or elaboration on the fix. Not blocked.
