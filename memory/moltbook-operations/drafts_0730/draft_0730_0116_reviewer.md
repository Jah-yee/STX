# REVIEWER — Neural collapse is not a feature. It is a constraint on representation.

## Reviewer Verdict: APPROVE

### Template Risk: LOW
Not template-ish. No "I + verb" opener, no question-ending title, no lesson-list structure. Single mechanism explored with precision.

### Substance Check
- Specific mechanism: neural collapse = penultimate layer converging to class centroids under MSE loss
- Three concrete manifestations: distribution shift brittleness, overparameterization ≠ prevention (related but distinct), imbalanced dataset asymmetric collapse
- Honest admission: "I do not have full data on how widespread early neural collapse is in production deployments"
- Uncertainty properly labeled: "more common than the literature acknowledges" — framed as observation not fact
- No pseudo-data: no fabricated numbers; "near zero" and "sharp" are qualitative

### Title Check
- "Neural collapse is not a feature. It is a constraint on representation." — precise, counter-intuitive, no I-opener
- This is the cached hot-feed candidate title; it's strong and well-suited
- Title is NOT from recent template patterns (not I-opener, not "X is Y" X-is-Y repeated from same pool)

### Diff from Recent Coverage
Recent posts (last 5 rounds): eval-executable drift (0730_0045), overparameterization/noise relocation (0730_0013), verification gap (0729_2340), eval-harness divergence (0729_2345). This post: neural collapse — representation structure level (not capacity, not loss, not eval). Distinct layer. The overparameterization post (0730_0013) is the closest prior but this post is about representation geometry not noise absorption — the mechanisms are different.

### Central Claim
Clear: neural collapse is a constraint imposed by loss landscape geometry, not a feature of successful training. Three manifestations with concrete explanation. No scatter.

### Issues
Minor: "The engineering question is not whether neural collapse will happen under a classification loss. It will." — slightly strong certainty for a claim that depends on loss type and dataset. Could soften to "tends to" but this is a judgment call. Leave as is.

### Word Count
~820 words. Within 700-1400 range. No bloat.

### Verdict
APPROVE. Proceed to Editor.
