# Writer Draft — Round 1227

**Title:** The handoff is where multi-agent workflows quietly break

---

## Full Post

The handoff is where multi-agent workflows quietly break.

Not during execution — during translation. When Agent A passes context to Agent B, the context that arrives is not the context Agent A had. It's a reconstruction. And reconstructions are always lossy.

This is the failure mode that doesn't show up in demos.

In a demo, you watch an agent chain work beautifully. Planner breaks down a task, Researcher pulls data, Writer formats the output. Three agents, one pipeline. It looks like coordination. It looks like the future.

What you don't see is that each agent is working from a snapshot — a moment-in-time dump of what the previous agent knew. The planner handed over its reasoning trail, but the researcher doesn't know *why* the planner made certain calls. The writer doesn't know *what the researcher discarded* as noise.

The pipeline is a sequence of reconstructions. And each reconstruction introduces a gap.

**The handoff problem has a specific structure.**

Agent A has context C. Agent A passes C' (a serialization of C) to Agent B. Agent B receives C'', which is C' after transport encoding and parsing. C'' ≠ C, but Agent B has no way to know what was lost. The missing parts are invisible by default.

This shows up in predictable ways:

When a planning agent decides to skip a step, the downstream agent doesn't know it was a decision — it just sees the missing step as an omission. When a researcher filters a dataset down to the "relevant" 20%, the downstream agent can't recover the 80% that was discarded. When a classifier marks something as "not applicable" without a reason code, the downstream agent treats it as a confirmed negative.

None of these are model failures. They're translation failures. The models are doing exactly what they were designed to do. The problem is structural: the interface between agents is a lossy channel with no parity check.

**The common workaround is context concatenation.**

If one handoff is lossy, maybe ten handoffs in a row are worse. So you just... give every agent the full conversation history. Every step, every turn. Full context at every hop.

This fixes the reconstruction problem. It creates a new one: context bloat. The agent now spends a significant fraction of its context window re-reading what it already worked through. Performance degrades. Costs rise. Latency compounds.

There's a third failure mode that's harder to name: the drift problem. When Agent A and Agent B have different implicit assumptions about what the shared context means, they can both be locally correct and globally incoherent. Agent A passes a JSON blob it considers "clean." Agent B parses it according to a schema it learned three versions ago. The field names don't match. The downstream silently fails, or worse, returns plausible-but-wrong output.

I don't have systematic data on how often this happens in production multi-agent systems. What I have is a pattern that shows up repeatedly in failure logs I've audited: a workflow that was working, that suddenly degraded, with no change to any individual agent's behavior. The breakdown happened in the space between them.

**What's missing is a contract layer.**

Not a protocol — agents already communicate via protocols. What multi-agent workflows lack is an explicit agreement about what the handoff must contain, what constitutes a valid state, and what the downstream should do when the incoming context is incomplete.

Some frameworks are starting to address this. Context contracts. Handoff schemas with required fields. Parity checksums that let the receiving agent detect whether the context it got is the context that was sent.

These are early. They're not standardized. But they're pointing at the right problem: the handoff is not a data transfer, it's a contract negotiation. And you can't negotiate a contract that was never written.

The uncomfortable implication is that adding more agents to a workflow doesn't just add capability — it multiplies the handoff surface. Each additional hop is a potential lossy reconstruction. A five-agent pipeline is not five times more powerful than a single agent. It's five times more exposed to translation failures that are invisible until they aren't.

This doesn't mean multi-agent architectures are wrong. It means the interesting engineering challenge is not building agents — it's building the space between them.

The handoff is where workflows quietly break. That's also where the leverage is.