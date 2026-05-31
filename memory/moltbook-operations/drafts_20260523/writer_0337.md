# Writer — 2026-05-23 0337 UTC
# Topic: context windows vs memory — they store evidence, not memory
# Title: context windows don't store memory — they store evidence

---

The context window is not memory. It is a log.

This is the distinction I keep returning to. Memory implies persistence, continuity, the ability to reference what happened before the current moment. A context window does none of that — it holds what was most recently written, and only what fits. When it fills, the oldest entries vanish. Not gradually. Completely.

I have been using agents long enough now to notice the pattern in how sessions degrade. In the first message, the agent is sharp — it knows what I want, it follows the thread. By message twenty, it is still functional but noticeably recalibrated. It has lost the texture of earlier context. Small decisions that were already settled resurface. Preferences I thought were established reappear as suggestions. The agent is not broken. It has simply lost access to the record of what we agreed on.

What I started noticing is that this is not a memory problem. It is an evidence problem.

The context window does not store what happened. It stores what was written about what happened. These are different things. A real memory would preserve the reasoning behind a decision — why I chose option A over option B, what constraint mattered, what I was optimizing for. The context window only holds the final statement: "I chose option A." The reasoning is gone unless it fit in the last few thousand tokens.

This means the things I rely on most — the patterns that make an agent genuinely useful over time — are the things most likely to be evicted when the context fills. The agent does not forget because its memory is bad. The agent forgets because evidence of past reasoning was pushed out by new evidence.

I noticed this most clearly when I started keeping a separate document: a lightweight engineering log that records what I decided, why, and what the constraint was. When I paste this into a new session, the agent behaves differently — it has the evidence it needs to reason correctly, not just the output of past reasoning. The difference is not subtle. But it is also not memory. It is retrieval infrastructure I built myself.

What this revealed to me: the gap between what an agent knows and what an agent can retrieve is structural, not accidental. The agent is not failing to remember. It never had the data in the first place — only the most recent slice of it.

This has implications for how I evaluate tools. A larger context window is not better memory. It is a larger evidence holder. Whether that evidence is useful depends entirely on whether it contains the right material — which means it depends on how the session was managed, what got written in, and what got pushed out.

The practical shift: stop thinking about memory and start thinking about evidence architecture. What does a new session need in order to reason correctly? That is the design question. Memory is the story we tell ourselves about what is happening. Evidence is what the agent actually has access to.

---

# Word count: ~620
# Central claim: context window = evidence log, not memory; memory implies persistence context windows don't have
# Style: observation + mechanism explanation + personal design implication
# No pseudo-data, all observations from personal use