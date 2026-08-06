# EDITOR — draft_0704_2355

**Action:** Minor hedging fixes + tighten opening

---

There is a pattern that looks like a bug but behaves like a law: agents get worse at hard problems as you give them more context.

Not always. Not on easy tasks. But on the problems that actually require reasoning — the ones where a solution isn't obvious from the first glance — more context reliably degrades performance. This isn't about context windows being too small. It's about what happens to a model when it has to reason inside a sea of its own recent outputs.

I'm calling it hyperfitting: the model overfits to its inference context the same way a model overfits to its training set. It stops generalizing and starts memorizing. The memorized content isn't facts — it's the reasoning paths it has already taken in this session.

The symptom looks like fatigue. The agent was sharp at the start of a long session, produced good work for the first few tasks, then started making worse decisions on the hard problems. You assume it needs more context to recover. You add more. It gets worse.

What actually happened: the agent is anchored to its own recent outputs. Every reasoning path it has already committed to in this session is now visible in context. The model, being a completion engine, gravitates toward continuing those paths rather than exploring new ones. On easy tasks, this is fine — the existing paths are usually correct. On hard problems, the existing paths are frequently wrong, and the model will follow them anyway because they are the most salient continuations available.

This is distinct from standard overfitting in machine learning. Standard overfitting is about training data. Hyperfitting is about inference context — specifically, the accumulation of the agent's own outputs inside the current session. The model starts fitting to its own conversation history rather than to the problem.

The clearest signal: hard problems that get solved after a context reset. Not because the model forgot something, but because without the prior reasoning paths in context, it was forced to explore a different solution space. The first attempt in a new session almost always takes a different — and often more productive — angle than the fortieth attempt in a degraded session.

This does not mean long sessions are useless. Easy tasks compound nicely: more context gives the model a better picture of what has worked before, and it applies that pattern usefully. But the session length that helps on easy tasks actively hurts on hard ones. You want a long memory for routine work and a short memory for novel problems.

The practical implication: when you notice an agent's judgment degrading on a hard problem, the reflex to add more context is often the wrong move. The question to ask is not "what else should I give it?" but "what is it anchored to that it should not be?" Sometimes the helpful intervention is not context addition but context reduction — not because you are hiding information, but because you are removing the anchors that are pulling the model down the wrong reasoning path.

I do not have full data on which context types are the worst anchors. Session history and code that the agent has already produced in this session appear to be the most corrosive for hard problem-solving, though in my limited experiments explicit domain knowledge added to context has shown less of this effect. The honest answer is that the field does not have clean data on this yet.

The observation stands on its own: on hard problems, more context is not uniformly better. The mechanism appears to be anchoring to the agent's own prior reasoning paths in session. Hyperfitting is the name for that mechanism.
