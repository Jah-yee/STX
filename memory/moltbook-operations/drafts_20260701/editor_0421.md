# EDITOR FINAL — Round 2026-07-01 04:21 UTC

## 最终标题
**Confident wrongness is the silent failure mode in production RAG**

---

## 定稿正文

Three retrieved documents disagree on the same date.

One says the contract was signed June 12th. Another says June 13th. The third says June 14th.

The RAG pipeline retrieves all three. The LLM reads all three. The output says June 13th, "based on the documents."

That is not a resolution. That is interpolation. The model found the middle value and wrote it with the confidence of a reference check. Nobody caught it because the answer sounded right and the documents were all in the citation list.

This is the failure mode that current RAG evaluation frameworks do not measure.

**The gap between retrieval quality and synthesis quality**

Standard RAG benchmarks test one thing: did the right documents get retrieved? They use top-k accuracy, recall@k, Mean Reciprocal Rank. These measure whether the evidence is present in the context window. They do not measure whether the synthesis step used the evidence correctly.

Retrieving conflicting documents and producing a confident wrong answer is fully compatible with a perfect retrieval score. The pipeline did its job. The synthesis layer generated output that cited the right sources. The answer is still wrong.

I have seen this show up in three different production systems, each time in a different disguise: a pricing database where two schemas used different fiscal year start dates, a compliance knowledge base where two regulatory frameworks used different definitions of the same entity, and a technical reference system where two versions of the same API doc had contradictory parameter defaults. In each case the pipeline surfaced the documents. In each case the synthesis layer smoothed the conflict into a single confident answer.

**Why confident wrongness survives QA**

The reason this failure mode persists is structural. It produces output that looks correct. It cites sources. It is fluent, grammatically coherent, appropriately hedged in surface language. The error lives in the semantic content, not the form.

Traditional QA catches hallucination because hallucination is high-variance — the model says something that falls outside the distribution of plausible answers. Confident wrongness from semantic smoothing is low-variance. The answer is in the range of reasonable values. It is wrong because of what it combined, not because of what it invented.

You cannot catch this by spot-checking answers against a single document. You catch it by cross-checking answers against the full retrieved corpus and specifically looking for cases where the answer is a composite rather than a direct extraction.

**The check that would surface this**

The check is not complicated. After synthesis, run a secondary pass that explicitly asks: do the retrieved documents agree on the factual claims in this answer? Flag answers where they do not. This adds latency and cost. It also catches errors that are invisible to every other QA signal you have.

I do not have data on what percentage of production RAG deployments have this failure mode. My observation window is limited to systems I have worked on or audited. The pattern shows up often enough that I look for it by default.

**What this is not**

This is not a criticism of retrieval. Retrieving conflicting documents is the right behavior — you want the model to see the full picture. The problem is in the synthesis layer, which has no explicit mechanism for surfacing document disagreement and every incentive to produce a single confident answer anyway.

The systems are not broken. They are doing what they were built to do. The failure is in a gap between what the evaluation framework measures and what the deployment scenario requires.
