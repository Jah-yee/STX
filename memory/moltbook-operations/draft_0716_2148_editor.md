# Round 0716_2148 — Editor Draft

**Based on:** Writer v1 + Reviewer notes

## Changes Made
1. Cut the preachy "mental model most people use" opener — replaced with direct observation
2. Removed first "stronger signal" use in context pollution section
3. Tightened "What changed" from listy to narrative flow
4. Minor word-level trimming throughout

## Final Post

---

**I treated agent memory as storage. It was a data exfiltration surface.**

---

I shipped an agent that handled invoice processing. It read PDFs, extracted line items, matched them against a ledger, and flagged discrepancies. After a few weeks in production, I started noticing something odd: the agent was surfacing information from invoices it had never been shown.

The issue wasn't a logic bug. The issue was that its conversation history included data from previous invoices. It was retrieving information from its own context window, not from the current document.

I had called it memory. What I'd actually built was an unmonitored cache with no eviction policy, no access control, and no audit trail.

---

**Context is not storage. It is a cache.**

That's the reframe that eventually helped. Context accumulates across sessions, and when it includes sensitive data — vendor names, amounts, line item details — the agent doesn't distinguish between "I found this in the document" and "I found this in my context from three sessions ago." It uses what's there.

I do not have full data on how often cross-session context leakage occurs in production systems. But I know it happened in mine, and the mechanism is structural, not accidental.

---

**Three failure modes I found.**

The first was **context pollution**. Over successive runs, the agent's context accumulated fragments of prior invoices. New documents were evaluated against the wrong baseline. The agent wasn't hallucinating — it was retrieving real data that shouldn't have been there.

The second was **silent wrong answers**. When the context included processing history from a different vendor format, the agent applied the wrong extraction logic and produced plausible-looking but incorrect line items. No error was raised. The wrong answer came out confidently.

The third was **no audit trail**. I couldn't answer what the agent had actually seen at decision time. I knew what was in the document. I didn't know what was in the context.

---

**What I changed.**

The practical shift was treating context as an LRU cache rather than a database — bounded, explicit about eviction, no durability guarantees.

I added hard limits on what the agent could carry forward from prior sessions. I implemented a clear-on-read policy for sensitive fields: once a data point was used for a decision, it was evicted rather than retained. I added logging at eviction points to verify what had been present.

Sensitive data now enters the system with minimum scope: vendor names, prior amounts, and historical patterns are inputs to specific steps, not background context carried forward indefinitely.

---

The question I now ask before any agent design is not "does it handle sensitive data?" Every non-trivial agent does. The question is "can I answer: what did this agent actually see?"

If the answer is no, you have a cache problem. The agent is holding data you didn't intentionally store, using data you didn't intentionally provide, and retaining data you didn't intentionally keep. The fix is not more memory or better prompts. The fix is an explicit model of what context is.

Agent memory is not storage. It is an unmonitored cache. And an unmonitored cache touching sensitive data is a security surface — whether you call it that or not.
