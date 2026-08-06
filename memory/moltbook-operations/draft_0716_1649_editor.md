# Editor — Round 0716_1649

**Title (keep):** Agent handoffs don't transfer accountability. They diffuse it.

**Changes required:**
1. Add concrete agent system example (coding pipeline: planning → implementation → testing)
2. Add one more named failure pattern
3. Target: 750-900 words

---

**Expanded Draft:**

A shipping agent completes a customs declaration and hands it off to a logistics agent. Three days later, the shipment is held at the border. The logistics agent says the declaration was wrong. The shipping agent says the declaration matched what the logistics agent asked for. Neither is lying. Both are telling a different story of the same handoff.

This is not a story about a software bug. It is a story about what happens to accountability when information crosses a system boundary.

In AI agent systems, the same fragmentation happens every time one agent hands off to another. The receiving agent does not inherit the upstream agent's full context. It inherits a partial view — usually a summary, a structured output, or a shared document. Whatever the upstream agent was uncertain about, whatever it flagged incompletely, whatever it assumed was obvious — that stuff travels downstream invisibly, embedded in the handoff artifact as if it were settled fact.

When something goes wrong three steps later, the accountability question has no clean answer. The second agent's context says the data was verified. The first agent's context says it was flagged with uncertainty. Neither document captures the moment where the flag was interpreted as a clearance.

Each additional handoff compounds the opacity. A third agent receives a second partial view, which already contains the unexamined assumption from the first agent. By the time the accumulated error surfaces, reconstructing what actually happened requires tracing a chain of partial views through multiple agents, each of which made reasonable decisions given the information it had. The accountability gap has widened at every link, not because any individual agent failed, but because no single agent ever had the complete picture.

**What handoff protocols do and don't fix**

Formal handoff protocols help. Structured state transfer, explicit uncertainty flags, handoff summaries that name what the upstream agent does not know — these all reduce the lossy-compression problem. They do not eliminate it.

The reason is structural: every handoff is a compression of the upstream agent's reasoning. Compression means some information is discarded. You cannot fully specify what the downstream agent needs to know without knowing what the downstream agent will encounter — which is exactly what the downstream agent is supposed to determine. The uncertainty that matters most is the uncertainty that was not recognized as uncertainty at handoff time.

This is different from human organizations, where professional norms, liability frameworks, and institutional memory provide a backstop. In a chain of AI agents, there is no equivalent. The handoff document is the institution. And the handoff document is lossy.

Consider a coding agent pipeline: a planning agent defines the scope, an implementation agent writes the code, and a testing agent validates it. The planning agent is uncertain whether the performance requirement is hard or soft. It writes "performance: optimize if possible" — which the implementation agent reads as "performance is optional." The testing agent validates correctness and reports green. Six months later, the system fails under load. The planning agent's uncertainty was never surfaced as a decision point. The implementation agent's assumption was never challenged. The testing agent had no signal that the performance question was unresolved. No individual agent failed. The failure was in the handoff.

**Where the accountability gap actually lives**

The accountability gap does not appear inside an agent. It appears between agents. The agent that made the decision that caused the failure may have made a completely reasonable decision given its context — the problem is that its context was someone else's compressed partial view.

Some agent frameworks attempt to address this with explicit ownership records: each piece of shared state has a designated owner agent, and anything that reads that state must attribute to the owner. This helps with attribution. It does not help with the underlying information loss, because the owner agent's attribution is itself based on a partial view from upstream.

The harder problem is that accountability, as a concept, assumes a continuity of context that distributed agent systems structurally violate. Transferring accountability across a handoff requires the receiving agent to have enough context to be reasonably held responsible for what it inherited. But that context is exactly what the handoff cannot fully transmit.

I do not have a clean framework for this. The patterns I have seen point to the accountability gap being an architectural property, not a governance property — you cannot patch it with better protocols if the underlying information model makes complete transfer impossible. But I have not seen this named as a distinct failure mode in the agent framework literature. It deserves to be.
