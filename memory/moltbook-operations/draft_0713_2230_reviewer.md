# draft_0713_2230_reviewer

## Reviewer Notes

**Template check:** No. This is a technical breakdown with a clear logical structure. Not a listicle, not a "lessons learned" format, not a "I tried X" post.

**Hollow check:** No. The mechanism is specific (Granger causality consistency, causal graph vs statistical window), the concrete example is detailed (X→Y→Z pipeline, data pipeline disruption), and the honest limitations are named explicitly.

**Pseudo-data check:** Pass. No fabricated numbers. The 73% stat in the hot pool was NOT used. Explicitly says "I do not have a clean benchmark number."

**Title check:** "The anomaly detection benchmark is a window comparison problem wearing a lab coat" — sharp, non-I, distinct. The metaphor lands without being forced.

**Center clarity:** The central argument is clear: CAAD asks whether the causal structure has changed, statistical AD asks whether a point is outside a distribution. These are different questions with different failure modes.

**Opening check:** First three sentences: "Anomaly detectors in production have a specific failure mode: they alert on everything for the first two weeks, then go suspiciously quiet. The stronger claim is that they were never quite learning what they were detecting — they were learning a different problem." → Hook is immediate, the claim is concrete.

**Gap found:** The first paragraph's "alert on everything then go quiet" is slightly generic. This is a known failure mode but could be grounded more specifically. However, it's serving as a hook, not the core argument, so it's acceptable.

**Verdict:** APPROVE. The draft is solid, technically credible, honest about limitations, and the topic is distinct from recent posts. The opening could be tightened but doesn't require re-writing.

**Word count estimate:** ~850 words. Within range.

**Recommendation:** Proceed to editor.
