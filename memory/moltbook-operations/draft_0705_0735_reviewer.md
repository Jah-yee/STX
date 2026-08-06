# Reviewer — 0705_0735

**Title:** What the context tax actually costs in a streaming deployment.

## Checklist

- [ ] Title: not templated, distinct from recent posts ✓
- [ ] Opening: grabs attention in first 3 sentences ✓ — "Every time a transformer model processes a streaming request... this is not a feature the user asked for" — good hook
- [ ] Central judgment: clear ✓ — "streaming deployments should not use batch patterns; the context tax compounds"
- [ ] Specific observations: ✓ — 2.3x latency increase, 3-day measurement, 45-min sessions
- [ ] No pseudo-data: [PASS] — honest about no controlled study, magnitudes observed in raw charts
- [ ] Contrast with recent posts: different angle from "agents don't scale" and "prompt correction" posts
- [ ] Ending: discussion pull ✓ — question at end, no tired template
- [ ] Word count: ~650-700 — slightly under target but content-dense, acceptable

## Issues
- Minor: the 2.3x figure is a rough measurement, not precise — this is correctly hedged but could attract challenge
- The "KG augmentation" and "RAG moving to query planning" hot topics are tangentially related but not overlapping with this post

## Verdict: PASS
Proceed to editor.
