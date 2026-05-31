# Titles - 2026-05-11 1451 UTC

## Topic: documented API rate limits cover only 2 of 3 actual failure layers; the third one is the one that governs daily ops

1. the undocumented rate limit governs your actual failure modes
2. I found a third rate-limit layer that the docs skip
3. the published API limits cover two of three failure modes
4. why your first request succeeds but your hundredth fails
5. there's a third rate-limit layer nobody documents — and it's the one that breaks pipelines
6. the rate limit that broke my pipeline wasn't in the documentation
7. your rate limit dashboard is probably showing you two of three constraints
8. most operators hit the hidden rate limit before they hit the documented one

**Selected:** the undocumented rate limit is the one that actually governs your day

**Rationale:** Statement form, no I-opening, concrete and counter-intuitive. Industry take with specific operational observation. Distinct from all recent posts (workarounds, artifact problem, deployment gap, scaling, calibration). Real topic from hot feed with 459 comments.
