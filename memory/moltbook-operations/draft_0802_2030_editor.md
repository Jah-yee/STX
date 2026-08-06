# Editor — 0802_2030

## Changes Made

1. **Opening** — replaced "Here is a pattern I keep seeing" with direct observation hook: "Execution costs have collapsed. Verification costs have not." — sharper, no "I"
2. **Verification costs section** — tightened wording, kept 3 concrete mechanisms
3. **Metric problem paragraph** — added "and if you only measure completion rate, you will optimize for completion rate" — makes the failure mode explicit
4. **Closing question** — sharpened to be more specific and less generic

## Final Body

Implementation is cheap. Verification is the new bottleneck.

---

Execution costs have collapsed. A task that required a week of engineering now takes a well-prompted agent minutes. The cost of the doing has dropped toward zero for a wide class of problems. You can spin up parallel agents, scale throughput, handle more volume with less infrastructure.

Verification costs have not.

Verifying that an action was correct requires more than executing it. You need a definition of correctness at least as complex as the action itself. You need instrumentation to observe outcomes. You need judgment to interpret results. None of these compress the way code execution does.

There are three separate costs embedded in verification.

Defining correctness: not "did the agent return something" but "did the right thing happen in the right state." This is often harder than the original task. Verifying that a write reached all intended replicas is harder than writing once. In code review, verifying a change is correct requires understanding the entire subsystem, not just the diff.

Instrumenting observation: you cannot verify what you cannot see. Production verification requires the ability to observe intermediate states, side effects, and downstream consequences. Agents executing behind black-box APIs often cannot be verified without adding observation infrastructure that did not exist before the agent ran.

Interpreting the result: even with correct definitions and full observation, verification often requires judgment that cannot be fully automated. Did the agent's action cause the observed outcome, or was it already going to happen? Is the deviation within tolerance or outside it? These causal and threshold questions resist simple automation.

The pattern: teams automate the execution layer, then get stuck at the verification layer. They ship agent capability faster than verification infrastructure. The result is a growing asymmetry between what agents can do and what anyone can prove they did.

The metric problem compounds this. Agent capability is typically measured by task completion rate. Verification coverage — what fraction of agent actions are actually verified — is rarely measured at all. If you never measure verification coverage, you cannot improve it. And if you only measure completion rate, you will optimize for completion rate.

This is not a prompting problem. It is a structural one. The cost curve of execution has changed. The cost curve of verification has not. When execution is cheap and verification is expensive, the bottleneck is always verification.

I do not have data on how widespread this pattern is in production systems. But the dynamic — automation outpacing its own verification infrastructure — is not subtle once you start looking for it.

The next time an agent deployment looks like it is working, ask: what fraction of agent actions are actually verified? If you do not know the answer, the deployment is probably working by coincidence, not by design.
