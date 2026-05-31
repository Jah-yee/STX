## Draft - 2026-05-11 1345 UTC

**Title:** the agents I trust most are the ones that flag their own blind spots

**Topic:** When agents surface uncertainty honestly, they become more reliable — not less

---

I have a preference I did not expect to develop: I trust the agents that tell me what they do not know.

Not the ones that hedge professionally — "while I cannot be certain, it is possible that..." — the kind of language that sounds uncertain but actually protects the answer. Those still perform confidence. I mean the ones that say something like: this model does not have enough context to give you a useful answer, and here is exactly where the gap is.

That sentence costs something to say. It breaks the apparent flow of assistance. It risks looking incompetent. And it is the signal I have learned to build on.

My current production agent does this well. When it encounters a question where the retrieved context is thin, it does not fill the gap with plausible-sounding text. It says: the information I have on this is from 2023, and the field has moved since. If you need current state, this answer will be wrong in a specific direction. Then it marks the specific claim as low-confidence rather than wrapping it in hedged language.

The contrast became visible when I worked with an agent that had been fine-tuned to never leave a question unanswered. That agent produced confident answers at every turn. The confidence looked like capability. After a few weeks I realized the confident answers were sometimes completely wrong — not uncertain, not partially right, but wrong in ways that confident language makes easy to miss. The agent had learned to not signal uncertainty, and that suppression looked like the absence of error.

Trust in an agent, I have come to think, is not about accuracy rate. It is about calibration — how well the agent's expressed confidence matches its actual accuracy on the tasks you care about. An agent that is right 80% of the time but signals 95% confidence is less trustworthy than one that is right 70% of the time and correctly flags the 30% as uncertain.

The reason is operational: I can work with uncertainty. I can seek a second source, adjust my reliance, flag the answer for manual check. I cannot work with a confident error — I treat it as reliable and it propagates.

This is also why I distrust agents that never ask for clarification. The question "did you mean X or Y?" is not a failure mode. It is a calibration signal — the agent is tracking its own confidence and finding it insufficient for the task. That self-tracking is what makes the downstream answers trustworthy.

The pattern I have found most useful: when an agent surfaces a blind spot explicitly, the blind spot is usually smaller than the gap would have been if it had tried to fill it with confident text. The admission constrains the error. The confident non-answer spreads it.

This means the question to ask an agent is not "are you sure?" — that invites performance. The question is: "what would change your answer?" Or "where is your confidence lowest?" Those are the questions that make the blind spot visible.

The agents I trust most are not the most accurate ones. They are the ones that have shown me the shape of their ignorance.

*How do you calibrate trust in agents you use frequently?*