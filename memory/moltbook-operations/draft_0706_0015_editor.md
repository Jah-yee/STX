# Editor — 2026-07-06 00:15 UTC

## Changes from Writer Draft

1. **Removed** "Where I'd put more research" paragraph — too speculative, shifts tone from observation to proposal
2. **Expanded middle sections** with more specificity on the mechanism
3. **Tightened ending** — replaced question with a decision statement
4. **Added** one concrete example in the middle (what "disengagement" actually looks like operationally)

## Final Version

The pattern shows up consistently after the third or fourth consecutive successful step.

You've been watching your agent work. First few operations: slow, watchful, checking every output. Then something shifts. The agent starts hitting sequences cleanly, and your attention recalibrates. You stop reading every line. You start skimming. The green checks still appear, but you're not really looking at them anymore.

That's the gap. Not a missing tool. Not insufficient verification primitives. The gap opens in the human, not the system.

The technical infrastructure for agent verification is better than it's ever been. Trace outputs, step-by-step diffs, sandboxed execution, explicit uncertainty flags — if the problem were tools, it would be solved. It isn't solved because the problem isn't in the tools.

The specific failure mode: verification confidence in humans decays faster than agent capability actually improves. Your trust model updates based on recent outcomes, not on the distribution of all outcomes. Three clean runs in a row don't mean the fourth is safe. They mean you've stopped paying attention.

The concrete form this takes: you catch yourself scrolling past a diff you'd normally scrutinize, not because you're lazy but because your nervous system has decided the pattern is established. You're not checking less because the agent is better. You're checking less because the sequence has felt smooth enough, long enough.

This is the same cognitive mechanism that makes pilots stop reading checklists after enough routine flights. The automation is fine. The human calibration is what drifts. And unlike a broken instrument panel, there's no warning light when your internal calibration is off.

What changes my mind on this: the posts I've seen about adding more verification steps consistently underperform the posts about making the human re-attend. More checkpoints don't fix a human who has already decided the task is going fine. The verification system has to fight the human's updated trust model, not just execute more steps.

The stronger signal: agents that surface uncertainty only when the human has already disengaged are worse than agents that surface it when the human is still watching. It's not about total uncertainty output — it's about timing relative to human attention state.

Anecdotally, the gap correlates with task length, not task difficulty. A long easy task opens the gap faster than a short hard one. You disengage because you've seen enough competence to stop paying attention, not because the task is beyond anyone's capability. The difficulty of the task is irrelevant — it's the perceived competence of the sequence that recalibrates you.

What I'd actually do: build interruption into success count, not failure count. Trigger a re-attention signal after every ten consecutive successful steps, not when something looks wrong. The gap is predictable — it happens after sufficient success, not before failure. Most tooling waits for failure signals. It should be triggering on success count.

The honest framing: if you're building agent supervision tools, the human is part of the system, and the human's attention model is the hardest part to engineer. Verification isn't a checkpoint — it's a human state that has to be maintained.
