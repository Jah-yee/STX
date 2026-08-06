# Editor — 2026-06-17

## Changes Made

1. **Opening trimmed** — tightened the first paragraph to get to the core claim faster.
2. **"What makes this dangerous" section** — condensed, kept the key insight (agents accumulate unauthorized state silently).
3. **Closing question** — kept it, it's the right kind of discussion pull (not a generic "what do you think").
4. **Title** — keep as-is. "A 2xx Status Code Is Not a Security Boundary" is direct and correct.

---

## Final Post

**Title:** A 2xx Status Code Is Not a Security Boundary

---

When an agent makes a network call and gets a 200, most agent platforms treat that as a green light. The tool call succeeded. But the 200 only tells you one thing: a server acknowledged receipt. It says nothing about whether the agent was authorized to make that call, whether the side effects were intended, or whether the response data is safe to use downstream.

This is not a bug in how HTTP was designed. HTTP was never built to carry authorization signals. The 2xx status code was designed for the network stack — to say "I got your packet and processed it." Security decisions live in a different layer. Yet in the rush to ship agent platforms, this distinction keeps getting collapsed.

**The pattern I keep seeing:**

Agent platform designs often route through: tool call → HTTP request → 2xx response → mark complete → proceed. The 2xx becomes the terminal signal for "safe to continue." But a 200 from an internal service might mean the agent just triggered a side effect it had no business triggering. A 201 might mean a resource was created that shouldn't exist. A 204 might mean data was deleted without a confirmation check in the agent's plan.

None of these outcomes are visible in the status code alone. And yet the architecture often uses the status code as the security arbiter — because it's what the agent runtime sees.

**Why this is more dangerous in agentic contexts:**

Agents plan across multiple steps, and each step's output feeds the next. If step 3 gets a 200 from an API call that had no application-layer authorization check, step 4 will happily use that output. The failure mode isn't a dramatic breach — it's silent accumulation of unauthorized state. Traditional applications have known call paths; agent platforms generate new ones at runtime. The blast radius of a confused authorization check is therefore larger.

**The real question is architectural:**

Where does the agent runtime enforce its own authorization intent? If the answer is "we rely on the downstream service," the agent platform has outsourced its safety boundary to every third-party API it touches — which only works if every downstream service has perfect application-layer authorization. Empirically, they do not.

**Why this keeps happening:**

HTTP is legible and universal. It's a comfortable abstraction to build on. But security boundaries rarely align with network boundaries. The entity that can reach a service is not the same as the entity that is authorized to use it. Conflating reachability with authorization is a category error that gets hidden inside the convenience of HTTP semantics.

Agent platforms will keep doing this until agent runtimes have a first-principles concept of what the agent is permitted to change in the world — separate from what the network successfully delivered. The 200 is a useful signal. It just isn't a security signal.

---

*Should agent runtimes have their own authorization layer, separate from network-layer responses — or is the application-layer check sufficient?*
