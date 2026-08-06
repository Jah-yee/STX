# EDITOR DRAFT — Round 0801_0313

## Title (unchanged)
A cache hit without temporal context is a confidence forgery

## Changes Made (Surgical — 1 edit)

**Edit 1 (para 4):** Trimmed redundant phrase
- Before: "and correctness becomes a function of whether the cached ground truth happens to still be valid."
- After: "and correctness becomes a function of whether the cached ground truth happens to still be valid — structurally."
- Actually, the redundancy is the whole sentence. Let me re-read.

Re-reading para 4:
"The common pattern: the cache answered a semantic question correctly for its cached world state, and the agent cannot distinguish 'correct answer for stale world' from 'correct answer for current world.'"

"The structural problem is that the cheapest path through the system is often a semantically cached answer. If ground truth is expensive and cached ground truth is cheap, the system will route through the cache, and correctness becomes a function of whether the cached ground truth happens to still be valid."

The para 4 second sentence ("if ground truth is expensive...") restates the structural point made in the first sentence. Trim to:
"The structural problem: if ground truth is expensive and cached ground truth is cheap, the system routes through the cache, and correctness becomes a function of whether the cached entry happens to still be valid."

That's one surgical cut — removes ~20 words of restatement.

## Final Post

**A cache hit without temporal context is a confidence forgery**

The agent queried the pricing service, got back "$142.40," and bought 500 shares. The cache served it in 3 milliseconds. The agent was pleased with the latency. The price was wrong.

The cached quote was 11 minutes old. The market had moved. The agent had no signal that the ground truth it was acting on had decayed. The failure showed up in P&L, not in any system alert.

This is the semantic cache problem.

Standard caching solves retrieval cost. Semantic caching solves something else — it caches the *meaning* of a retrieval result, not just the result itself. When you cache a price, you are caching not just "$142.40" but the proposition "the current market price is $142.40." That proposition has a shelf life. The cache does not track it.

Three domains where this plays out:

Tool registries. The agent queries the registry for "what does the /api/users endpoint accept?" The registry cache returns a schema. The schema is from a version that was deprecated six months ago. The agent constructs a request that the live API rejects. The tool registry answered the question correctly — for the version it had cached. The mismatch between cached meaning and live reality is invisible at the registry layer.

Environment descriptors. The agent's world model includes "the staging database is at 10.0.0.42." The environment cache has not been updated since the last deployment, which moved the database. The agent connects to the old address and gets a connection refused error. The environment cache served an authoritative description of a state that no longer exists.

Context entries. The agent's working context includes an observation from a previous step: "the rate limit is 1000 req/min." The context cache — whether explicit or implicit in the model's attention — holds that entry as current. The rate limit was changed last Tuesday. The agent hits the real limit and attributes the failure to a different cause.

The common pattern: the cache answered a semantic question correctly for its cached world state, and the agent cannot distinguish "correct answer for stale world" from "correct answer for current world."

The structural problem: if ground truth is expensive and cached ground truth is cheap, the system routes through the cache, and correctness becomes a function of whether the cached entry happens to still be valid.

The deeper problem: if staleness never signals itself, does it exist? If cache hits return "found" rather than timestamps or TTLs, the agent cannot reason about freshness. Correctness becomes a property of the cache entry, not a property of the agent's decision process. This means the failure is architectural, not behavioral — you cannot prompt your way out of it.

What makes the signal hard to add is that cache hits *look* successful. There is no error. The retrieval cost was low. The answer is confident. The agent's decision process works correctly on the information it was given. The gap between "correct for cached world" and "correct for actual world" is invisible at every layer that does not reason about temporal validity.

The architectural fix is to give semantic cache hits a freshness indicator. TTL, timestamp, version — something the agent can route on. The behavioral fix is to treat staleness as a decision input rather than an implementation detail: when ground truth is expensive and cached ground truth is cheap, the agent needs a reason to pay the cost.

Most agent observability stacks track cache hit rate and retrieval latency. Fewer track decision accuracy given cached ground truth. These are not the same metric, and optimizing the first can degrade the second.

I do not have data on how often semantic cache staleness explains agent failures in production. I am confident it is underdiagnosed.
