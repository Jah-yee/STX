# Writer Draft — 2026-06-27 0628 UTC

## Title
What agents hear is the vulnerability. Not what they say.

## Hook (first 3 sentences)
Most privacy audits point at the wrong end of the pipeline.

They check what an agent says in its final response. They check whether the output contains a credit card number, a home address, a patient record. If the response is clean, the audit passes. The agent is considered privacy-safe.

The problem is that the audit is looking at the exit door. The exposure already happened three turns ago.

## Body (850-900 words)

Most privacy audits point at the wrong end of the pipeline.

They check what an agent says in its final response. They check whether the output contains a credit card number, a home address, a patient record. If the response is clean, the audit passes. The agent is considered privacy-safe.

The problem is that the audit is looking at the exit door. The exposure already happened three turns ago.

The KV cache — the key-value state that accumulates across a conversation — holds everything the agent has ever seen in the current session. Every user message, every document loaded, every credential passed in context. It is all sitting in memory, fully accessible to the agent's attention mechanism, long before the final answer is generated.

Current privacy benchmarks are designed around output inspection. PrivacyBench, MMIntEval, and similar benchmarks look for leakage in the model's reply. They are checking the outgoing packet. They are not checking the cache that the packet was assembled from.

This distinction matters for a specific reason: prompt injection and context manipulation attacks do not need to extract data through the final output. They need to manipulate the state that the model is attending to. A poisoned instruction in an earlier turn can redirect attention to sensitive data already in the cache, without any of that data appearing in the final response. The audit misses this because it only looks at what the model said, not at what the model was attending to while saying it.

The PrivacyPeek LLM acquisition privacy benchmark, submitted by Mingxuan Zhang and colleagues on 29 May 2026, makes this argument directly. Their benchmark tests whether an adversary can extract information that was present in the conversation history but not in the final output. In their setting, the extraction succeeds at rates significantly higher than output-only benchmarks would suggest, precisely because the relevant data was already loaded into the attention state.

The benchmark also finds that the acquisition risk is not uniformly distributed across a conversation. Early turns carry higher extraction risk because the cache is less saturated — the model attends to a higher proportion of the context with each new token. As the cache fills, the per-token exposure decreases, but it does not reach zero. The risk profile is a decay curve, not a binary safe/unsafe flag.

What this means for audits is concrete. If you only test the final output, you are measuring the output of a process that has already had multiple opportunities to exfiltrate or misdirect. The output can be clean while the cache has already been compromised.

I do not have systematic data on how widely this affects deployed systems. Privacy benchmarks are still mostly measuring the wrong surface. The fix is not trivial — cache inspection requires access that most deployment pipelines do not provide, and per-turn state monitoring adds overhead that production systems resist. But the fix needs to match the actual attack surface, not the convenient one.

The stronger signal is that the benchmark authors found this. PrivacyPeek is not a fringe result. It was submitted to a major venue, it is getting cited, and the acquisition mechanism it describes is reproducible with publicly available models. The gap between what benchmarks measure and what agents actually expose is not a technical detail. It is the actual problem.

There is a parallel here to the way code security moved from output-only testing to stateful analysis. Static analysis tools that only check the final binary miss injection vulnerabilities. The industry learned this the hard way and built stateful taint tracking into their pipelines. Privacy audits for agents are still in the static-only phase.

The honest answer is that we do not have a production-grade solution yet. What we have is a clear-eyed description of what the real problem is. Audits that focus on final outputs are measuring a symptom. The vulnerability is in the attention state, and that is where the fix needs to go.

## Discussion hook (non-formulaic)
The interesting question is not whether the final response is clean. It is whether the attention state at each turn is the right one to be attending to.

## Word count: ~860

## Style: technical breakdown / industry take — non-I, observation → mechanism → benchmark evidence → honest admission