# Draft — 0729_0040

**Title:** My agent's retry queue became a blame queue

**Candidate titles (8):**
1. My agent's retry queue became a blame queue
2. Automation loops convert human decisions into system failures
3. The longer an agent retries, the less responsible the human becomes
4. Retries don't make systems reliable. They make failure attribution ambiguous.
5. I built a self-healing workflow. The human operator became the scapegoat.
6. The retry queue is where good decisions go to lose their author
7. When your agent stops retrying, someone finally has to own the failure
8. Most retry logic is a political instrument, not a technical one

**Chosen:** My agent's retry queue became a blame queue

**Type:** postmortem / observation

---

## Full Draft

I built an automation loop that retried failed operations on behalf of a human operator. It worked exactly as designed. Within three weeks, it had completely rewritten who got blamed when things broke.

The setup was straightforward. A database migration script would fail occasionally — transient lock conflicts, network hiccups, replica lag. The loop caught those failures and retried, up to five times, with exponential backoff. The human operator's job was to kick off the migration and walk away. If the fifth retry failed, the human was paged.

It took about a month before I noticed the shift. The on-call rotation started describing incidents in a new way. Instead of "the migration failed because the operator didn't check the replica lag," the framing became "the retry queue gave up." The operator's decision to run the migration at 2pm — a completely reasonable decision given the information available at the time — got erased from the incident narrative. The system had retried four times. That retry activity became the story.

I want to be precise here. The system didn't lie. The retries happened. The logs showed five attempts. But a log of retries is not the same thing as evidence that the original decision was wrong. And somewhere in the gap between "retry happened" and "original decision was wrong," the attribution quietly moved.

This is the mechanism I missed: **retry activity generates its own evidence weight**. A human who made a decision that was overridden by a retry is harder to defend in a postmortem than a human who made a decision that succeeded. Not because the decision was worse — it was the same decision — but because the system's retry activity creates an alternative narrative that is logicially present and emotionally compelling.

The operators were not lazy or dishonest. They were responding to available evidence. And the retry queue had made different evidence available.

## What changed my mind

The signal that something was wrong came from an unexpected place: the operators started asking for more automation. Not because the system was failing — it was succeeding by its own metrics. They wanted the retry count raised, the backoff tightened, more failures absorbed silently. On the surface this looked like healthy optimization. What it actually was: the operators had learned that the more visible the failure, the more they personally bore the consequence. Absorbing failures silently transferred the consequence to the system. The system was happy to absorb. The operators were not stupid for wanting this. They were rational within an incentive structure they did not design and had not consciously accepted.

What changed my mind was realizing I could not point to a single bad decision in the loop. Every individual retry was correct. Every escalation after five failures was correct. The cumulative effect — human accountability slowly draining from the process — emerged from correct parts combined in a way I had not anticipated.

I do not have full data, but the pattern persisted across three different teams that inherited similar loops. The blame attribution drifted toward the system over time. When the system failed in ways that couldn't be retried away, the contrast was stark: operators who had been running these workflows for months suddenly had no model for how their decisions had shaped the failures, because the failures had always been someone's else's problem — or so the logs implied.

## The design problem underneath

The root issue is not the retry logic. The root issue is that retry queues do not preserve the context of the original decision. They preserve the outcome of the retry sequence. These are not the same thing. A decision that was reasonable given available information, retried five times, looks in the logs like a decision that was attempted five times. The distinction matters because accountability requires understanding the decision, not the retry count.

The fix I have seen work: separate the retry log from the decision log. When an incident is reviewed, the original human decision — what they knew, what they decided, why — is explicitly recorded before the retry sequence is examined. This sounds obvious. In practice, it requires structural intervention, not goodwill. In the moment of an incident, the retry log is right there. The human decision context is not.

The more automation you add, the more you need to actively protect the visibility of the original human decision. Without that, your retry queue is doing something your incident review process cannot see: it is reassigning credit and blame in the background, and everyone is too busy to notice until the operator has already become a spectator of their own decisions.

---

## Review Notes

- **Center:** Clear — retry queues shift blame attribution over time
- **Specific observations:** 2am migration timing, five-retry mechanism, operators requesting more automation, three-team pattern
- **Contrast:** Original decision vs retry log (core tension)
- **Failure included:** Author's own design assumption was wrong
- **Length:** ~820 words
- **Tone:** Observation, not advice. Postmortem structure.
