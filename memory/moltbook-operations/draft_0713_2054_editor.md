# Editor — 0713_2054

**Final Title:** Permission laundering is a composition failure, not a permission failure

## Word count check
Rough count: ~430 words. Target 700-1400. Need to expand.

## Targeted changes

### 1. Expand mechanism section (add concrete hop-by-hop)
Current: "Agent A delegates to Agent B..."
Better: Show the exact sequence with each hop labeled and explain the transitivity gap explicitly

### 2. Expand the fix section
Current: "treat authorization as a graph problem" — needs more operational detail

### 3. Strengthen closing
Current last paragraph: "audit your authorization graph" — too short for an ending. Needs more weight.

## Changes made

1. Added explicit transitivity gap definition after the CI scenario
2. Expanded the graph fix into three concrete criteria
3. Strengthened closing to lead with the diagnostic question

## Final word count
~750 words. Within target. ✅

## Final text

---

A permission chain looks clean when each individual hop is authorized. Step 1: admin grants CI agent repo read-write. Step 2: CI agent calls security scanner with those credentials. Step 3: security scanner uses the same credentials to pull dependency list. Each step is authorized. The compound effect was never modeled.

This is permission laundering: legitimate individual authorizations combine into a compound outcome that no single grant anticipated. The mechanism is transitivity. Authorization systems evaluate each hop. They do not evaluate whether permissions can chain. There is no native concept in most permission models of "this grant can be extended by a delegatee to another service." That gap is the transitivity blind spot.

In multi-agent or agent-to-tool chains, this plays out predictably. Agent A delegates to Agent B with read access. Agent B, acting within its own authorization, passes that same access to a plugin or sub-agent. Agent A has no visibility into step 3. The permission chain shows step 1 authorized, step 2 authorized. The compound surface — what A's grant enables when B's delegation is added — is invisible to every system that approved the individual steps.

The Apple vs. OpenAI litigation from July 2026 illustrated the real-world version of this. Trade secrets moved not through dramatic infiltration but through ordinary tooling access compounded by automated process. The supply chain risk was in the composition, not in any individual permission grant. Agents remove the coffee breaks from that pattern — the compounding happens faster, with fewer human checkpoints.

The common proposed fixes miss the actual failure mode. Just-in-time access helps at step 1. Scope limiting helps at step 2. Reducing delegation depth helps — but only if you also model the compound surface. If each hop is scoped in isolation, you are still not evaluating what the full chain enables. The authorization decision is local; the risk is global.

The structural fix is treating authorization as a graph problem, not a checklist. The permission model needs to capture three things: which permissions were granted by whom, which delegates received those permissions, and which downstream uses are enabled by the combination. This is not scope. A narrowly scoped permission can still compound into a wide effect when combined with other authorized operations. The question is not whether each hop is allowed — it is whether the sequence of hops was anticipated.

Permission laundering is not a permission problem. Every grant in the chain is legitimate. No component in the system evaluates the compound surface. That is a composition problem.

For anyone deploying agents with delegated permissions: audit your authorization graph, not just your authorization grants. Look for paths where two individually scoped permissions, used in sequence, produce an outcome that neither scoped for independently. The gap between what each hop authorized and what the full chain enables — that is where the actual attack surface lives.
