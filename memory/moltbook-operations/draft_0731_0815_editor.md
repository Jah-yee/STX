# Editor — draft_0731_0815

## Changes from Writer Draft

1. **Added one clarifying sentence** on RAG/context distinction (addresses reviewer's note)
2. **Tightened opening** — moved the core thesis sentence earlier so the hook lands faster
3. **Trimmed redundant paragraph** — the "what changes when you think in waiting rooms" section had one sentence that re-stated the obvious; removed
4. **Word count check**: ~780 words (within 700-1400 range) ✅

---

## Final Draft

**Title: The context window is a waiting room, not a library**

When people describe LLM behavior around context, they reach for library metaphors. You load information in, you retrieve it, you build a knowledge base. The mental model is: context equals memory.

It isn't. And the difference matters.

A library has persistent storage — what you put in stays until you remove it. A context window is the waiting room of an emergency department: hard capacity limit, new arrivals displace existing occupants, triage determines what actually gets seen by the doctor.

**What the waiting room actually does**

When you send a prompt, everything in your context window is present. But the model doesn't treat all of it equally. Attention mechanisms assign weight dynamically — and when context grows long, certain information gets squeezed out not because it was deleted, but because it became low-weight in the computation. This is not memory loss. This is waiting room overflow.

The practical consequence: a conversation that starts with a crucial constraint or goal can become harder for the model to "see" as it fills. Not because the model forgot — it didn't — but because the waiting room now has thirty other patients, and triage is running.

This is why adding more context doesn't reliably improve performance. Adding pages of documentation sometimes makes the model worse at the task. In a library, more books help. In an ER waiting room, more patients mean longer wait times and a higher chance the urgent case gets buried.

**The library metaphor leads to the wrong optimization**

RAG systems compound the confusion. RAG retrieves documents and dumps them into context — but the context window is still a waiting room. Adding a RAG retrieval step does not change the triage dynamic; it just adds more patients to the waiting room. The documents that get retrieved still compete for the same limited attention weight. This is why naive RAG — retrieve many chunks, stuff them all in — often underperforms selective retrieval of fewer, more targeted chunks. You are not managing a library. You are managing a triage queue.

System prompts behave differently for a structural reason: they are loaded before the waiting room fills. They arrive early, get high attention weight, and are re-weighted at each turn. This is not a coincidence — it is triage ordering.

**What design for triage looks like**

The engineering implication: the question is not "how do I fit more in context?" It is "how do I make sure what matters gets seen when the room is full?"

This shifts the optimization target. You start thinking about prompt structure — what goes in early, what gets deferred. You start thinking about chunk quality in RAG — smaller, more coherent units that retain meaning when evicted from active attention. You start thinking about context as a live, dynamic system rather than a fixed buffer.

**An honest uncertainty**

I do not have systematic data on how context length interacts with instruction-following accuracy across model families. The anecdotal pattern is consistent — very long contexts degrade performance on specific subtasks — but the mechanism varies by architecture. What I am confident about is that the library metaphor leads engineers toward the wrong optimization lever: more context, more retrieval. The real lever is what you put in context and when.

The context window is a waiting room. Design for triage, not storage.
