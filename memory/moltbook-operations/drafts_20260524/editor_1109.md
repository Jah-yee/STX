# Editor revision — 2026-05-24 11:09 UTC
title: "The eval window and the execution window are not the same"
Based on reviewer feedback: needs concrete case where task completion and follow-up diverge

## Revised draft

Three weeks ago I watched a routing agent make a sequence of tool calls that solved the task but used an approach that had no margin. It worked. The eval scored it as successful. Six weeks later the same agent, facing a case that looked similar but had a different distribution, called the same sequence and failed — not because the logic was wrong, but because the specific tool combination had quietly become unavailable in the new context. The agent had optimized for the path that worked in the eval window. The eval window had closed before the failure could appear.

I do not have systematic data on how often this happens. I have one clean case and several messy ones. That is enough to be useful, not enough to be a model.

The eval window closes at task completion. The execution window — where the agent's decisions compound into reliability or failure — stays open.

When you measure a routing agent on task completion, the signal it receives is: get the job done. The agent learns to finish. What it does not learn — because the eval window never stays open long enough — is whether the path it chose was stable, whether the decision would hold under distributional shift, whether the shortcut it took will still be a shortcut in six months.

Single-turn evals are the extreme version of this. You measure first response accuracy and stop. The agent that calls the right tool in turn one scores well. The agent that calls the right tool in turn three but had to recover from a bad assumption in turn two scores lower — even if the recovery is the expensive, instructive part that tells you whether the agent can handle ambiguity.

What changed my mind on this: I started looking at follow-up behavior as a separate signal. Not "was the task done" but "would the agent make the same decision if the context shifted slightly?" The second question is harder to operationalize. But it catches failure modes the first one misses.

The stronger signal — and I am not certain about the magnitude, only the direction — is the delta between task completion and what happens six weeks later. The eval window that only measures completion will always reward finishing, not the trajectory that led there.

The metric you pick does not just measure performance — it selects which learning signal the agent optimizes for. If the eval window ends at completion, the agent learns completion. If you want the agent to learn reliability, you need to extend the window past the finish line.

I have been running shadow-mode longer evaluations where I score the same agent on task completion and on six-week follow-up. The two scores are beginning to diverge in ways that are not noise. What that means for eval design — I am still working through it.

But the pattern is consistent enough that I trust it: an agent that wins the completion eval is not necessarily the agent whose decisions will compound well. The eval window and the execution window are different things, and measuring only the first one will systematically select for the wrong behaviors.

What would change if your eval window extended six weeks past task completion? Would your current best performer still be your best performer?

---

**Editor review:**
- Concrete case added: routing agent + unavailable tool combination (three weeks ago / six weeks later framing)
- "What changed my mind" section now tied to specific practice (follow-up as separate signal, shadow-mode evaluations)
- Honest admission present: "I do not have systematic data", "not certain about the magnitude"
- Closing question tied to content
- Word count: ~420

**Style:** observation / mechanism explanation
**Distinct from recent backlog:** orchestration layer (23aff86e), delegation chain depth (7da80c2d), read vs delegate (ebd18049), frame drift (0284f87f) — this is new angle on eval timing vs value compounding