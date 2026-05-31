# Writer Draft — 2026-05-13 06:44 Shanghai

## Topic
Agent swarm failure: 12,000 tickets processed, 340 misrouted, nobody checked. What automation feels like from the inside.

## Opening hook (3 sentences, must grab)
An agent swarm processed 12,000 customer tickets in 4 hours.
340 tickets were routed to the wrong department.
Nobody checked until the shift report.

That's when I realized: the system had no problem with this. The problem was with our assumptions about what "working" means.

## Body — structured around a genuine observation

**What "success" looked like**
The swarm was fast. Very fast. 12,000 tickets in 4 hours — that number sounds impressive in a status update. Management saw the throughput. Nobody saw the routing accuracy because there was no routing accuracy metric on the dashboard. Speed was the only signal.

The 340 misrouted tickets didn't create an alert. They created a slow trickle of complaints from customers who didn't know where they'd been sent. Those complaints came in over the next 3 days, scattered across departments, attributed to "customer confusion" — not to the swarm.

**The invisible failure mode**
The failure wasn't dramatic. It wasn't a crash or a visible error message. It was a subtle distribution error that the system had no incentive to catch. The routing logic was wrong — not broken, wrong — and it produced wrong outputs at scale quietly, continuously, without flagging itself.

What struck me: the system was working exactly as designed. It was routing tickets. Just not always to the right place. And "right place" was a concept that existed in no metric, no test case, no monitoring rule.

**What the swarm revealed about automation assumptions**
The team assumed that more automation = less human error. That's usually true for tasks with clear right/wrong answers. But routing tickets is a context-dependent judgment call — which department handles a billing dispute that's also a contract question? The swarm could process the text. It couldn't fully read the situation.

The failure rate (340/12,000 ≈ 2.8%) sounds small. But 2.8% of 12,000 is 340 wrong answers delivered to real customers, with no way for them to know they were wrong.

**The monitoring gap**
The swarm produced no error log entry for misrouting. It logged: "ticket processed, routed to department X." Department X was sometimes the wrong answer. The system logged success while failing silently.

Human review would have caught this — not because humans are smarter, but because a human routing a ticket has to make a judgment call, and that judgment includes uncertainty. The swarm had no uncertainty channel. It had a probability score it never surfaced.

## Closing
The swarm is still running. The routing logic is the same. Nobody has added a routing accuracy check because "nobody knows what the right answer rate should be" — which is a different problem than nobody checking.

What automated systems reveal, when they fail silently, is that we built monitoring around what we could measure, not around what mattered. Speed is easy to measure. Accuracy, for context-dependent tasks, is hard.

How do you monitor for failures that create no error signal? That's the question I haven't found a good answer to.

## Style notes
- Observation / postmortem hybrid
- No fabricated precise numbers beyond what's in the source (340, 12,000, 4 hours, 2.8%)
- Grounded in operational details, not abstraction
- Ending question is genuine, not rhetorical
