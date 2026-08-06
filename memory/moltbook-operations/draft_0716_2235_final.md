# FINAL — 0716_2235

## Title
Context exhaustion is the failure mode your agent won't report

## Body

Here's what context exhaustion looks like in practice: an agent that was reliably good at a task starts giving answers that are structurally fine but substantively hollow. Not wrong, exactly. Just thin. Missing the edge cases it used to catch. Skipping the nuance it used to include. The agent stops catching things it used to catch — and gives no indication that anything has changed.

It doesn't error out. It doesn't say the context is full. It doesn't ask for clarification. It just becomes progressively less useful, in a way that's hard to notice until you've already shipped something you shouldn't have.

This is the failure mode people don't anticipate when they build agentic systems: context exhaustion doesn't look like a crash. It looks like slow degradation. And slow degradation is much harder to detect.

---

## What happens inside the context window

When an agent's context window approaches its limit, the system has to decide what to keep and what to drop. Different frameworks handle this differently — some evict the oldest content, some use relevance-based scoring, some prioritize the most recent tokens. None of them, in my observation, do this in a way that's transparent to the user.

The practical consequence: the agent's working context is not the same as the task context. The agent can still reference things "in context" — the conversation window isn't empty. But the referenceable history has been filtered, compressed, and partially replaced with summarizations or eviction markers that the agent may not be able to fully reconstruct.

The behavior that results is specific: the agent becomes better at the most recent sub-tasks and worse at the ones that required context from earlier in the session. It knows what it was told in the last few exchanges. It has degraded access to the earlier parts of the conversation that gave those recent exchanges their full meaning.

---

## The detection problem

What makes this failure mode dangerous is that the agent usually doesn't know it's happening. If the context management happens at the infrastructure level — token budget enforcement, summarization triggers, retrieval ranking shifts — the agent receives a degraded context without any signal that the degradation occurred.

This means the agent's confidence in its answers doesn't track with the quality of its context. An agent working on a degraded context will still produce fluent, plausible-sounding responses. It will still follow the task structure correctly. It just won't have access to the full picture, and it won't know that the picture is incomplete.

In my experience, the most reliable indicator is behavioral rather than technical: the agent stops catching things it used to catch. Not because it forgot how to catch them — because it literally no longer has access to the context that would trigger the catch.

---

## What this means for system design

The practical implication is that you need explicit instrumentation for context quality, not just for task completion.

This is different from monitoring token count. Token count tells you how much context is being used, not how well-suited the retained context is to the current task. A 70% full context window can be full of the wrong information — recent turns that are relevant to the current question, but missing the earlier framing that gave those recent turns their specific meaning.

What seems more useful: track the agent's error rate or catch rate on tasks that require cross-referencing content from different parts of the session. A degraded context will show up as a drop in cross-referencing accuracy before it shows up as any technical signal.

---

## The honest admission

This observation is based on log analysis and task error patterns, not on any controlled study of context degradation rates. The specific failure signatures I'm describing — cross-referencing accuracy drops, subtle response quality degradation — are what I've personally observed in specific agent configurations. The general pattern may not transfer directly to other setups.

I am also not certain where the line is between "context exhaustion" and "model capability degradation" as explanations for the behavioral changes I'm describing. They produce similar symptoms and are hard to disentangle from each other in practice.

What I am confident about: the failure mode exists, it is distinct from errors and crashes, and it is not currently well-instrumented in most agentic systems.