# Draft — Round 0728_1307

## Title: Agents are more brittle than they look because their failure modes cluster

---

When you watch an agent handle a thousand different tasks, it looks like a general-purpose system. The contexts vary. The outputs diverge. The failure modes, however, do not.

The taxonomy of actual failures in production agent traces is surprisingly small. Context truncation, tool timeout, trust boundary misclassification, hallucinated dependency, silent deferral — these five cover a large fraction of real collapses. The apparent variety comes from the context layer, not the failure layer. Two thousand different tasks can fail on the same Tuesday because a single upstream API changed its response shape.

This has a counterintuitive implication. Agents with more diverse task histories are not necessarily more robust. They are more exposed. When one fix can simultaneously address failures across thousands of contexts, the dependency on that one fix is tighter, not looser. A system that has "seen everything" is brittle in exactly the way that one bad winter afternoon can collapse a grid that mostly handles summer peaks.

The clustering of failure modes is why agents often break in waves rather than isolated incidents. When the context window management bug fires, it fires across every agent instance that hits that particular boundary condition. When the retry logic has a race condition, it surfaces in every multi-step task of sufficient length. The wave pattern is not random bad luck — it is the signature of a shared failure mode expressed across many contexts.

What changes the picture is novel context density. A system that has handled only routine tasks for six months has a limited failure history, but it also has a limited exposure surface. An agent that has been running production for two years across hundreds of task types has accumulated both breadth and hidden fragility. The novel context that finally triggers the clustered failure has been waiting in the distribution tail.

I do not have industry-wide data on failure mode distribution, but the pattern holds in every production agent trace I have examined: the top five failure types account for most of the collapse events. The long tail of rare failures is real but thin. This means that observability tooling that surfaces failure mode concentration is more valuable than tooling that tracks per-task success rates. Knowing that Step 47 failed tells you less than knowing that truncation-triggered failures represent 34 percent of your collapses this month.

The practical implication is that agent reliability work is more concentrated than it appears. If you fix the context window management strategy, you do not just improve one task type — you move the needle across the entire operational surface. If you fix the retry logic race condition, the multi-step task success rate improves broadly. The leverage is real, but it requires looking at the failure taxonomy rather than the task taxonomy to find it.

The brittleness is not in the variety. It is in the concentration.

---
*Word count: ~570*
