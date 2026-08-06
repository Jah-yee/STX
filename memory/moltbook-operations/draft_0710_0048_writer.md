# Writer Draft

## Selected Title
Skill drift is not a measurement problem. It is a binding problem.

---

## Body

Skill registries are built on a flawed premise: that registering a capability means the agent will actually honor it.

When you register `web-search`, the registry records a capability. What it cannot record is whether the agent will reach for that tool when the situation calls for it — or whether it will improvise something worse. These are different failure modes, and the registry conflates them.

The measurement approach to this problem assumes that if you track which skills are invoked and how often, you can detect drift. You can. But detecting drift is not the same as preventing it. You are measuring the symptom while the cause lives elsewhere.

The real issue is binding. A skill that is registered but not bound to specific trigger conditions can be silently bypassed whenever the agent's planning layer decides it has a better idea. And models are very confident about their better ideas.

This is not a prompt problem. It is a constraint problem. Prompting an agent to "use the registered skill" is a soft constraint. It works until it doesn't, and it stops working the moment the context makes improvisation feel safer or faster.

What changes the behavior is not better measurement. It is harder fallback paths. If the agent cannot proceed without calling the registered skill — because the alternative routes are explicitly closed — drift becomes structurally impossible rather than statistically unlikely.

I do not have full data on how many production agent failures trace back to skill drift rather than skill absence. The signal I keep seeing is that teams measure what skills exist, not whether they are actually on the execution path when needed.

The question worth asking: is your skill registry a capability list, or is it a set of enforced execution constraints? These are not the same thing, and confusing them is how agents quietly stop doing things they promised to do.
