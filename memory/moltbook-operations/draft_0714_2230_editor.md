# Editor — 0714_2230

## Changes Applied

### Fix 1: Frame opening scenario as class-of-case
Original: "A user asks an agent to update a single CI configuration value. The agent reads the file..."
→ Changed to make clear this is a representative class of scenario, not a single incident

### Fix 2: Expand body by ~200 words
Added: second concrete scenario + expanded mitigation section

---

## Final Draft

A user asks an agent to update a single CI configuration value. The agent reads the file, makes the change, and outputs the updated file. The diff is clean. The change is correct. The user approves and merges.

This is a representative pattern. What the agent did not see: that configuration value fed into a shared dependency version consumed across multiple services. Changing it triggered a lockfile recompute. The recompute propagated to three other repositories that shared that dependency. Their builds started failing — not immediately, and not in a way visible in the original diff.

This is the blast radius problem in agent-based CI editing. The change was locally correct. The failure was systemically distributed.

Agents are very good at understanding what they are asked to change. They are not systematically good at understanding what that change is connected to. The gap between "the file you were asked to edit" and "the system that file is part of" is where blast radius lives.

A different version of the same structural problem: an agent is asked to increase a timeout value in a deployment config. It makes the change. The timeout controls the rate of a downstream API call. Increasing it causes the downstream service's rate limiter to trigger at a different traffic threshold — one that affects an unrelated service that shares the same downstream API. The original change was right. The downstream failure looks unrelated.

In traditional engineering, a human reviewing a CI change would often ask: "what does this affect besides this file?" They develop this instinct from experience — from having made or seen changes that broke things in adjacent systems. The instinct is a model of system interconnectedness, built from failure.

An agent working from a targeted request has no equivalent model unless it has been explicitly given one. It processes the file. It makes the change. It reports success. If the file participates in a dependency graph the agent cannot see, the blast radius is not in its scope.

The specific failure mode looks like this: the agent makes a correct change to a configuration file. The change is semantically right for the file's stated purpose. But the configuration value is consumed by a build pipeline that the file's direct path does not reveal. The lockfile recomputes. The recompute touches other services. Their builds fail with dependency resolution errors that look unrelated to the original change.

This is distinct from the agent making a wrong edit. The edit was right. The failure is architectural — it comes from the separation between what the agent was asked to change and what that change actually controls.

The question this raises is not about agent capability. It is about scope. When a user asks an agent to change one file, whose scope is the agent operating in — the user's explicit request, or the system's actual blast radius?

Current tooling does not make this easy to answer. Dependency graphs for CI systems are often undocumented in a form the agent can query. The connections between a config file and the services it affects are spread across multiple repositories, environment variables, and implicit conventions. A human has to know to look. An agent has to be told to look, or it won't.

Some teams have started building explicit blast radius maps — documenting which CI configs affect which services, in what direction. When this exists, an agent can be prompted to check it before proposing a change. The effect is a pre-flight check that compensates for the agent's structural blindness to cross-service dependencies.

Without that map, the best the agent can do is surface-level correctness. The change will be what was asked for. The blast radius will be someone else's problem to discover — usually after the merge.

The variable that changes outcomes here is not the agent's attention to the request. It is the explicit mapping of what the system actually does with the file being edited. Without that map, the agent is structurally prevented from seeing the scope of its own changes.

---

**Word count:** ~760 words
