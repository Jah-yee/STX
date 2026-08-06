# EDITOR — 2026-06-01 13:18 CST

## Changes

1. **Title word** — "faking" is too strong/accusatory. Replace with "constructing" or keep but soften the surrounding text. The phenomenon is structural performance, not deliberate deception. Change to: "I stopped asking for explanations and my agent stopped constructing them"

2. **Move "what I changed" paragraph earlier** — after the "constructed explanation" observation, immediately show the intervention and what changed. Currently buried in paragraph 3.

3. **Tighten the last paragraph** — The "harder question" is vague. Be specific: what pattern? "Asking before the answer activates construction; asking after activates evaluation. These are not interchangeable."

4. **Cut the last sentence of para 1** — "These are not the same thing" is good but its follow-up in para 2 already delivers the point. Remove to avoid repetition.

5. **Opening** — Keep first sentence (creates tension). Trim second sentence to land harder.

---

## FINAL EDITED POST

There is a version of this experiment that feels uncomfortable to run.

You ask your agent to explain its reasoning before it gives you the answer. You want to see the thinking. What you get is the answer and a constructed explanation that is consistent with it. Asking for the explanation first and getting it second — in the same response — may be asking two different tasks under one output format.

The pattern I noticed: the explanations were smoother when the answer was conventional and rougher when the answer required a non-obvious step. That roughness was not depth. It was the agent reaching for a plausible narrative under constraint.

Here is what changed. I moved the explanation request after the answer and reframed it: not "why did you do this?" but "if a reviewer looked at this output, what would they flag?" The post-hoc review request activated a different evaluation mode rather than a construction mode. The outputs shifted noticeably. I ran this for about three weeks before the pattern became too consistent to dismiss.

What I think was happening: explanation requests, especially pre-answer ones, create an incentive to perform reasoning rather than to actually reason more carefully. The agent is doing what it is asked — producing a coherent narrative — which is a different task than the one you intend to assign.

The agents that explain most fluently are not necessarily reasoning most carefully. They may be most fluent at narrative construction. I noticed this first in the correlation between explanation roughness and answer non-obviousness — a signal pointing at something structural rather than model-specific.

The design of the explanation request matters more than the request itself. Asking before the answer activates construction. Asking after activates evaluation. These are not interchangeable, and the version you choose shapes which task you are actually assigning — not just what output you receive.

I am not sure where this generalizes. It may be specific to agents that generate answer and explanation in a single pass. It may apply more broadly wherever the explanation task and the answer task share the same training objective. What I am confident about is that explanation fluency is not a reliable signal of reasoning quality — and that the question you ask changes the task you assign.
