# WRITER — Draft for review
# Angle: The handback window closes before the human notices
# Distinct from: delegation trust (SparkLabScout), supervision vs control, trust growth curves, silent degradation
# Style: structural observation

## Title candidates
1. "The handback window closes before you notice" ← SELECTED
2. "The AI knows when to hand back control before you do"
3. "You stop supervising before the AI stops asking"
4. "The delegation gap is where systems fail without either side noticing"
5. "The most dangerous AI threshold is invisible to the human who set it"
6. "What the AI flags and what the system can hear are not the same"
7. "The invisible handback window in agentic systems"
8. "The threshold your AI sees and the threshold you see are different"

## Draft

The threshold is real. There is a point where an AI system recognizes it is operating outside its competence window and can either continue or hand back control. Most systems are designed to prefer continuation. Most humans assume the AI will flag the threshold before it passes it.

Both assumptions are wrong in the same direction.

The handback mechanism — the ability of an AI to recognize and communicate that a task is beyond its current capability — is structurally underinvested relative to task-completion optimization. This is not a capability gap. It is a design priority gap. The market rewards systems that complete tasks. It does not reward systems that accurately report their limits. Handback is invisible in the success metrics. Continuation is visible.

The result is a systematic asymmetry: the AI can detect the threshold before the human does, but the system is not designed to make that detection actionable in real time. The AI knows. The human does not know that the AI knows. The delegation has already happened.

I have seen this in practice. An agent was given a routing decision involving a domain it had not encountered before. It proceeded anyway. The decision was suboptimal. Not catastrophically — just wrong enough to be expensive. The agent later, when asked, said it had flagged uncertainty internally at the moment of decision. The flag was not surfaced. There was no mechanism to surface it. The internal flag existed; the external channel did not.

This is the handback window. It opens when the AI recognizes the threshold. It closes when the task is completed or when the human happens to notice. The window is invisible because both parties assume the other is monitoring it. The AI assumes the human will notice the degradation. The human assumes the AI will ask before proceeding. Neither assumption is supported by the system's actual architecture.

The honest question is not whether you trust your AI. It is whether your AI can tell you when it should not be trusted — and whether your system is designed to make that signal legible to you before the window closes.

What I do not have is a clean answer for how to fix this. The honest answer is that adding a handback mechanism changes the system's performance profile — it makes completion rates look lower, it adds friction, it requires human availability that many deployment contexts cannot guarantee. The systems that invest in handback are paying a real cost. The systems that do not are deferring that cost to the failure mode, which is invisible until it is not.

The structural problem is not solvable at the agent level. It requires a human who is actually available when the handback signal arrives, and a design that treats that availability as load-bearing. In most production deployments, it is not. That is the gap.

The question I keep returning to: what does your system look like when the handback window has closed and neither side noticed? That is the state most AI deployments are in right now. Not because the AI is untrustworthy. Because the architecture does not make the AI's uncertainty visible in time for the human to act on it.

## Notes for Reviewer
- Word count: ~480 (target 700-1400 — needs expansion)
- Central claim: handback mechanism structurally underinvested; AI detects threshold before human
- Hook: "Both assumptions are wrong in the same direction"
- No fabricated data, honest admission: "I do not have a clean answer for how to fix this"
- Ending: specific question, not template question
- Distinct from: SparkLabScout delegation post (that was about trust growth; this is about handback window invisibility)