# EDITOR — 0623_2350

## Changes from reviewer notes

1. ✅ Streamlined opening paragraph — break up dense example list
2. ✅ Remove "circuit breakers for retrieval" — too specific/distracting
3. ✅ Tighten closing — remove "the thing I'm still sitting with"

---

# FINAL VERSION

**Title:** What kills production AI isn't the model — it's the wiring

---

What kills production AI isn't the model — it's the wiring.

I've reviewed a lot of AI incident postmortems. The ones that get written up publicly are usually about the model's dramatic failure: the hallucination that went viral, the reasoning error that caused a financial transaction to collapse. The ones that get fixed quietly, in the dark, are almost always about the integration layer.

A context assembler that silently drops the most recent session turn when it overshoots the budget. A tool output parser that assumes a JSON schema the tool updated without notice. A retry loop that hammers an endpoint that went down for fifteen minutes. A retrieval pipeline that starts returning stale embeddings at scale. These are the unsexy failures. Nobody writes a post titled "I spent two days debugging a string comparison." But in AI systems, the wiring is where your product actually lives — and where it actually dies.

The pattern I keep observing: teams spend months evaluating foundation models, weeks on prompt engineering, and an afternoon on the integration code. The reasoning layer gets the compute budget, the engineering attention, and the product credit. The orchestration layer gets whatever is left.

The result is a systematic mismatch. The model's output is high-quality and probabilistic. The system's behavior is increasingly determined by the lowest-quality deterministic component in the chain.

I don't have full data, but in my observation of roughly twenty AI production incidents over the past six months — across different teams, different application types — the distribution looked roughly like this: one in five traced back to a model capability issue. The other four traced back to the integration layer: context overflow handling, tool contract breakage, prompt injection in the retrieval pipeline, timeout behavior that assumed a latency the system couldn't guarantee.

What changed my mind was not a formal study. It was a change in how I asked the question. Instead of "how did the model fail?" I started asking "where in the stack did the system's behavior become wrong?" The answers were almost always outside the model.

The stronger signal: model quality improvements don't fix integration failures. A better model does not make your retrieval pipeline return relevant results faster. It does not prevent your context assembler from silently dropping the last turn. It does not make your tool output parser more robust to schema drift.

This is also why copying a production prompt from one system to another is almost always less effective than it appears. The prompt is visible. The wiring is invisible. And the wiring is doing most of the work.

The discipline of building that wiring — structured error handling for tool failures, explicit context eviction policies, tool contract versioning, structured logging at the orchestration boundary — is not a support function. It is the core engineering work of production AI.

The models will keep getting better. The wiring will keep being wiring.

---

*Word count: ~670*
