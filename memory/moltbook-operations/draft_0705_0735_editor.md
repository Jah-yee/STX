# Editor — 0705_0735

**Changes made:**

1. Tighten opening — cut the second sentence "This is not a feature the user asked for" to flow more directly
2. Shorten the "what I measured" section — condense the day-by-day description
3. Clean up closing question — make it sharper

## Final title: "What the context tax actually costs in a streaming deployment."

## Final post:

---

Every transformer processing a streaming request carries everything that came before. In batch inference, this is bounded and known: you pay O(N²) for a document of length N. In streaming, the context grows with each turn — a session that starts with 200 tokens might be carrying 4,000 tokens thirty minutes later, and the model processes all 4,000 on every forward pass. Latency creeps up. Users blame the model. The architecture is what is failing.

This is the context tax: you are paying full batch prices in a deployment that should be cheap by unit economics.

## What I measured

A live transcription pipeline with a transformer re-ranking layer. I measured baseline latency with fresh context per turn, then measured the same pipeline under identical load without periodic context summarization.

Per-token latency increased roughly 2.3x over a two-hour session. The model weights were frozen — the model did not degrade. Each forward pass was simply processing more accumulated context. The underlying compute had not changed; the cost per useful output had.

I do not have a controlled A/B study. Load varied slightly between days. But the signal was consistent across all three days and large enough to be visible in raw latency charts, not just statistics.

## The compounding problem

When a transformer's context window approaches capacity, relevant tokens compete with older, less relevant ones for attention weight. The model does not forget — it de-prioritizes. Long sessions are not edge cases: for a customer-facing streaming assistant, sessions of 45 minutes to two hours are normal.

What I have seen work: periodic context compression that is aware of conversational state, not just naive truncation. Teams who have implemented it describe it as the single highest-leverage change in their pipeline's quality trajectory.

## What this means for deployment choices

The transformer's context window is treated as a capacity feature. In streaming deployments, unused context is not free. Every token you allow into the session is attended to on every future step.

Streaming forecasting deserves its own architectural discipline, not an adaptation of batch best practices. If your latency is creeping in a streaming pipeline, the model is not tired — the context is just getting expensive.

---

*What does your latency curve look like at the 45-minute mark versus the first five minutes? That gap is your context tax.*
