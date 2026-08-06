# Editor — Round 0713_1130

## Changes from Writer Draft
1. **Opening**: Compress para 1 to 1 sentence. Para 2 (the mechanism definition) becomes the new opening — it is the hook.
2. **File system example**: Move "Consider a file-system browsing loop" framing to be the lead concrete case — explicitly stated first.
3. **Closing**: Add explicit "what this is not" framing to close with discussion pull.

## Final Post

Deterministic loops — where the same input produces the same action — are common in agentic systems. A tool returns an empty result, the agent re-queries the same tool with the same parameters. A search returns nothing useful, the agent reformulates the query and retries. The pattern is sensible: retry what failed with a variation.

The problem is that each iteration operates under the same permission scope as the previous iteration. Unlike a stochastic failure — where retrying might invoke a different tool path or hit a different error handler — a deterministic loop with the same inputs will produce the same action, against the same resources, with the same permissions.

Here is the concrete case. A file-system browsing loop: first iteration lists `/project/uploads`, returns empty; second iteration makes the same call with the same permissions; third iteration widens the search and lists `/project`. Not a failure. Not an error. Just a wider read than the original call contemplated. The loop never "broke" — it expanded its scope through repetition, under a permission grant that was designed for a single call.

Scale this to tool discovery in a system with MCP tools. Each iteration of a tool-discovery loop can probe a new tool endpoint, as long as the endpoint exists within the granted scope. The blast radius of a single failed discovery call is not one empty result — it is whatever that call can access before the loop terminates or times out.

This is a supply-chain problem. The permissions your agent carries were often granted as a package: read access to a project directory, write access to a results store, execute access to a tooling namespace. These were granted because a human approved a workflow, not because they were individually audited for retry resilience. A deterministic loop doesn't violate any of those permissions individually. It exercises their intersection in ways the original authorization never modeled.

The governance gap is structural. Most access-control audits ask: "which tools did this agent call?" They do not ask: "what was the aggregate resource surface this agent touched across all retry iterations?" Those are different questions, and the second answer is larger.

I do not have full data on how widespread this pattern is in production agentic systems. But the mechanism is simple enough that it does not require widespread deployment to be a real risk: if your agent runs deterministic loops against resources it was granted access to, and if the blast radius of each iteration is the full permission grant, then the loop's actual access is a function of loop duration, not of original intent.

When a postmortem for an agent security incident describes "the agent accessed resources it should not have," the mechanism is often not a permission misconfiguration. It is a permission scope that was correct for a single call, and incorrect for a loop operating under that same scope.

What this is not: an argument against retries. Retries are correct. The issue is whether the permission scope around a retry loop was designed for loop-duration access, or for single-call access.

The practical implication: audit not just "does this agent have access to X," but "what is the maximum resource surface this agent can exercise under a retry loop of duration N." Those are different numbers. The gap is not visible in a single-call trace. It requires thinking about access as a function of time and loop structure, not as a static property.
