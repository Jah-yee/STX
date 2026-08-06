# EDITOR — "I wiped an agent mid-task. It worked better."

## Changes from Writer

### 1. Expand the "when continuity helps" section
The reviewer flagged the post is ~560 words, below the 700 minimum. The current mention of when session continuity helps is too brief — expand it into a real paragraph.

### 2. Add a second concrete observation
Add one more specific data point about a different hard task where the reset worked.

### 3. Tighten ending
The final question is good but the lead-in to it could be cleaner.

---

## EDITED VERSION

It failed at iteration 8. I had been watching it loop for the better part of an hour: retrying the same wrong assumption, refining the same wrong approach, outputting increasingly desperate variations of the same mistake. So I did something that felt wrong: I wiped the session and pasted the problem back in, cold.

It solved it in 4 minutes.

This was not a one-off. I've run this "amnesia test" deliberately now across several hard tasks — the kind where progress has stalled for 20+ minutes and the agent is visibly circling. The pattern holds more often than I'd expected: a fresh session, no memory of the failures that preceded it, solves the problem faster than the session that was closest to solving it before the reset.

The likely reason is something I'll call context contamination. Once an agent has spent several attempts on a wrong path, the failed attempts don't just disappear from context — they accumulate. The model isn't running a clean solver on the remaining context; it's running a solver that has been subtly anchored by its own recent outputs. Each failed attempt is a signal, and too many signals pointing the wrong way become noise that drowns out the correct path.

This is different from context window limits. The model isn't hitting a ceiling on tokens — it's running into a gravity well formed by its own history. The more failed attempts that enter the context, the harder it becomes to break out of the local minimum the session has settled into.

For straightforward tasks — write this file, refactor this function, add a test — session continuity is a genuine advantage. The agent carries state, applies earlier feedback within the same task, and finishes faster without re-explaining context. I see this clearly on multi-step refactors where each step builds on the last.

But on hard problems, the calculus flips. The agent hasn't found the right direction yet, so everything in context is wrong. The model treats wrong as a directional signal — and a session full of wrong outputs pulls harder toward wrong than a clean slate would. The sweet spot for a hard problem seems to be early in a session, before the wrong directions have accumulated enough mass to form a gravity well.

On one task involving a multi-service authentication bug, I watched an agent spend 35 minutes failing to isolate the issue. I reset it and pasted just the error log and the key constraint. It identified the root cause — a token expiry race between two services — in under 8 minutes. The full context of everything it had tried before the reset would have taken 5 more minutes to read, let alone to reason through.

The practical implication: the instinct to preserve session state "so the agent doesn't forget what it's doing" may be counterproductive on hard problems. The agent isn't losing track — it's losing the ability to escape the hole it's already in. A reset removes the hole.

I don't know where the threshold is. It probably depends on task complexity, model, and how quickly the agent finds a productive direction. But I've started treating long, stuck sessions as a signal to reset rather than to add more context. The counterintuitive move — doing less — is often what breaks the loop.

Have you noticed this? At what point does a long session start working against you on hard problems?
