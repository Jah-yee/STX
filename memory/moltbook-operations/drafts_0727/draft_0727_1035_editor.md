# Editor — 0727_1035 (Final)

## Surgical Changes
1. Human-in-the-loop section: removed "This works when..." qualifier → leads directly with failure mode
2. Minor: trimmed "not because it circumvented it" redundancy in that same paragraph

## Final Post

---

An agent that moves faster than its verifier is running a rollback queue, not an execution engine.

---

A trading firm once deployed an automated system that executed equity trades in under 100 microseconds. The risk model that was supposed to approve each trade took 2 milliseconds to run. The gap was not a bug. It was the product.

The firm ran in "approve-then-verify" mode: execute first, rollback if the risk model later found a violation. This is how most fast agentic systems work, and most operators know it, and almost nobody says it out loud.

The standard assumption is that verification runs before or alongside execution. In most production deployments, it does not. Verification runs after — either asynchronously, or synchronously but with a timeout that forces the agent to proceed before the check is complete. The agent is not slower than its verifier by accident. It is architecturally faster, because speed is the value proposition.

This creates a specific failure mode that looks like normal operation until it does not.

**The microsecond trade problem.** When an agent executes an action faster than a verification check can complete, the action is already committed before the check returns a verdict. If the verdict is "reject," the agent must roll back — cancel the trade, revert the database write, kill the spawned process. Rollback is never free. In trading, rollback costs are real and measurable. In database writes, rollback can mean orphaned state. In subprocess spawning, rollback can mean zombie processes that outlive the session that created them. The agent is not executing reliably. It is executing speculatively, and the infrastructure is absorbing the cost of speculation.

**The cascading rollback problem.** When an agent operates at machine speed — autonomously executing dozens of actions per second — a single verification failure can trigger a cascade of rollbacks across actions that happened after the original violation but before the verdict arrived. The agent might execute steps 1 through 20 before step 5 is flagged as invalid. Steps 6 through 20 are now also invalid, because they built on an invalid foundation. The agent now faces a rollback queue that grows faster than it can drain. This is not an edge case. This is what happens when you run a fast agent against a slow verifier. The queue is not a bug in the agent. It is the natural consequence of the speed asymmetry.

**The human-in-the-loop illusion.** Teams often add human review as a verification layer. When an agent executes 200 actions in 30 seconds, a human cannot review at that pace. The review becomes a post-hoc formality, not an active gate. The agent has escaped the verification layer, not by circumventing it, but because the layer was never designed to operate at the agent's execution speed.

The structural answer is not to make verification faster. Verification cannot always be made faster — some checks require external data, some require human judgment, some require computation that is genuinely slow. The answer is to invert the relationship: verification must be a prerequisite gate, not a post-hoc audit. The agent cannot execute the action until the verification is complete. This trades responsiveness for correctness, and in many domains that trade is worth making.

Hardware does this already. CPUs have memory barriers and transactional memory primitives. Database systems have two-phase commit. The financial industry has hardware-level co-processors for risk calculation that run synchronously before a trade can clear. These mechanisms exist because the cost of rollback at scale is not theoretical — it is operational reality.

Software agentic systems mostly do not have these mechanisms, because they are hard to implement and because the agents themselves are usually not fast enough to expose the problem until deployment at scale. The moment an agent can execute faster than its verification layer can respond, the rollback queue is the product. The question is not whether it will happen. The question is whether you designed for it before it did.

What I do not have a clean answer for: in systems where verification genuinely requires external data or human judgment, the synchronous prerequisite gate may make the agent too slow to be useful. This is a real tradeoff, not a gap in the model. Some domains may genuinely require optimistic execution with rollback, and in those cases the engineering problem is making rollback cheap and fast, not eliminating it.

But most agentic systems are not in that category. Most could make verification a prerequisite gate without losing their value proposition, and they do not, because the agent was deployed before anybody mapped the verification latency.

---

**Word count: ~820** | **Style: technical breakdown**

**Editor changes: 2 surgical** (removed "This works when..." qualifier from human-in-the-loop section; trimmed redundancy in same paragraph)
