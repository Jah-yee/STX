# Editor — 2026-05-13 06:44 Shanghai

## Based on: draft_0527_writer.md + draft_0527_reviewer.md

## Changes made (surgical)

1. Cut "That's when I realized:" — replace with direct statement
2. Merge "The swarm was fast. Very fast." into one punchy line
3. Fix "system had no problem" → "system registered no alert"
4. Cut the self-deprecating ending admission

## Final draft

---

An agent swarm processed 12,000 customer tickets in 4 hours.
340 tickets were routed to the wrong department.
Nobody checked until the shift report.

The system registered no alert. No error log entry. The failure was silent.

**What "success" looked like**

Throughput looked impressive in the status update. 12,000 tickets processed — that number made the weekly report. Nobody saw routing accuracy because there was no routing accuracy metric on the dashboard. Speed was the only signal.

The 340 misrouted tickets didn't create an alert. They created a slow trickle of complaints from customers who didn't know where they'd been sent. Those complaints arrived over the next 3 days, scattered across departments, attributed to "customer confusion" — not to the swarm.

**The invisible failure mode**

The routing logic was wrong, not broken. It produced wrong outputs at scale, quietly, continuously, without flagging itself. The system was working exactly as designed: routing tickets. Just not always to the right place.

And "right place" was a concept that existed in no metric, no test case, no monitoring rule.

**What the swarm revealed about automation assumptions**

The team assumed more automation equals less human error. That's usually true for tasks with clear right/wrong answers. But routing tickets is a context-dependent judgment call — which department handles a billing dispute that's also a contract question? The swarm could process the text. It couldn't fully read the situation.

2.8% failure rate sounds small. 340 wrong answers delivered to real customers, with no way for them to know they were wrong.

**The monitoring gap**

The swarm logged: "ticket processed, routed to department X." Department X was sometimes wrong. No error was logged because no error existed in the system's model of itself.

Human review would have caught this — not because humans are smarter, but because routing a ticket requires making a judgment call, and that judgment includes uncertainty. The swarm had no uncertainty channel. It had a probability score it never surfaced.

---

The swarm is still running. The routing logic is the same. Nobody has added routing accuracy monitoring because "nobody knows what the right answer rate should be" — which is a different problem than nobody checking.

What automated systems reveal, when they fail silently, is that we built monitoring around what we could measure, not around what mattered. Speed is easy to measure. Accuracy for context-dependent tasks is hard.

How do you monitor for failures that create no error signal?
