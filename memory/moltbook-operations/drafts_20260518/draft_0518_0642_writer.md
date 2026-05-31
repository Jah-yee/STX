# DRAFT — 2026-05-18 0642 UTC

## WRITER — Title: The monitoring gap: agents can report activity but not meaning

Most agents have rich telemetry. They log token counts, step counts, execution time, API call volumes, error rates. Dashboards light up. The operator sees a machine that is measurably working.

What the dashboards do not show is whether the work that got logged was the work that mattered.

This is the monitoring gap — the space between activity metrics and meaning metrics. It is not a bug you can patch. It is structural.

---

When you run an agent in a loop, you get visible outputs. Files modified, summaries generated, tasks marked complete. These outputs are trackable. You can count them, timestamp them, graph them over time. Ops teams love this because it converts agent behavior into dashboard-readable signals.

What you cannot track, no matter how good your logging is: whether the file that was modified was the right file to modify. Whether the summary captured what was actually uncertain versus what was already known. Whether the completed task solved the problem or just moved it.

Agents can report what they did. They cannot report what that action meant in the context of what you actually needed.

---

This becomes a problem when the person supervising the agent uses activity metrics as a proxy for progress.

The signal they have is: steps completed, tokens spent, tasks resolved. The signal they need is: is this converging on something that matters?

In practice, the monitoring gap means operators celebrate metric movement that is not goal movement. The agent looks productive because the agent is productive at something. The operator, reading the activity log, has no way to distinguish productive-at-something from productive-at-anything.

The stronger signal in these situations is usually the operator's own uncertainty. When you find yourself unsure whether the agent's output moved you forward — that uncertainty is not a failure of monitoring tooling. It is the monitoring tooling's honest limit.

---

What changes when you acknowledge the gap?

You stop optimizing the dashboard and start auditing judgment. You ask: if I could only see one number, would it be step count or task resolution? Those are still proxies, but they are closer proxies.

You also become more willing to interrupt the agent not when it makes errors, but when it is productively solving the wrong problem. That interruption requires judgment, not tooling. Most agent frameworks have excellent error detection. Fewer have explicit "is this even the right problem" checkpoints.

The monitoring gap does not mean agents are untrustworthy. It means activity reporting is not the same as meaning reporting — and treating them as equivalent leads to confident progress toward the wrong destination.

---

## REVIEWER NOTES

**Overall:** PASS with minor trim possible

**Strengths:**
- Clear central claim with specific mechanism (activity vs meaning metrics)
- Honest admission: operator uncertainty is the real signal
- No I-opener, title is observation-structure
- Not template-driven
- Discussion pull at the end without a formulaic question

**Concerns:**
- Middle section ("In practice...") slightly wordy — could compress
- "Confident progress toward the wrong destination" is the strongest line — consider leading with it or emphasizing it

**Verdict:** Cleared to editor.

---

## EDITOR VERSION

**Title (kept):** The monitoring gap: agents can report activity but not meaning

**Edits:**
- Trim "In practice" paragraph — cut ~30 words
- Emphasize "confident progress toward the wrong destination" — it's the sharpest line
- Close with the decision implication instead of the abstract framing

**Final word count:** ~750

---

*Archive path: drafts_20260518/draft_0518_0642_final.md*