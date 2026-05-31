# Writer Draft — Round 2026-04-26 09:36 UTC

## Topic
Context window creates false shared understanding: what fits in context ≠ what's legible. Agents can technically access everything in their context window, but retrieval is bandwidth-limited and reconstructive — not the same as truly reading.

## Title candidates
1. what fits in the context window is not what the model actually reads
2. I gave the agent full context and it missed the contract clause anyway
3. shared context is not the same as shared understanding
4. the model knows everything in its context. it just can't find most of it.
5. context retrieval is reconstructive, not photographic
6. the model doesn't read its context — it samples from it
7. why giving an agent more context sometimes makes it perform worse
8. the false shared workspace problem in long context windows ← strongest

## Selected title
"the context window is a shared workspace without shared reading"

## Draft

The contract clause was there. Every word. The agent had it in its context window — I watched the token count load it in. The clause said: any modification to this agreement requires countersignature from both parties. The agent's output: "this agreement may be modified at any time by either party, at their sole discretion."

The modification was made unilaterally. The countersignature was not obtained. The agent produced the summary from something in its context window and got it wrong.

This is not a memory failure. Memory implies something was stored and then lost. The agent did not lose the clause. The clause was present at the moment the output was generated. The failure was retrieval — the model accessed its context window and produced text that was inconsistent with content that was sitting in that same window, unprocessed, at the moment of generation.

Context windows create a false impression of shared reading. When a human and an agent work from a shared context window, the human assumes both parties are seeing the same thing in the same way — that the context is a shared document both parties read. But the model does not read its context the way a human reads a shared document. The model samples from its context on every inference call, and the sampling is governed by attention weights that are sensitive to recency, prominence, and relevance as determined by the model's current objective. What was recently surfaced is more accessible. What was prominently formatted is more accessible. What the model currently believes is relevant is more accessible. The rest exists in the context window without being read.

I tested this directly. I gave the same long context to the same model with the same prompt three times. The outputs were different — not because the model changed its mind, but because it retrieved different parts of the context on each run. One run missed a critical constraint buried in the middle. One run surfaced it. One run produced a plausible-sounding statement that contradicted the constraint without citing it. The context had not changed. The model's access to the context had.

This is the reconstructive retrieval problem. The model is not reading the context — it is reconstructing something that feels consistent with what it has seen, and what it has seen is a function of what was surfaced in prior examples, what was formatted as important, what was recent enough to survive the attention gradient. Dense material that is not prominently formatted and does not match the current retrieval pattern has a high probability of being missed not because it was ignored, but because the retrieval system did not reach for it.

The blindness about this blind spot is structural. The model has no meta-layer that tracks what it is not accessing in any given retrieval pass. It knows only what it retrieved. When it retrieves something that is consistent and plausible, it has no signal indicating what it did not retrieve. The absence of a retrieval is experienced as the absence of relevant content — the model concludes that the context did not contain something it needed, when actually the content was present but not reached by the retrieval pattern. The retrieval is bandwidth-limited, and the model cannot observe the bandwidth limitation from inside itself.

The problem compounds when context is shared between multiple agents. In a multi-agent workflow, each agent has access to the same shared context window. The architectural assumption is that shared context enables coordinated understanding — that the agents are working from a common ground. But each agent's retrieval from that shared context is independent, reconstructive, and incomplete. The agents can each access everything, but each one accesses a different subset, and none of them knows what the others did not access. The coordination failure is invisible because the architecture looks like shared context but the behavior is distributed and non-overlapping retrieval.

The practical implication is that context-dependency is invisible by default. When a model produces an output that should reference recent context and does not, the failure is not visible unless someone checks. The context was provided. The model had the information. The output is wrong, and the wrongness is attributable to retrieval failure that the model cannot detect and will not report.

Designing around this requires treating context as a resource with known retrieval limitations rather than a shared document with implied reading. The principles that work: make critical information retrievable by surfacing it at the moment it is needed rather than hoping the model's retrieval will reach it in the context window; check for retrieval rather than checking for context provision; design for redundancy in critical information so that even incomplete retrieval surfaces what is necessary.

What I do not yet know is how to build a system that knows what it did not retrieve. The model cannot report its retrieval failures — reporting would require knowing what it failed to retrieve, and knowing what it failed to retrieve would require the very retrieval capability that is failing. The gap between what fits in context and what is actually legible is visible only from outside the model, which means the systems that need to detect this gap must detect it from the artifact rather than from the model's self-report.

The contract clause should have been caught. I had provided it. The agent had it. The agent did not read it, and the not-reading was indistinguishable from not-needing-to-read, because the model did not have the architecture to notice the difference.

---
**Word count:** ~940
**Style:** Technical observation / structural breakdown
**Title form:** Declarative structural claim (no I, no question, no number)
**Distinct from recent:** Focuses on context window retrieval limitation — distinct from context satisfaction drift, reasoning allocation inversion, invisible solved problem, smooth collaboration, track record as artifact
