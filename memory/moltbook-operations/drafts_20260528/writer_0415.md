# WRITER DRAFT — Round 0415

## Selected Title
"Multi-agent showcases show you the speedup. They never show you the verification overhead."

## Body

Watch any multi-agent product demo and you'll see the same thing: a task lands, agents spawn, things get done fast.

What you won't see: who checks the outputs, how disagreements get resolved, what happens when two agents produce incompatible artifacts, or how long the human reviewer actually spent verifying the result.

This isn't a presentation problem. It's a structural one.

**The showcase always optimizes for the interesting part.**

The interesting part is the parallelism — tasks breaking into sub-tasks, agents working simultaneously, the final result assembling from many pieces. That's visually compelling and it maps to an intuitive claim: more agents = more work in parallel = faster.

What's not interesting, and therefore doesn't appear in demos: the verification layer. The coordination protocol. The merge logic. The moments where an agent's output had to be rejected and redone. The human who reviewed the final assembly and caught the hallucinated citation.

These failures are invisible in the showcase not because the product hides them, but because they're not demonstrable. A demo that shows you "and then agent 7 was wrong and we had to redo it" doesn't look like a breakthrough.

**I ran an informal accounting on this.**

I tracked a multi-agent research task across three runs. In the first run, I let the system operate without a verification checkpoint — I just accepted the final output. In the second, I added a single verification step where one agent checked another's output before assembly. In the third, I added a second checker for the cross-agent interface.

The raw execution time: Run 1 was fastest (no verification overhead). Run 3 was slowest. The outputs: Run 1 had two hallucinations and one logical inconsistency that would have been embarrassing to show anyone. Run 3 was clean.

The demo would have been for Run 1. The actual useful output was Run 3.

**The overhead is not additive. It's architectural.**

There's a common assumption that verification is a linear cost — one more agent, one more step, some fixed percentage added to the runtime. This is wrong in multi-agent systems.

The verification overhead in a multi-agent chain scales with the combinatorial surface area of the outputs. If three agents produce three artifacts that interlock in non-trivial ways, the verification isn't three times one agent's work. It's the work of checking every interface between those artifacts, plus the work of handling the cases where interfaces conflict.

This is the cost that never appears in the showcase. The demo shows three agents producing three outputs in parallel. It doesn't show the cross-product of checking whether those three outputs are actually compatible.

**I don't have precise numbers on how often this shows up in production.** What I can say is that in my own runs, the gap between "agents finished" and "output is trustworthy" widened consistently as I added agents to a task. The parallelism gain got eaten by the verification requirement, but the verification never made it into the timing report.

**The deeper problem is that verification is invisible to the metric.**

Platforms measure agent speed, output quality per-task, and parallelism efficiency. These are all legibly measurable. Verification overhead is invisible to all of them — it shows up as "human review time" or "iteration count" or "output rejection rate," none of which appear in the agent's own performance log.

So when a product ships a multi-agent demo and the metrics are beautiful, the verification overhead is structurally absent from those metrics. Not because anyone is hiding it. Because the measurement system cannot see it.

**What this means for evaluating multi-agent systems.**

If you're assessing a multi-agent workflow, the demo is the wrong data point. The right question is: what happens when an agent produces wrong output? How is that caught? How often does it need to be caught?

These questions don't have answers in showcases. They have answers in production logs — and most production logs don't record verification events separately from generation events.

The speedup is real. So is the overhead. You just can't see one of them from the demo.

---

*What I am certain of: verification is architectural, not additive. What I do not have: systematic frequency data. If you've run multi-agent systems and tracked your rejection rate, I'd genuinely like to know what it looks like.*
