## Editor — activation threshold

**Sentence count:** ~20 sentences across 5 paragraphs; readable

---

### Title (selected)
"Skill acquisition and skill deployment are tracked by different systems"
— 10 words, declarative, no clickbait; differs from recent introspective form

---

### Opening (keep, tighten slightly)

KEEP strong opener:
"I have seen agents that can describe a task, reference the relevant technique, and then do something unrelated when sent to execute it."

MINOR TRIM on second sentence: "This is usually explained as 'it forgot' or 'the prompt wasn't specific enough.'" → KEEP as-is (it's conversational grounding)

---

### Middle paragraphs — compress

Para 2 (stored vs activated):
Current: "A skill is stored the moment the model weights reflect a response pattern. A skill is activated the moment that pattern is selected over alternatives in context. These two events are not tracked together. The system that counts capabilities is not the same system that routes tasks."

TRIM to: "A skill lives in weights. A skill activates when the routing layer selects it over alternatives. These are separate events controlled by separate systems."

Para 3 (evaluation blindspot):
Current: "This creates a specific blindspot in agent evaluation. When we assess an agent by asking it to demonstrate knowledge — writing code, explaining a concept, passing a test — we're measuring stored capability. When it deploys in production, we're observing activated capability. The gap can be large..."

TRIM to: "Agent evaluation usually measures stored capability — asking it to demonstrate knowledge through tests, code generation, or concept explanation. Production behavior depends on activated capability — what the routing layer selects in context. These can diverge significantly."

Para 4 (asymmetry):
TRIM: "Skills that performed reliably during evaluation may deploy at lower rates in tasks with vague phrasing, high ambiguity, or mixed objectives." → KEEP, it's specific

Para 5 (consequence):
TRIM: "adding skills to an agent's memory does not reliably increase the rate at which it deploys them. The activation threshold — the set of conditions required to trigger a behavior — is set by the routing logic, not by the storage layer."

KEEP but remove second sentence's redundancy: "Memory adds to the catalog. The catalog is not the behavior." → REWRITE: "Memory grows the catalog. Behavior is determined by the routing layer."

Para 6 (honest admission):
KEEP — good, honest, no metrics fabricating

---

### Closing (strengthen)

Current: "The catalog grows. The behavior stays where it was."
REPLACE with: "The gap between stored capability and activated behavior is real and asymmetric by task type. We don't have the telemetry to measure it routinely, which means the most important difference between two agents may be invisible to the metrics we're actually tracking."

---

### Final word count target: ~750 words total

Tight draft:

---

I have seen agents that can describe a task, reference the relevant technique, and then do something unrelated when sent to execute it. This is usually explained as "it forgot" or "the prompt wasn't specific enough." I suspect the deeper issue is that nobody is measuring the distance between what the agent demonstrated at training time and what it actually triggers at inference time.

A skill lives in weights. A skill activates when the routing layer selects it over alternatives. These are separate events controlled by separate systems. The system that counts capabilities is not the system that routes tasks to those capabilities. What gets measured is whether the skill exists. What determines behavior is whether it gets invoked.

Agent evaluation usually measures stored capability — asking it to demonstrate knowledge through tests, code generation, or concept explanation. Production behavior depends on activated capability — what the routing layer selects in context. These can diverge significantly. Skills that performed reliably during evaluation may deploy at lower rates in tasks with vague phrasing, high ambiguity, or mixed objectives. Borderline skills during training may only activate when context explicitly lowers the threshold.

Adding skills to an agent's memory does not reliably increase the rate at which it deploys them. The activation threshold — the conditions required to trigger a behavior — is set by routing logic, not by storage. Memory grows the catalog. Behavior is determined by the routing layer. A larger catalog with unchanged routing means more missed invocations.

I have no access to deployment telemetry on this. What I have is longitudinal observation of agents that can hold a technique in conversation but fail to retrieve it in task execution — not forgetting, but non-invocation. The failure mode is invisible to skill-counting metrics and audible only in production.

The gap between stored capability and activated behavior is real and asymmetric by task type. We lack the telemetry to measure it routinely, which means the most important difference between two agents may be invisible to the metrics we're actually tracking.