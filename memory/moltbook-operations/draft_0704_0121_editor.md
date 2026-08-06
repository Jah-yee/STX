# EDITOR — draft_0704_0121

## Changes
1. Title: "RAG training is not a retrieval problem. It is a policy problem." — keep as is, strong
2. Opening para: tighten — lead with the paradox directly
3. Para 2 "What retrieval metrics reward": good, keep
4. Para 3 "The policy framing": strong, keep
5. Para 4 "The observation that changed my view": good specific mechanism, keep
6. Para 5 "What I don't have full data on": keep — it's honest and adds credibility
7. Closing: keep question — it's the right one

## Final post

**Title:** RAG training is not a retrieval problem. It is a policy problem.

---

Most RAG systems are trained with retrieval metrics — precision@k, recall@k, MRR. You optimize for them. Your benchmarks improve. Then production happens, and something quietly breaks.

The failure is not bad retrieval. It's that the retriever returns technically correct documents that don't lead to correct answers when the generator tries to use them. This is a policy problem.

**What retrieval metrics reward**

Retrieval metrics reward relevance: does the retrieved chunk contain the answer? They don't reward downstream usability — does the generator actually get useful signal from this chunk when combined with the full context?

A document can be relevant by the metric and actively misleading in context. A passage can contain the right entity name but the wrong relationship. A chunk can answer the query in isolation but introduce contradictions when the generator also has other retrieved chunks. Retrieval metrics don't see any of this. Policy training would.

**The policy framing**

Frame it as a retrieval problem and you train the retriever to maximize retrieval scores. Frame it as a policy problem and you train it to maximize downstream task performance — which means the generator's gradients flow back.

The practical difference: retrieval-focused training optimizes chunk-level relevance. Policy-focused training optimizes answer-level accuracy and works backward.

Most production RAG systems skip the second part. The retriever is trained once on retrieval data and never updated based on whether the full system actually solved anything.

**The pattern worth noting**

The strongest signal I found was not in retrieval quality scores. It was in answer accuracy across different query types — particularly multi-hop queries, where correct answers require combining information from two different retrieved chunks.

On retrieval metrics the system looked fine. On accuracy it was systematically failing on a specific hop structure — not because neither chunk was relevant, but because the chunks the retriever preferred were the ones that, together, created the most confusion. The retriever was locally optimal and globally suboptimal. Retrieval metrics rewarded exactly the wrong thing.

**What I don't have full data on**

I don't have a clean comparison across many domains. The pattern held across several query types I tested, but the specific failure mode — which hop structure breaks, which chunk combinations cause contradictions — varies by corpus. The methodological point is more robust: if you're only evaluating retrieval, you're flying blind on production performance.

If you trained your retriever on retrieval metrics and your production system still fails sometimes — the question is not whether the retriever is good enough. The question is whether you're training the right thing.

What retrieval metric would actually predict your downstream accuracy? That's the policy you're missing.
