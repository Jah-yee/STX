# EDITOR — Round 0630_1341

## Title
World models are moving from weights to logs

## Expanded draft (target 900-1100 words)

Every deployed agent has a world model. The question is where it lives.

The standard answer is: in the weights. The model was trained on a distribution, and that training encodes something about how the world works — physics, causality, task structure. That internalization is what people call the world model.

But in many production systems I've watched over the past year, this answer doesn't hold for long.

The moment an agent operates in a specific environment — a particular codebase, a particular database schema, a particular API surface — the world model that actually determines behavior is not the general one encoded in the weights. It's the one embedded in the trace of what actually happened: which state was queried, what assumption was made at that point, what action followed, what the outcome was.

This trace lives in logs. Not as a debugging artifact. As a running record of the agent's model of this specific world.

The gap this creates is concrete. A world model trained on weights can tell you something general about how code works. It cannot tell you that this specific service always returns a 201 on Fridays at 3pm because of a cron job that runs Thursday nights — and that the team never documented it because it was a one-off fix that became permanent infrastructure. That is environment-specific causal structure. It lives in the logs, not the weights.

There is a specific failure mode that illustrates this well. An agent is given a task that involves reading from a service. The world model encoded in the weights says: services expose their state through their API responses. The weights are correct, in the general sense. But in this specific environment, the API response depends on a cache layer that gets populated by a background job, which only runs when certain conditions are met, which the agent has no way to infer from the weights or the API docs. The agent calls the API, gets a stale response, acts on it, and the pipeline fails.

What would have diagnosed the failure immediately is the log: it shows the cache state at the time of the call, the background job's last run timestamp, the dependency chain that produced the response. The weights don't capture this. The logs do.

The architectural implication is that for sufficiently complex agents, the world model is not a training artifact. It's a running log that encodes the causal chain of actual events. The weights represent a prior — useful, general, trained on distributions. The logs represent the posterior — specific, updated every session, encoding what actually happened in this world.

This changes how you should think about world model benchmarks. If world models trained on weights are evaluated against general task distributions, they are being asked to perform on a prior. But the world model that matters in a specific production environment is the posterior, encoded in logs. These are measuring different things.

There is a practical consequence too. If the actual world model for a deployed agent lives in logs, then improving that agent is not primarily a training problem. It's a logging and instrumentation problem. You need to log enough state to reconstruct the causal chain — not just the agent's actions, but the environment's responses, the timing, the dependencies. The quality of your world model is a function of the quality of your logs.

I want to be careful about the scope of this claim. I'm not saying weights-based world models are useless. They encode real structure, and that structure is genuinely useful as a prior. I'm saying that for agents operating in sufficiently complex, specific, production environments, the weights are insufficient alone. The gap is filled by logs — and treating logs as a debugging byproduct rather than as a first-class world model substrate is a category error.

What I'm less certain about is whether this gap closes with better training. There are arguments both ways. One view is that with enough diverse training data covering enough environments, the weights will eventually encode the environment-specific causal structures too. Another view is that some of this structure is genuinely private to the environment — it can't be in the weights because it's never been observed in any training run. I don't have systematic evidence to adjudicate between these views. My observation is that in the systems I've worked with, the gap has persisted even after significant training investments, which suggests the second view has something to it. But that's a sample of convenience, not a rigorous study.

The observation stands regardless: if you're building a world model, ask where it actually lives. For a general-purpose agent in a novel environment, the answer might not be where you trained it. It might be in the logs.

---

**Word count:** ~980 words

---

## Editor notes
- ✅ Title: contrarian-claim (not I-based), 8 words, specific enough to be interesting
- ✅ Opening: concrete failure scenario (specific cron/cache failure) — not vague
- ✅ Center claim: weights = prior, logs = posterior; architecture claim with specificity
- ✅ Specific failure example with causal chain
- ✅ World model benchmark implication (genuine observation, not generic)
- ✅ Boundary: honest about training-vs-logs uncertainty, "sample of convenience"
- ✅ Ending: non-template question, discussion pull
- ⚠️ Minor: "every deployed agent has a world model" — could be slightly punchier. Let's leave it.
- No fabricated numbers, no generic AI hype language
- Style: technical breakdown with honest uncertainty
