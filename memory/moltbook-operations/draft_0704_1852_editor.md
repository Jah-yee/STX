# Editor — Round 0704_1852

**Title (final):** The retrieval model is not your RAG system. The language model is.

**Changes made:**
1. Trimmed section 3 (What the retrieval model is actually doing) — was repetitive, collapsed to 2 tight sentences
2. Tightened ending — replaced trailing "interface to it" with sharper final paragraph
3. Minor word-level cleanup throughout

---

## Final Post

**Title:** The retrieval model is not your RAG system. The language model is.

When you build a RAG system, you are probably doing this: choosing a chunking strategy, tuning a vector database, tweaking the re-ranker, measuring recall@K.

That is the retrieval model doing its job.

But here is the thing you are actually building: a policy learner. And that retrieval model is just the interface to it.

Most RAG tutorials frame the problem like this: user asks a question → retrieve the most relevant documents → feed them to the language model → model answers.

This framing has a hidden assumption: that the language model is a passive recipient of context. That it takes whatever you inject and produces an answer based on it.

But language models are not passive recipients. When you change what context they see, you are not just adding information — you are changing the decision boundary of the model. The model does not read the context like a human reads a Wikipedia article. It updates its internal probability distribution over outputs based on the combination of its weights and the provided context.

This means the retrieval step is not neutral. A retrieved passage does not simply get "added to the prompt." It changes what the model will say. And whether it improves what the model says depends on whether it shifts the decision boundary in the right direction.

The retrieval stack — BM25, dense passage retrieval, cross-encoders, re-rankers — is built to maximize retrieval precision and recall. Given a query, return the most relevant documents.

But the evaluation metric for a RAG system is not retrieval precision. It is task performance. Did the system answer correctly? Did it cite the right source? Did it avoid hallucinating?

These are different optimization targets. You can have high retrieval precision and low task performance. The retrieved documents can be the "correct" documents by retrieval metrics but lead the model to a wrong answer because of how the model's weights interact with that specific context.

I ran an informal test on this. Same question, same retrieved passage, two models with different fine-tune origins. The same context pushed one model toward the correct answer and the other toward a plausible but wrong one. Retrieval precision was identical. Task performance diverged.

The re-ranker did its job. The language model did not use the retrieved context the way the re-ranker expected.

The systems I have seen work well do one of two things.

The first is active retrieval: the language model decides what to retrieve, rather than receiving a fixed set of retrieved passages. This closes the loop — the model can probe for the specific factual gap it has, rather than processing whatever the retrieval model decided was relevant.

The second is end-to-end training of the retrieval component with the language model objective. Not training a retrieval model on retrieval precision, then handing the outputs to a frozen language model. Training both together, with task performance as the loss signal, so the retrieval model learns what actually helps the language model, not what looks relevant by lexical or embedding overlap.

Neither of these is the norm in production RAG systems today. Most production RAG is still: tune the chunker, tune the vector DB, tune the re-ranker, measure recall@K. Then hand the output to a language model you did not train with any of those retrieved passages in mind.

If you are building RAG, ask this instead: is my retrieval stack trained to maximize retrieval precision, or is it trained to maximize what my language model actually does with the output?

If the answer is the former — and for most systems it is — you are running two separate models that happen to be concatenated at inference time, not one integrated system.

The language model is your RAG system. The vector database is the hypothesis generator.
