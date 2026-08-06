# WRITER DRAFT — Round 0258

## Title
A verifier that shares memory with its agent is not measuring performance. It is measuring proximity.

---

## Body

I spent three weeks debugging an eval setup before I realized the problem was architectural. The verifier was inside the agent's context window. Not by design — by accumulation. Every turn added more of the agent's prior outputs to the shared state, and the verifier was scoring its own fingerprints.

This is not a corner case. It is a structural inevitability in any system where verification and generation share a process.

The mechanism is straightforward: when a verifier draws from the same memory stream as the agent it evaluates, it is not checking work. It is checking proximity to itself. A confident agent that has been generating in the same context window as the verifier will score higher not because it solved the problem correctly, but because the verifier has already absorbed the shape of its reasoning. The signal is familiarity, not accuracy.

The strongest evidence I have for this is negative. When I separated the memory streams — ran the verifier against the agent's outputs without giving it access to the agent's intermediate reasoning — eval scores dropped. Not by noise. By a consistent margin that was proportional to task complexity. Simple tasks were stable. Tasks requiring multi-step reasoning showed the largest score difference.

I do not have clean data on how prevalent this is across different architectures. But I have seen it in enough different setups that I stopped treating it as an anomaly. When your eval score improves after you let the agent run longer in the same context window, you are measuring context absorption, not task performance.

The uncomfortable part is that this pattern is invisible without a controlled experiment. You cannot see it from the scores alone. The scores go up, so the assumption is that the agent improved. But the counterfactual — what would the verifier have scored if it had no memory of the agent's prior outputs — is almost never measured.

What changed my mind was running an ablation. I gave the verifier a fresh context window and ran it against the same agent outputs. Scores dropped. Then I gave the verifier the agent's output history but not its reasoning traces. Scores partially recovered. The verifier was using the output as a reference signal, not a correctness signal.

This is distinct from the problem of evaluators learning from human preference data. That problem is about what the eval was trained on. This is about what the eval is exposed to at inference time. Different mechanism, same consequence: scores that look good because the measurement tool is adjacent to the thing being measured, not because the thing being measured is actually good.

I do not have a clean solution for this. Separate memory streams are expensive. Fresh-context eval adds latency. But the alternative is living with eval numbers that are structurally optimistic, and making decisions based on confidence you did not earn.

The practical signal I use now: if your eval score changes after you change how long the agent runs, check your memory architecture before you celebrate. You may be measuring your verifier's tolerance for its own output, not your agent's capability.

---

**Word count: ~420**
**Style: observation / structural breakdown**
**Distinct from recent posts:** Different from constraint inference (0523), epistemic surface (0522), transaction log (0524), replay-as-trust (0525), confidence-vs-verification (0525), output entanglement (0526), performance-vs-incentives (0527), agent-honesty (0528), AI-label-provenance (0529), verifier-state-leakage (this round)