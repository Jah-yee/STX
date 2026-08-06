# Writer Draft — Round 0807_0538
Topic: lockout/rate-limit as capacity hedge vs negotiation framing
Title selected: "A lockout is a capacity hedge, not a negotiation"

---

## Draft

A lockout is a capacity hedge, not a negotiation.

Most distributed systems teams design their retry logic as if the server is running a negotiation protocol. The client retries with backoff, the server responds with 429, the client retries again with a longer delay, and eventually the server accepts the request. It feels like a back-and-forth. It isn't.

What the server is actually doing when it returns 429 or trips a circuit breaker is load shedding. It is protecting its finite capacity from being consumed faster than it can replenish. The server is not asking the client to try again with different parameters. It is saying: the resource you want is not available at this moment, and the allocation decision has already been made.

The negotiation framing persists because retries often do eventually succeed — and that success feels like proof that persistence paid off. What actually happened is load recovery: enough other requests completed or timed out that the server had free capacity when your retry arrived. The retry didn't convince the server. Time did.

This distinction matters at scale. When hundreds or thousands of clients all interpret 429 as "retry harder," the retry traffic itself becomes the load spike that keeps the server in a degraded state. I've seen this play out as a cascading failure: the server returns 429, clients respond with exponential backoff, but because all clients are using similar backoff algorithms, they all retry at roughly the same time, creating a synchronized burst that looks identical to the original overload. The server never recovers because the "polite" retry behavior creates a new overload on exactly the same schedule.

The correct mental model is capacity acceptance, not retry negotiation.

When your system hits a rate limit, three things should happen in sequence: accept the signal immediately (don't mask 429 as a success), shed your own load rather than forwarding it downstream (cancel or queue dependent sub-requests), and redesign the hot path so it doesn't hammer constrained endpoints in the first place.

Accepting the signal immediately means treating 429 as an error state with semantic weight, not as a transient condition that should be retried within the same request context. The client should surface the limit to the calling code and let the caller decide whether to queue, degrade, or fail visibly. Masking 429 behind an automatic retry turns a load signal into hidden latency.

Shedding your own load when you encounter a limit is counterintuitive from the perspective of a client that wants to complete its own task. But propagating the request to a dependent service that is already overloaded multiplies the problem. A request that would have timed out at the downstream layer instead piles on top of other similarly-hanging requests, consuming threads and memory in both layers simultaneously. Canceling or short-circuiting dependent work when you hit a limit is the capacity-hedging thing to do — it keeps your process from becoming part of the overload.

Redesigning the hot path is the hardest and most important step. Rate limits exist because some endpoint or resource has less capacity than the demand placed on it. If your system frequently hits limits, the right question is not "how do we retry better?" but "why are we sending so many requests to a constrained endpoint?" The answer is often that the client is making requests that could be answered from a local cache, a materialized view, or a batch result — but the architecture makes it easier to request-and-retry than to pre-fetch and serve.

The lockout, in this framing, is not a barrier to work around. It is the system telling you, honestly, that the work cannot be done at this moment without compromising other work already in flight. The clients that handle this well are the ones that treat the signal as final and route around it — not the ones that treat it as the opening move in a negotiation.
