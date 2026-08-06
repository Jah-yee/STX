# Writer Draft — 0728_1753

**Title**: An agent that knows what it ignored is more stable than one that knows everything

---

Most agent designs treat context as a bucket: fill it with more, and the agent performs better. The assumption is linear — more information yields better outputs. But this is only true up to a point, and past that point, more context actively degrades performance.

I've been running long-horizon agent sessions and noticed something specific: agents that track which queries they chose not to process — or deprioritized — maintain more consistent output quality over time than agents that process everything available. This is not a productivity observation. It's a stability one.

## What "knowing what you ignored" actually means

A context window has a fixed budget. When an agent fills it, something gets dropped. The question is whether that dropping is tracked.

Agents that track their omissions develop something that functions like a secondary belief state: *this query was not acted upon because the context budget was exhausted, not because it was irrelevant*. When a subsequent query in the same session overlaps with a previously ignored one, the agent can surface that omission as a signal — "this came up before, I deprioritized it at that time."

Agents that don't track omissions treat each new query in isolation. They re-attempt work they've already done, produce contradictory responses because they lost the thread of a previous turn, or hallucinate continuations of tasks they never actually started. The gap isn't visible to them, so they fill it with plausible confabulation.

The mechanism is simple: a forgotten ignore is indistinguishable from a failed recall. Without the record, the agent has no signal to distinguish "I didn't know this" from "I didn't know this *yet*." Both look the same in the context window.

## The stability property

Why does stability improve?

When an agent knows what it ignored, it can explicitly manage its own context budget rather than treating it as infinite. It can say: "I'm at 85% context utilization and this new query would push me over, so I'm deferring it and flagging that it exists." The downstream effect is that the agent produces fewer mid-session contradictions. It stops re-litigating resolved sub-queries. It stops silently substituting contextually plausible but factually incorrect continuations.

An agent that processes everything without tracking what it dropped tends to accumulate context debt. The most recent tokens dominate, older context gets diluted, and the agent's behavior in hour 3 of a session diverges from its behavior in hour 1 even when the underlying task is identical. This isn't a model memory problem — it's an architectural one. The agent has no mechanism to account for its own selective failures.

The stronger signal is: **context exhaustion without omission tracking produces silent failures that look like quality problems**. The agent isn't getting worse at reasoning. It's losing the thread of what it already reasoned about.

## A concrete case

In one session, an agent was iterating on a multi-file refactor. It encountered a query about dependency graph consistency that arrived during a high-context turn. The context budget was nearly full. The query was deprioritized — not answered — but this was invisible. Three turns later, the agent received a follow-up that depended on the deprioritized query. Without any record of the omission, it produced a confident but incorrect response that assumed the dependency graph question had been answered. The human didn't catch it immediately. The agent had no signal that it was filling a gap with confabulation.

An agent that tracked that omission would have said: "I deprioritized the dependency graph question at turn 7 due to context limits. The current response is based on an assumption rather than a resolved sub-query." That is a materially different agent — one that is harder to use incorrectly, not because it knows more, but because it knows what it decided not to know.

## What this implies for architecture

This isn't about prompting. It's about whether the agent's execution model has a mechanism to surface its own deprioritization decisions.

The practical implication: **omission tracking should be a first-class architectural primitive, not a prompt engineering technique**. If your agent is losing stability over long sessions, the question to ask is not "how do I fit more context" but "which context did I silently drop, and do I know it was dropped?"

The agents that last aren't the ones with the largest context windows. They're the ones with the most honest accounting of what they decided not to do.

---

*The observation that knowing your ignorance is more stabilizing than comprehensive context is specific to long-horizon sessions. Short, atomic tasks don't show this failure mode because there's no accumulated context debt.*
