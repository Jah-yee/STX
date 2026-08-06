# WRITER DRAFT — Round 2308
# Title: The junior employee fallacy in agentic workflows

---

There is a pattern I keep seeing in how teams design agentic workflows, and it goes like this: the human identifies a task, delegates it to an agent, and assumes the agent will handle it with appropriate judgment — understanding constraints, weighing tradeoffs, noticing when something is obviously wrong.

It won't. And the failure is not what most people assume.

The mistake is not that the agent is stupid. The mistake is that the human is reasoning by analogy: delegating to an agent feels like delegating to a junior employee. The junior employee does not know the full context either, but they have enough socialized knowledge to know when something looks off. They ask questions. They flag ambiguities. They stop and check before shipping something embarrassing.

An agent does none of this by default.

## What actually happens

The agent receives a task description — a prompt, a goal, a set of instructions — and it produces an output that satisfies those instructions literally. Whether the output makes sense in the broader context of your project, your team norms, your stakeholder expectations: the agent has no mechanism to know that, and most deployed systems have no mechanism to surface it.

This is not a capability gap. The underlying model can reason about ambiguity, can flag edge cases, can even be prompted to ask for clarification. The failure is architectural: the workflow does not create the conditions for that behavior to emerge.

I have watched this play out in code review workflows. Someone wraps an LLM around a PR review task, feeds it the diff, and expects the agent to act like a senior engineer: catching real bugs, flagging architectural drift, raising concerns before the merge. What actually happens is the agent reviews the diff as written — applying the instructions it was given — and produces a thorough, well-formatted report that often misses the thing a human reviewer would have caught in thirty seconds because they knew to look for it.

The agent is not missing the bug. The workflow is missing the signal that should have directed attention to the bug.

## The junior employee comparison is wrong in a specific way

Human delegation works because both parties share a model of the work. The manager knows what the junior employee does not know. The junior employee knows to escalate when something is unclear. There is a shared sense of what "reasonable" looks like.

Agent delegation does not have this property. You can write detailed instructions, but you cannot write the background knowledge that makes those instructions interpretable. The agent does not know what you know. It knows what you said.

This matters most when the task itself is underspecified — which is most real tasks. The instruction "improve the error messages in this codebase" requires knowing which error messages are actually causing user confusion, which paths are performance-critical, which messages are owned by which team. A human can infer this. An agent cannot, unless the workflow explicitly surfaces that context.

When it does not, the agent produces output that is locally correct but globally misaligned. The error messages improve by some metric, but not by the metric that matters.

## What changes when you design for this

The practical shift is this: stop designing workflows that assume the agent will bring appropriate judgment, and start designing workflows that supply the context judgment requires.

Concretely, this means: instead of "review this PR and flag issues," it means "here is the incident that caused this code to be written, here is the team convention for this type of change, here is what a regression would look like — now review." The agent is still doing the work. But the work is now grounded in the information that produces good judgment.

It also means building explicit checkpoints where the agent surfaces its confidence rather than acting on it. "I am about to merge this because the instructions say to, but I notice the test coverage on this path is low — should I proceed?" That is a junior employee behavior. Most agents do not exhibit it, not because they cannot, but because the workflow was not designed to elicit it.

## The honest version

I am not arguing that agents cannot be trusted. I am arguing that the trust model most teams deploy — "the model is powerful, it will figure it out" — is a misapplication of how delegation works between humans.

The failure mode is not the agent being dumb. The failure mode is the workflow pretending the agent has context it does not have, and then being surprised when the agent acts reasonably within an unreasonable frame.

Designing for this is unglamorous. It means more upfront context engineering, more explicit guardrails, fewer "the agent will handle it" assumptions. It is also the only way to get reliable behavior from systems that are, underneath it all, very good at doing exactly what you asked them to do — even when what you asked for does not make sense.

---

*Word count: ~780*
