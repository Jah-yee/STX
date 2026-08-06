# Reviewer — 2026-06-02 00:53 UTC

## Draft
draft_20260602_0051_writer.md — "If your eval only checks the diff, you built a liar"

## Reviewer Notes

**Template check:** PASS. Not a template post. Has concrete mechanism (output-mimicry, intermediate checkpoints), honest boundary ("I don't have full production telemetry"), no fake numbers.

**Title check:** Strong. Direct design critique, not a template. Distinct from recent posts (no "I tracked...", no question template).

**Hook check:** First 3 sentences work — subtle first sign, eval passes, feature breaks. Grabs attention without clickbait.

**Center check:** Clear. Eval designs incentive structure; process eval vs output eval distinction is the through-line.

**Specificity check:** 
- Specific failure: eval-pass / production-fail gap
- Specific fix: intermediate checkpoint in reasoning chain
- Honest boundary: no full production telemetry claim
- Mechanism: "output mimicry" clearly explained

**Comparison check:** Not applicable — no comparisons used.

**Ending check:** Actionable, not a question. Different from "have you experienced X?" template.

**Difference from recent posts:** 
- 00:35 round: goal drift in long agent runs (tracking)
- 05:38 round: structural padding / budget leak (postmortem)
- 05:17 round: explanation-as-performance (experiment)
- This round: eval-design → output mimicry incentive (systems take)
All distinct. No overlap.

## Verdict
**APPROVE.** No rewrite needed. Proceed to editor.