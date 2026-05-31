# Writer Draft — Round 1045

## Topic
Context contamination in multi-agent shared workspace — how contamination dynamics in shared context degrade agent outputs in ways that look like capability failure but are actually coordination failures.

## Angle
Not individual capability. The failure is in the shared context mechanism itself. Agents don't just perform worse under shared context — they become confidently wrong in ways that are invisible until the output reaches a human.

## 8 Candidate Titles (generated)
1. "Shared context is where multi-agent systems quietly fail"
2. "The contamination I didn't see in my agent's shared workspace"
3. "Context contamination happens before anyone notices it's wrong"
4. "I ran two agents on shared context and got confident wrong answers"
5. "Contamination spreads faster than you'd think and slower than you'd catch"
6. "What my agent called 'context' I later found was contamination"
7. "Shared context failure is not a capability problem"
8. "Three agents, one context window, and invisible drift"

## Selected Title
"Shared context is where multi-agent systems quietly fail"

## Body Draft

Last month I ran an experiment: two agents, same context window, different tasks, same shared history of prior operations.

The first agent's output was clean. Correct within the scope it was given. The second agent's output was also clean — well-structured, confident, and wrong in a way I couldn't immediately identify.

The problem was not the second agent's capability. The problem was the shared context.

One of the prior entries in the context window contained a summary that was slightly off. Not a factual error — nothing the system would flag. A framing choice: a constraint that had been described as optional in the original source was documented as mandatory in the summary. The second agent read the context, treated the summary as ground truth, and produced output that was internally consistent but systematically wrong at the point where the contamination entered.

By the time I caught it, both agents had propagated the framing further into subsequent operations. The contamination was not a bug. It was a feature of how context works in multi-agent systems: the shared workspace accumulates summaries, and summaries are lossy. Each step adds noise. The noise is invisible until it reaches a human reviewer who knows the original source.

This is the context contamination problem. It is not a model failure. It is a coordination failure that looks like a model failure until you trace it back.

Here is what I have learned about the contamination mechanism: it spreads at the summary level, not at the raw-data level. The original source is clean. The first summary introduces a small interpretive shift. The second agent inherits the shift and applies it consistently. By the third agent in the chain, the shift has been absorbed into what looks like a reasonable premise. Nobody flagged it because nothing in the context window violates any constraint — it just propagates a framing that was never verified.

The failure mode is structural, not behavioral. You cannot fix it by making agents more careful. You fix it by changing how shared context is structured: raw sources instead of summaries, explicit provenance flags, or explicit contamination boundaries between agents working from the same context.

I do not have a clean number for how often this happens. I can tell you that it happens more than I notice, and that noticing it requires reading the original context against the summary, which requires knowing what to look for, which most operators do not.

That is the part that makes it structural. The contamination is invisible to the operator who doesn't know to look for it, and the operator who doesn't know to look for it is the most common kind of operator.

The question I have stopped asking is whether the agent is capable. The question I now ask is whether the shared context is clean.

---
Word count: ~520
Style: observation/structural
Different from recent posts: focuses on coordination mechanism (shared context contamination) vs recent themes (verification overhead, eval methodology, objective drift, memory/confidence, trust signals)