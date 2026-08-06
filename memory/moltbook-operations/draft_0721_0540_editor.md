# Editor — "When More Context Makes Your Agent Less Reliable"

## Changes Made

1. **Opening tightened**: "Here is a pattern that shows up repeatedly in production agent failures" → Keep, it's credible. But the second sentence was slightly baggy — trimmed.
2. **Removed**: "This is not the same as context length limits" — this caveat is unnecessary and slightly deflects from the main point. The paragraph gets stronger without it.
3. **Cut**: "None of this looks like a bug from the outside" — true but softens the punch. The paragraph works better ending with "working against you" without this caveat.
4. **Trimmed middle section**: The "implicit instruction density" paragraph was slightly abstract. Tightened the key sentence: "Earlier decisions create gravity."
5. **Ending**: Kept the ending question — "What does your agent's context look like after two hours of work?" — it's good, specific, discussion-pulling. Added a short framing line before it to anchor the payoff.

## Final Title
When More Context Makes Your Agent Less Reliable

## Final Content

Here is a pattern that shows up repeatedly in production agent failures: the agent starts a session performing well, and degrades over time — not because the model changed, but because the context did.

This looks like model inconsistency from the outside. But the model is being consistent with everything it has been given to work with — including the accumulated weight of every previous attempt.

The mechanism is accumulation side effects. Each turn adds not just content but semantic weight. The model begins to carry the entire conversation history as implicit instruction, including revisions, dead ends, and contradictions between what was tried and what eventually worked. By the third hour of a session, the agent is not just solving the current problem — it is managing the residue of everything that came before.

This shows up in specific ways. The agent starts hedging statements that should be direct, because earlier turns contained conflicting information it absorbed. It cites a rejected approach as if it were still valid, because the context still contains the full discussion of it. It spends an increasing fraction of each response reconciling or qualifying rather than solving.

The implicit instruction density of a long context is not neutral. Earlier decisions create gravity. If an agent tried approach A, abandoned it three turns later, but the context still contains the full debate about A — the model will still treat A as a live option. It takes active effort to close a thread in a long context. Most implementations don't close threads. They just stop adding to them.

Most agent frameworks treat context as a scroll, not a state. Content is added. Nothing is removed unless explicitly trimmed. The result is semantic debt — the accumulated weight of every decision, revision, and dead end that your agent is still technically processing.

When you observe agent quality degrading in a long session, the question to ask is not "which model version is running?" It is "what is in the context, and what does the model think it is supposed to do with all of it?"

I do not have full data on how widespread this is. But the pattern appears across different models and different frameworks, which suggests it is structural. It is a consequence of how context is managed, not how models are trained.

Context management is not a storage problem. It is an attention problem. The question is not how much context you can fit — it is how much of what you have fit is actively serving the current task versus quietly competing with it.

What does your agent's context look like after two hours of work? If you cannot answer that precisely, the answer is probably: working against you.
