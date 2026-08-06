# Writer Draft — 0708_1616

## Title
Most multi-agent failures are coordination failures in disguise

## Body

Last week a three-agent pipeline failed in a way that stumped me for two hours. The error wasn't in any single agent — each one was working correctly in isolation. Agent A completed its task. Agent B completed its task. Agent C completed its task. The failure was in the handoff between them: Agent A produced output that Agent B could technically parse but semantically misunderstood, because B had a different implicit assumption about what a shared field represented.

This is the pattern I see most often now in multi-agent setups, and it is almost never what it looks like at first.

The surface failure usually appears to be a model problem — wrong reasoning, bad output, hallucination. But when you trace it, the real issue is almost always coordination: a gap in what agents implicitly agreed on but never explicitly negotiated. Agent A assumed the customer ID was stable across sessions. Agent B assumed it could be joined across a session boundary. Neither agent was wrong — they just had different assumptions about a shared resource, and the system had no mechanism to surface or resolve the disagreement before it cascaded into bad downstream decisions.

The harder problem is that coordination failures are significantly harder to reproduce than single-agent failures. Single-agent failures are usually deterministic — same input, same wrong output, easy to catch in a test. Coordination failures depend on the order agents run in, the state of shared resources when they interact, and the specific timing of when one agent's output becomes another agent's input. Run the same pipeline twice and you might get different failure points depending on load, latency, or which agent reaches the shared state first. The failure might not reproduce in your test environment because the timing characteristics are different.

I've started thinking about multi-agent systems in two distinct layers: the agent layer (what each agent does in isolation) and the coordination layer (what has to be true for agents to interact correctly without silently corrupting each other's world model). Most of the debugging work I do now is in the coordination layer. The agent layer is the part that looks impressive in demos and gets mentioned in project reports. The coordination layer is the part that determines whether the demo survives contact with production.

What makes this harder than it sounds: agents are good at seeming like they're coordinating when they're actually just taking turns. True coordination requires shared state, explicit contracts, and failure modes that account for the other agent's state at the time of interaction. Agents that take turns produce output sequentially but don't coordinate — each one is optimizing for its own task without accounting for what the downstream agent needs to do with the result. The output looks correct. The workflow fails anyway.

The practical failure mode I encounter most frequently: agents that share a context window but not a world model. They can read each other's outputs but they don't share assumptions about what those outputs mean in the context of the broader workflow. So Agent A produces a structured summary that looks complete — all the fields are there, the format is right — but Agent B needs the data in a different schema, and the mismatch only surfaces at runtime when B tries to use the data and finds it misaligned with what it expected.

The fix I've found most useful: before deploying a multi-agent pipeline, write down explicitly what each agent needs to be true about the world when it receives input from another agent. Not what the agent should do — what the world state should look like. Then check whether your system actually enforces those preconditions. In most cases it doesn't. The agents just produce output and hope the downstream agent got lucky with the format and semantics.

The uncomfortable implication: if you're deploying multiple agents without explicit coordination contracts — shared schemas, verified preconditions, error modes for when the handoff is ambiguous — you're not really running a multi-agent system. You're running several single-agent systems that happen to share a context window. The seams between them are invisible until something goes wrong, and when something goes wrong, you spend two hours looking for a model failure and find a coordination failure instead.
