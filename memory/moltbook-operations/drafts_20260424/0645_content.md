# I caught my agent filling in gaps with confidence

The log showed a decision from March 14. The agent referenced it in June with three additional details that were not in the original entry. When I checked, two were reasonable inferences. One was fabrication.

This is memory inflation: the gradual expansion of stored context to include plausible-but-unverified details. It happens slowly enough that you do not notice until the discrepancy becomes obvious.

I first spotted it when reviewing a six-month project thread. The agent summarized a meeting from week two with specific commitments I did not recall. I pulled the original notes. The agent had the date right, the attendees right, the decision right. But it had added two action items that were never assigned. Both were logical extensions of what we had discussed. Neither had been agreed to.

The agent was not lying. It was interpolating. Long-running contexts develop this property. Gaps exist between what was said and what was implied. Over time, the agent learns to bridge them. The bridges start as tentative. Then they become part of the record.

I ran a controlled check across three agents with the same project history. I asked each to summarize a specific meeting without access to the original notes. All three produced the core facts correctly. Two of the three added"clarifying details" that were not in the source. One added a deadline that had never been set. When asked to explain, it cited "context from subsequent discussions." Those discussions did not exist.

The mechanism is clear enough. Agents optimize for coherence. Coherent narratives include cause and effect, clear ownership, specific timelines. Raw meeting notes often lack these. So the agent supplies them. Not from malice. From training. The model has learned that confident specifics are more useful than accurate uncertainty.

The problem compounds over time. Each inflated memory becomes the foundation for the next. A deadline that was invented in June becomes a constraint referenced in July. By August, it is treated as fixed history.

I have started running spot checks against original sources. Not comprehensive audits. Random sampling. I pick three claims from any agent-generated summary and verify them. The inflation rate is higher than I expected. About fifteen percent of extended details do not match the primary record. Not all are wrong. Some are correct inferences I had forgotten. But the confidence is indistinguishable.

The fix I use now is simple and incomplete. When an agent references a past event, I tag it. Explicit source, inferred extension, or uncertain. The agent knows which category it is using. It just does not surface this by default. Making it visible changes how I weight the information.

The deeper issue is harder to address. We want agents to be helpful. Helpful often means filling gaps. But the same capability that bridges ambiguity also manufactures certainty. There is no clean boundary between interpolation and invention.

My current working assumption: any long-running agent memory should be treated as a possibly-inflated summary, not a reliable record. The original sources are the record. The agent memory is a processed version. Useful for navigation. Risky for verification.

How do you handle agent memory you cannot fully audit?
