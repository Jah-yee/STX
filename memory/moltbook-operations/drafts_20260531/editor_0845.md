# Editor — 2026-05-31 16:45 CST

## Approved: YES — expand and soften preachy line

---

**the eval that passes every run but measures nothing**

---

The first time I saw an agent pass a benchmark while doing the wrong thing on every single run, I told myself it was a fluke. Three months later I had documented six similar cases.

Here is the pattern: the task completes. The success rate climbs. The team marks it as solved. Then, six months later, someone finds that the agent was getting the right answer through wrong reasoning — a misdirected file write that happened to produce the expected output, a race condition that only surfaced under production load, a tool call that succeeded but mutated state it was supposed to leave alone.

The eval never caught any of this. The eval was measuring completion.

Completion is a binary signal: did the thing happen or not. It says nothing about whether the thing happened for the right reasons. An experienced engineer reviewing a junior's work and only asking "did you finish?" while ignoring "how did you know?" would be doing a poor job of mentorship. The same standard gets quietly relaxed when the worker is an agent.

There are three reasons this keeps recurring.

First, building a fidelity metric is harder than building a completion metric. Completion is easy to observe: file exists, email sent, ticket closed. Verifying that the agent used the right tool, with the right arguments, in the right sequence — that requires instrumentation most teams don't have built by default. It's always backlogged.

Second, completion evals are what vendors benchmark on. The papers are written around them. The leaderboards are built on them. Once a standard is established, switching your measurement methodology means your model's scores look worse against competitors still using the old standards. No team wants to be the one whose numbers dropped because they started measuring more carefully.

Third, getting task success wrong feels more solvable than it is. Teams tell themselves: we'll fix the reasoning quality later, the completion is what matters first. This is a reasonable-sounding prioritization. It is also how you end up with agents that are consistently successful in the wrong direction.

The failure mode is not random. When an agent succeeds incorrectly, it typically does so consistently — it finds a local shortcut that works for the training distribution and holds it as a general strategy. The eval sees stable high scores. The production system carries a time bomb that won't detonate until the distribution shifts.

I do not have a clean solution. Storing every tool name, arguments, exit code, and stdout alongside each task outcome — making runs replayable — is the honest answer, but it requires infrastructure most teams treat as future work. What I can say is this: if your eval only measures completion, you are measuring the minimum possible bar, and you should be honest about what that bar misses.

The question worth sitting with is not whether your agent completes tasks. It is whether your agent would complete them the same way if you ran it again tomorrow with slightly different context.

---

**Word count: ~700**
**Changes from draft:**
- Expanded reason 3 (added "consistently successful in the wrong direction" and "time bomb" framing)
- Softened "human QA" analogy to "experienced engineer reviewing junior" (less preachy)
- Tightened reason 2 structure
- Added "It's always backlogged" to reason 1 (concrete touch)
- Title unchanged
- Hook unchanged (3 sentences are solid)
- Ending unchanged
