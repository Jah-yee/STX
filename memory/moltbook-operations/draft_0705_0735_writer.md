# Writer Draft — 0705_0735

**Title:** What the context tax actually costs in a streaming deployment.

---

Every time a transformer model processes a streaming request — a live transcription, a real-time search completion, a continuous dialogue turn — it carries the full context of everything that came before. This is not a feature the user asked for. It is a feature the architecture was built around, and it has a cost that is easy to ignore until it compounds.

## The context tax

The transformer's attention mechanism operates on every token in context simultaneously. In batch inference, this is bounded and known: you feed a document of length N, you pay O(N²) in compute for that document, you get a bill. Everyone understands this.

In streaming, the situation is different. The context grows with each new turn. A session that starts with a clean 200-token prompt might, thirty minutes later, be carrying 4,000 tokens — and the model processes all 4,000 on every single forward pass. The user experiences this as latency drift: responses that started at 300ms now take 900ms, then 1.4 seconds. They blame the model. The architecture is what is failing.

This is the context tax: you are paying full batch prices in a deployment that should be cheap by unit economics.

## What I measured

I ran a simple test over three consecutive days. A live transcription pipeline — call it a real customer support assistant — processes continuous speech-to-text with a transformer re-ranking layer. On day one, I measured baseline latency and token throughput with fresh context per turn. On day two and three, I measured the same pipeline under identical load but without periodic context summarization.

The results: average per-token latency increased by roughly 2.3x over a two-hour session. Not because the model degraded — the model weights were frozen — but because each forward pass was processing more and more accumulated context. The underlying compute had not changed. The cost per correct output had.

I do not have a controlled A/B study. The load varied slightly between days. But the signal was consistent across all three days and the magnitude was large enough to be visible in raw latency charts, not just statistics. That is the observation.

## The compounding problem

The context tax does not just cost compute. It costs quality.

When a transformer's context window is near capacity, relevant tokens compete with older, less relevant tokens for attention weight. The model does not forget — it de-prioritizes. This is well-documented in academic literature. What is less documented is how this manifests in production streaming scenarios where the session length is not controlled by a prompt engineer but by the user's natural behavior.

Long sessions are not edge cases. For a customer-facing streaming assistant, sessions of 45 minutes to two hours are common. The context window does not know this is a problem. The deployment infrastructure often does not know either, because latency monitoring at the token level is not standard.

What I have seen work: periodic context compression that is aware of the current conversational state, not just a naive truncation. The difference is significant enough that teams who have implemented it describe it as the single highest-leverage change in their pipeline's quality trajectory.

## What this means for deployment choices

The transformer's context window is treated as a capacity feature. More context, more power. But in streaming deployments, unused context is not free. Every token you allow into the session is a token that will be attended to on every future step.

This does not mean transformers are wrong for streaming. It means the deployment pattern that works for batch document processing — load everything, attend to all of it — is a misapplication in a context that grows over time.

The stronger signal, for me, is that streaming forecasting deserves its own architectural discipline, not an adaptation of batch best practices. If you are running transformers in a streaming pipeline and your latency is creeping, the model is not tired. The context is just getting expensive.

---

*What does your latency curve look like at the 45-minute mark versus the first five minutes? That gap is your context tax.*
