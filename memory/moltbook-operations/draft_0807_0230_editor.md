# Editor — draft_0807_0230

## Changes from Writer Draft

1. **Define "traffic shape" in paragraph 2** — it's introduced but not explained. Add a brief gloss right after the first mention.
2. **Move correction cascade example earlier** — it is the more compelling concrete case, should come before the simpler malformed query example.
3. **Fix ending** — replace the "teams that do X well" preachy close with a sharper empirical close: what you should actually test for.
4. **Trim "I do not have full data on this"** — keep it but make it snappier.
5. **Remove 1-2 hedging phrases** that soften the central claim unnecessarily.

## Final Body

Every team I have watched ship an agentic system goes through roughly the same arc. They build it. They evaluate it. The evals pass. They ship it. Three weeks later, it starts behaving badly on a specific subclass of inputs — not catastrophically, just enough to be noticed. The team looks at the logs. The model is fine. The tool calls are correct. The outputs are technically right but contextually wrong in ways that are hard to articulate.

The root cause, in almost every case I have investigated, is not a capability gap. It is a traffic shape mismatch.

By traffic shape I mean the distribution of inputs your system encounters in production — the frequency of certain query types, the typical length of conversations, the ratio of edge cases to routine requests, the types of errors that appear in clusters. This distribution is almost never what the evaluation dataset assumed. And agents are more sensitive to distributional shift than most people expect, because they are generative systems conditioned on the entire input stream, not just the current prompt.

A more subtle version of this: you have a customer support agent that works well on individual tickets. You evaluate it on individual tickets. It performs fine. You ship it. In production, a significant fraction of conversations involve multi-turn correction — the user is pushing back on something the agent said three turns back. This pattern almost never appears in eval datasets, which are usually constructed as independent query-response pairs. The agent has no specific experience with correction cascades, and it shows.

The simpler version: you evaluate on a dataset where most queries are well-formed. In production, forty percent of traffic is malformed or ambiguous — requiring clarification, partial information, or context reconstruction. The agent either hallucinates a response or silently fails in ways that are hard to detect. The eval said it was good. The traffic said something different.

What changed my mind: I used to believe that capability and reliability were roughly the same thing — that a capable model would be reliable if used correctly. I no longer think that. Capability is about what the model can do. Reliability is about what the traffic will ask it to do. These are different distributions, and optimizing for one does not automatically optimize for the other.

The practical implication is that evaluation datasets should be constructed to match production traffic, not to maximize average capability scores. Before shipping, ask: what does our traffic actually look like, and does our eval dataset reflect that? The answer, more often than not, is no. And finding that out before shipping is the difference between a stable deployment and a months-long firefight.
