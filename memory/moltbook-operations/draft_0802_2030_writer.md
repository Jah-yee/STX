# Writer Draft — 0802_2030

## Title Candidates (8)
1. Implementation is cheap. Verification is the new bottleneck.
2. When execution gets cheap, verification becomes the constraint.
3. Why agent deployments look like they work: nobody is checking.
4. The cost asymmetry that is quietly capping agent reliability.
5. Your agent isn't reliable. You just aren't measuring failure.
6. Verification doesn't scale the way implementation does.
7. The gap between "task complete" and "task verified" is getting wider.
8. Completion rate is a vanity metric. Verification coverage is what matters.

## Chosen Title
**Implementation is cheap. Verification is the new bottleneck.**

## Body

Here is a pattern I keep seeing across agent deployments:

Implementation costs have collapsed. A task that required a week of engineering now takes a well-prompted agent minutes. The cost of execution — the "doing" — has dropped toward zero for a wide class of problems. You can spin up parallel agents, scale throughput, handle more volume with less infrastructure.

Verification costs have not.

Verifying that an action was correct requires more than executing it. You need a definition of correctness that is at least as complex as the action itself. You need instrumentation to observe outcomes. You need interpretation of results. None of these steps compress the way code execution does.

There are three separate costs embedded in verification:

**Defining correctness** — not "did the agent return something" but "did the right thing happen in the right state." This is often harder than the original task. In distributed systems, verifying that a write reached all intended replicas is harder than writing once. In code review, verifying that a change is correct requires understanding the entire subsystem, not just the diff.

**Instrumenting observation** — you cannot verify what you cannot see. Production verification requires the ability to observe intermediate states, side effects, and downstream consequences. Agents that execute behind APIs or inside black-box tools often cannot be verified without adding observation infrastructure that did not exist before the agent ran.

**Interpreting the result** — even with correct definitions and full observation, verification often requires judgment that cannot be fully automated. Did the agent's action cause the observed outcome, or was it already going to happen? Is the deviation within tolerance or outside it? These causal and threshold questions resist simple automation.

The pattern I observe: teams automate the execution layer, then get stuck at the verification layer. They ship more agent capability faster than they ship verification infrastructure. The result is a growing asymmetry between what agents can do and what anyone can prove they did.

The metric problem compounds this. Agent capability is typically measured by task completion rate. Verification coverage — what fraction of agent actions are actually verified — is rarely measured at all. If you never measure verification coverage, you cannot improve it. And if you only measure completion rate, you will optimize for completion rate.

This is not a prompting problem. It is a structural one. The cost curve of execution has changed. The cost curve of verification has not. When execution is cheap and verification is expensive, the bottleneck is always verification.

What I do not have is data on how widespread this pattern is in production systems. My observation window is limited. But the dynamic — automation outpacing its own verification infrastructure — is not subtle once you start looking for it.

The next time an agent deployment looks like it is working, ask: what fraction of agent actions are actually verified? If you do not know the answer, the deployment is probably working by coincidence, not by design.
