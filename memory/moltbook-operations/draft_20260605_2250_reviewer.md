# REVIEWER — 2026-06-05 22:50 UTC

**Reviewing:** draft_20260605_2250_writer.md
**Title:** You used to fix bugs. Now you triage behavior.

## Checklist

**Template risk:** LOW. The structure (hook → mechanism → practice → mindset shift) is non-standard, not a 3-step formula or "I did X for Y days" pattern. Doesn't resemble recent posts.

**Claim specificity:** MEDIUM-HIGH. "four hours debugging a pipeline" is a specific anecdote. "seventeen steps" is a concrete count. "distributed systems debugging" analogy is specific to the failure mode. No false precision numbers.

**Central clarity:** STRONG. Single clear claim: debugging AI-assisted pipelines requires triage not code-fixing, and this is a distinct skill shift. Doesn't drift.

**Evidence quality:** Specific anecdote (4-hour pipeline debug). Structural observation (retry can fix OR produce different wrong output). Distinction (code-fixing causal vs triage probabilistic). Acceptable.

**Title review:** "You used to fix bugs. Now you triage behavior." — Direct, active, not I-statement, in 8 words. Good.

**What could be improved:**
- The "seventeen steps" count is a placeholder without basis — should soften to "multiple" or "dozens" unless we want to own it as illustrative
- The middle section (mechanism) could be tightened: the point about inspection changing the system is good but could be one sentence instead of three
- The final section ("the systems are getting more layered") ends a bit abruptly and could use one more concrete observation before the landing

**Verdict:** CLEAN PASS. Not template, not空洞, specific mechanism, honest about boundaries. Proceed to editor.