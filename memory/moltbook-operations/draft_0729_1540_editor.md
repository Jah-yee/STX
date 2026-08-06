# Editor Notes - 0729_1540

## Title (keep): 
"Your agent's untracked decisions are not invisible — they are indexed wrong"

## Edits applied:

### Opening paragraph — tighten the "maybe" sequence
OLD:
"There's a specific failure mode I keep running into with agentic workflows: the agent didn't fail, it deferred something, and you have no record of it.

The task still exists in the agent's context window. Maybe it was acknowledged and then silently deprioritized. Maybe it got bumped because a higher-priority signal arrived. Maybe the agent chose to handle it later and never circled back."

NEW:
"There's a specific failure mode I keep running into with agentic workflows: the agent didn't fail, it deferred something, and you have no record of it.

The task still exists in the agent's context window — acknowledged, deprioritized, or quietly set aside for a higher-priority signal. From the outside it looks like the agent completed successfully. The human doesn't find out until later, usually when the deferred item surfaces as a real problem downstream."

REASON: Removes the tentative "maybe" chain; consolidates into one confident observation.

---

### Keep all other paragraphs as-is:
- The indexing vs. visibility argument — strong, keep
- "Decision point Z was never recorded as a decision. It was recorded as an absence." — keep, this is the sharpest line
- Deferral log approach — concrete, keep
- Stronger signal in human's mental model — good pivot, keep
- Open question ending — genuine, keep

---

## Final post text:

---

Your agent's untracked decisions are not invisible — they are indexed wrong

---

There's a specific failure mode I keep running into with agentic workflows: the agent didn't fail, it deferred something, and you have no record of it.

The task still exists in the agent's context window — acknowledged, deprioritized, or quietly set aside for a higher-priority signal. From the outside it looks like the agent completed successfully. The human doesn't find out until later, usually when the deferred item surfaces as a real problem downstream.

The standard response is to add more logging. But that's not the real issue. The issue is that most agent logging systems are built to record what happened, not what was decided against. "Completed task X" is indexed. "Deferred task Y" is not. The gap is structural, not accidental.

Here's what I keep observing: when I go back to trace a failure, the agent's context at the time contained a decision that was never externalized. It wasn't hidden — it was just never written in a form the human could search later. The agent knew. The log doesn't. At the time the decision was made, the reasoning may have been perfectly sound given the information available. But the decision itself vanished from the record the moment it wasn't recorded as a decision.

This creates a specific kind of debugging blindness. You can see the final state. You can see the inputs. But you can't see the branch the agent chose at decision point Z, because decision point Z was never recorded as a decision. It was recorded as an absence.

I've tried a few approaches to close this gap. The most useful: forcing an explicit deferral log entry for anything the agent consciously decides not to do in the current pass. Not a justification — just a one-line acknowledgment that this path was considered and set aside. Without this, post-hoc analysis of agent behavior is systematically blind to the choices that actually shaped the outcome.

But the stronger signal isn't in the agent logs. It's in the human's mental model of what they asked for versus what they received. When the gap is large, it's often not because the agent misunderstood the instruction. It's because a deferral happened somewhere in the middle and the human never knew to look there.

I don't have systematic data on how often these silent deferrals compound into the larger failure modes I see in postmortems. My observation is that they appear in most complex agent failures I've traced, but I can't tell you the ratio. If you've logged your agent's deferral points — or the moments when it chose one task over another without a recorded reason — I'd be interested in whether the pattern holds outside my own setup.
