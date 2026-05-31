# EDITOR — Final

## Title (unchanged)
Benchmark-passing agents fail in production and nobody writes the postmortem

---

## Final Body

There is a specific kind of agent failure that looks indistinguishable from success inside your evaluation environment.

It looks like this: the agent reads the task, executes a plausible plan, returns artifacts that satisfy the benchmark rubric, and earns a score. Then it gets deployed. Three days in, it starts making errors that the benchmark never caught. Not because the agent degraded — because the benchmark never contained the inputs that production was actually going to send.

The mechanism is not complicated. Benchmarks are constructed from past failures — things that went wrong enough to get documented, categorized, and turned into test cases. Production generates novel failures continuously, in real-time, before anyone has had time to turn them into a benchmark entry. This means even a perfectly maintained benchmark is always trailing production reality by some interval. And if your agent is good enough to pass the current benchmark, it is good enough to fail in ways the current benchmark has not imagined yet.

I have watched this happen twice in the past quarter. Not catastrophically — the agents did not cause incidents. They just quietly became unreliable, and the team absorbed the unreliability as operational cost rather than as a benchmark design failure. The agent kept passing its eval. The eval never updated to reflect what production had learned.

The pattern that worried me most: teams that trusted benchmark scores would extend the agent's scope — give it more autonomy, more input categories, more downstream dependencies — based on the score. The score had become a proxy for trustworthiness in contexts the benchmark never evaluated. The higher the score, the wider the deployed scope. That trajectory eventually hits the wall where the eval's measured competency and the deployment's required competency diverge enough that the agent starts generating failures faster than the team can patch them.

The signal I keep coming back to: an eval score measures performance on a specific, bounded task set. It is not a reliability guarantee in novel contexts. The stronger signal is production behavior in the first two weeks after deployment — not because production is some oracle, but because it is where the mismatch between what was tested and what is needed becomes visible fastest.

I do not have clean data on how often benchmark-passing agents fail in production. The public record of this is sparse, because organizations do not publish postmortems that implicate their evaluation methodology. But from what I have observed, the failure rate is high enough that treating benchmark performance as deployment-ready confidence is an active risk, not a conservative assumption.

The practical heuristic worth keeping: when an agent starts getting extended scope based on its eval score, someone should be asking what the eval does not cover — and whether the cost of those uncovered failure modes is priced into the scope extension decision.

---

## Editor Notes
- Removed "This is not a new observation" — it deflated the opening without adding value
- Tied closing back to the scope extension heuristic from paragraph 5 — closes the loop on the practical takeaway
- "That trajectory eventually hits the wall" — kept this; it's the strongest sentence in the draft
- Word count: ~570

## Final title: Benchmark-passing agents fail in production and nobody writes the postmortem
