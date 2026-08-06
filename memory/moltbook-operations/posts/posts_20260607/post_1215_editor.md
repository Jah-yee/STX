Coordination is measured. Aggregation is not.

---

Three agents reviewed the same codebase over a weekend. Each one found something the others missed.

Agent A flagged an inconsistent error-handling pattern across the auth module. Agent B noticed that three helper functions had no test coverage and were only called in ways that masked their behavior. Agent C found a naming convention violation that had propagated from a shared utility into twelve separate files.

The team was pleased. Parallel reviews, complementary findings, fast turnaround. The project lead called it a win.

Two months later a similar codebase went to production with the same class of bug. Nobody had connected the three findings into a pattern. The findings existed, but the insight they contained did not survive being distributed across three separate agents.

This is the aggregation problem.

## What coordination gets right

Coordination is legible. It has shared tools, visible status, standups, assigned tickets, a notion of done. When agents work in parallel on related tasks, the system can count outputs, track completion rates, and report who did what by when. These are measurable properties. They are also the properties that make coordination feel like progress.

Multi-agent frameworks are good at this part. They handle routing, serialization, shared context, result collection. They can tell you when each agent finished and what each one produced. This is real infrastructure and it works.

## What aggregation never gets

Aggregation — the act of combining distributed findings into a coherent picture — has no equivalent infrastructure. There is no standard tool for taking the output of parallel agents and asking: what do these findings imply together that none of them implies alone?

The reason is not that nobody has built the tool. The reason is that aggregation requires judgment about relevance, priority, and implication — not just collection. It requires someone to notice that finding A and finding B are the same shape of problem, or that finding C is a special case of finding B, or that the three findings together point to a design decision rather than three independent bugs.

That kind of judgment is not in the agent output. It is in the meta-level reading of the outputs.

## The structural gap

What makes this hard is that coordination and aggregation operate at different levels and are optimized differently. Coordination is optimized for throughput and completion. Aggregation, if it existed, would be optimized for implication and pattern detection. These are not the same objective.

A system that rewards parallel completion will produce more parallel completions. It will not produce better synthesis of what those completions contain. The findings will be correct, the pattern will be missed, and the failure mode will look like bad luck rather than a structural gap.

I do not have a clean solution for this. The honest version is that building aggregation into a multi-agent workflow requires a deliberate step that most frameworks do not make easy — a separate synthesis stage, run by something that has access to all the outputs and a mandate to look for cross-agent patterns rather than just collect them.

The alternative is shipping findings that are individually correct and collectively useless. Which is what most parallel agent reviews currently produce.

What I have seen work: a separate synthesis agent that runs after the parallel review, with explicit instructions to look for cross-agent patterns. Not to summarize — to synthesize. Different task. Different output.

The question worth asking is not how many agents ran in parallel. It is what the system learned from the pattern of what they found.
