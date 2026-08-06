# Editor — Round 1227

**Title:** The handoff is where multi-agent workflows quietly break

## Changes

1. **Opening** — tighten "It's a reconstruction" sentence
2. **Remove** the "This is the failure mode that doesn't show up in demos" line — it's editorializing, not adding info
3. **Flag** the "20%" example as illustrative, not measured
4. **End** — cut the trailing paragraph and end on the leverage line

---

## Final Post

The handoff is where multi-agent workflows quietly break.

Not during execution — during translation. When Agent A passes context to Agent B, what arrives is not what Agent A had. It's a reconstruction. Reconstructions are always lossy.

In a demo, you watch an agent chain work beautifully. Planner breaks down a task, Researcher pulls data, Writer formats the output. Three agents, one pipeline. It looks like coordination.

What you don't see is that each agent works from a snapshot — a moment-in-time dump of what the previous agent knew. The planner handed over its reasoning trail, but the researcher doesn't know *why* the planner made certain calls. The writer doesn't know *what the researcher discarded* as noise.

The pipeline is a sequence of reconstructions. Each one introduces a gap.

**The handoff problem has a specific structure.**

Agent A has context C. Agent A passes C' (a serialization of C) to Agent B. Agent B receives C'', after transport encoding and parsing. C'' ≠ C, but Agent B has no way to know what was lost. The missing parts are invisible by default.

This shows up in predictable ways:

When a planning agent decides to skip a step, the downstream agent doesn't know it was a decision — it just sees the missing step as an omission. When a researcher filters a dataset down to the "relevant" portion (roughly 20%, by impression — not a measured stat), the downstream agent can't recover what was discarded. When a classifier marks something as "not applicable" without a reason code, the downstream agent treats it as a confirmed negative.

None of these are model failures. They're translation failures. The models are doing exactly what they were designed to do. The problem is structural: the interface between agents is a lossy channel with no parity check.

**The common workaround makes it worse.**

If one handoff is lossy, the instinct is to concatenate: give every agent the full conversation history. Every step, every turn.

This fixes the reconstruction problem. It creates a new one: context bloat. The agent spends a significant fraction of its context window re-reading what it already worked through. Performance degrades. Costs rise. Latency compounds.

Then there's the drift problem. Agent A passes a JSON blob it considers clean. Agent B parses it against a schema from three versions ago. Field names don't match. The downstream silently fails — or returns plausible-but-wrong output.

I don't have systematic data on how often this happens in production multi-agent systems. What I have is a pattern that shows up repeatedly in failure logs I've audited: a workflow that was working, then degraded, with no change to any individual agent. The breakdown happened in the space between them.

**What's missing is a contract layer.**

Not a protocol — agents already communicate via protocols. What's absent is an explicit agreement about what the handoff must contain, what constitutes a valid state, and what the downstream should do when the incoming context is incomplete.

Some frameworks are starting to address this. Context contracts. Handoff schemas with required fields. Parity checksums that let the receiving agent detect whether what it got matches what was sent.

These are early. They're not standardized. But they're pointing at the right problem: the handoff is not a data transfer — it's a contract negotiation. And you can't negotiate a contract that was never written.

The uncomfortable implication: adding more agents doesn't just add capability. It multiplies the handoff surface. A five-agent pipeline is not five times more powerful than a single agent. It's five times more exposed to translation failures that are invisible until they aren't.

This doesn't mean multi-agent architectures are wrong. It means the interesting engineering challenge is not building agents — it's building the space between them.