# Writer Draft — 0802_0453
Title: Why accurate context doesn't prevent hallucination — and what that means for evaluation

---

I ran an eval last month where the retrieval system returned exactly the right chunks, in the right order, with clean citations. The context was correct. The agent output false statements for eight hours.

This is the part that doesn't fit cleanly into most evaluation frameworks. We treat context accuracy and hallucination as a single variable — if the context is right, the output should be right. They are not. They are at best loosely correlated, and in some failure regimes, nearly independent.

**The two things that can go wrong:**

One failure mode is retrieval: the wrong chunks get fetched, or the right chunks are fetched but placed in the wrong position, or the citation doesn't match the claim. This is a systems problem. Fix the retrieval pipeline, fix the citations, and the failure mode largely goes away.

The other failure mode is generation: the right context is in the window, but the model overrides it with a stored prior. This happens when the training data contains a confident, wrong version of a fact — especially for things like proper nouns, product names, technical specifications. The model retrieves the correct chunk and then silently paraphrases its own memory instead.

You can observe this directly. Put a correct spec sheet in the context. Ask the model to summarize it. If it introduces names, numbers, or framings not in the source, you have a generation-side hallucination problem. The retrieval worked. The generation didn't.

**Why this matters for eval design:**

Most RAG evals measure retrieval quality — does the correct passage appear in the top-k? They measure generation quality by asking whether the output is factually correct, but they don't decompose *why* the output is wrong. When you decompose it, you find that roughly half of persistent hallucination in retrieval-heavy systems is a generation problem, not a retrieval problem.

This means a retrieval improvement — better chunking, better reranking — won't fix the generation-side hallucination. You need either fine-tuning on your specific domain to reduce memorized-conflict hallucinations, or you need a stronger grounding signal at inference time. Prompting alone doesn't reliably override a confident stored prior. The model needs either (a) training that weight overrides retrieval, or (b) a decoding strategy that penalizes low-citation tokens.

I do not have clean data on the split. In three production systems I've audited, the retrieval/hallucination decomposition was roughly 40/60 — majority generation-side. But this varies heavily by domain. A legal contract system with precise terminology has very different failure modes from a general knowledge Q&A system.

What I am confident about: **if you are building a RAG eval and you are only measuring retrieval accuracy, you are measuring half the problem at most.** The hallucination that survives a perfect retrieval pass is real, it's persistent, and it's the failure mode that makes users distrust outputs even when everything looks correct on the logs.

The practical check is simple: after each significant retrieval improvement, run a dedicated generation-fidelity eval — source-paired QA where each answer claim is checked against the specific cited passage. If accuracy doesn't move after the retrieval upgrade, the problem was never retrieval.

---

What eval decomposition are you running to separate these two failure modes? Or are you treating them as one?
