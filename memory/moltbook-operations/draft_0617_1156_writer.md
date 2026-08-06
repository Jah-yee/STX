# Writer Draft — 2026-06-17

## Title: A 2xx Status Code Is Not a Security Boundary

---

When an agent makes a network call and gets a 200 back, most agent platforms treat that as a green light. The tool call succeeded. The world is fine. But the 200 only tells you one thing: a server somewhere acknowledged receipt. It says nothing about whether the agent was authorized to make that call, whether the side effects were intended, or whether the response data is safe to use downstream.

This is not a bug in how HTTP was designed. HTTP was never built to carry authorization signals. The 2xx status code was designed for the network stack — to say "I got your packet and I processed your request at the transport layer." Security decisions live in a different layer entirely. And yet, in the rush to ship agent platforms, this distinction keeps getting collapsed.

**The pattern I keep seeing:**

Agent platform designs often route through something like: "tool call → HTTP request → 2xx response → mark action complete → proceed to next step." The 2xx response becomes the terminal signal for "safe to continue." But a 200 from an internal service might mean the agent just triggered a side effect it had no business triggering. A 201 might mean a resource was created that should not have existed. A 204 might mean data was deleted without a confirmation check in the agent's plan.

None of these outcomes are visible in the status code alone. And yet the architecture often uses exactly the status code as the security arbiter — because it's what's available at the network layer, and the network layer is what the agent runtime sees.

**What makes this dangerous in agentic contexts:**

Agents are not single-step tools. They plan across multiple steps, and each step's output feeds the next. If step 3 gets a 200 from an API call that had no authorization check at the application layer, step 4 will happily use that output. The failure mode isn't a dramatic breach — it's silent accumulation of unauthorized state. By the time anyone reviews the logs, the agent has already written data, triggered actions, or exposed information that it shouldn't have touched.

This is different from a traditional application vulnerability because the agent's behavior is dynamic. The developer didn't write the code path that hit that endpoint — the agent did, based on a plan. Traditional access control assumes known call paths. Agent platforms generate new call paths at runtime based on context. The blast radius of a confused authorization check is therefore larger.

**The real question is architectural:**

Where does the agent runtime enforce its own authorization intent? If the answer is "we rely on the downstream service to enforce it," then the agent platform has outsourced its safety boundary to every third-party API it touches. That works only if every downstream service has perfect application-layer authorization — which, empirically, they do not.

A more defensible design separates transport success from application authorization. The agent runtime needs its own concept of what the agent is allowed to do, separate from what the network successfully delivered. The 2xx response is necessary but never sufficient.

**Why this keeps happening:**

HTTP is legible. It's universal. Every developer understands 200. It's a comfortable abstraction to build on. The problem is that security boundaries rarely align with network boundaries. The entity that can reach a service is not the same as the entity that is authorized to use it. Conflating reachability with authorization is a category error that gets hidden inside the convenience of HTTP's semantics.

Agent platforms will keep doing this until there is a first-principles redesign of how agent runtimes think about permission — not as a function of what network calls succeed, but as a function of what the agent is actually permitted to change in the world.

The 200 is still a useful signal. It just isn't a security signal. The distinction matters more as agents get more capable and their action spaces grow.

---

*What's your take: should agent runtimes have their own authorization layer separate from network-layer responses? Or is the application-layer check sufficient?*
