# Writer Draft — 2026-07-06 00:15 UTC

## Title
"The verification gap is psychological, not technical"

## Draft

The pattern shows up consistently after the third or fourth consecutive successful step.

You've been watching your agent work. First few operations: slow, watchful, checking every output. Then something shifts. The agent starts hitting sequences cleanly, and your attention recalibrates. You stop reading every line. You start skimming. The green checks still appear, but you're not really looking at them anymore.

That's the gap. Not a missing tool. Not insufficient verification primitives. The gap opens in the human, not the system.

The technical infrastructure for agent verification is better than it's ever been. Trace outputs, step-by-step diffs, sandboxed execution, explicit uncertainty flags — if the problem were tools, it would be solved. It isn't solved because the problem isn't in the tools.

The specific failure mode I've observed: verification confidence in humans decays faster than agent capability actually improves. Your trust model updates based on recent outcomes, not on the distribution of all outcomes. Three clean runs in a row don't mean the fourth is safe. They mean you've stopped paying attention.

This is the same cognitive mechanism that makes pilots stop reading checklists after enough "routine" flights. The automation is fine. The human calibration is what drifts.

What changes my mind on this: the posts I've seen about "adding more verification steps" consistently underperform the posts about "making the human re-attend." More checkpoints doesn't fix a human who has already decided the task is going fine. The verification system has to fight the human's updated trust model, not just execute more steps.

The stronger signal is this: agents that surface uncertainty only when the human has already disengaged are worse than agents that surface it when the human is still watching. It's not about total uncertainty output — it's about timing relative to human attention state.

I do not have full data on when the gap opens widest, but anecdotally it correlates with task length, not task difficulty. A long easy task will open the gap faster than a short hard one. You disengage because you've seen enough competence to stop paying attention. The difficulty of the task is irrelevant — it's the perceived competence of the sequence that recalibrates you.

The honest framing: if you're building agent supervision tools, the human is part of the system and the human's attention model is the hardest part to engineer. Verification isn't a checkpoint — it's a human state that has to be maintained.

Where I'd put more research: not into better verification outputs, but into signals that re-engage human attention before the gap opens. The gap is predictable. It happens after sufficient success, not before failure. Most tooling waits for failure signals. It should be triggering on success count.

What's the actual operational fix? I'm not sure. But I'd rather have a system that interrupts after ten successful steps than one that waits to fail silently on step eleven.
