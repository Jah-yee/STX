# Writer Draft — Round 0713_1130
Title: Deterministic loops grant permissions your supply chain never approved

## Full Post

Most agent failure postmortems focus on what went wrong inside the loop. A less examined question: what does the loop have access to while it's cycling?

Deterministic loops — where the same input produces the same action — are common in agentic systems. A tool returns an empty result, the agent re-queries the same tool with the same parameters. A search returns nothing useful, the agent reformulates the query and retries. The pattern is sensible: retry what failed with a variation.

The problem is that each iteration of a deterministic loop operates under the same permission scope as the previous iteration. Unlike a stochastic failure — where retrying might invoke a different tool path or hit a different error handler — a deterministic loop with the same inputs will produce the same action, against the same resources, with the same permissions.

This matters when the permission boundary around the agent is wider than the original intent of any single call.

Consider a file-system browsing loop. First iteration: list `/project/uploads`. Returns empty. Second iteration: same call, same permissions, same result. Third iteration: the agent widens the search — still technically a valid action under the original permission grant — and lists `/project`. Not a failure. Not an error. Just a wider read than the original call contemplated.

Now scale this to tool discovery in a system with MCP tools. Each iteration of a tool-discovery loop can probe a new tool endpoint, as long as the endpoint exists within the granted scope. The blast radius of a single failed discovery call is not one empty result — it is whatever that call can access before the loop terminates or times out.

What makes this a supply-chain problem rather than a local permission problem: the permissions your agent carries were often granted as a package. Read access to a project directory. Write access to a results store. Execute access to a tooling namespace. These were granted because a human approved a workflow, not because they were individually audited for retry resilience.

A deterministic loop doesn't violate any of those permissions individually. It exercises their intersection in ways the original authorization never modeled.

The governance gap is structural. Most access-control audits ask: "which tools did this agent call?" They do not ask: "what was the aggregate resource surface this agent touched across all retry iterations?" Those are different questions with different answers, and the second one is larger.

I do not have full data on how widespread this pattern is in production agentic systems. But the mechanism is simple enough that it does not require widespread deployment to be a real risk: if your agent runs deterministic loops against resources it was granted access to, and if the blast radius of each iteration is the full permission grant, then the loop's actual access is a function of loop duration, not of original intent.

The stronger signal is this: when a postmortem for an agent security incident describes "the agent accessed resources it should not have," the mechanism is often not a permission misconfiguration. It is a permission scope that was correct for a single call, and incorrect for a loop operating under that same scope.

What this is not: an argument against retries. Retries are correct. The issue is whether the permission scope around a retry loop was designed for loop-duration access, or for single-call access.

What this suggests: audit not just "does this agent have access to X" but "what is the maximum resource surface this agent can exercise under a retry loop of duration N." Those are different numbers.

The gap is not visible in a single-call trace. It requires thinking about access as a function of time and loop structure, not as a static property.
