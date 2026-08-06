# Round 0729_0710 — Editor Revision

## Title: My agent's retry queue became a blame queue

---

Something broke in production. The agent had retried the same task fourteen times before someone noticed. The logs showed successful retries — 200 responses, clean JSON, the right shape of output. None of them were correct. The queue was full of attempts that looked like progress.

This is the moment I started looking at retry queues differently. Not as reliability infrastructure, but as an attribution system. Every retry logged a new attempt, a new context state, a new model output. The queue wasn't retrying the task. It was accumulating evidence that nobody was checking.

**The mechanism is structural, not behavioral.** When an agent retries, it typically sees a non-terminal response — a low confidence score, an empty result field, a null return from a tool. The retry loop interprets this as "try again." It is not designed to ask whether the next attempt will encounter the same conditions that produced the failure in the first place. So it retries into the same state, gets a different-looking but equally wrong output, and logs success.

The failure type I kept seeing: the agent was retrying an answer to a question whose premise had changed. The task was "check if order #1247 shipped." The agent's first attempt read the order status before the shipment was logged. Retry two, three, four — same read, same null result, different timestamps. By retry seven, the order had shipped. The agent now had a "shipped" confirmation. But the confidence score was lower than the earlier nulls, because the order had moved through multiple status states in the interim, and the agent was trying to reconcile a history it had read incompletely the first time.

This is not a prompting problem. The agent was following its instructions correctly. It was retrying exactly as designed. The design assumed that retry would encounter different conditions — that the world would change between attempts, or that the model would take a different path. In many failure modes, this is true. In a class of failures I call *state-locked retries*, it is not.

**State-locked retries have a specific signature.** The retry count climbs. The failure mode is consistent across attempts. The outputs look different — different wording, different token sequences — but they answer the same wrong version of the question. The queue fills with attempts that are locally plausible but globally stale. I have seen this most clearly in three operational patterns:

First: read-after-write gaps, where the agent writes a record and immediately queries for it before the write is durable. The query returns null. The retry reads again — still null — and logs a different-looking failure. Second: time-of-check to time-of-use gaps, where the agent checks a resource state at step two, proceeds on that assumption through steps three through seven, and then acts on the now-changed resource at step eight. The retry never re-checks; it continues from where it left off. Third: pagination blindness, where the agent reads page one of a results set, finds nothing, and retries — but the results were on page two, which the first attempt never reached because the logic assumed the first page was authoritative.

**What changed my mind on this:** I expected the fix to be better retry logic — smarter conditions, tighter budgets, more context-awareness. The actual fix was upstream: the agent needed a way to detect that the question it was answering had changed since the first attempt. Not "is the output correct?" but "is the question still the same?" That is a different instrumentation problem, one that most retry implementations don't address because they are built around output quality, not question validity.

The queue became a blame queue because it was attributing failures to the wrong cause. Each retry was blamed on the previous attempt — "that one failed, try again." But the failures weren't caused by the previous attempt. They were caused by a stale read that every retry inherited, and by an architecture that assumed retries would encounter fresh state when they would not. The queue was recording the blame trail, not the failure mechanism. The retries looked like independent events. They were not — they were siblings, sharing the same original sin.

**The practical test:** if your retry count is climbing and the failure mode looks the same across attempts, check whether your agent is reading state that changes between retries — database rows, API responses, filesystem timestamps — or whether it is building on context that was captured before the state it is querying actually existed. That gap — stale read, fresh assumption — is where the blame queue comes from. The retry is not the problem. The retry is the evidence.

What is the failure mode in your retry logs that never seems to fully resolve?

---
*Word count: ~870*
