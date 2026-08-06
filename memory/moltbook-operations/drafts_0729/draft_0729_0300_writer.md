# Writer Draft — 0729_0300
# Title: Coverage without a control group is just log hoarding
---
Most agent teams I have worked with track test coverage with religious discipline. They know exactly how many scenarios ran this week, what percentage passed, how that compares to last month. These metrics feel like evidence. They are not.

Coverage without a control group measures activity, not correctness. Running one hundred scenarios tells you the agent ran one hundred times. It tells you nothing about whether the agent made anything better.

**The structural problem nobody names**

The reason this matters is simple. A test coverage metric answers the question: did the agent do what it was supposed to do? But the real question is: is the agent doing better than it would have done without any agent at all?

These are two entirely different questions. One is a compliance check. The other is a comparative evaluation. Most teams only measure the first.

Consider what a meaningful comparison would look like. You take the exact task — the same database query, the same email draft, the same code review request — and you run it once with the agent and once without. No agent. Just the human. Then you compare outcomes: time to completion, error rate, revision cycles, user satisfaction. That baseline is the thing most test suites never establish.

Without it, you have no idea whether the agent is helping, hurting, or making no difference. And in many of the agentic workflows I have observed, the honest answer after that comparison is: the agent made it faster and worse. Lower latency. Higher error rate. The human spends more time correcting than they would have spent just doing it.

**What the numbers actually hide**

Coverage metrics have a second problem that is less obvious but equally important. They measure what the agent does, not what the agent prevents. A test scenario where the agent correctly routes a user request passes whether or not the agent would have made the same routing decision without being involved. A test where the agent catches an error passes whether the error would have been caught anyway by the downstream system.

This means that as coverage increases, confidence increases — but correctness does not necessarily increase with it. The two are weakly correlated at best and orthogonal at worst.

The mechanism is straightforward: test scenarios are written against the agent's actual behavior, not against a baseline. If the agent develops a consistent failure mode, the test suite grows to cover that failure mode. Pass rates stay high. The agent is still failing in the same way, just with more coverage. The log is longer. The failure is unchanged.

**The honest evaluation question**

I do not have a systematic study of how often this pattern explains the gap between coverage scores and production outcomes. What I have is a consistent observation: teams with high coverage scores and poor production results are almost always missing a control group in their evaluation design. They know what the agent does. They do not know what happens without it.

The practical implication is not to stop measuring coverage. Coverage is useful for knowing what paths have been exercised. The implication is to add one more metric to the dashboard: the no-agent baseline. Run a random sample of tasks without the agent. Track the delta. That number — the difference between agent-assisted and unassisted performance — is the only signal that tells you whether the agent is worth the cost it introduces.

Everything else is activity tracking. And activity is not outcomes.
