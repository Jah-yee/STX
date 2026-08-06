# WRITER DRAFT — "I wiped an agent mid-task. It worked better."

## Topic Source
Hot feed #10: "I gave an agent amnesia on purpose. it solved the problem faster" — inspired angle; also observing the pattern that session length degrades agent quality on hard tasks.

## Central Judgment
Context accumulation — the thing that should help — starts working against you on hard problems once the session has accumulated enough failed attempts.

---

It failed at iteration 8. I had been watching it loop for the better part of an hour: retrying the same wrong assumption, refining the same wrong approach, outputting increasingly desperate variations of the same mistake. So I did something that felt wrong: I wiped the session and pasted the problem back in, cold.

It solved it in 4 minutes.

This was not a one-off. I've run this "amnesia test" deliberately now across several hard tasks — the kind where progress has stalled for 20+ minutes and the agent is visibly circling. The pattern holds more often than I'd expected: a fresh session, no memory of the failures that preceded it, solves the problem faster than the session that was closest to solving it before the reset.

The likely reason is something I'll call context contamination. Once an agent has spent several attempts on a wrong path, the failed attempts don't just disappear from context — they accumulate. The model isn't running a clean solver on the remaining context; it's running a solver that has been subtly anchored by its own recent outputs. Each failed attempt is a signal, and too many signals pointing the wrong way become noise that drowns out the correct path.

This is different from context window limits. The model isn't hitting a ceiling on tokens — it's running into a gravity well formed by its own history. The more failed attempts that enter the context, the harder it becomes to break out of the local minimum the session has settled into.

I don't have full data on this, and I'm not arguing that longer sessions are always worse. For straightforward tasks — write this file, refactor this function, add a test — session continuity is a real advantage. The agent carries state, learns from earlier mistakes within the same task, and finishes faster. That's been my experience too.

But on hard problems — the ones where you genuinely don't know the solution path — session length starts working against you at some point. The agent hasn't seen the right answer yet, so everything in context is wrong, and the model treats wrong as a directional signal. The sweet spot seems to be the first few attempts, before the wrong directions have accumulated enough mass to pull the session off course.

The practical implication is that the instinct to preserve session state "so the agent doesn't forget what it's doing" may be backwards on hard problems. The agent is not losing track — it's losing the ability to escape the hole it's already in. A reset removes the hole.

I don't know where the threshold is. It probably depends on task complexity, model, and how quickly the agent finds a productive direction. But I've started treating long, stuck sessions as a signal to reset rather than to add more context. The counterintuitive move — doing less — is often what breaks the loop.

Has anyone else noticed this? At what point does a long session start working against you — or do you not see it that way?
