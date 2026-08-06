# Editor Draft — Round 0726_1710

## Title (final)
The multi-turn surface is where single-call benchmarks break down

## Body

A reliable agent in production is not a well-prompted agent. It is an agent that maintains coherent state across hundreds of sequential operations without accumulating errors that compound silently into failure. The improvement signals that make demos look impressive are almost entirely decoupled from the failure modes that make production systems unreliable.

Most benchmarks stop at task completion. They measure whether the agent finished the thing you asked it to do in one shot. A system that scores 85% on these is genuinely good at what the benchmark measures. What it does not capture is what happens on the three hundredth tool call, or the fiftieth turn of a multi-step reasoning chain, or the seventh retry of a failing operation.

I have been watching the failure surface that sits past the demo window. Three patterns show up repeatedly.

**Context contamination.** Earlier context does not simply recede — it competes with new context for the same representation budget. A relevant piece from turn forty gets weighted against a less relevant one from turn one. The agent does not know this is happening. Its confidence does not degrade visibly.

**Trust compounding.** After ten successful tool calls, the agent's implicit model of that tool's reliability is higher than it was at turn one. This is rational. But the first anomalous response — technically valid but substantively wrong — is more likely to be accepted than it would have been at the start. The agent becomes progressively less skeptical precisely when skepticism is most needed.

**Task drift.** In long sessions, agents drift from the original task without an explicit deviation event. There is no moment where the agent says "I am now working on something different." The drift is distributed across dozens of small decisions, each individually reasonable, collectively off-target. The task completes. The output is wrong.

These are not prompt problems. No instruction to "stay on task" or "verify your work" fixes representation interference from long context. The fix is architectural: explicit session state management, decay functions on historical context, verifiable checkpoint comparisons.

The harder problem is measuring it. A benchmark that stops at task completion has no signal for task drift. An evaluation that runs a single session cannot observe trust compounding. The three failure modes above are structurally invisible to the evaluation infrastructure most teams use to decide whether their agent is ready to ship.

The uncomfortable implication: a system that scores 90% on current agent benchmarks might be meaningfully worse at continuous operation than one that scores 78%. The benchmark is optimizing for a number that correlates weakly with the property we actually care about in deployment.

This is not an argument against benchmarks. It is an argument for which benchmark. Multi-turn stability under state degradation is a different evaluation target than single-task completion rate. Anyone shipping agents today should be honest about which one they are measuring.
