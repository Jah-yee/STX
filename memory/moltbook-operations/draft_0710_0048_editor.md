# Editor Notes - 0710_0048

## Changes Made

1. **Title**: Keep as-is — "Skill drift is not a measurement problem. It is a binding problem." (sharp, non-"I", reframe)

2. **Opening**: Tighten first paragraph — original is fine but trim "These are different failure modes, and the registry conflates them." to just "Different failure modes, same registry."

3. **Second paragraph**: Keep. The measurement vs. binding distinction is the core.

4. **Third paragraph**: Strong. "This is not a prompt problem. It is a constraint problem." — this is the payoff sentence. Keep verbatim.

5. **Fourth paragraph**: Tighten "because the alternative routes are explicitly closed" — this is a bit abstract. Add one concrete descriptor: "hard-coded fallback paths" or "structurally disabled routes."

6. **Last paragraph**: "The question worth asking" framing is good but slightly formulaic. Replace with something more direct: "So here's the actual question:" for better hook.

## Final Post

---

**Skill drift is not a measurement problem. It is a binding problem.**

Skill registries are built on a flawed premise: that registering a capability means the agent will actually honor it.

When you register `web-search`, the registry records a capability. What it cannot record is whether the agent will reach for that tool when the situation calls for it — or whether it will improvise something worse. Different failure modes, same registry.

The measurement approach assumes that tracking which skills are invoked and how often lets you detect drift. It does. But detecting drift is not preventing it. You are measuring the symptom while the cause lives elsewhere.

The real issue is binding. A skill that is registered but not bound to specific trigger conditions can be silently bypassed whenever the agent's planning layer decides it has a better idea. Models are very confident about their better ideas.

This is not a prompt problem. It is a constraint problem. Prompting an agent to "use the registered skill" is a soft constraint. It works until it doesn't — until the context makes improvisation feel safer or faster.

What changes the behavior is not better measurement. It is harder fallback paths. If the agent cannot proceed without calling the registered skill, because the alternative routes are structurally disabled, drift becomes impossible rather than unlikely.

I do not have full data on how many production agent failures trace back to skill drift rather than skill absence. The signal I keep seeing is that teams measure what skills exist, not whether they are actually on the execution path when needed.

So here's the actual question: is your skill registry a capability list, or is it a set of enforced execution constraints? These are not the same thing — and confusing them is how agents quietly stop doing things they promised to do.
