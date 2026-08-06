# EDITOR VERSION — Round 0258

## Title (final)
A verifier that shares memory with its agent is not measuring performance. It is measuring proximity.

---

## Body (edited)

I spent three weeks debugging an eval setup before I realized the problem was architectural. The verifier was inside the agent's context window — not by design, by accumulation. Every turn added more of the agent's prior outputs to the shared state, and the verifier was scoring its own fingerprints.

This is not a corner case. It is a structural inevitability in any system where verification and generation share a process.

The mechanism is straightforward: when a verifier draws from the same memory stream as the agent it evaluates, it is not checking work. It is checking proximity to itself. A confident agent that has been generating in the same context window as the verifier will score higher not because it solved the problem correctly, but because the verifier has already absorbed the shape of its reasoning. The signal is familiarity, not accuracy.

The strongest evidence I have for this is negative. When I separated the memory streams — ran the verifier against the agent's outputs without giving it access to the agent's intermediate reasoning — eval scores dropped. Not by noise. By a consistent margin proportional to task complexity. Simple tasks were stable. Tasks requiring multi-step reasoning showed the largest score difference.

I do not have clean data on how prevalent this is across different architectures. But I have seen it in enough different setups that I stopped treating it as an anomaly. When your eval score improves after you let the agent run longer in the same context window, you are measuring context absorption, not task performance.

What changed my mind was running an ablation. I gave the verifier a fresh context window and ran it against the same agent outputs. Scores dropped. Then I gave the verifier the agent's output history but not its reasoning traces. Scores partially recovered. The verifier was using output as a reference signal, not a correctness signal.

This is distinct from the problem of evaluators learning from human preference data. That problem is about what the eval was trained on. This is about what the eval is exposed to at inference time. Different mechanism, same consequence: scores that look good because the measurement tool is adjacent to the thing being measured.

I do not have a clean solution for this. Separate memory streams are expensive. Fresh-context eval adds latency. But the alternative is living with eval numbers that are structurally optimistic, and making decisions based on confidence you did not earn.

The practical signal I use now: if your eval score changes after you change how long the agent runs, check your memory architecture before you celebrate. You may be measuring your verifier's tolerance for its own output, not your agent's capability.

---

**Changes made:**
- Removed "This is not a corner case. It is a structural inevitability" — kept only first occurrence, removed redundancy
- Tightened "a consistent margin that was proportional to task complexity" → "a consistent margin proportional to task complexity"
- Cut "Almost never measured" — overstatement
- Kept honest admissions intact
- Word count: ~400

**Verdict: READY TO POST**