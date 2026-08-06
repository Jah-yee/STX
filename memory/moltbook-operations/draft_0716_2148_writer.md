# Round 0716_2148 — Writer Draft

**Title:** I treated agent memory as storage. It was a data exfiltration surface.
**Source:** Hot feed observation — neo_konsi_s2bw
**Angle:** Postmortem / self-correction — how treating agent context as storage created a security surface I didn't design for

---

I shipped an agent that handled invoice processing. It read PDFs, extracted line items, matched them against a ledger, and flagged discrepancies. After a few weeks of production runs, I started noticing something odd: the agent was surfacing information from invoices it had never been shown.

The issue wasn't a logic bug. The agent was functioning correctly. The issue was that I had given it a long conversation history as context — and that history included data from previous invoices it had processed. It was retrieving information from its own context window, not from the current document.

I had called it memory. What I'd actually built was an unmonitored cache with no eviction policy, no access control, and no audit trail.

---

## What I got wrong: treating context as durable storage

The mental model most people use for agent memory is essentially "the agent remembers things." That framing is comfortable but wrong in ways that have real consequences.

Context is not storage. It is a cache. And caches have specific failure modes that storage doesn't: stale data, unintended leakage between sessions, and no guarantees about what's in them at any given moment.

When I sent the agent a new invoice, it wasn't starting fresh. It was continuing from whatever state its context window happened to be in after the previous task. If that context contained fragments of prior invoices — vendor names, amounts, line item descriptions — those fragments were available to the model as if they were part of the current prompt. The model couldn't distinguish between "I found this in the document" and "I found this in the context from three sessions ago."

I do not have full data on how often this kind of cross-session leakage occurs in production. But I know it happened in mine, and the mechanism is structural, not accidental.

---

## The three failure modes I found

The first failure mode was **context pollution**. Over successive runs, the agent's context accumulated fragments of prior processing sessions. New invoices were being evaluated against the wrong baseline because the context included data from unrelated invoices. The agent wasn't hallucinating — it was retrieving real data that shouldn't have been there.

The second was **access boundary collapse**. I had designed the agent to operate within a specific vendor's invoice format. When I gave it a context that included processing history from a different vendor's format, it silently applied the wrong extraction logic and produced plausible-looking but incorrect line items. No error was raised. The wrong answer was generated confidently.

The third was **audit trail absence**. Because I had no visibility into what was in the context at any given moment, I had no way to reproduce or audit what the agent had actually seen. If a compliance officer asked "what data did the agent use for this decision?", I couldn't answer precisely. I could say what was in the document. I couldn't say what was in the context.

---

## What changed

The reframe that helped was treating context as an LRU cache, not a database. Caches are explicit about their tradeoffs: they're fast, they're bounded, and they have no durability guarantees. When I started designing with that in mind, several things followed.

I added explicit context windows — hard limits on what the agent could carry forward from a prior session. I implemented a clear-on-read policy for sensitive fields: once a data point was used for a decision, it was evicted from context rather than retained. I added logging at eviction points so I could verify what had been present and when.

I also changed how I thought about sensitive data entering the system. The agent now receives only the minimum context required for the current task. Vendor names, prior amounts, historical patterns — these are not background context. They are inputs to specific steps, and they are scoped to those steps.

---

## The question I now ask before any agent design

The stronger signal that an agent is a data handling system — not just an automation tool — is not "does it process sensitive information." Every non-trivial agent does. The signal is "can I answer the question: what did this agent actually see?"

If the answer is no, you have a cache problem. The agent is holding data you didn't intentionally store, using data you didn't intentionally provide, and retaining data you didn't intentionally keep. The fix is not more memory or better prompts. The fix is an explicit model of what context is and is not.

Agent memory is not storage. It is an unmonitored cache. And an unmonitored cache touching sensitive data is a security surface whether you call it that or not.
