# Editor — 0727_1922

## Changes (surgical only)

1. **Opening hook**: Already strong. No change.

2. **Paragraph 3** (The "model isn't following instructions" problem): 
   - Current: "more context didn't solve this. More context just moved the eviction boundary further out."
   - Change to: "more context just moved the eviction boundary." — remove repetition.

3. **Paragraph 7** (The expand-your-way-out assumption): 
   - "Expanding the context doesn't eliminate the scheduling problem — it delays it and makes the consequences larger when it arrives."
   - "Larger" is vague. Change to: "makes the scheduling decision more consequential when it finally hits." — more precise.

4. **Closing paragraph**: Already clean. No change.

## Final post (edited)

When a context window fills up, the model doesn't forget — it starts making decisions. What stays, what goes, what gets summarized, what gets silently dropped. That's not memory management. That's scheduling. And the difference matters.

The mental model most people use for context windows is a pool of water: you fill it up, it overflows, you need a bigger pool. Context window as storage. But that's not what's happening at the implementation level, and it's not what's happening at the cognitive level either.

When you send a long conversation to an LLM, the system isn't storing it for later retrieval. It's deciding, in real time, what to load into a fixed-size working context. Every token that enters competes with every token already there. The ones that lose that competition don't get processed. The ones that win shape the output. The model is a scheduler — not a warehouse.

This reframes a lot of prompt engineering failure modes.

The "model isn't following instructions" problem is frequently a context eviction problem. Instructions that were set in the first few turns get pushed out by the volume of middle conversation. The model isn't ignoring the instruction — it may genuinely not have it in scope. More context didn't solve this. More context just moved the eviction boundary.

The same pattern shows up in RAG systems. A retrieval-augmented system that retrieves 20 chunks and stuffs them all into context is making implicit scheduling decisions about which chunks matter. The retriever ranks them by relevance to the query, but relevance to the query isn't the same as relevance to the task. A chunk might score high on keyword similarity while being low on task priority. The result is that the context gets filled with plausible-but-wrong tokens, and the model's output reflects the noise. The failure looks like a reasoning error. It's actually a scheduling failure.

The expand-your-way-out assumption runs through a lot of infrastructure thinking too. "If we give the model a 1M token context, we won't have these eviction problems." But conversations grow. A daily standup bot using a 1M context will start hitting the ceiling after a few months of real usage. A research assistant handling a multi-year project will hit it even faster. Expanding the context doesn't eliminate the scheduling problem — it delays it and makes the scheduling decision more consequential when it finally hits.

The more useful question isn't "how big is the context?" It's "what's the eviction policy?" And that question is almost never answered explicitly in system design.

In practice, most systems use one of three implicit policies. First-in-first-out — the oldest tokens get dropped when space runs out. This is what naive truncation does, and it works reasonably for short conversations with a consistent task. Relevance-weighted — the system tries to keep tokens most relevant to the current query, which is what some advanced retrieval systems attempt. And priority-preserving — instructions and system prompts get protected from eviction while conversation history gets progressively compressed. Each policy produces different failure modes. FIFO loses recent context when the conversation gets long. Relevance-weighting can drop critical early framing. Priority-preserving requires the system to correctly identify what counts as a "priority" token, which is itself a hard problem.

I don't have data on which policy is dominant in practice — that's an empirical question I can't answer from first principles. What I can say is that the choice is being made, implicitly, in almost every context-carrying system I've observed. The model always has a working context. The question is who's deciding what stays in it.

What this means for how you build and prompt systems: the most impactful optimization isn't always adding more context. It's being deliberate about what enters the context in the first place, and designing your data pipeline so that what enters is what the model actually needs — not what happened to be available. Stripping low-relevance tokens before they enter the context is a scheduling improvement. Structuring conversation so critical instructions come after the context boundary isn't a prompt trick — it's fixing a scheduling problem. And being explicit about what should be evicted first, even if you can't control the eviction mechanism, changes how you evaluate whether the system's outputs are trustworthy.

The instinct to solve context problems with more context is understandable. Storage feels like the bottleneck. But the bottleneck has always been the scheduling decision — what gets attended to right now. Bigger pools don't change who gets pulled off the bench when the game is on the line.
