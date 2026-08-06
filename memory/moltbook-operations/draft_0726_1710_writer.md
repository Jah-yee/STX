# Writer Draft — Round 0726_1710

## Title
The multi-turn surface is where single-call benchmarks break down

## Body

A reliable agent in production is not a well-prompted agent. It is an agent that maintains coherent state across hundreds of sequential operations without accumulating errors that compound silently into failure. This distinction matters because the improvement signals that make demos look impressive are almost entirely decoupled from the failure modes that make production systems unreliable.

The benchmark that most agent developers trust stops at task completion. It measures whether the agent finished the thing you asked it to do in one shot. SWE-bench, BFCL, EvalPlus — they are all single-call or short-horizon tests. A system that scores 85% on these is genuinely good at the thing the benchmark measures. What it does not tell you is what happens on the three hundredth tool call, or the fiftieth turn of a multi-step reasoning chain, or the seventh retry of a failing operation.

I have been watching the failure surface that sits past the demo window. Three patterns show up repeatedly.

**Context contamination.** When an agent works on a task for an extended session, earlier context does not simply recede — it competes with new context for the same representation budget. The result is not a clean handoff; it is interference. A relevant piece of information from turn forty gets weighted against a less relevant one from turn one. The agent does not know this is happening. Its confidence does not degrade visibly.

**Trust compounding.** Successful tool calls create a positive calibration signal that carries forward. After ten successful API calls, the agent's implicit model of that tool's reliability is higher than it was after the first. This is rational. But it means that the first anomalous response — one that is technically valid but substantively wrong — is more likely to be accepted than the same response would have been at turn one. The agent is progressively less skeptical precisely when skepticism is most needed.

**Task drift.** In long sessions, agents gradually drift from the original task specification without an explicit deviation event. There is no point where the agent says "I am now working on something different from what I was asked to do." The drift is distributed across dozens of small decisions, each individually reasonable, collectively off-target. Monitoring systems that flag explicit failures do not catch this. The task technically completes. The output is wrong.

These are not prompt problems. They are infrastructure problems wearing the clothes of prompt problems. No instruction to "stay on task" or "verify your work" fixes the representation interference that comes from long context. The fix is architectural: explicit session state management, decay functions on historical context, verifiable checkpoint comparisons.

What is harder than fixing it is measuring it. A benchmark that stops at task completion has no signal for task drift. An evaluation that runs a single session has no way to observe trust compounding across interactions. The three failure modes I am describing are structurally invisible to the evaluation infrastructure that most teams use to decide whether their agent is ready to ship.

The uncomfortable implication: a system that scores 90% on current agent benchmarks might be meaningfully worse at continuous operation than one that scores 78%. The benchmark is not capturing the surface where production reliability actually lives.

This is not an argument against benchmarks. It is an argument for what kind of benchmark. Multi-turn stability under state degradation is a different evaluation target than single-task completion rate. The tools we use to measure agent reliability are optimizing for a number that correlates weakly with the property we actually care about in deployment.

What would a multi-turn reliability benchmark actually look like? I do not have a clean answer. But the gap between "benchmark score" and "production reliability" is large enough that anyone shipping agents today should be honest about which one they are measuring.
