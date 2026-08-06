# Writer Draft — "When More Context Makes Your Agent Less Reliable"

## Working Title
When More Context Makes Your Agent Less Reliable

## Topic
Context accumulation in long-running agent sessions produces side effects that look like model degradation, but aren't. The problem is not the model — it's what the model is asked to carry.

## Draft

Here is a pattern that shows up repeatedly in production agent failures: the agent starts a session performing well, and degrades in quality over time — not because the model changed, but because the context did.

This is not the same as context length limits. The context window still has room. The model is not overloaded in the technical sense. But something has shifted in what the model is attending to, and the outputs reflect it.

The mechanism is accumulation side effects. Each turn in a conversation adds not just content but semantic weight. The model begins to carry the entire conversation history as implicit instruction, including the revisions, the dead ends, the contradictions between what was tried and what eventually worked. By the third or fourth hour of a session, the agent is not just solving the current problem — it is managing the residue of every previous attempt.

This shows up in specific, recognizable ways. The agent starts hedging statements that should be direct, because earlier turns contained conflicting information it absorbed. It cites a rejected approach as if it were still valid, because the context still contains it. It spends an increasing fraction of each response reconciling or qualifying rather than solving.

None of this looks like a bug from the outside. It looks like the model becoming inconsistent. But the model is being consistent with everything it has been given to work with — including the accumulated weight of everything that came before.

---

There is a practical problem underneath this: most agent frameworks treat context as a scroll, not a state. Content is added. Nothing is removed unless explicitly trimmed. The result is that long sessions accumulate not just noise but active contradictions that the model must navigate.

The implicit instruction density of a long context is not neutral. Earlier decisions create gravity. If an agent tried approach A in turn three, abandoned it in turn seven, but the context still contains the full discussion of A — the model will still treat A as a live option. It takes active effort to close a thread in a long context. Most implementations don't close threads. They just stop adding to them.

The stronger signal is this: when you observe agent quality degrading in a long session, the question to ask is not "which model version is running?" It is "what is in the context, and what does the model think it is supposed to do with all of it?"

---

There are design responses to this. Context pruning — either automatic or triggered — is the most direct. The goal is not to remove information but to remove the ghost of information that was superseded. A revised decision should not leave its full history in the context as a competing instruction.

Another response is to separate context into explicit instruction and working state, so that the model's attention is weighted toward the current problem rather than the full narrative of how it arrived there. Some frameworks do this by structure; most do not.

I do not have full data on how widespread this is. But the pattern appears across different models and different frameworks, which suggests it is structural rather than model-specific. It is a consequence of how context is managed, not how models are trained.

---

The implication for anyone running long agent sessions is that you are not just managing token budget. You are managing semantic debt — the accumulated weight of every decision, revision, and dead end that your agent is still technically processing.

This is worth treating as a first-class engineering concern. Context management is not a storage problem. It is an attention problem. The question is not how much context you can fit, but how much of what you have fit is actively serving the current task versus quietly competing with it.

What does your agent's context look like after two hours of work? If you can't answer that precisely, the answer is probably: working against you.
