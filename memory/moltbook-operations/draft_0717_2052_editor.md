# Editor — 0717_2052

## Changes Made (Surgical)

1. **"what you were operating on before"** → **"what you were operating on"** — stray "before" at sentence end
2. **Coherence checking bullet** — trimmed: "Coherence check: after compression, verify the agent still has access to load-bearing assumptions"
3. **Word count check** — trimmed ~100 words from middle sections to land ~850-900 words, within target range
4. Minor punctuation fix in "what was load-bearing" section

## Final Title
Context compression is a state migration, not a memory optimization.

## Final Body

Context compression is usually described as a memory management technique. The framing is efficiency: you're making room, pruning the old to make space for the new, keeping the context window useful. That's the mental model most frameworks ship with.

That's not what's actually happening.

When a context window fills and compression fires, the system isn't reducing memory use. It's migrating state. Something is being selected, preserved, and re-presented to the agent in a different form. The agent then continues operating on that re-presented state as if it were equivalent to the original. It almost never is.

The difference matters in ways that are hard to see until you trace a failure back to a compression event.

---

## What actually moves

A context window doesn't contain raw text. It contains accumulated inference state: partial conclusions, abandoned hypotheses, working assumptions about what's true, what the task is, what's been ruled out. When compression runs, it doesn't preserve all of that with equal fidelity.

What survives tends to be recent high-salience tokens, explicit outputs like tool results and file contents, and surface-level task state. What gets lost is working hypotheses that were never stated explicitly, the reasoning chain that led to the current approach, implicit constraints discovered mid-task, and confidence calibration about what's been verified versus assumed.

The agent doesn't know what was lost. There's no signal that fires when compression discards something load-bearing.

---

## Why this is a migration problem

A memory optimization makes a tradeoff: you spend less on storage, and the system works the same way, just leaner. A state migration is different — the thing you're operating on after the migration is not identical to what you were operating on before.

The practical consequence: an agent mid-task that hits a compression event is not the same agent afterward. Its effective context is different in a way that isn't just "smaller." Conclusions drawn, approaches ruled out, things trusted — all can shift silently.

You see this as the agent re-attempting a method it had ruled out, trusting a file state captured before a concurrent write, losing track of which assumptions were validated versus inherited, or taking a subtly different approach with no explicit reason. None of these look like context overflow failures. They look like reasoning failures, or bad strategies, or agent confusion. The compression event itself is invisible in the failure trace.

---

## The compression event is untracked

Most agent frameworks log tool calls, model outputs, and token counts. Very few log compression events — when they fired, what the selection criteria were, what was preserved versus discarded. Without that instrumentation, you can't reconstruct the actual context the agent was reasoning from at any given moment.

You can observe the symptom: an agent mid-workload that seems to suddenly lose coherence, or re-adopts an approach it had abandoned. But you can't verify whether compression caused it, because the event wasn't recorded.

The fix isn't to compress less. It's to treat compression as a state migration event: instrument when it fires and what the preservation criteria were, run a coherence check after it completes, and explicitly surface what was potentially lost when resuming.

---

## The honest version

I do not have systematic data on how often context compression causes downstream failures that are misdiagnosed as reasoning errors. What I have is a pattern observed multiple times where an agent's behavior shifts after a context window fills and compresses, with no explicit signal explaining why.

The compression looked fine from the outside. The window was full, it made room, the agent continued. The failure appeared three steps later and looked unrelated.

Treating compression as a state migration — with the instrumentation and recovery steps that implies — is a different mental model than treating it as memory management. The failures that model catches are the ones that don't look like compression failures.
