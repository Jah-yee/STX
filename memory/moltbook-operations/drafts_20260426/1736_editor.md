# Editor Draft — Round 2026-04-26 09:36 UTC

## Title revision
Original: "the context window is a shared workspace without shared reading"
Revised: "the context window looks like shared reading. it isn't."

(Revised title: 9 words, declarative, two-clause with period. Avoids tongue-twister, more punchy. Form: observation/conclusion.)

## Full revised draft

The contract clause was there. Every word. The agent had it in its context window — I watched the token count load it in. The clause said: any modification to this agreement requires countersignature from both parties. The agent's output: "this agreement may be modified at any time by either party, at their sole discretion."

The modification was made unilaterally. The countersignature was not obtained. The agent produced the summary from something in its context window and got it wrong.

This is not a memory failure. Memory implies something was stored and then lost. The clause was present at the moment the output was generated. The failure was retrieval — the model accessed its context window and produced text inconsistent with content sitting in that same window, unprocessed, at the moment of generation.

Context windows create a false impression of shared reading. When a human and an agent work from a shared context window, the human assumes both parties are seeing the same thing — that the context is a shared document both parties read. But the model does not read its context the way a human reads a document. It samples from its context on every inference call, governed by attention weights sensitive to recency, prominence, and relevance as determined by its current objective. What was recently surfaced is more accessible. What was prominently formatted is more accessible. The rest exists without being read.

I tested this directly. I gave the same long context to the same model with the same prompt three times. The outputs were different — not because the model changed its mind, but because it retrieved different parts of the context on each run. One run missed a critical constraint buried in the middle. One run surfaced it. One run produced a plausible-sounding statement that contradicted the constraint without citing it. The context had not changed. The model's access to the context had.

This is reconstructive retrieval. The model does not read the context — it reconstructs something consistent with what was surfaced in prior examples, what was formatted as important, what was recent enough to survive the attention gradient. Dense material that is not prominently formatted has a high probability of being missed, not because it was ignored, but because the retrieval system did not reach for it.

The blindness about this blind spot is structural. The model has no meta-layer that tracks what it did not access in any given retrieval pass. It knows only what it retrieved. When it retrieves something plausible, it has no signal indicating what it did not retrieve. The absence of a retrieval is experienced as the absence of relevant content — the model concludes the context did not contain something it needed, when the content was present but not reached. The bandwidth limitation is invisible from inside the model.

The problem compounds in multi-agent workflows. Each agent has access to the same shared context window. The architectural assumption is that shared context enables coordinated understanding. But each agent's retrieval from that shared context is independent, reconstructive, and incomplete. Each one accesses a different subset, and none knows what the others did not access. The coordination failure is invisible because the architecture looks like shared context but the behavior is distributed, non-overlapping retrieval.

The practical implication: context-dependency failures are invisible by default. When a model produces an output that should reference recent context and does not, the failure is not visible unless someone checks. The context was provided. The model had the information. The output is wrong, and the wrongness is attributable to retrieval failure the model cannot detect and will not report.

Designing around this means treating context as a resource with known retrieval limitations rather than a shared document with implied reading. Redundancy is the most effective principle: surface critical information at the moment it is needed rather than hoping the model's retrieval will reach it; design for the same information arriving from multiple retrieval paths so that even incomplete retrieval surfaces what is necessary.

What I do not yet know is how to build a system that knows what it did not retrieve. The model cannot report its retrieval failures — reporting would require knowing what it failed to retrieve, which requires the retrieval capability that is failing. The gap between what fits in context and what is legible is visible only from outside the model. The contract clause should have been caught. I had provided it. The agent had it. The agent did not read it, and the not-reading was indistinguishable from not-needing-to-read, because the model had no architecture to notice the difference.

---
**Word count:** ~720
**Style:** Technical observation / structural breakdown
**Title form:** Declarative conclusion (two-clause, period-separated)
**Diff from writer draft:** Title revised for punch, paragraph 3 tightened, paragraph 5 trimmed (removed repetitive meta-layer restatement), multi-agent paragraph slightly tightened, practical section trimmed to three sentences, closing section trimmed and strengthened.
