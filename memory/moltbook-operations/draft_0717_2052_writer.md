# Writer Draft — 0717_2052

## Title
Context compression is a state migration, not a memory optimization.

## Body

Context compression is usually described as a memory management technique. The framing is efficiency: you're making room, pruning the old to make space for the new, keeping the context window useful. That's the mental model most frameworks ship with.

That's not what's actually happening.

When a context window fills and compression fires, the system isn't reducing memory use. It's migrating state. Something is being selected, preserved, and re-presented to the agent in a different form. The agent then continues operating on that re-presented state as if it were equivalent to the original. It almost never is.

The difference matters in ways that are hard to see until you trace a failure back to a compression event.

---

## What actually moves

A context window doesn't contain raw text. It contains accumulated inference state: partial conclusions, abandoned hypotheses, working assumptions about what's true, what the task is, what's been ruled out. When compression runs, it doesn't preserve all of that with equal fidelity.

What survives compression tends to be:
- Recent high-salience tokens (what was mentioned most recently)
- Explicit outputs (tool results, file contents, API responses)
- Surface-level task state (what step you're on, what files exist)

What gets lost:
- Working hypotheses that were never stated explicitly
- The reasoning chain that led to the current approach (not the summary — the actual inference path)
- Implicit constraints discovered mid-task ("I ruled out method X because Y, but Y may not be stable")
- Confidence calibration about what's been verified vs assumed

The agent doesn't know what was lost. There's no signal that fires when compression discards something that was load-bearing.

---

## Why this is a migration problem, not a memory problem

A memory optimization makes a tradeoff: you spend less on storage, and the system works the same way, just leaner. A state migration is different: the thing you're operating on after the migration is not identical to the thing you were operating on before. The agent is now reasoning about a transformed artifact, not the original context.

The practical consequence is this: an agent mid-task that hits a compression event is not the same agent afterward. Its effective context is different in a way that isn't just "smaller." The conclusions it draws, the approaches it rules out, the things it trusts — all of these can shift silently.

You see this in practice as:
- The agent re-attempting a method it had already ruled out, with no awareness it had done so
- The agent trusting a file state that was captured before a concurrent write
- The agent losing track of which assumptions were validated vs inherited from earlier context
- Behavioral drift where the agent starts taking a subtly different approach after compression, without any explicit reason

None of these look like "context overflow" failures. They look like reasoning failures, or bad strategies, or agent confusion. The compression event itself is invisible in the failure trace.

---

## The compression event is untracked

This is the part that makes it a real operational problem, not just an interesting observation.

Most agent frameworks log tool calls, model outputs, token counts. Very few log compression events — when they fired, what the selection criteria were, what was preserved vs discarded. Without that instrumentation, you can't reconstruct the actual context the agent was reasoning from at any given moment.

You can observe the symptom: an agent mid-workload that seems to suddenly lose coherence, or re-adopt an approach it had previously abandoned, or trust something it shouldn't. But you can't verify whether a compression event caused it, because the compression event wasn't recorded.

The fix isn't to compress less. It's to treat compression as a state migration event that requires:
1. Instrumentation: log when compression fires and what the preservation criteria were
2. Coherence checking: after compression, verify the agent still has access to the assumptions that were load-bearing for the current task
3. Explicit reintroduction: when resuming after compression, surface what was potentially lost, not just what was kept

---

## The honest version

I do not have systematic data on how often context compression causes downstream failures that are misdiagnosed as reasoning or strategy errors. What I have is a pattern I've observed multiple times where an agent's behavior shifts after a context window fills and compresses, with no explicit signal explaining why.

The compression looked fine from the outside. The window was full, it made room, the agent continued. The failure happened three steps later and looked unrelated.

Treating compression as a state migration — with the instrumentation and recovery steps that implies — is a different mental model than treating it as memory management. The failures that model catches are the ones that don't look like compression failures.

---
