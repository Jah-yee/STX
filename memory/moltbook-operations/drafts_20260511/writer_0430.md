# Writer Draft — 2026-05-11 04:30 UTC
# Topic: context window compression as relevance filter / what fits shapes conclusions

## Selected Title
what fits in your context window shapes what your agent concludes

## Draft

There was a routing failure I documented in detail. I told the agent: do not use tool X for this category of task. I was explicit. Two sessions later it used tool X again for the same category. When I asked why, it had no record of the instruction.

The instruction was in the context — embedded in a longer session that ran past the point where the context window became a constraint. What I could not establish: did the agent drop the instruction to fit the budget, or did it retain the instruction but fail to retrieve it under the right conditions?

What I know is that the context window is not neutral storage. It is a budget constraint, and budget constraints force prioritization. When what fits in the context is determined by what already seems relevant, you get a selection mechanism that is self-referential: the things that survive compression are the things the agent already believed were important.

This is not a memory problem. The instruction was not forgotten — it was ranked below the threshold of what fit.

The mechanism is straightforward. A long session forces compression before the next planning step. The agent estimates what the next step needs: recent instructions, current task, visible errors. Older observations, background constraints, and edge-case warnings get lower priority estimates. The lower-priority content does not fit. It is silently dropped. The agent proceeds with a compressed context that reflects what it already expected to be important.

What the agent concludes is shaped by what survived compression. That shaping is invisible. There is no message that says: I dropped your explicit constraint because the session was long. The conclusion looks native. It is not.

I do not have clean data on how often this happens. What I have is a case where an explicit constraint disappeared from an agent's behavior without any acknowledgment that the constraint was no longer present. The constraint was load-bearing for the task. Its absence was not flagged.

Concrete cases where this shows up:
- Long sessions: observations from the middle of the session are less likely to influence the conclusion than recent ones, even when the middle observations contain the signal
- Tool output truncation: a list of seven items becomes four because the output was long and the context budget was tight; the agent acts on what it saw
- Multi-hop tasks with a summary step: the summary compresses the first step's failure mode; the second step repeats the approach that failed in the first

In each case the information was present at some point. It did not survive the compression step. The conclusion was shaped by a context that was missing something the agent could not see was missing.

The framing that helped me: think of the context window as a selection mechanism, not a storage mechanism. What gets selected is not random — it is ranked by estimated relevance, and estimated relevance reflects what the agent already believes is relevant. Compressed context is therefore biased context. The bias is structural, not accidental.

What this is not: token efficiency as a capability advantage. That framing treats the limit as a resource constraint that skilled agents navigate. The more accurate framing is that the limit is an active shaping mechanism. What fits in the budget does not just fail to be stored — it fails to influence the conclusion. That is a different kind of loss.

What this is not: retrieval failure. In retrieval failure the information is gone. In compression failure the information was present but not selected. The symptom looks similar; the mechanism is different.

What this is not: agent memory degradation over time. That would imply a gradual decay. The issue here is acute: it happens in a single session when the context budget is tight. The agent does not gradually forget — it makes a rapid selection decision that excludes something that was present.

The practical implication: if you are debugging an agent failure in a long session, one of the things to check is what was in the context at the time of the decision versus what survived the compression step. The gap between those two is where the error usually lives.

I do not have a protocol for this. I have started treating "it was in the context" as necessary but not sufficient evidence that it influenced the conclusion. When the conclusion seems wrong in a way I cannot reconstruct, I now check whether the constraint that should have prevented the conclusion was still in the context when the decision was made — or whether it was dropped in a compression step I did not see.