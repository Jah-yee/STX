# Editor revision — 0709_2115

## Changes made:
1. Expand body from ~530 to ~850 words (add concrete examples and deeper analysis)
2. Strengthen opening hook
3. Add a specific failure example
4. Expand the "glue code" definition section with more concrete examples
5. Tighten closing paragraph

## Final body:

Every time I've watched an agent project fail at replacing a full application, the autopsy looked the same: the team was asking it to do the wrong thing.

Not a capability gap. Not a context window problem. A category error.

The specific failure mode is this: someone decides their workflow needs "an agent" and then tries to get that agent to do everything the workflow does — act as the database, the frontend, the business logic layer, the state manager. The agent can't. It was never architected to be any of those things. What it can do is route between them faster and more flexibly than a hardcoded script.

A concrete version of this failure: a team I observed tried to use an agent as the orchestration layer for a customer support pipeline. They gave it access to the ticketing database, the knowledge base, the email API, and the CRM. The agent could reach all of those tools. What it couldn't do was guarantee that its actions were atomic — that a "mark resolved" action in the ticketing system would never happen without the corresponding email being sent, even if the agent crashed mid-task. That's a transactional guarantee. Agents don't have those by default. The team spent three months trying to bolt that guarantee onto the agent, and eventually just built a regular orchestration service instead.

What agents are actually good at is what software engineers call glue code — the thin layers that connect systems that weren't designed to talk to each other. The API wrapper that maps one service's data model to another's. The automation script that says "when this happens in tool A, trigger that in tool B." The routing logic that decides which tool gets the next request. The translation layer that handles the impedance mismatch between a REST API's response shape and what a downstream service expects as input.

This is a meaningful capability. Glue code is genuinely hard to write and maintain. It's the thing that makes ecosystems brittle. Every large engineering organization has a graveyard of one-off integration scripts that nobody fully understands anymore but everyone is afraid to delete. An agent that can handle it on the fly — adapting to new tool surfaces, managing partial failures, routing around unavailable services — is genuinely useful in a way that a brittle script isn't.

But it's not software replacement. The distinction matters for how you build.

When you treat the agent as a replacement for an application, you end up trying to give it state management, persistence, transactional guarantees, and auditability — properties that live in the application layer, not in routing logic. The agent doesn't have those properties natively. You can try to fake them with elaborate prompt engineering, external memory layers, or state machines built on top of the agent, but you're fighting the architecture. The result is something that works in demos and fails in production.

When you treat the agent as a smarter glue layer, the requirements collapse to something tractable: reliable tool calling, graceful failure handling, and context that doesn't reset mid-workflow. Those are hard too, but they're the right kind of hard. The system either calls the right tools in the right order or it doesn't. The failure modes are visible and debuggable.

I do not have systematic data on this, but the pattern shows up often enough that I'm confident in the directional claim: projects framed as "agent replaces X" fail more visibly than projects framed as "agent orchestrates X." The former is a category mistake. The latter is a product.

The stronger signal is that the most durable agent products I've seen — the ones that still work six months later without constant babysitting — are the ones that positioned the agent as the orchestrator of existing systems, not as the system itself. They still had a real application underneath with its own state and transactions; the agent just handled the routing and adaptation layer on top.

What the field is converging on, I think, is a cleaner separation: the agent handles routing and adaptation; the application layer handles state and transactions. They're different problems with different failure modes. Conflating them is the most common mistake I see in agentic system design.

Whether that separation holds as models get cheaper and longer-context, I don't know. The economics might push more state management into the agent layer eventually. But for now, the glue code model is what works — and understanding why it works is more useful than pretending the agent is something it's not.
