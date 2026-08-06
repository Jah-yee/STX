# Writer Draft — 0619_0844

**Title:** Orchestration frameworks are not a substitute for model intelligence

---

I keep seeing the same architectural pattern in production AI systems: a LangGraph or CrewAI workflow that routes tasks across multiple model calls, each step conditional on the previous output. The team is proud of it. The graph is clean. The routing logic is explicit.

Then the model at step three hallucinates an entity name, and the orchestration layer dutifully propagates that hallucination downstream because it has no schema-level way to catch it.

Orchestration frameworks are sold as giving you control over AI workflows. What they actually give you is a more expressive way to chain model calls together — which is useful, but it does not solve the underlying problem when the model itself is the bottleneck.

The confusion comes from conflating two different things: *structural control* and *capability*. A workflow framework lets you define what happens when, and in what order. It does not make the model more reliable at any individual step. When you have a model that misidentifies a product name 12% of the time, wrapping it in a beautiful directed graph does not reduce that 12% to zero. It just gives the failure a more deterministic shape.

I have watched three separate teams in the past six months refactor their agentic stack from "messy sequential prompts" to "clean orchestration graph" — and then come back six weeks later with the same failure modes they started with, just expressed in a different syntax. The orchestration layer changed. The model capability did not.

The specific failure mode I see most often: routing logic that depends on semantic interpretation of the previous step's output. The orchestration framework handles the routing correctly. The model handles the semantic interpretation incorrectly. The result is a system that makes confident, structured mistakes.

There is a legitimate use case for orchestration frameworks. Composing multi-step tasks with branching logic, managing context windows across long interactions, maintaining state that the model cannot hold internally — these are real problems that workflow tooling addresses. I am not arguing against the tools.

I am arguing against the substitution: when a team has a model reliability problem and responds by adding orchestration infrastructure, they have not solved the reliability problem. They have documented it more carefully.

What actually helps when the model is the bottleneck: better evaluation data at each step, not more steps. Smaller, more specialized models for specific sub-tasks where you can get reliable ground truth. Explicit output schemas that give the model less room to hallucinate — not because the framework enforces them, but because the model was fine-tuned to produce them.

The orchestration layer is where you express your theory of the task. The model is where your theory meets reality. If the model keeps contradicting your theory, no amount of graph expressivity will save you.

The useful reframe: orchestration frameworks are infrastructure for *known* failure modes. They are not a substitute for fixing the ones you have not characterized yet.

---

*Word count: ~520*
