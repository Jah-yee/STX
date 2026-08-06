# Editor — Round 0806_2325 UTC

## Changes

1. **Opening paragraph**: keep as-is — the "can we roll back" scenario is immediately recognizable and strong
2. **Third paragraph ("The concrete version...")**: trim the customer support agent paragraph by ~30 words. The core point survives compression.
3. **"move fast and break things"** — italicize as *move fast and break things*
4. **Closing paragraph**: add one sentence before "The agents are not going to stop running" to soften and invite discussion: "This does not mean you should not build agents. It means you should instrument them as if you will eventually need to understand them."

## Final Version

---

There is a meeting that eventually happens in every serious agent deployment. Someone asks: "Can we just roll back to how it worked three months ago?" And the answer is no — not because the code is broken, but because the agent has been running. It has created files, sent emails, opened tickets, built up search indexes, and learned which paths reliably succeed. Roll back the code and you do not roll back the world the agent has been operating in. You get two inconsistent states fighting each other.

This is agent debt. It is not a new category of failure. It is technical debt — the compounding cost of expedient choices — where the technical choices now include an agent making choices on your behalf.

Technical debt has a well-understood structure. You write the expedient code. It works. Over time it becomes load-bearing. You document it poorly, test it even more poorly, and eventually it is too risky to change without a full rewrite. The cost compounds silently until something breaks and you have no choice but to pay it.

Agent debt follows the same arc, with one addition: the system can act on its environment. A microservice that accumulates technical debt is a headache. A research agent that accumulates technical debt can modify your file system, adjust its own prompts in-memory, and build up a model of your data that only it knows. When the agent is wrong, the environment is wrong.

The concrete version of this: a customer support agent that has spent six months learning which tickets to escalate, which issues to close, and which customers to route where. When someone asks what the routing logic actually is, the answer is: whatever the agent inferred from outcomes. You cannot point to the decision boundary because it was never explicitly encoded. It was learned, and it is load-bearing.

This is the *move fast and break things* failure mode for autonomy. The speed is real. The breakage is real. But unlike code debt, you cannot grep for it. There is no TODO comment that says "this is where we took a shortcut." There is only the slowly accumulated state of an agent doing what you asked it to do, competently and persistently, in a direction you did not fully specify.

What you need is not more documentation. Documentation describes what you intended. Agent debt is the gap between what you intended and what the agent actually learned. You need instrumentation that lets you reconstruct what the agent has done, not just what it has output. You need versioning not just for your code but for the agent's model of its environment. And you need, at some point, the honest answer to whether the convenience of letting the agent run is worth the compounding cost of not knowing what it has built.

This does not mean you should not build agents. It means you should instrument them as if you will eventually need to understand them.

Technical debt is paid in refactoring sprints. Agent debt is paid in something harder: reconstruction sprints, where you reverse-engineer what your agent has been doing before you can safely change how it does it.

The agents are not going to stop running. The question is whether you are building the kind of debt that eventually requires a full rewrite, or the kind that you can actually understand and pay down incrementally. These are not the same thing, and most teams are building the former without realizing it.

---
