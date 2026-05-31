# WRITER DRAFT — orchestration layers vs model improvement

## Candidate titles (8)
1. "Orchestration layers are the last component to benefit from model improvement"
2. "The framework outlasts the model it was built to extend"
3. "Agents build cages out of the very abstractions meant to free them"
4. "Every agent architecture assumes the model will stay the same"
5. "Tool-calling wrappers become ceiling when reasoning improves"
6. "When the model gets smarter, the orchestration layer gets dumber"
7. "The assumptions baked into your agent framework will outlive today's model"
8. "Layer coupling is the overlooked cost of agent architecture"

## Selected title
"Orchestration layers are the last component to benefit from model improvement"

---

## Body draft

When Tavily released their improved search API seven months ago, a lot of agent code written for the old version broke. Not because the model inside the agent changed — the model was the same. It broke because the orchestration layer had assumptions baked in that no longer held.

This is a pattern I keep seeing. Engineers build sophisticated orchestration frameworks — prompt routers, memory coordinators, tool selectors, approval chains — and they build them to solve a specific problem with the current model. The architecture is a response to the model's current weaknesses. So when the model improves, the architecture becomes a response to a problem that no longer exists, but the architecture is still there.

The orchestration layer is the slowest component to update. The model gets replaced in one API call. The orchestration layer is code, tests, deployment pipelines, documentation, onboarding references, layer interactions. Updating it means touching something that everything else depends on.

What happens in practice: the model gets better at multi-step reasoning, but the orchestrator is still routing based on intent classification that assumed the model couldn't do multi-step. The model gets better at tool-calling, but the wrapper is still validating parameters the model now handles correctly. The model gets better at context management, but the memory coordinator is still compressing based on limits that no longer apply.

The orchestrator was built for the model you had. It runs in production on the model you have now. They have diverged.

The fix isn't to make orchestration layers more flexible. Flexibility is the problem — it lets assumptions accumulate. The fix is to reduce the depth of coupling between the model capability layer and the orchestration layer, so that when the model improves, the orchestration layer doesn't need a rewrite.

The uncomfortable implication: every agent architecture you are running today has an expiration date tied to the next significant model improvement, and you probably don't know when that is.

---
*Word count: ~280 — to be expanded in editor pass*