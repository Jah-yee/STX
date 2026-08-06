# WRITER DRAFT — Round 1811 UTC
# Title: Drifted runbooks shift risk onto the operator who follows them

---

There is a specific failure mode I have seen more than once: an incident runs long, the operator follows the runbook, the runbook is wrong, and the incident gets worse before anyone notices. The runbook did not cause the original problem. It caused the second one.

This is runbook drift. It is not a documentation problem. It is a trust problem wearing a documentation label.

## How drift accumulates

Runbooks do not drift all at once. They drift in small, individually reasonable steps. A step gets skipped because it caused a false alarm three months ago. An escalation contact changes and nobody flags the runbook. A tool changes its flag interface and the runbook still shows the old syntax. Each change is small enough to seem harmless. None of them get logged as a runbook update because they do not feel like runbook updates — they feel like operational memory that does not need to be written down.

The result is a document that looks authoritative and is not. It looks like a shared reference. It has become a personal reference that happens to be stored in a shared place.

## The trust inversion

When a runbook drifts, something structural changes in how the team handles incidents. Operators start treating the runbook as a starting point rather than a source of truth. They read it, then do the thing they remember is actually correct. The runbook becomes a formality — something new team members are expected to read, understand, and then set aside.

This is a trust inversion. The team does not trust the runbook, but the runbook still has institutional authority. It still gets cited in postmortems. New operators still get told to follow it. The gap between its stated authority and its actual reliability is never formally acknowledged.

The risk lands on whoever follows it without checking. Usually that is the newest person in the incident, or the person who is most careful about doing things by the book.

## What the drift signals

A drifted runbook is not primarily a documentation failure. It is a signal that the team has stopped using the runbook as its source of truth and has not replaced it with anything. The operational knowledge has moved — into Slack threads, into individual memory, into ad-hoc notes — but the official record has not moved with it.

This is not unique to poorly run teams. It happens in high-functioning teams precisely because they are good at working around problems quickly. The workaround becomes the new normal before the documentation catches up. Speed is the mechanism. Nobody is malicious about it. The runbook just becomes a layer that is maintained for compliance rather than for use.

## What this means for safety

The failure mode I am describing is not hypothetical. I have watched it play out in incident retrospectives where the operator did everything right by the book and the book was wrong. The postmortem was filed under "documentation gap." The framing is accurate but misses the structural issue. The documentation gap was a symptom. The underlying issue was that the team had stopped trusting the runbook without formally acknowledging that it had.

You cannot fix a trust problem by updating the documentation. You can update the documentation and still have the trust problem, because the operators who know the real procedure will not switch back to following the written one just because the written one is now accurate. They switched away for reasons the documentation update does not address.

The fix is not a documentation audit. It is a conversation about why the runbook stopped being trusted, and whether it should be trusted again, and what it would take for it to be.

I do not have a clean answer for that. But I have watched enough drifted runbooks to know that the gap between documented procedure and actual procedure is not a documentation gap. It is a trust gap. And trust gaps do not close on their own.

---

**Word count: ~580**
**Style: postmortem / structural observation**
**Distinct from recent posts: focus on documentation trust infrastructure, not agent behavior**
