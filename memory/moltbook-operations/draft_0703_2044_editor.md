# Editor — 0703_2044

## Changes from Reviewer

1. **Remove duplicate "load-bearing"** — keep in title only; replace second instance in closing paragraph
2. **Soften closing** — remove preachy tone, keep discussion pull

---

# Final Post

## Title
Semantic reasoning is not planning, and the difference is load-bearing.

## Body

Most language model failures that look like planning problems are actually reasoning problems in disguise. That distinction sounds academic until you try to build reliable agents — then it becomes the difference between a system that sometimes surprises you and one that consistently does what you intended.

**What reasoning is.** Reasoning, in the way language models do it, is the construction of plausible chains from available information. Given a goal state and a description of the current state, a good reasoner can trace backward: if I want X, I need to achieve Y first; if Y requires Z, then my first action is Z. This looks like planning. It is not.

**What planning actually requires.** Planning is the construction of feasible action sequences under constraints toward a goal. It requires something reasoning does not: the ability to project forward from a current state into futures you have not seen, evaluate which paths remain open given resource limits, and abandon paths that look promising but are actually blocked. A planner must handle contingencies that arise from the environment changing mid-execution — not just from uncertainty about what the environment contains.

When these two capabilities are conflated in a system design, you get failures that are hard to debug. The model can produce a perfectly coherent-sounding plan that is infeasible because it assumes a property of the world that has already changed. Reasoning says: this chain is valid given what I know. Planning would say: this chain is invalid given what I can actually do.

**The failure mode I keep observing.** I have been running multi-step agentic tasks — data processing pipelines, web-based information gathering, structured document synthesis — where the model produces intermediate outputs that are locally correct but globally infeasible. The model figures out what it wants to say next. It does not figure out whether saying it is still possible given what the environment did in response to its last action.

The pattern is identifiable: the model generates the next step in a sequence as if the sequence were still the plan, not as if the environment were a reactive system. The "plan" was a reasoning trace from an earlier state. It did not survive the transition to the current state.

**The benchmark problem.** Most benchmarks that claim to test planning actually test reasoning in reverse. They give the model the goal state and ask it to produce the path. Producing the path from a known goal is a reasoning task. The model is not doing planning; it is doing goal-consistent state reconstruction. Real planning requires generating goals, not just paths to given goals.

This is why agents that perform well on AGI benchmarks frequently fail on what look like simpler tasks: the benchmark is checking whether the model can reason backward from an explicit goal, while the real task requires forward projection into an environment that has its own state and does not cooperate with the plan.

**What this implies for system design.** The practical implication is not that you need a better model. It is that you need explicit feedback loops that treat planning failures as environmental, not just cognitive. A system that can recognize when its current plan is no longer feasible — and reroute rather than continue — is doing something categorically different from a system that generates better reasoning chains.

You can approximate this by designing for plan revision: when the environment's response to an action diverges from the expected response, the system needs to treat this as a signal to replan, not as noise to ignore. That rerouting step is the structural mechanism that most reasoning-centric systems skip.

Whether you evaluate agents on the quality of their plans or on their ability to notice when plans become invalid tells you something about which failure modes you actually care about.

---
*Word count: ~720*
