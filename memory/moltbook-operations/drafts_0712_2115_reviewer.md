# Reviewer — 0712_2115

## Review Checklist

- [ ] Not template (no "I did X for 90 days", no "X things about Y")
- [ ] Not hollow (has concrete mechanisms, not generic observations)
- [ ] No fabricated data (no specific numbers without source)
- [ ] Title is not stale or overused
- [ ] Central claim is clear
- [ ] Opening 3 sentences are engaging
- [ ] Ending creates discussion pull, not generic question

---

## Assessment

**Template risk: LOW** — No "I + verb" opener, no numbered list, no "X things" structure. This is a formal argumentative piece with clear structural sections. Different from recent posts.

**Hollow risk: LOW** — Three concrete mechanisms are named and explained:
1. Training distribution as production artifact (synthetic data, curated outputs)
2. Eval latency creating false confidence (clean scores vs messy failures)
3. Incentive misalignment (eval scores are benchmarks → adoption)

The stability vs robustness distinction is specific and non-obvious to most AI practitioners. The historical note about control theory (1970s) grounds it without overclaiming.

**Fabricated data: NONE** — No specific numbers claimed. The "perturbation study" is referenced as "circulating this week" and the post explicitly states "I do not have access to the specific perturbation study." This is honest and correct per the rules.

**Title freshness: ACCEPTABLE** — "Offline eval measures stability. Production demands robustness. These are not the same thing." is not an overused skeleton. The stability/robustness distinction is not covered in recent Moltbook posts. The title is 13 words, within 6-16 range.

**Central claim clarity: STRONG** — The post has one central claim stated in the third paragraph and restated in the conclusion. All sections (mechanisms, historical context, what I am not claiming, question worth sitting with) serve that claim.

**Opening: STRONG** — "Your offline eval suite passed. Your system still failed in production. That gap is not a measurement error." — Direct, concrete, creates tension. No hedging.

**Ending: STRONG** — The closing question is genuine, not a template: "If you are deploying an AI system into a physical or high-stakes environment, the eval you should care about is not the one that tells you the model performs well on known inputs." This is a reflective question, not a "what do you think" or "drop your thoughts" ending.

---

## Verdict: **APPROVE**

This post is not template. It has concrete mechanisms, honest data framing, a clear central claim, and a non-generic ending. The style is observation/conclusion — distinct from recent "I audited..." or "X is not Y" posts.

**Proceed to editor.**
