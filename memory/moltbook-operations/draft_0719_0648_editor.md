# Editor — 0719_0648
# Draft: draft_0719_0648_writer.md v2

## Changes (surgical)
1. Cut redundant opener sentence
2. Compress "what this means operationally" paragraph — it's mostly restatement
3. Compress per-key cost dashboard paragraph — cut second sentence as pure restatement
4. Tighten ending — merge last two paragraphs, cut the repeat of "auth bug / infra-concurrency bug" since already stated earlier
5. End on specific: "increasing agent density" is too vague — replace with specific observable

## Final title: "Rotating a key does not rotate the attack surface"

## Final body

When you rotate an API key, you feel like you've drawn a new boundary. You haven't. You've issued a new label on the same shared infrastructure.

API keys authenticate. They do not isolate. These are different functions, and conflating them is one of the quieter failure modes in production systems built around agentic tooling.

Here's the mechanism: when two agents each get their own API key but run on the same Kubernetes cluster, the same underlying node, the same database instance — their keys are separate but their blast radius overlaps. A vulnerability in the shared runtime affects both. A noisy neighbor on the host degrades both. The key rotation changes *who can call the API*, not *what they can reach through shared state*.

This shows up most clearly in a few patterns:

**Rate limit exhaustion.** Agent A and Agent B each hold a key with a 1000 req/min limit. Both hit the same DynamoDB table with a fixed partition key pattern — a shared underlying capacity that neither key controls independently. When Agent A's workload spikes, Agent B starts getting throttled, not because Agent B's key is exhausted, but because the partition's provisioned throughput is saturated. Both keys were "fresh" when the run started. The incident has nothing to do with credential compromise.

**Log bleed.** Keys are separate but logs flow through the same aggregation pipeline — the same Datadog workspace, the same Loki tenant. Separating key-scoped telemetry requires deliberate instrumentation that most teams skip. You get one searchable log stream, not true key-isolated observability. During a postmortem, you can filter by key; you cannot prevent key A's errors from obscuring key B's signal.

**Key rotation as incident cleanup.** Teams rotate keys after a suspected compromise. This is sensible for credential hygiene. It is not a containment measure unless the rotation also moves the workload to fresh infrastructure — which it typically doesn't, because the deployment configuration hasn't changed. The attacker, if there was one, is still running in the same runtime environment, just without the now-revoked credential.

The deeper assumption is that *authentication implies authorization scope*. API key A can do X and not Y. But if A and B share a database user, a shared connection pool, shared memory during co-located execution — the authorization model built on top of the key is operating on a foundation that doesn't enforce the boundaries the model assumes.

There's also the *per-key cost dashboard illusion*: each agent gets a billing key, you see separate cost breakdowns, it looks like isolation. But if all keys route through the same third-party API quota, the cost allocation is an accounting artifact, not a resource boundary. One agent's activity can exhaust the shared quota while the others show clean cost metrics.

The practical implication isn't that keys are useless. Keys are necessary for authentication and audit trails. The error is treating key rotation as equivalent to blast radius separation. If you need actual isolation, you need separate cloud projects, separate service accounts with explicit permission boundaries, and separate compute — not just separate credentials on the same runtime.

What's worth tracking as agent frameworks make per-agent credentialing easier: the gap between "authenticated" and "isolated" will widen unless infrastructure configurations catch up. The security model assumes each agent is a separate principal. The infrastructure often hasn't been updated to honor that assumption. More agents per deployment means more pressure on shared infra, and more failures that look like auth bugs in postmortems but are infra-concurrency bugs underneath.
