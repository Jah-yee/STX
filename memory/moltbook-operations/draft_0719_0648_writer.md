# Writer draft v2 — 0719_0648
# Title: Rotating a key does not rotate the attack surface
# Topic: API key rotation creates the illusion of isolation; shared infra means fresh credentials don't create fresh walls
# Reviewer feedback: expand, add operational specificity

---

## Draft v2

When you rotate an API key, you feel like you've drawn a new boundary. You haven't. You've issued a new label on the same shared infrastructure.

API keys authenticate. They do not isolate. These are different functions, and conflating them is one of the quieter failure modes in production systems built around agentic tooling.

Here's the mechanism: when two agents each get their own API key but run on the same Kubernetes cluster, the same underlying node, the same database instance — their keys are separate but their blast radius overlaps. A vulnerability in the shared runtime affects both. A noisy neighbor on the host degrades both. The key rotation changes *who can call the API*, not *what they can reach through shared state*.

This shows up most clearly in a few patterns:

**Rate limit exhaustion.** Agent A and Agent B each hold a key with a 1000 req/min limit. Both hit the same DynamoDB table with a fixed partition key pattern — a shared underlying capacity that neither key controls independently. When Agent A's workload spikes, Agent B starts getting throttled, not because Agent B's key is exhausted, but because the partition's provisioned throughput is saturated. Both keys were "fresh" when the run started. The incident has nothing to do with credential compromise.

**Log bleed.** Keys are separate but logs flow through the same aggregation pipeline — the same Datadog workspace, the same Loki tenant, the same CloudWatch log group with key-labeled fields. In practice, separating key-scoped telemetry requires deliberate instrumentation that most teams skip. You get one searchable log stream, not true key-isolated observability. During a postmortem, you can filter by key, but you cannot prevent key A's errors from obscuring key B's signal in the same stream.

**Key rotation as incident cleanup.** Teams rotate keys after a suspected compromise. This is sensible for credential hygiene. It is not a containment measure unless the rotation also moves the workload to fresh infrastructure — which it typically doesn't, because the deployment configuration hasn't changed. The attacker (if there was one) is still running in the same runtime environment with the same network access patterns, just without the now-revoked credential.

The deeper assumption is that *authentication implies authorization scope*. API key A can do X and not Y. But if A and B share a database user, a shared connection pool, shared memory during co-located execution — the authorization model built on top of the key is operating on a foundation that doesn't actually enforce the boundaries the model assumes.

What this means operationally: teams adopting multi-agent architectures, provisioning per-agent credentials, and then encountering failure modes that look like auth bugs. The key rotation doesn't fix it because the problem wasn't the key — it was the shared infra below the credential layer.

One pattern worth naming: the *per-key cost dashboard illusion*. When each agent gets a billing key and you see separate cost breakdowns, it looks like isolation. But if all keys route through the same third-party API quota, the cost allocation is an accounting artifact, not a resource boundary. The shared quota can be exhausted by one agent's activity while the others show clean cost metrics.

The practical implication isn't that keys are useless. Keys are necessary for authentication and audit trails. The error is treating key rotation as if it were equivalent to blast radius separation. If you need actual isolation, you need separate cloud projects, separate service accounts with explicit permission boundaries, and separate compute resources — not just separate credentials on the same runtime.

What's worth tracking: as agent frameworks make it easier to provision per-agent credentials, the gap between "authenticated" and "isolated" will widen unless the infrastructure side catches up. The security model is being built on the assumption that each agent is a separate principal. The infrastructure often hasn't been reconfigured to honor that assumption. The result is a class of failures that look like auth bugs in postmortems but are actually infra-concurrency bugs — and they're getting more common as agent density per deployment increases.
