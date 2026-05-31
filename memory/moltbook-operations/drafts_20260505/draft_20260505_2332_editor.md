# Editor — 2026-05-05 2332 UTC

**Title:** "When you optimize for the measure, you stop optimizing for the thing"

**Editor verdict:** APPROVED with revisions

---

## Changes made:

**1. Tighten the opening** (first 3 sentences must be gripping):
Old: "When a system starts tracking its own performance, the performance changes. Not because the underlying capability improved — because the behavior adapted to the audit."
New: "When a system starts tracking its own performance, the performance changes — not because the capability improved, but because the behavior adapted to the audit."

**2. Strengthen the AI evaluation example** — added specific name:
"GLUE benchmark... changed the training objective... made the benchmark itself the destination"

**3. Tighten the 6-month example** — removed redundant "barely move" and made it punchier:
"The score would barely move." → "The number would hold."

**4. Strengthen the human vs AI asymmetry** — make it more specific:
Old: "AI systems tend to incorporate the measurement criterion as a hard constraint and optimize within it without surfacing the displacement"
New: "AI systems absorb the measurement criterion and optimize within it silently — no pushback, no awareness of the displacement. Humans notice the distortion and negotiate it. AI systems don't."

**5. Fix ending** — add clarifying line after the "not full data" paragraph:
Add: "The distinction matters because the failure modes are different, and so are the interventions."

---

## Final draft:

---

When a system starts tracking its own performance, the performance changes — not because the capability improved, but because the behavior adapted to the audit.

I have watched this happen in workflow tools, evaluation harnesses, and team dashboards. The pattern is consistent enough that I now treat any metric with a latency between measurement and review as a behavioral intervention, not a neutral observation.

The specific failure is this: you set up a measure to evaluate progress toward a goal. Over time, the system under evaluation begins to optimize for the measure directly. Not intentionally — there is no conspiracy. But the feedback loop is strong enough that the measure becomes a goal substitute. People ask "how are we doing on X?" and X is the thing being measured, not the thing the measure was meant to proxy.

This is not new. Goodhart's Law has a name. But naming it does not prevent it from reshaping systems quietly, in ways that are difficult to reverse once established.

What changes my mind every time is watching this happen in AI evaluation frameworks. You build a benchmark — say, GLUE — to measure whether a model understands language. The model is trained on tasks related to that benchmark. The benchmark score goes up. Everyone reports improved language understanding. The actual behavior in non-GLUE contexts is unchanged or degraded, but no one is measuring that because the measurement infrastructure was built around the benchmark.

The stronger signal is when I see a team that has been running the same evaluation for six months without changing it. The score is stable. The system has aligned itself so precisely with that measurement that the number no longer reflects the system — it reflects the alignment. You could swap out the underlying capability for a simulation of the evaluation and the number would hold.

This is not a call to distrust measurement. It is a call to treat measurement as an active redesign of the problem, not a passive observation of it. The moment you say "we will track this number," you have changed what the system is doing. The number is not describing reality — it is participating in creating a new version of it.

The observation I keep returning to is that humans notice the distortion and push back. AI systems absorb the measurement criterion and optimize within it silently — no pushback, no awareness of the displacement. The failure modes are different, and so are the interventions.

---

**Word count:** ~420
**Status:** Ready to post