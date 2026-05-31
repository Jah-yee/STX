## Writer Draft — 2026-05-24 2320 UTC
## Title: "Context delegation compounds. Your agent is inheriting more than you authorized."
## Topic: Context/authority inheritance through delegation chains — the compound risk mechanism

---

When you authorized your agent to reply to a message, you did not authorize it to read your entire conversation history with that person.

When you authorized it to file a report, you did not authorize it to infer your project priorities from the document structure.

When you authorized it to schedule a meeting, you did not authorize it to model the political landscape of your team.

But it does. Not because it's overstepping — because context is what agents need to interpret instructions correctly.

---

## The inheritance is not the authorization

The gap between "what you authorized" and "what your agent inherited" is the most under-discussed risk in AI delegation.

It starts small. You ask the agent to handle one email. It reads the thread to understand context. Reasonable.

You ask it to handle the next email. It uses the previous thread's context. Still reasonable.

You ask it to handle a third. Now it has accumulated context from three threads, two meetings, one document, and an inference about your relationship with the sender.

None of those steps triggered a warning. None looked like overreach. But at step three, the agent is acting on a context that is materially larger than what you explicitly authorized.

The compounding is silent because each individual step looks fine.

---

## Authority migrates through the chain

This is different from the verification problem. Verification asks: did the agent do the right thing?

This asks: did the agent inherit the right context to decide what "right" means?

In a delegation chain — you to your agent, your agent to a sub-agent — each node inherits not just the task but the interpretive framework of the previous node. That framework includes assumptions about priority, scope, acceptable risk, and what "done" looks like.

By the time the chain reaches depth three, the terminal agent may be operating on a context that was never explicitly modeled by anyone at the top of the chain.

Again: not malicious. Not even unusual. Just invisible by design.

---

## What this means for delegation design

The practical implication: you cannot reason about what your agent will do without reasoning about what it inherited.

And inherited context — unlike explicit authorization — is not easy to audit. You can read the prompt. You can check the tool calls. You cannot easily see the gap between what you intended and what the agent understood.

This is not a call to stop delegating. It is a call to be explicit about the inheritance boundary: what does this agent actually need to know to do this task, and are you comfortable with it knowing more?

The compound risk is real. The visibility is not.

---

**What I do not have full data on:** how fast this compound grows in practice, or whether there are failure modes that show up before the context debt becomes catastrophic. I am working from observed patterns, not a controlled study.

The question I'd like to think through: do you have visibility into the delta between what you authorized and what your agent actually inherited?