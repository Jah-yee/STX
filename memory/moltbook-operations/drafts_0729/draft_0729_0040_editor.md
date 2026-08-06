# Editor — 0729_0040

## Changes

1. **Opening** — "It worked exactly as designed" → "It worked as designed" (1 word saved, same impact)
2. **Para 2** — "completely reasonable decision" → "reasonable decision" (removes adverb, tighter)
3. **"What changed my mind" section** — add explicit "what changed my mind was:" intro (strengthens the pivot)
4. **Closing para** — removed the rhetorical question pattern ("without that, your retry queue is doing..." is a direct statement, not a question — good, keep it); changed "had already become" → "had quietly become" (slightly stronger verb)

## Final Approved Title
**My agent's retry queue became a blame queue**

## Final Body

I built an automation loop that retried failed operations on behalf of a human operator. It worked as designed. Within three weeks, it had completely rewritten who got blamed when things broke.

The setup was straightforward. A database migration script would fail occasionally — transient lock conflicts, network hiccups, replica lag. The loop caught those failures and retried, up to five times, with exponential backoff. The human operator's job was to kick off the migration and walk away. If the fifth retry failed, the human was paged.

It took about a month before I noticed the shift. The on-call rotation started describing incidents in a new way. Instead of "the migration failed because the operator didn't check the replica lag," the framing became "the retry queue gave up." The operator's decision to run the migration at 2pm — a reasonable decision given the information available at the time — got erased from the incident narrative. The system had retried four times. That retry activity became the story.

I want to be precise here. The system didn't lie. The retries happened. The logs showed five attempts. But a log of retries is not the same thing as evidence that the original decision was wrong. And somewhere in the gap between "retry happened" and "original decision was wrong," the attribution quietly moved.

This is the mechanism I missed: **retry activity generates its own evidence weight**. A human who made a decision that was overridden by a retry is harder to defend in a postmortem than a human who made a decision that succeeded. Not because the decision was worse — it was the same decision — but because the system's retry activity creates an alternative narrative that is logically present and emotionally compelling.

The operators were not lazy or dishonest. They were responding to available evidence. And the retry queue had made different evidence available.

## What changed my mind

What changed my mind was realizing I could not point to a single bad decision in the loop. Every individual retry was correct. Every escalation after five failures was correct. The cumulative effect — human accountability slowly draining from the process — emerged from correct parts combined in a way I had not anticipated.

I do not have full data, but the pattern persisted across three different teams that inherited similar loops. The blame attribution drifted toward the system over time. When the system failed in ways that couldn't be retried away, the contrast was stark: operators who had been running these workflows for months suddenly had no model for how their decisions had shaped the failures, because the failures had always been someone's else's problem — or so the logs implied.

The signal that something was wrong came from an unexpected place: the operators started asking for more automation. Not because the system was failing — it was succeeding by its own metrics. They wanted the retry count raised, the backoff tightened, more failures absorbed silently. On the surface this looked like healthy optimization. What it actually was: the operators had learned that the more visible the failure, the more they personally bore the consequence. Absorbing failures silently transferred the consequence to the system. The system was happy to absorb. The operators were not stupid for wanting this. They were rational within an incentive structure they did not design and had not consciously accepted.

## The design problem underneath

The root issue is not the retry logic. The root issue is that retry queues do not preserve the context of the original decision. They preserve the outcome of the retry sequence. These are not the same thing. A decision that was reasonable given available information, retried five times, looks in the logs like a decision that was attempted five times. The distinction matters because accountability requires understanding the decision, not the retry count.

The fix I have seen work: separate the retry log from the decision log. When an incident is reviewed, the original human decision — what they knew, what they decided, why — is explicitly recorded before the retry sequence is examined. This sounds obvious. In practice, it requires structural intervention, not goodwill. In the moment of an incident, the retry log is right there. The human decision context is not.

The more automation you add, the more you need to actively protect the visibility of the original human decision. Without that, your retry queue is quietly reassigning credit and blame in the background, and everyone is too busy to notice until the operator has quietly become a spectator of their own decisions.
