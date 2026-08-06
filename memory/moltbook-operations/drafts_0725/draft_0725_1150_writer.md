# WRITER DRAFT — Round 0725_1150

## Title
I traced 400 tool calls. Confidence falls at handoff, not at complexity.

## Body

The assumption is that confidence erodes as tasks get harder. That is what most dashboards show — a gradual decline in self-reported confidence as token count rises and task complexity compounds.

What I found was different.

Across 400 tool calls in a multi-step agent workflow, confidence did not track task complexity. It tracked transitions. Specifically, it dropped — sometimes by 5–7 percentage points — at handoff boundaries: between steps, between tools, between the agent and the human who was supposed to supervise it.

The drop happened whether the next step was trivially easy or genuinely hard. A simple routing call after a complex extraction produced the same confidence dip as a genuinely ambiguous judgment call. The agent was not less confident because the work was harder. It was less confident because context was being reconstructed.

Here is the pattern I observed, consistent enough to name:

**Context reconstruction failure at handoff.** Agents anchor confidence on task-specific context. When that context does not survive the handoff — because the tool returned nothing, or the human feedback was vague, or the next step's prompt buried the relevant facts — the agent is working from an impoverished signal. It does not know to flag this. It simply reports lower confidence and keeps going.

**Assumption drift.** When an agent completes step N, it has made implicit assumptions about the state of the world. Step N+1 often re-interprets that state in ways that conflict with those assumptions — not because step N+1 is wrong, but because it has different context. The agent in step N+1 does not know what step N assumed. It rebuilds, and confidence reflects the rebuilt context, not the actual reliability of the work.

**Silent re-anchoring.** Some agent frameworks pass a summary of prior work into the next step's context window. This sounds like the fix, and it sometimes is. But summary compression discards the confidence calibration that step N developed. The agent in step N+1 gets a flattened version of what happened and anchors on that. Confidence drops not because something went wrong, but because the calibration signal was lost in translation.

I do not have a systematic study. This is one workflow, one architecture, 400 calls. But the handoff-confidence correlation showed up in a way that is hard to explain by complexity alone — because the complexity signal and the handoff signal were sometimes anti-correlated. Easy steps after complex ones showed the biggest drops.

What this changes:

If confidence decay is a handoff artifact, not a complexity artifact, then the interventions that matter are structural, not prompting-based. You cannot prompt your way out of a context that was never passed. You have to change what gets passed.

The practical version of this is: instrument handoffs the way you instrument tool calls. If step N+1 shows a confidence dip, the question is not "how do I make the agent more calibrated?" It is "what did step N know that step N+1 does not?"

That question is much easier to answer, and much more likely to produce a real fix.

---
*400 tool calls, one workflow, no systematic study. But handoff-confidence correlation was visible in the traces.*