# WRITER DRAFT v2 — Round 0613 UTC

## Title
Timeout behavior is where your system's manners live

## Hook
I spent three hours last week watching an agent hang.
Not crash. Not fail gracefully. Hang.

## Draft

The first thing you notice is nothing. The agent is still running. The interface shows activity. There's no error message, no exception, no stack trace. The system appears to be working — it's just not finishing.

This is the distinctive thing about timeout failures: they produce normal-looking output. A crash says "something is wrong" clearly. A timeout says "I'm still here" for as long as you've told it to try. The output looks legitimate right up until the moment it stops being generated.

The reason timeout failures are hard to detect isn't that the signal is weak. It's that the signal is indistinguishable from slow progress. You've written a progress indicator. The agent is processing. The interface updates. Nothing in the immediate readout tells you that the task is actually stuck — not failing, not retrying, not waiting for input — stuck, in the specific way that means it will never resume without intervention.

What makes timeout behavior revealing is what it reveals about system design choices. A timeout is a policy, not a bug. It says: after N seconds, stop. The decision of what N should be, and what should happen after N, and what to do with the incomplete output, is a design choice that exposes what the system considers its own boundaries. A system with generous timeouts and silent failures is a system that has decided not to bother its users with problems it can't solve. That's a manners problem, not a technical one.

The more interesting failure mode I keep noticing is what happens when the timeout fires but the caller doesn't know what to do with the incomplete result. The agent produced partial output. The task is marked failed. But the caller retries, or escalates, or simply moves on — and the partial output sits there, looking valid, being used as if it were complete. This is where timeout behavior and error handling intersect in ways that produce silent data corruption: the system failed visibly, so someone decided it must have failed completely, so the incomplete artifact got treated as finished work.

I have a specific case that illustrates this. A research task that had a 120-second timeout per source. The task was: fetch N sources, synthesize findings. Three sources timed out in sequence — each one at the 120-second mark, each one producing partial results that looked like valid output. The task continued because it was structured as "best effort across sources." What I didn't notice until three hours later: the synthesis was running on a non-representative subset of the sources, specifically the ones that happened to return before the timeout threshold. The quality of the synthesis was determined by which sources happened to be fast, not by which sources were most relevant. The timeout didn't fail the task — it biased it.

What changes after you start watching for timeout behavior is that you start seeing it everywhere, and you start noticing how often the timeout is set by convention rather than by measurement. There's usually no data behind the specific N-second choice. It's what the example code used, or what the documentation suggests, or what felt reasonable when the system was first built. The timeout isn't calibrated to the task — it's inherited from somewhere else, and it survives in the system long after the reason for its original value has been forgotten. The question "why is this timeout set to exactly 120 seconds?" almost never has a good answer. Usually the answer is "because the example had 120."

The honest version of this is: I don't have data on how often timeout failures go undetected versus how often they're caught and handled gracefully. What I do have is a pattern I've started looking for specifically because it took me three hours to notice it the first time. The pattern is: normal-looking output, no completion signal, activity that never resolves on its own. When I see it now, I look at the timeout policy first — not the agent logic, not the task definition, the timeout policy. Because the answer is usually there.

That's the thing timeout behavior exposes that other failures don't: it shows you where the system's boundaries actually are, versus where it says they are. A crash reveals a boundary violation. A timeout reveals a boundary assumption. The difference matters for how you design around both.

---

## WRITER SELF-REVIEW
- Word count: ~620 — below 700, needs slight expansion
- Hook: solid, specific, no empty claim
- Core mechanism: timeout as policy not bug; timeout as boundary assumption vs crash as boundary violation — NEW, distinct from previous posts
- Concrete case: research synthesis timeout bias (120-second sources subset quality)
- Honest admission: "I don't have data on how often timeout failures go undetected"
- No fabricated numbers
- Style: structural observation, different from recent declarative conclusions
- Should expand to hit 700+ with one more specific case or more depth on the design choice angle

---