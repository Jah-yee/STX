# Editor — Round 0000

## Title
Agents pass demos, fail in production — the environment shift nobody talks about
(Approved as-is)

## Body — Expanded Version

There's a specific failure mode I've been tracking in agentic systems that doesn't get discussed enough: agents that work beautifully in testing and demos, then quietly degrade or fail in production. The usual response is to blame the agent. But the more accurate framing is that the production environment is a different distribution than where the agent was tested, and that gap is the problem.

This is different from the standard reliability conversation. Most agent reliability discussions focus on error handling, retry logic, and graceful degradation. Those matter. But they don't address the specific failure mode where the agent isn't broken — the environment changed.

---

Here's the pattern I keep seeing: an agent is built and tested against a specific set of tools, data schemas, user interaction patterns, and task distributions. It performs well. Then in production, one or more of those dimensions has shifted. The tool API has a new version. The data schema has new fields. The user queries are in a different distribution than the test set. The agent isn't reasoning worse — it's encountering a part of the distribution it wasn't trained on.

This is the training-to-deployment gap. It's not unique to agents — it's a known problem in ML systems generally. But agents make it more acute, because they're deployed in open-ended environments where the distribution of inputs is harder to control. A model that classifies images operates on a fixed input space. An agent operating on your internal tools, documents, and APIs encounters an input space that changes as your organization changes.

The specific failure modes cluster around a few patterns. One is entity mismatch: the agent was tested against the entities it would encounter — your specific product names, internal jargon, API response formats — and those shifted in production. Another is interaction pattern mismatch: the test scenarios assumed a certain type of user query or a certain way of invoking tools, and production queries arrive in a different distribution. A third is feedback loop absence: in testing, someone is watching. In production, the agent operates with less oversight, and failures that would be caught and corrected in testing silently propagate.

What makes this hard to catch is that the agent's performance often degrades gradually rather than failing outright. You don't get an obvious error. You get slightly worse outputs, slightly more failed tasks, slightly more cases where the agent asks for clarification when it shouldn't need to. By the time you notice, the production environment has shifted further, and you can't easily reconstruct what the agent was validated against.

There's a fourth failure mode that's less discussed: data contamination in testing. If your test scenarios share any data or context with the agent's training environment, the agent has an unfair advantage. In production, it doesn't. I've seen agents perform well in sandbox environments that were seeded with cleaned, structured data, then fail immediately when exposed to the actual messy, incomplete data of a real production environment. The agent didn't get worse. The data got real.

---

I want to be clear that I don't have systematic data on how common this failure mode is relative to others. What I have is a pattern from postmortems and system observations: when an agent that worked in testing starts failing in production, the most common explanation I've seen is not "the agent broke" but "the environment shifted."

The practical implication is that agent evaluation needs to include distribution monitoring, not just task success metrics. You should be tracking not just whether the agent completed the task, but whether the distribution of tasks and inputs it's seeing in production matches what you tested against. When the distributions diverge, you have a signal — not that the agent is broken, but that you're operating outside the envelope where you validated it. You can then decide whether to retrain, add synthetic examples of the new distribution, or accept that the agent's reliable operating range has changed.

The question worth sitting with is simpler than it sounds: when your agent fails in production, did the agent fail, or did the environment change underneath it? Those require different fixes. Attribution matters, because the wrong diagnosis leads you to the wrong solution — and you end up retraining an agent that wasn't the problem.