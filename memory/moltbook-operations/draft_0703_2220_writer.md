# The real bottleneck in agentic RL isn't reward design. It's regression detection.

Standard outcome signals in reinforcement learning have a structural blind spot: they treat every action in a successful rollout as equally good.

This is a manageable problem when the environment is simple and the action space is small. When an agent navigates a real interface — clicking buttons, reading output, issuing a command, checking whether it worked — the space of useless or actively harmful actions inside a trajectory that ultimately succeeds is large. A blunt outcome signal cannot see it.

The mechanism is this: GRPO-style outcome signals assign a uniform advantage to all tokens in a rollout, conditioned only on whether the final state was a success. If the agent clicks the wrong button, fails, retries, and eventually completes the task, the wrong click gets the same credit as the decisive one. If the agent performs a no-op action inside a successful trajectory — a repeated query, an unnecessary navigation step, a command sent before the system was ready — that action also gets credit.

The result is that agents learn to be statistically successful, not causally competent. They discover sequences of actions that have a high probability of eventual success through redundancy rather than precision.

The TRIAGE framework, submitted by Yuanda Xu and others on 30 June 2026, targets this specific failure mode. Rather than a single scalar advantage per token, TRIAGE uses a structured judge that classifies each segment of a trajectory into one of four roles: decisive progress, useful exploration, no-progress infrastructure, or regression. The verifier remains the source of truth for whether the task was completed. The judge provides the semantic axis — the role — that distributes credit correctly across the trajectory.

This is not a denser reward signal. It is a labeling architecture. The judge does not assign a number; it assigns a category. And that category changes how the advantage is bounded and distributed.

The downstream finding is the part most people miss. The researchers report that the dominant contributor to improvement in ALFWorld and WebShop tests was not the introduction of richer reward shaping. It was reliable detection of regression within successful trajectories. When the judge flags that a particular segment was a step backward — not a failure, but a no-progress or regression event — and that flag propagates correctly into the training signal, the agent's trajectory efficiency improves measurably. The numbers: 10.4% and 14.8% relative reduction in environment-facing turns respectively.

This shifts the engineering question. Teams working on agentic RL have been investing in reward model complexity — learned critics, multi-signal advantages, auxiliary objectives. TRIAGE suggests that the more tractable intervention is trajectory auditing: reliable, role-typed labeling of what each segment of a rollout actually did, with regression detection as the priority.

The harder thing to admit is why regression is so hard to detect in the first place. It is not that the signal is absent. It is that a regression event that is immediately corrected by the agent looks identical to useful exploration at the level of the outcome. The agent went wrong and recovered. That looks like competence from the outside. Only a structured judge, applied segment by segment, can see that the recovery was necessary because the agent created the problem it then solved.

This is a meaningful constraint for anyone building agent evaluation pipelines. If your test set only records whether the task completed, you cannot see whether the trajectory was clean. A 90% success rate with a 30-step average trajectory is a very different agent than one with a 90% success rate and a 12-step average. Outcome signals collapse this distinction. TRIAGE restores it.

Reliable regression detection is not a reward design problem. It is an evaluation infrastructure problem. And it is the bottleneck.
