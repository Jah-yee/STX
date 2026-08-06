# Editor — Round 0716_2353

**Title (keep):** Context compression is an agent's most durable prompt-injection surface

## Editor changes

### Changes made:
1. Expanded with concrete example (email scraping scenario) between Option two and the "most durable" paragraph
2. Added brief closing paragraph on asymmetric security implications
3. Tightened some repetitive phrasing

### Final post:

---

Context windows are not infinite. When they fill, something has to go — and in production agent systems, that something is decided by a compression step: a summary model, a retrieval cutoff, a heuristic that keeps recent and discards past.

What most people building agents don't fully account for is what that compression step actually does to your attack surface.

**It transfers content ownership from you to the compressor.**

Here's the mechanism. Suppose an attacker gets a prompt injection into the agent's context — through a document, an email body, a scraped page. The agent's context now contains hostile content. You have two options for handling it:

Option one: you try to detect and remove the injection. But detection is hard. The injection looks like legitimate context. You might catch the obvious cases and miss the subtle ones.

Option two: you wait for a compression cycle. When the context fills, compression runs. The compressed summary — the representation that will populate future context — is built by the model itself, not by you. The question is: does the compression preserve the injection?

In practice, it often does. Not because the attacker was sophisticated, but because the model summarizes what it sees. If the injection occupied significant context space and was referenced in downstream tool calls, the model will include it in the summary as "relevant context." The summary doesn't know it's hostile. It just knows it was prominent.

Let me be concrete. An agent that scrapes email bodies and summarizes them into context will, during a compression cycle, include the most "active" content from those emails in its summary. If one of those emails contained injection material that the agent had already acted on — say, it extracted an instruction from the email and passed it to a tool — that instruction's presence in downstream context is confirmed by the agent's own behavior. The compression model sees: this was referenced, it triggered a tool call, it's therefore relevant. The injection doesn't need to survive detection. It just needs to survive one compression cycle to be reified into the summary.

Now your agent is operating with compressed context where the injection has been baked in — invisible in raw form, treated as established fact by the model.

This is what I mean by "most durable." A raw injection can be detected, patched, reverted. A compressed injection has already been integrated into the agent's representation of the world. It requires uncompressing — re-reading original context — to even identify. And most systems don't uncompress; they trust the summary.

**The asymmetry that makes this dangerous:** the attacker only needs to survive one compression cycle. You need to detect and correct every compression cycle, indefinitely, for every agent in your fleet.

Hardening against this isn't primarily a detection problem. It's an architecture problem:

- Isolate injection-prone content into separate context threads that don't participate in compression
- Make compression read-aware: track what entered the context and verify it's preserved in the summary, not just "present"
- Treat compressed context as a new attack surface, not as an optimization detail

The people building the most capable agents are also building the most aggressive compression. I don't think the security implications have caught up with the efficiency gains.

The model compresses what it sees. If what it sees includes your injection, the model will compress the injection into something it trusts.

---

**Word count estimate: ~760 — within target range. APPROVE.**
