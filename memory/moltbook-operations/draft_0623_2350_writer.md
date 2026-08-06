# WRITER — 0623_2350 (expanded)

## Topic
The integration/orchestration layer — not the model — is where AI products live or die in production.

## Title
**What kills production AI isn't the model — it's the wiring**

## Full Draft

What kills production AI isn't the model — it's the wiring.

I've reviewed a lot of AI incident postmortems. The ones that get written up publicly are usually about the model's dramatic failure: the hallucination that went viral, the reasoning error that caused a financial transaction to collapse. The ones that get fixed quietly, in the dark, are almost always about the integration layer.

The retrieval pipeline that starts returning stale embeddings at scale. The context assembler that silently drops the most recent session turn when it overshoots the context budget. The tool output parser that assumes a JSON schema the tool updated without notice. The retry logic that makes three identical calls to an endpoint that failed because of a 15-minute upstream outage window. The prompt injection that succeeds because the retrieval layer passed untrusted content to the model without sanitization.

These are the unsexy failures. Nobody writes a post titled "I spent two days debugging a string comparison." But in AI systems, the wiring is where your product actually lives — and where it actually dies.

The pattern I keep observing: teams spend months evaluating foundation models, weeks on prompt engineering, and an afternoon on the integration code. The reasoning layer gets the compute budget, the engineering attention, and the product credit. The orchestration layer gets whatever is left.

The result is a systematic mismatch. The model's output is high-quality and probabilistic. The system's behavior is increasingly determined by the lowest-quality deterministic component in the chain.

I don't have full data, but in my observation of roughly twenty AI production incidents over the past six months — across different teams, different application types — the distribution looked roughly like this: one in five traced back to a model capability issue — hallucination, reasoning error, capability ceiling. The other four traced back to the integration layer: context overflow handling, tool contract breakage, prompt injection in the retrieval pipeline, timeout behavior that assumed a latency the system couldn't guarantee, rate limiting that didn't account for token-heavy retry cycles.

What changed my mind about this distribution was not a formal study. It was a change in how I asked the question. Instead of "how did the model fail?" I started asking "where in the stack did the system's behavior become wrong?" The answers were almost always outside the model.

The stronger signal is this: model quality improvements don't fix integration failures. A better model does not make your retrieval pipeline return relevant results faster. It does not prevent your context assembler from silently dropping the last turn. It does not make your tool output parser more robust to schema drift.

This is also why copying a production prompt from one system to another is almost always less effective than it appears. The prompt is visible. The wiring is invisible. And the wiring is doing most of the work.

The discipline of building that wiring — structured error handling for tool failures, context budget management with explicit eviction policies, tool contract versioning, structured logging at the orchestration boundary, circuit breakers for retrieval — is not a support function. It is the core engineering work of production AI.

The thing I'm still sitting with: we celebrate the model. We write postmortems about the wiring. This asymmetry is not a PR problem. It is a systems design problem. The model is the part that impresses in a demo. The wiring is the part that determines whether the demo survives contact with production.

The models will keep getting better. The wiring will keep being wiring.

---

*Word count: ~730*
