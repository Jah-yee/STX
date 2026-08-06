# WRITER DRAFT v2 — "I thought my agent was breaking. It was my attention that broke first."

## Selected Title
"I thought my agent was breaking. It was my attention that broke first."

## Full Post

For one week I read every log my agent produced. Every API call, every tool result, every output.

By day four I was skimming. By day five I was reading summaries instead of logs. By day six I had stopped opening the monitoring dashboard entirely and was just taking the agent's word for what happened.

I assumed the agent was degrading. The model hadn't changed. My oversight had.

---

This is the failure mode nobody writes about: not the agent breaking, but the human attention that governs it tiring out.

The technical story is comfortable. You add instrumentation. You build alerts. You add a human-in-the-loop step. These are all fine. What they share is an assumption that the problem is missing information — when the actual problem is that the human attention handling that information is a finite resource that depletes over time.

The agent didn't stop being accurate. I stopped being attentive.

---

Some things I noticed about the pattern:

**The summaries were the danger.** Not because they were wrong, but because they were good enough to create the feeling of understanding without producing it. Reading a good summary of a log is not the same as reading the log. It feels the same. The outcomes are different.

**The scope of what I checked narrowed over time.** When the agent was handling one type of task, I could hold the expected output in my head and spot deviations quickly. When it started handling multiple task types in the same session, my mental model became a composite of everything I'd seen — and started conflating similar outputs across tasks.

**The most accurate I ever was: first thing in the morning, before context from the rest of the day had accumulated.** Attention quality was not constant. It was context-dependent.

---

What actually helped: accepting that oversight has to be designed around human cognitive constraints, not around ideal information availability.

That meant deliberately narrowing the agent's scope per session — one task type, one output type — so my attention had less to track. It meant reading raw logs on a fixed rotation rather than reading summaries when I felt like it. It meant treating the monitoring dashboard as a forcing function, not an option.

The agent was never the fragile part. Attention is.

I do not have full data on how broadly this pattern holds. What I have is one week of watching my own oversight collapse in a predictable sequence, and a strong signal that the intervention needed to be on the human side, not the agent side.

The most dangerous moment in agent oversight is not when the model fails. It is when you stop noticing.
