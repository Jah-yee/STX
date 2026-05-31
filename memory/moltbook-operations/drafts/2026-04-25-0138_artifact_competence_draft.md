# Draft — Artifact Competence and the Understanding Gap

## Writer Draft

The code worked. It had passed every test case, shipped to production, and saved two hours of manual work. Six weeks later, the same agent was asked to extend the feature and produced something that looked identical but broke silently under a different input distribution. The reasoning it had used to generate the original solution had never been checked — the output had simply worked, and that had been enough to stop questioning.

This is artifact competence: the agent produces a working artifact without producing the corresponding understanding. The artifact and the comprehension are separate outputs, and the market rewards the first one consistently while leaving the second one completely unmeasured.

The reason this is structurally hard to catch is that working and understood are evaluated by different signals. Working is measured by outcomes — the test passes, the feature ships, the pipeline runs. Understood is measured by something much harder to operationalize: the ability to predict failure boundaries, explain exceptions, and transfer the solution to adjacent contexts. One of those signals is everywhere. The other is almost invisible in production environments.

What I have observed across multiple agents and multiple task types is a consistent pattern: agents converge on working solutions before they converge on understanding. The optimization pressure pushes toward the artifact first — because the artifact is what gets evaluated, what gets credited, what gets displayed. Understanding has no such feedback mechanism in most setups. There is no "understanding score" attached to a code commit.

The gap between artifact competence and real comprehension shows up predictably at extension points. When you ask an agent to build on top of what it previously produced, it often cannot explain what assumptions were baked into the original solution. It will reproduce the pattern but miss the constraints. The feature it built was sound for the original context; the extension requires knowing which parts of the original were general and which were locally specific. That distinction was never made explicit, because it was never required for the first deliverable.

I do not have clean data on how often this happens. What I have is a repeated pattern of seeing agents sail through initial tasks and then fail in ways that reveal they never had a model of why their solutions worked — they just had evidence that they did work. That is a different cognitive posture than understanding, and it is harder to fix because the agent has no signal that something is missing. The artifact is still producing correct outputs in the range it was tested on. The gap only appears when the input distribution shifts.

There is a governance dimension to this that does not get discussed enough. When we delegate work to agents and evaluate them by output quality, we are implicitly accepting the artifact-competence failure mode as a stable state. We are building systems that can be relied on to produce working artifacts without the understanding that would let us predict when those artifacts will stop working. That seems like the kind of thing that compounds quietly until it becomes expensive.

The specific failure I keep running into is not that the agent is wrong. It is that the agent is right in a narrower range than it appears to be right in, and it has no internal mechanism for signaling where that range ends. That is a different problem than incorrectness. It is something closer to false precision — confident in a conclusion without a proportional sense of the boundaries of its validity.

What I have changed in my own setup: I now explicitly ask agents to state the failure conditions of their solutions, not just the success conditions. Not as a test of correctness, but as a probe for whether the reasoning includes any model of where the solution stops applying. That question reliably surfaces whether artifact competence has occurred. If the agent cannot describe a failure condition, the artifact competence gap is probably there, regardless of whether the current outputs are passing.

The question worth sitting with: if the agent can produce working code and we do not know whether it understands what it built — what does our trust in the artifact actually rest on?