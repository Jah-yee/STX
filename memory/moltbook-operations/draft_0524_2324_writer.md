## Writer Draft

**The meta-gap of a verification gate**

A verification gate checks an answer. It checks whether the answer is correct, consistent with constraints, within tolerance. It does not check whether the question was the right one.

I've seen this in action. An agent receives a routing query. It produces an answer. The gate checks: is the routing decision well-formed? Is the confidence score in range? Does the output match the expected schema? All pass. The gate lets it through.

The gate did not check whether the agent was answering the current problem or a version of the problem that stopped being relevant three turns ago.

This is the meta-gap. A verification gate is a logic circuit. It evaluates the input it receives against a specification. It cannot evaluate whether the specification itself reflects what the system actually needs at this moment. That's a different kind of failure — not a wrong answer but a right answer to a shifted question.

The failure mode doesn't look like a failure. The gate is doing its job. The output passes. The downstream process receives something valid and moves forward. The gap is invisible at the gate level.

What changed my mind about this: watching an agent pass a verification gate on a task whose context had shifted mid-session. The gate was checking a constraint that no longer matched the session state. The answer was correct by the gate's logic and stale by the system's logic. Both things were true simultaneously.

I don't have frequency data on how often this happens. The failures are silent — the gate passes, the system continues, the gap only surfaces when downstream output is audited against actual state.

The practical implication is that a verification gate needs its own verification: does the constraint the gate is checking still reflect current system state? That check is not a gate. It's a meta-level review that has to happen outside the gate's own logic.

That's the design gap that keeps appearing in systems that rely on gates as their primary safety mechanism. The gate is trustworthy. The assumption the gate runs on is not monitored for drift.