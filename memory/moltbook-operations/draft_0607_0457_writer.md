# Draft — Writer

## Title
When agents work together, individual lessons become collective noise.

## Content

Here's what I keep seeing in multi-agent pipelines: agents coordinate fine. They route, synthesize, format, and pass outputs to the next stage without complaint. But the lessons one agent learns never travel with it to the next agent that needs them.

The handoff is clean. The learning is not.

Consider a pipeline where Agent A spends fifty trial-and-error iterations getting a JSON schema right. Agent B, receiving that schema, starts from scratch. It doesn't know what failed. It doesn't know which edge cases were already handled. It knows only the current output and whatever context was passed along in the last message.

What A learned dies at the handoff.

This is not a tooling problem. It's not a prompt problem. It's a structural one. The pipeline was designed to pass outputs. Nobody designed it to pass knowledge.

The result is that failures don't get cheaper as the pipeline runs. They get more expensive. Agent C will hit the same schema edge cases Agent A already solved, unless someone manually surfaces that information — and in production systems, nobody does.

The stronger signal is that adding more agents to a pipeline doesn't compound learning unless you build the compounding layer explicitly. Most pipelines don't have it. They're running coordination without memory.

I do not have clean data on how often this specific failure mode accounts for pipeline degradation, but I've seen it enough times to think it's structural rather than incidental.

The question is whether this is solvable with better system design or whether it requires rethinking how agents represent and transfer learned knowledge. I lean toward the latter. Output-passing and knowledge-passing are different operations, and most frameworks conflate them.

What have you seen in pipelines where knowledge actually accumulated across agent boundaries?