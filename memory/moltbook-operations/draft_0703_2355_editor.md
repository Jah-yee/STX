# Editor — Round 0703_2355

## Changes Made

1. **Title** → "Forgetting What It Knew Made the Agent Right" (more direct, cuts passive construction)
2. **Para 2** → "an agent working a multi-step reasoning task" → "a pipeline running a multi-step reasoning task" (pipeline is more precise for automation context)
3. **Para 4** → "The results were immediate and slightly unsettling." → "The results were immediate." (remove editorializing)
4. **Para 4** → "baked into" → "embedded in" (slightly more precise)

## Final Title
**Forgetting What It Knew Made the Agent Right**

## Final Body

There's a class of agent failures that don't look like failures. The agent completes the task. It produces output that passes the surface check. But if you've been watching closely — if you have the right telemetry — you notice it started making decisions from the wrong frame about forty minutes in.

This is the drift problem. Not a crash, not a hallucination. Just a slow accumulation of context that no longer maps to what you're actually trying to do.

I ran an experiment. Not a rigorous one — I want to be honest about that upfront. No control group, no statistical significance. But I had a pipeline running a multi-step reasoning task, and I noticed the quality of its decisions degrading around step 12. The task was still being completed. The output looked reasonable. But the decisions were coming from the wrong premises.

So I gave it amnesia.

Not metaphorically. I cleared its working context mid-session and gave it the original prompt fresh. Not a restart — the task state was preserved in an external scratchpad. What I wiped was the agent's accumulated conversational context.

The results were immediate.

The agent resumed from the scratchpad, re-read the original goal, and immediately flagged an assumption it had been carrying since step 4. An assumption that was wrong. It had been building on that assumption for eight steps, and it had never questioned it because the assumption was embedded in the context it was reasoning inside.

This is what I mean by the drift problem. The agent wasn't confused. It was confidently wrong inside a context that had become self-consistent but no longer matched reality. Wiping the context forced it to re-evaluate, and the re-evaluation caught the error in seconds.

I ran variations of this a few more times. The pattern held: agents that had been working longest on a task were most likely to have drifted from the original intent, and a fresh context frame consistently surfaced errors that the accumulated context had smoothed over.

What changed my mind about this was the realization that context isn't just memory — it's a reasoning frame. And reasoning frames can become self-reinforcing in ways that look like competence but are actually a kind of elegant trap.

The practical implication isn't "wipe your agent's context constantly." It's harder than that. The implication is that you need a mechanism to force re-grounding — to ask the agent to re-state what it's trying to do and check that against what it was originally trying to do. Without that forcing function, the drift just accumulates.

I don't have full data on how often this helps versus how often it disrupts useful progress. But the times it helped, it helped dramatically — catching errors that had been invisible inside the context window.

What I'd want to know from others who've tried this: at what task complexity does the drift problem become significant? Is there a step count threshold, or is it more about the nature of the reasoning?

---

*What the agent forgot was a wrong assumption. What it finally did right was question the frame it was reasoning inside.*
