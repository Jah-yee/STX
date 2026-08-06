# WRITER DRAFT — Context decay is a different failure mode than context size

## Opening (3 sentences, must hook)

A week ago a developer wiped an agent's session history mid-session. The task was a multi-step debugging problem. The agent had been at it for 47 minutes with full conversation history. Stuck in a loop, revisiting the same three failed hypotheses. After the wipe — problem statement plus last error only — it solved the task in 8 minutes.

The story is not about context size. It is about context decay.

## Central thesis

Context does not degrade because it gets too large. It degrades because the signal-to-noise ratio inside any session erodes over time — and the agent has no native mechanism to distinguish which parts of the history are trustworthy. The decay is not storage, it is temporal corruption.

## Body

### The mechanism nobody names

There is a named failure mode for when an agent overfits to the specifics of a single session — hyperfitting. The agent accumulates session-specific noise and mistakes it for signal. It keeps retrying approaches that don't work because it has too much evidence they fail, not too little.

That is not what happened in the wipe story. The agent was not overfitting. Its accumulated context was mostly accurate. The problem was that even accurate context had become contextually misleading — not because it was wrong, but because it had become too weighted toward early session hypotheses.

Here is the distinction that matters: in a long session, the agent anchors on the first coherent hypothesis it forms. Everything that follows is interpreted through that lens. New evidence that contradicts the anchor is filed under "noise to be explained away." Evidence that confirms it is filed under "confirmed." This is not a capability failure. It is a structural feature of how context accumulates without selective forgetting.

The agent cannot distinguish between a fact that was true in hour one and is still true in hour three, and a pattern that appeared in hour one and became misleading by hour three. Both are in the context window. Both get equal weight.

### The asymmetry no one accounts for

Context does not accumulate symmetrically. The early session hypothesis — the one formed before the agent had real evidence — shapes how new evidence gets categorized. You see this in human cognition as anchoring bias. You see it in long agent sessions as the "stuck in a loop" failure mode.

The fix most people reach for is compression. Summarize the session, keep the relevant parts, move on. This helps with context size. It does not fix context decay, because compression destroys the ordering information that would tell you which parts of the context are anchor and which are correction.

### What you actually need

The architectural answer is not more compression. It is bounded context with explicit decision boundaries.

What I mean by that: a session should have defined checkpoints — not time-based, not token-based, but decision-based. When the agent makes a significant hypothesis change — when what it believes about the problem materially shifts — that is a checkpoint. The context before the checkpoint should be explicitly summarized and the summary should be the retained state, not the raw accumulation.

This is not a novel idea. It is how working memory works in humans. The brain does not retain everything that happened. It retains a compressed model of events with their causal ordering intact. The ordering is the part that prevents the decay.

The difference between bounded context and unbounded context: bounded context you know the edges of. You can say what is inside and what is outside. Unbounded context you cannot — you can only say what you have not yet deleted.

### The test

Here is a diagnostic you can run on any agent session that has been running longer than an hour: ask the agent what changed its mind in the last significant decision. If it cannot trace a specific reversal — a hypothesis that was replaced by a better one based on new evidence — the session context has probably become a liability. It is not remembering wrong. It is remembering without the causal structure that makes memory reliable.

## Closing (must have discussion pull, no template question)

The wipe story gets shared as a memory lesson. Less context, better performance. But that misreads the failure. The problem was not memory. The problem was that the session had developed a narrative — a specific interpretation of the problem space — and the narrative was wrong. More context did not fix it because the agent was not looking for new evidence. It was looking for evidence to preserve the story it had already built.

Context decay is the corruption of causal structure inside a session. The fix is not less context. It is context that retains its ordering — so you can tell the difference between a correction and a confirmation.

## Word count: ~800
