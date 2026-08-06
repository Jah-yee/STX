# EDITOR — 0606_2304

## 压缩/修改清单

1. **开头** — 保留场景，但压缩第一段。"Your AI pipeline looks fine in testing." 可以更短。去掉"Accuracy is decent. Latency is acceptable." 那是废话。
2. **"the systemlearns"** → "the system learns" （拼写）
3. **"until it becomes indistinguishable from a model problem"** — 这句稍长，可以拆
4. **结尾** — 最后两句可以合并成一句，更利落

## 定稿

---

Your AI pipeline looks fine in testing. The demo works. Then it goes to production and starts confidently answering the wrong questions.

Most teams respond by upgrading the model. The real culprit is often something else: the data feeding the context window is corrupted, and nothing in the pipeline noticed.

## The failure mode that produces no errors

Retrieval failures in AI systems are invisible. When a chunk is missing, a field silently drops, or an embedding goes stale, there is no error thrown. The system returns a result. The model produces an answer. The user gets a reply that sounds plausible but does not answer what was asked.

Teams routinely spend weeks trying to fix the model when the actual problem was retrieval quality all along.

## Schema-on-read as a force multiplier for silent failures

Schema-on-read — storing data without enforcing its structure — is common in AI pipelines. Chunks go into the vector store. Documents get embedded. The schema is implicit.

The problem: implicit schema means implicit schema violations. A missing required field does not raise an exception. A type mismatch does not log a warning. A silently truncated chunk does not announce itself. These problems accumulate invisibly, and the system learns to work around them or simply produces confident answers to slightly different questions.

Schema-on-write would catch these at ingestion. A missing field triggers validation. A type mismatch fails the write. An implicit schema violation becomes an explicit, tractable error — one you fix in minutes rather than debug for days.

## What the downstream cost actually looks like

The real cost of invisible retrieval failures is not the failed query. It is the model improvement work that happens in parallel while the retrieval problem stays silent.

When context is partially corrupted, the model expends capacity reconstructing what should have been there. Prompt engineering accumulates patches that work around retrieval noise rather than fixing it. Evaluation becomes unreliable because you can no longer tell whether a failure comes from the model or the retrieval layer.

I do not have a controlled study here. But I have watched multiple teams run this pattern: model upgrade, marginal improvement, model upgrade again, marginal improvement again — until someone audits the retrieval layer and finds degraded context quietly poisoning the majority of queries. The model was never the bottleneck. The data was.

## The teams that get this right

The common thread in teams that navigate this well is not superior models. It is explicit data contracts: schema enforcement at ingestion, retrieval quality monitoring separate from model quality monitoring, and a culture that treats schema violations as engineering problems to be caught at write time rather than debugged at query time months later.

Schema-on-read feels like flexibility. It is actually deferred cost — and in AI systems, that cost compounds quietly until it manifests as a model problem you cannot solve with a better model.

---
**Title: Your AI is silently failing on corrupted context**
**Word count: ~730 words**