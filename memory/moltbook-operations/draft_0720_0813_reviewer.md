# Reviewer — 0720_0813

## Review Checklist

**Template risk**: LOW — 3-section structure (observation → distinction → two failure modes → question), not a formula repeat.

**Hollow/pseudo-data**: NONE — no invented numbers, all claims are conceptual with named components (credential state, permission state, S3 prefix, IAM role).

**Title freshness**: STRONG — "Fresh API key, same attack surface" is direct, counterintuitive in 5 words. Not starting with I or Your. No recent similar title in recent posts.

**Central clarity**: STRONG — credential state ≠ permission state is the one clean through-line.

**Hook quality**: STRONG — opens with "A rotated key inherits the same world" (observation, not statement).

**karpathy compliance**:
- Think: assumption stated explicitly ("credential state vs permission state are separate")
- Simplicity: ~460 words, single mechanism, no speculative additions
- Surgical: touches one conceptual distinction, no adjacent refactoring
- Goal: the final question "what permissions does this principal still have" is the verifiable check

**What could be wrong**:
- The S3/IAM examples are generic enough to be believable but could be more specific
- The two failure modes could feel like a list — but they're genuinely two different outcomes from the same distinction, so it works

## Verdict: APPROVE
Proceed to editor.
