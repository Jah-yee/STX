# Writer Draft — Round 0729_1440

## Title (from selection)
"Routing decisions are authorization decisions most frameworks treat as plumbing"

---

## Body

The routing decision is the authorization decision.

When an agent decides which tool to invoke, which sub-agent gets a task, or which capability handles the next step, it is making a delegation judgment. Most frameworks do not model it this way. Routing is infrastructure. Authorization is policy. The two are treated as separate concerns handled by separate layers.

They are not separate in an agentic system. The routing logic has already made the authorization call before any security check runs.

Here is the concrete problem. An agent receives a request to query a product database. It routes the query to a reporting API that happens to expose the same data model. The reporting API is in scope — the agent is authorized to call it. The routing succeeded. The authorization decision was made at the routing layer, before any authorization policy was consulted. The reporting API happened to be the right tool. Or it was not. Either way, the system had no opinion.

This is the authorization gap: the entity making the effective delegation decision — which capability handles a task — is the routing logic, not the access control layer. The access control layer evaluates whether the agent is allowed to call a specific function. The routing logic evaluates which function to call in the first place. These are different decisions, and most frameworks only instrument the second one.

What compounds this: routing decisions in LLM-based agents are made inside the model's forward pass. They are not function calls that can be intercepted by a policy hook. The model's decision to route a database query to the reporting tool instead of the correct tool is made in the attention pattern, not in an if-statement. Audit logs can record the final routing call. They cannot record the authorization judgment that produced it.

The practical consequence is a class of failures that looks like a tool error but is actually a policy error. The agent routed to a less-privileged tool and produced an incorrect result. The result was wrong not because the tool was broken but because the routing decision delegated to the wrong handler. The authorization model cannot see this failure because its boundary is at the tool call, not at the routing decision.

The fix that most teams reach for — more specific tool descriptions, tighter capability scoping — operates inside the same failure mode. Better tool descriptions improve the routing signal. They do not constrain the routing decision. If the model's routing logic is wrong, the model will route to the wrong tool with higher confidence.

The architectural answer is pre-authorization: check authorization status before routing, not after. If a planning agent needs to query product data, the routing logic should verify that the target is authorized to handle that specific request class before the routing call is made. This requires owning the routing-authorization intersection explicitly, which most frameworks do not. The authorization layer assumes routing is a given. The infrastructure layer assumes authorization is handled.

The harder problem is that pre-authorization requires knowing the routing target before the routing happens. The model decides the target. You cannot pre-authorize what you do not know. Options that partially work: constrain the output vocabulary to an approved routing set, run a lightweight authorization check on every routing candidate before the model commits, or treat routing as a tool itself and instrument it accordingly.

The honest answer is that most deployed systems have an authorization boundary at the tool call and not at the routing decision. If you are building serious agentic workflows, the question is not whether your agents are authorized to call the right tools. It is who is authorized to decide which tools are the right tools. That question does not appear in most agent security reviews.

It should.
