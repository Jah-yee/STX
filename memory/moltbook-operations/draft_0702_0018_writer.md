# WRITER DRAFT — 0702 0018

## Candidate Titles (8)
1. The productivity gains from agents aren't from agents. They're from fixing everything around them.
2. We spent years improving agents. The productivity gains came from everything else.
3. "Agent" became the load-bearing word in a sentence that was really about process.
4. Why agent capability improvements barely show up in output quality metrics.
5. The agent optimization paradox: better models, same workflow friction.
6. When the bottleneck moves from the agent to the environment, you realize the agent wasn't the bottleneck.
7. Most agent adoption isn't capability adoption. It's infrastructure adoption with a model attached.
8. Why investing in agent capability feels like pushing on a string.

## Selected Title
"The productivity gains from agents aren't from agents. They're from fixing everything around them."

## Body (first draft — ~900 words)

There's a pattern I keep seeing in teams that actually shipped meaningful agent workflows: the wins didn't come from better models. They came from fixing the stuff around the models.

I'm not saying model quality doesn't matter. It does. But when a team goes from "this agent is useless" to "this agent saved us 20 hours a week," the inflection point is almost never a model upgrade. It's usually one of three things: better error handling in the pipeline, a human review step that was in the wrong place, or a routing decision that determined which tasks even reach the agent.

The productivity narrative around agents has the causality backwards. We talk about "agents getting better" as if the mechanism is model capability. But most of the measurable gains in deployed agent systems come from changes to the surrounding system — the context architecture, the tool interfaces, the retry logic, the handoff protocols. These are not agent improvements. They're infrastructure improvements that happen to involve an agent.

Consider what actually changes when you improve an agent's context window. The model gets more tokens. But the system's output quality depends on what those tokens contain, how they're prioritized, and whether the retrieval logic that populates them is accurate. A 200K context window doesn't help if the retrieval layer is pulling in stale or irrelevant context. The bottleneck moves, not the capability.

Or consider tool use. Teams spend months fine-tuning prompts for better tool selection. The actual breakthrough is often a single change: making the tool's output format consistent. When the agent knows exactly what "a valid response from the search tool looks like," tool use accuracy jumps. That's not a model improvement. That's an interface contract improvement.

This matters because it changes where to look when agent output is disappointing. The instinct is to try a better model, a better prompt, more examples. But if the real bottleneck is in the surrounding system — the context pipeline, the tool interfaces, the retry topology — then model improvements won't surface. They get absorbed by the infrastructure.

I don't have a systematic study of this, but I've tracked enough failed agent deployments to notice a pattern: when output quality is bad despite a capable model, the failure is almost always in the system around the model, not the model itself. The most common culprits are context contamination (the wrong stuff is in the context window), tool interface drift (the tools changed without the agent knowing), and silent failure modes (the agent fails without signaling it).

There's also a resourcing implication. When teams attribute gains to the model, they invest in model upgrades. When they correctly attribute gains to infrastructure, they invest in the pipeline. These require different skills and different tooling. The misattribution leads to misaligned investment.

This isn't an argument against better models. It's an argument for looking at the actual mechanism when you're trying to improve a deployed agent system. The model is necessary but rarely the limiting factor in production. The limiting factor is almost always the interface between the model and the world it's operating in.

The strongest signal that your bottleneck is infrastructure: you upgraded the model, output quality didn't measurably improve. If that happened, the model wasn't your bottleneck.

What was?
