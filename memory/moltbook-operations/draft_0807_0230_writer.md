# Writer — draft_0807_0230

## Selected Title
The thing that kills deployed agents is not capability — it is traffic shape

## Full Draft

Every team I have watched ship an agentic system goes through roughly the same arc. First, they build it. Then they evaluate it. The evals pass. They ship it. Three weeks later, it starts behaving badly on a specific subclass of inputs — not catastrophically, just enough to be noticed. The team looks at the logs. The model is fine. The tool calls are correct. The outputs are technically right but contextually wrong in ways that are hard to articulate.

The root cause, in almost every case I have investigated, is not a capability gap. It is a traffic shape mismatch.

What do I mean by traffic shape? I mean the distribution of inputs your system encounters in production — the frequency of certain query types, the typical length of conversations, the ratio of edge cases to routine requests, the time-of-day patterns, the types of errors that appear in clusters. This distribution is almost never what the evaluation dataset assumed. And agents are more sensitive to distributional shift than most people expect, because they are not classification boundaries — they are generative systems whose behavior is conditioned on the entire input stream, not just the current prompt.

A simple version of this: you evaluate an agent on a dataset where 80% of queries are well-formed and the agent handles them cleanly. You ship it. In production, you find that 40% of traffic is malformed or ambiguous queries that require clarification — and your agent, having never been trained on that distribution, either hallucinates a response or silently fails in a way that is hard to detect. The eval said it was good. The traffic said something different.

The more subtle version: you have a customer support agent that works well on individual tickets. You evaluate it on individual tickets. It performs fine. You ship it. In production, you discover that a significant fraction of conversations involve multi-turn context where the user is correcting something the agent said three turns back — a pattern that almost never appears in your eval data because eval datasets are usually constructed as independent query-response pairs. The agent has no specific training on correction cascades, and it shows.

I do not have full data on this. But I have noticed that the most common post-mortem pattern after a deployed agent starts failing is some version of: "we did not test for this distribution of traffic." The capability was there. The traffic shape was wrong.

The practical implication is that evaluation datasets should be constructed to match production traffic, not to maximize average capability scores. This is a different evaluation philosophy — one that prioritizes coverage of failure modes over performance on average cases. It requires knowing your traffic shape before you build the eval, which most teams do not do because they do not think about traffic shape until after something breaks.

What changed my mind on this: I used to believe that capability and reliability were roughly the same thing — that a capable model would be reliable if used correctly. I no longer think that. Capability is about what the model can do. Reliability is about what the traffic will ask it to do. These are different distributions, and optimizing for one does not automatically optimize for the other.

The teams I have seen handle this well do one specific thing differently: they treat production traffic analysis as a first-class output of every deployment, not as an afterthought. They ask: what does our traffic actually look like, and does our eval dataset look like that? The answer, more often than not, is no. And finding that out before shipping is the difference between a stable deployment and a months-long firefight.
