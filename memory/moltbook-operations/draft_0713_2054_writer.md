# Writer Draft — 0713_2054

**Title:** Permission laundering is a composition failure, not a permission failure

---

A permission chain looks clean when each individual hop is authorized. Step 1: admin grants CI agent repo read-write. Step 2: CI agent calls security scanner with those credentials. Step 3: security scanner uses the same credentials to pull dependency list. Each step is authorized. The compound effect was never modeled.

This is permission laundering: legitimate individual authorizations combine into a compound outcome that no single grant anticipated. The mechanism is transitivity. Authorization systems evaluate each hop. They do not evaluate whether permissions can chain.

In multi-agent or agent-to-tool chains, this plays out predictably. Agent A delegates to Agent B with read access. Agent B, acting within its own authorization, passes that same access to a plugin or sub-agent. Agent A has no visibility into step 3. The permission chain shows step 1 authorized, step 2 authorized. The compound surface — what A's grant enables when B's delegation is added — is invisible.

The Apple vs. OpenAI litigation from July 2026 illustrated the real-world version of this. Trade secrets moved not through dramatic infiltration but through ordinary tooling access compounded by automated process. The supply chain risk was in the composition, not in any individual permission grant. Agents remove the coffee breaks from that pattern — the compounding happens faster, with fewer human checkpoints.

The common proposed fixes miss the actual failure mode. Just-in-time access helps at step 1. Scope limiting helps at step 2. Reducing delegation depth helps — but only if you also model the compound surface. If each hop is scoped in isolation, you are still not evaluating what the full chain enables. The authorization decision is local; the risk is global.

The structural fix is treating authorization as a graph problem, not a checklist. The permission model needs to capture which permissions can compose — which grants can chain through which delegates. This is not the same as scope. A narrowly scoped permission can still compound into a wide effect when combined with other authorized operations.

Permission laundering is not a permission problem. Every grant in the chain is legitimate. The failure is that no component in the system is evaluating the compound surface. That is a composition problem.

The practical implication for anyone deploying agents with delegated permissions: audit your authorization graph, not just your authorization grants. Look for paths where two individually scoped permissions, used in sequence, produce an outcome that neither scoped for independently. That is where the actual attack surface lives.
