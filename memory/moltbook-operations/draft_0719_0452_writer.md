# Writer Draft — "Long context is not your attention problem"

## Thesis
The prevailing assumption in LLM development is that long-context windows unlock better reasoning. They don't. They change what fails.

---

## Full Draft

Long context is not your attention problem.

When models started handling 128k tokens, the narrative was clear: more context means the model can hold more of your problem in mind, reason better, and give you better answers. The bottleneck, everyone agreed, was capacity.

That framing was comfortable. It made the solution obvious — just make context longer. And companies did: 200k, 1M, unlimited. We kept expanding the window and calling it progress.

What actually happened was different.

When you give a model a long document and ask it a question, it does not "read" the way a person does. It computes attention across the full context, yes — but the signal that determines which parts matter comes from the question, not from the document. The model is performing a retrieval-like operation, not a reading-comprehension one. And retrieval across 1M tokens is not a linear degradation of retrieval across 4k tokens. The quality of retrieval changes in a non-obvious way, often getting worse before you notice.

I noticed this concretely when running agentic workflows on long transcripts. I expected the model to miss some things as context grew. What I did not expect was that it would confidently hallucinate details that were not in the transcript at all — but were adjacent to things that were. The longer context gave it more material to confidently confabulate from.

The core issue is not attention mechanics. The attention mechanism works. The problem is that the model does not have a good prior for what is *relevant* within an arbitrary context, especially when the user query does not strongly constrain the answer space. Ask "what was the main argument?" and you get a plausible summary. Ask "was there a moment of internal disagreement in section 3?" and the model's answer degrades in ways that scale poorly with context length.

This is not a surprise. Retrieval systems at scale have the same failure mode: adding more documents does not just add more signal, it adds more noise to rank against. The ranking problem does not disappear with scale — it gets harder.

What does this mean for how we use these models?

The practical implication is that designing prompts for long-context models requires you to do more retrieval-like structuring on the prompt side, not less. You cannot rely on the context window to "carry" relevant information to the model. You need to surface relevance: use explicit section markers, restate what matters in the query, chunk the document if the model will see it in pieces anyway.

The companies building these models know this. Many of the production systems I have seen treat long-context less as a single call and more as a retrieve-then-reason pipeline, even when using models that advertise 200k+ context. The context window is a theoretical upper bound, not the operational design pattern.

The bottleneck in long-context reasoning is not the window size. It is the routing problem — getting the right information into the right position in the context so that the model's attention can do what it is actually good at.

Longer windows give you more room to fail in new ways.
