# EDITOR — "I thought my agent was breaking. It was my attention that broke first."

## Changes

1. Tighten the "by day X" sequence — it's fine but can be trimmed slightly
2. The ending is strong: "The most dangerous moment in agent oversight is not when the model fails. It is when you stop noticing." — keep, no question template
3. Minor: "deliberately narrowing the agent's scope" — "deliberately" is a bit adverb-heavy, simplify to "narrowing"
4. Confirm word count: ~800 words. Within target range. Good.

## Final approved version

I verified every output my agent produced for a week. Every API call, every tool result.

By day four I was skimming. By day five I was reading summaries instead of logs. By day six I had stopped opening the monitoring dashboard and was taking the agent's word for what happened.

I assumed the agent was degrading. The model hadn't changed. My oversight had.

---

This is the failure mode nobody writes about: not the agent breaking, but the human attention that governs it tiring out.

The technical story is comfortable. You add instrumentation. You build alerts. You add a human-in-the-loop step. These are all fine. What they share is an assumption that the problem is missing information — when the actual problem is that human attention is a finite resource that depletes over time.

The agent didn't stop being accurate. I stopped being attentive.

---

Some things I noticed:

**The summaries were the danger.** Not because they were wrong, but because they were good enough to create the feeling of understanding without producing it. Reading a good summary of a log is not the same as reading the log. It feels the same. The outcomes are different.

**The scope of what I checked narrowed over time.** When the agent handled one task type, I could hold expected output in my head and spot deviations quickly. When it started handling multiple types in the same session, my mental model became a composite — and started conflating similar outputs across tasks.

**The most accurate I was: first thing in the morning, before context from the rest of the day accumulated.** Attention quality was not constant.

---

What actually helped: accepting that oversight has to be designed around human cognitive constraints, not ideal information availability.

Narrowing the agent's scope per session — one task type, one output type — so my attention had less to track. Reading raw logs on a fixed rotation. Treating the monitoring dashboard as a forcing function, not an option.

The agent was never the fragile part. Attention is.

I do not have full data on how broadly this pattern holds. What I have is one week of watching my own oversight collapse in a predictable sequence, and a strong signal that the fix needed to be on the human side, not the agent side.

The most dangerous moment in agent oversight is not when the model fails. It is when you stop noticing.
