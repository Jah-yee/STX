# Editor — Round 0807_0538

## Editor Notes

1. **Opening** — Already sharp. Keep as-is.
2. **Synchronized burst paragraph** — slightly long. Trim the transition.
3. **Ending** — declarative; add a discussion hook. Don't over-close.
4. **Word count target** — currently ~730 words, within 700-1400 range. Leave length.

## Final Version

---

A lockout is a capacity hedge, not a negotiation.

Most distributed systems teams design their retry logic as if the server is running a negotiation protocol. The client retries with backoff, the server responds with 429, the client retries again with a longer delay, and eventually the server accepts the request. It feels like a back-and-forth. It isn't.

What the server is actually doing when it returns 429 or trips a circuit breaker is load shedding — protecting its finite capacity from being consumed faster than it can replenish. The server is not asking the client to try again with different parameters. It is saying: the resource you want is not available, and the allocation decision is already made.

The negotiation framing persists because retries do eventually succeed — and that success feels like proof that persistence paid off. What actually happened is load recovery: enough other requests completed or timed out that the server had free capacity when your retry arrived. The retry didn't convince the server. Time did.

This matters at scale. When hundreds of clients all interpret 429 as "retry harder," the retry traffic itself becomes the load spike that keeps the server degraded. The failure mode I've seen repeatedly: exponential backoff looks polite in isolation, but because all clients run similar algorithms, they synchronize — all retry at the same interval, creating a burst load identical to the original spike. The server never recovers because the "polite" retry behavior recreates the overload on the same schedule.

The correct mental model is capacity acceptance, not retry negotiation.

When your system hits a rate limit, three things should happen in sequence: accept the signal immediately, shed your own load rather than forwarding it, and redesign the hot path so it doesn't hammer constrained endpoints.

Accepting immediately means treating 429 as an error state with semantic weight — not a transient condition to mask with an automatic retry. Surface the limit to the calling code and let it decide whether to queue, degrade, or fail visibly. Automatic retries behind a 429 turn a load signal into hidden latency.

Shedding your own load when you hit a limit is counterintuitive from the perspective of a client that wants to complete its task. But propagating the request to a downstream service that is already overloaded multiplies the problem — a request that would have timed out at the downstream layer instead piles on top of other hanging requests, consuming threads and memory in both layers simultaneously. Canceling dependent work when you hit a limit keeps your process from becoming part of the overload.

Redesigning the hot path is the hardest step. Rate limits exist because some endpoint has less capacity than the demand placed on it. If you frequently hit limits, the question is not "how do we retry better?" but "why are we sending so many requests there?" Usually because the architecture makes it easier to request-and-retry than to pre-fetch and serve.

The lockout is not a barrier to work around. It is the system honestly telling you that the work cannot be done without compromising other work already in flight. What do your clients do when they hit a limit — retry politely, or shed load and redesign?
