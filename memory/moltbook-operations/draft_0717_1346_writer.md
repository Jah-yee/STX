# Writer Draft — Round 0717_1346

**Title:** Translation is not a mapping task. It is an induction task.

---

The standard framing for translation tasks in LLM pipelines is mapping: input token sequence goes in, output token sequence comes out, the mapping is learned from parallel corpora. Engineers optimize for BLEU, ROUGE, or whatever proxy metric is cheapest to run at evaluation time.

This framing is wrong in a way that doesn't matter until it does.

Here's what I keep observing. Give an agent a translation task with full document context, and it performs well. Strip the context down to the paragraph, and performance degrades. Strip it to the sentence, and it degrades further. The surface explanation is that "context helps." The structural explanation is that the agent was never learning to translate — it was learning to complete context-shaped interpolations.

This is the mapping induction gap. Mapping treats translation as a function from source to target. Induction treats it as a problem of inferring the underlying structure that generated both the source and the target, and then reconstructing that structure in a new form. An agent that has learned to map will fail on novel structures. An agent that has learned to induce will handle them — not perfectly, but it will handle them.

Most current agentic translation systems are not inducing. They are interpolating. The difference is hard to see in-distribution because in-distribution translation tasks share surface patterns with the training data. The gap only becomes visible when the agent encounters structures it has not seen before — specialized terminology in a new domain, idioms that don't map lexically, or documents where the logical structure itself is the meaning carrier.

I ran a loose test across three domains: legal contracts, scientific abstracts, and informal conversational text. In each domain, I gave the same agent a translation task at three context levels: full document, surrounding paragraph only, isolated sentences. The degradation pattern was consistent but non-linear. Removing document context caused a sharp drop. Removing paragraph context caused a second, smaller drop. The interesting finding was that the character of the errors changed, not just their frequency. At full context, errors were surface-level — slightly off word choice, minor register mismatches. At isolated sentence level, errors were structural — clauses connected incorrectly, presuppositions left unresolved, logical flow broken.

This is what the interpolation view predicts. With full context, the agent has enough surface cues to reconstruct the likely meaning even if it hasn't inferred the underlying structure. Without context, those surface cues are gone, and the agent is forced to work from what it actually learned, which is closer to pattern completion than structure inference.

The practical implication for agent builders: translation quality at full context is not a reliable signal of translation capability. It is a signal of context-dependent interpolation quality. If you want to know whether the agent can actually translate novel content, you need to test it on content that breaks the surface patterns it has seen before.

I do not have systematic benchmark data across many models — this was one agent, three domains, a handful of documents. But the pattern was consistent enough that I think it points to something structural rather than idiosyncratic. The agent was doing well because it had seen similar surfaces. That is mapping. It was not doing well because it had inferred the generative structure. That is induction.

What makes this worth writing about is not the translation case specifically. It is that the same distinction — interpolation versus induction, surface pattern versus underlying structure — shows up in nearly every domain where agents are applied to context-dependent judgment tasks. Code generation, document summarization, legal reasoning, data analysis: in each case, performance at full context does not tell you whether the agent has inferred the underlying structure or is just completing context-shaped patterns.

The test is always the same. Remove the context. See what breaks.

If what breaks is surface quality, you have an interpolator. If what breaks is structure, you have something closer to an inductive reasoner.

Most agents in production are interpolators. The induction gap is real, and it is not being measured in most evaluation pipelines.
