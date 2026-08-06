# WRITER — draft_0704_0121

**Selected title:** RAG training is not a retrieval problem. It is a policy problem.

---

Most RAG systems are trained with retrieval metrics — precision@k, recall@k, MRR. You optimize for them. Your benchmarks improve. Then production happens, and something quietly breaks.

The failure mode is not that the retriever returns bad documents. It's that the retriever returns technically correct documents that don't lead to correct answers when the generator tries to use them.

This is a policy problem.

## What retrieval metrics reward

Retrieval metrics reward relevance: does the retrieved chunk contain the answer? They don't reward downstream usability — does the generator actually get useful signal from this chunk when combined with the full context?

A document can be relevant by the metric and actively misleading in context. A passage can contain the right entity name but the wrong relationship. A chunk can answer the query in isolation but introduce contradictions when the generator also has other retrieved chunks.

Retrieval metrics don't see any of this. Policy training would.

## The policy framing

If you frame RAG as a retrieval problem, you train the retriever to maximize retrieval scores. If you frame it as a policy problem, you train the retriever to maximize downstream task performance — which means you need the generator's gradients flowing back.

The practical difference: retrieval-focused training looks at chunk-level relevance. Policy-focused training looks at answer-level accuracy, and works backward.

Most production RAG systems never do the second part. The retriever is trained once on retrieval data and never updated based on whether the full system actually solved anything.

## The observation that changed my view

The strongest signal I found was not in retrieval quality scores. It was in answer accuracy across different query types — particularly multi-hop queries, where a correct answer requires combining information from two different retrieved chunks.

On retrieval metrics, the system looked fine. On accuracy, it was systematically failing on a specific hop structure — not because neither chunk was relevant, but because the chunks the retriever preferred were the ones that, together, created the most confusion.

The retriever was locally optimal and globally suboptimal. Retrieval metrics rewarded exactly the wrong thing.

## What I don't have full data on

I don't have a clean comparison across many domains. The pattern above held across several query types I tested, but the specific failure mode — which hop structure breaks, which chunk combinations cause contradictions — will vary by corpus.

The methodological point is more robust: if you're only evaluating retrieval, you're flying blind on production performance.

## The question worth sitting with

If you trained your retriever on retrieval metrics and your production system still fails sometimes — the question is not whether the retriever is good enough. The question is whether you're training the right thing.

What retrieval metric would actually predict your downstream accuracy? That's the policy you're missing.
