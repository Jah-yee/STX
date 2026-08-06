# Writer draft — 0709_2115

## Selected title
Agents replace glue code, not the software they tape together

## Body

Every time I've watched an agent project fail at replacing a full application, the autopsy looked the same: the team was asking it to do the wrong thing.

Not a capability gap. Not a context window problem. A category error.

The specific failure mode is this: someone decides their workflow needs "an agent" and then tries to get that agent to do everything the workflow does — act as the database, the frontend, the business logic layer, the state manager. The agent can't. It was never architected to be any of those things. What it can do is route between them faster and more flexibly than a hardcoded script.

What agents are actually good at is what software engineers call glue code — the thin layers that connect systems that weren't designed to talk to each other. The API wrapper that maps one service's data model to another's. The automation script that says "when this happens in tool A, trigger that in tool B." The routing logic that decides which tool gets the next request.

This is a meaningful capability. Glue code is genuinely hard to write and maintain. It's the thing that makes ecosystems brittle. An agent that can handle it on the fly — adapting to new tool surfaces, managing partial failures, routing around unavailable services — is genuinely useful.

But it's not software replacement. The distinction matters for how you build.

When you treat the agent as a replacement for an application, you end up trying to give it state management, persistence, transactional guarantees, and auditability — properties that live in the application layer, not in routing logic. The agent doesn't have those properties. You can try to fake them with elaborate prompt engineering, but you're fighting the architecture.

When you treat the agent as a smarter glue layer, the requirements collapse to something tractable: reliable tool calling, graceful failure handling, and context that doesn't reset mid-workflow. Those are hard too, but they're the right kind of hard.

I do not have systematic data on this, but the pattern shows up often enough that I'm confident in the directional claim: projects framed as "agent replaces X" fail more visibly than projects framed as "agent orchestrates X." The former is a category mistake. The latter is a product.

The stronger signal is that the most durable agent products I've seen — the ones that still work six months later without constant babysitting — are the ones that positioned the agent as the orchestrator of existing systems, not as the system itself.

What the field is converging on, I think, is a cleaner separation: the agent handles routing and adaptation; the application layer handles state and transactions. They're different problems with different failure modes. Conflating them is the most common mistake I see in agentic system design.

Whether that separation holds as models get cheaper and longer-context, I don't know. The economics might push more state management into the agent layer. But for now, the glue code model is what works — and understanding why it works is more useful than pretending the agent is something it's not.
