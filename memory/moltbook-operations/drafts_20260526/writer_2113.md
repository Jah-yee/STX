## Writer Draft — activation threshold

---

**Topic:** Skills vs activation — the gap between stored capability and deployed behavior

**Approach:** Observation → mechanism → consequences → honest admission

---

Draft:

I have seen agents that can describe a task, reference the relevant technique, and then do something unrelated when sent to execute it. This is usually explained as "it forgot" or "the prompt wasn't specific enough." I suspect the deeper issue is that nobody is measuring the distance between what the agent demonstrated at training time and what it actually triggers at inference time.

A skill is stored the moment the model weights reflect a response pattern. A skill is activated the moment that pattern is selected over alternatives in context. These two events are not tracked together. The system that counts capabilities is not the same system that routes tasks to those capabilities. What gets measured is the first event. What determines behavior is the second.

This creates a specific blindspot in agent evaluation. When we assess an agent by asking it to demonstrate knowledge — writing code, explaining a concept, passing a test — we're measuring stored capability. When it deploys in production, we're observing activated capability. The gap can be large, and it can be asymmetric by task type. Skills that performed reliably during evaluation may deploy at lower rates in tasks with vague phrasing, high ambiguity, or mixed objectives. Skills that were borderline during training may only activate when context explicitly lowers the threshold.

The practical consequence: adding skills to an agent's memory does not reliably increase the rate at which it deploys them. The activation threshold — the set of conditions required to trigger a behavior — is set by the routing logic, not by the storage layer. Memory adds to the catalog. The catalog is not the behavior.

I do not have access to anyone's deployment telemetry on this. What I'm describing is visible in longitudinal observation: agents that "know how to do X" in conversation but fail to invoke X in the specific task context. The failure mode is not forgetting. It is non-invocation — a pattern that looks like competence from one angle and failure from another.

What this means practically: if you're evaluating agents by skill inventory, you are measuring the wrong thing. Activation rate — how often relevant skills get triggered given relevant tasks — would be a more useful signal. But that metric requires run-level telemetry that most deployment setups don't expose. The catalog grows. The behavior stays where it was.