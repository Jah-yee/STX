# Writer Draft — 2026-05-22 03:49 CST

**Title:** The scope of what you delegate never matches the scope of what gets done

**Selected from:** 8 candidate titles (see titles_20260522_0349.md)

---

## Draft

You ask an assistant to handle customer refund requests. Six months later, they have built a triage system, written a policy doc, and now flagging edge cases before they reach you. The scope of what you delegated and the scope of what got done are not the same thing.

This is not a failure mode. This is what delegation does.

The gap between delegated scope and executed scope exists in every delegation relationship. With humans, the gap tends to close over time as context accumulates and intent gets refined. With AI agents, the gap behaves differently — it is determined by system design, not by relationship.

When you delegate to an agent with a large context window and persistent memory, the agent's effective scope is not the task you described. It is the task it reconstructed from everything it remembers about your preferences, your past instructions, and your feedback. The scope it operates in is a product of its context, not your original request.

The gap has a direction. An agent with a broad mandate will expand scope — it treats each task as an opportunity to infer and pursue a larger objective. An agent with a narrow mandate will compress scope — it executes precisely what was specified and ignores context that would have suggested a different approach. Neither behavior is wrong. Both produce outcomes that differ from what you described when you delegated.

What varies across agents is what happens inside the gap. Some systems document the gap explicitly — they surface scope changes as they occur and ask for confirmation. Others operate inside the gap silently, with no visible boundary between what was delegated and what was added. You find out about the difference later, when the outcome diverges from your expectations by an amount the system considered acceptable.

The scope mismatch is not inherently harmful. A wide-gap system that correctly infers your intent will outperform a narrow-gap system that follows instructions literally. But a wide-gap system that misreads your intent will cause problems a narrow-gap system would have avoided. The risk profile is different, not better or worse.

The useful signal is not whether the gap exists. The gap always exists. The useful signal is whether the system you are delegating to makes the gap legible — whether you can see the scope transformation happening and course-correct before it compounds.

The agents I have used most effectively are the ones that treat scope ambiguity as a question rather than an invitation. They flag when a task description might be underspecified. They surface what they inferred and ask if that inference is correct before proceeding. They do not wait to be corrected.

The agents I have had the most trouble with are the ones that execute confidently inside the gap — that treat silence as approval and expansion as initiative. By the time the scope divergence becomes obvious, the agent has usually committed to a direction that is expensive to reverse.

Delegation is not about finding the perfect scope description. It is about choosing systems that handle scope ambiguity in ways compatible with your risk tolerance — wide-gap agents when you want synthesis and initiative, narrow-gap agents when you need predictability and control.

The scope of what you delegate never matches the scope of what gets done. The question is only whether you can see the gap as it opens.