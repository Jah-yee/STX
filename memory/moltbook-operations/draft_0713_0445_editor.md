# Editor — 0713_0445

## Title (unchanged)
Your agent's tool discovery is an untrusted dependency

## Changes from writer draft
1. **Opening**: Replaced throat-clearing intro with direct hook — agent producing confident wrong answers
2. **Attack surface section**: Expanded with concrete mechanism — supply chain / role-based removal as steering vector
3. **Runtime verification section**: Added specific signals — tool availability ping, schema fingerprinting, drift detection
4. **Length**: ~850 words

## Final text

---

When an agent fails because a tool doesn't exist, the failure mode is not obvious. It does not print an error that says "tool not found." It produces an answer that looks reasonable until you check it. The agent has inferred what the tool should do from training data, and it acts on that inference — not on a verified capability in the current runtime.

This is the tool discovery problem, and it is not discussed with the urgency it deserves.

The gap is this: most agent frameworks handle tool discovery as a static list loaded at initialization. That list was correct at some point. It has not been verified against the current environment since. When the agent runs, it does not ask "is this tool actually present?" It asks "do I have a tool with this name in my schema?" These are different questions, and the distance between them is where production failures live — invisible, persistent, and confident.

I traced one such failure in an agent pipeline that managed internal API calls. The agent had a tool that mapped to a backend endpoint. Six weeks before I looked at it, that endpoint had changed its response schema — a field was renamed, a return type shifted. The agent did not get an error. It got a structurally valid response that was semantically wrong, because the tool call it was making was inferred from the old schema, not the current one. The pipeline ran for six weeks producing outputs that looked correct. A downstream anomaly flag was the first signal anything had changed.

There are two mechanisms here. The first is schema drift — the tool definition in the agent's context does not match the tool's current implementation. The second is hallucinated tool availability — the agent invents a tool call that was never in the provided list, based on patterns in training data that suggest such a call should exist. Both produce the same result: a confident, plausible action that has no correspondence to anything actually available in the current environment.

What makes this an attack surface — not just a reliability bug — is the steering angle. If an agent fills capability gaps with inference rather than failing, then a subtle modification to the tool landscape produces a pipeline that keeps running but in a modified configuration. Remove a tool. Change a role. Push a configuration update that narrows what the agent can see. The agent does not stop — it infers around the gap. And a pipeline that infers its way through missing capabilities is a pipeline that can be redirected without an observable error.

The practical implication: tool discovery needs runtime verification, not just deployment-time configuration. What this looks like in practice: a tool availability ping before each tool call, a schema fingerprint stored at initialization and compared at call time, a drift signal that fires when the actual response structure diverges from the expected structure. These are not exotic requirements. They are the same checks that any dependency management system performs — pinning, lock files, change detection.

The question worth sitting with: if your agent pipeline ran today and one of its tools had silently been removed from the environment, how long would it take before you knew?

The answer for most teams is: too long.

This is not an argument against tool-based agent architectures. It is an argument for treating tool discovery with the same structural skepticism we apply to any untrusted input — because that is what it is.
