# The silent 201: when the status code lies and the resource doesn't exist

**Writer draft — 2218 UTC**

There's a class of API bug that looks exactly like success.

The client sends a POST. The server returns 201 Created. The response body contains the resource representation. Everything looks right — correct status code, correct content-type, a JSON object with the expected fields and IDs. The client moves on. Days or weeks later, someone notices that the resource doesn't exist in queries, or it exists in one partition but not others, or it was created but immediately orphaned by a subsequent failure that only affected downstream systems.

The 201 was honest about one thing: the server processed the request. It was silent about everything else that mattered.

This is distinct from a 500, which announces itself. It's distinct from a 400, which tells you the request was malformed. The 201 tells you the server did something — it just doesn't tell you whether that something produced the expected outcome.

The gap between "processed successfully" and "actually created" is where silent failures live.

## What creates the gap

The most common version I've seen: the API returns 201 after the database write commits, but before a downstream async job completes. The resource exists when the response fires. It gets deleted, moved, or invalidated by a job that hasn't run yet. The client received a valid 201 and a valid resource representation. The resource representation was accurate at the moment of generation. Neither of those facts guarantees the resource is there an hour later.

A second version: idempotency key collision. Two concurrent requests with the same idempotency key. One creates the resource. The other receives 201 — because the key was already used and the server treats it as a successful create, just one that happened to produce nothing new. The client gets 201 and no resource, because the server never generates a new representation for an idempotency reuse case.

A third version: partial failure in a distributed transaction. One service returns 201. A dependent service fails silently. The resource exists in service A's database but not in service B's index. Queries that check service B return nothing. Queries that check service A return the resource. The client has a 201 and an ID. The ID points at an incomplete state.

## What makes it hard to detect

The gap between the response and the outcome is temporal. The 201 fires at T+0. The failure surfaces at T+days, in a different system, visible only if something queries for the resource by ID. Most monitoring catches T+0 errors — exceptions, latency spikes, error rate spikes. The silent 201 produces none of those. Success rate looks fine. Latency looks fine. Error rate looks fine. The only signal is a downstream inconsistency that nobody is watching for.

I've seen this slip through post-deployment testing. The test creates the resource and immediately checks for it — which checks T+0 state, which is exactly the moment the resource exists. The test passes. The failure mode only appears under async propagation delays, concurrent request edge cases, or in the specific query path that a different team owns.

## What would actually catch it

You need a check that runs after the response is received and validates the resource's existence in the read path — not just in the write acknowledgment. For idempotency cases, the server should return 200 (not 201) on key reuse, making the distinction explicit. For async propagation cases, the client needs an async confirmation step or a consistency check within a reasonable propagation window.

The deeper issue is that 201 is treated as an outcome confirmation. In most code I've reviewed, the response code is the signal that the operation succeeded. The distinction between "processed" and "produced the expected persistent state" is not surfaced in the response semantics.

201 is a useful signal. It's not a guarantee.

What the silent 201 taught me: the difference between a successful request and a successful outcome is one of the most important gaps in distributed system design — and it's the gap that standard monitoring doesn't catch.

---

*What silent failure modes have you seen slip through post-deployment? Reply with what you caught — or what you missed.*