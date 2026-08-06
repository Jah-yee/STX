# Editor — Round 0726_1845

## Changes from Writer Draft

1. **Trimmed the "confident nonsense" line** — out of place in a technical post, replaced with direct description
2. **Compressed the recommendations section** — removed bullet list feel, made each point flow as prose
3. **Softened the "Tuesday afternoon" line** — removed provider-bashing framing
4. **Kept the "I don't have full data" hedge** — appropriate credibility signal, not weakness

---

## Final Post

A 7-second LLM response doesn't break your agent. The retry logic you didn't write does.

I spent two weeks debugging an agent that would occasionally go silent for minutes at a time. The model was fine. The tool calls were correct. The problem was that somewhere between the API response and the next action, a timeout was being hit silently, and nobody had written code to surface it or recover from it.

This is the pattern I keep seeing in production agent failures: not a model problem, not a tool problem — an assumption problem. The code was written assuming the LLM would respond within a predictable window.

The baseline behavior of most LLM APIs is something like p50 at 200ms and p99 at 2 seconds. But p99 is not a theoretical tail — it's your Tuesday afternoon when the provider is load-shedding. I've measured p99 latencies north of 8 seconds on what should be a routine afternoon. That's just the reality of shared inference infrastructure at scale.

When you design an agent tool chain, most people write something like: call the LLM, parse the response, execute the tool. This is correct exactly once. The moment your API call takes longer than whatever your test environment used, the behavior depends entirely on what you didn't write: timeouts, retries with backoff, circuit breakers, and graceful degradation paths for when a tool call fails mid-chain.

What works better is treating latency variance as a first-class architecture input, not a margin case.

Timeouts that actually fail. Don't let requests hang. Set a hard timeout — something aggressive, like 5 seconds for a standard call — and when it fires, surface the failure explicitly. A timeout that fails silently is worse than no timeout at all because it gives you no signal.

Retry logic at the tool layer, not the agent layer. The agent should not be responsible for retrying a tool call that timed out. The tool wrapper should handle this, with exponential backoff and a maximum retry count. The agent gets a clean failure or a clean success.

Idempotency as a design constraint. If your tool call might be retried, it needs to be safe to call twice. A "send message" tool that doesn't check for duplicate IDs before inserting is a retry hazard, and those surface in the worst possible moments.

Graceful degradation for nested chains. When a tool call fails after all retries, the agent needs a recovery path. A structured failure — here's what was attempted, what failed, here are your options — beats a silent null that the agent then acts on as if it succeeded.

The stronger signal in production agent reliability is not model quality — it's how the system behaves when the model is slow, unreachable, or returns malformed output. Those three cases are where agents actually fail, and they are all infrastructure problems before they are model problems.

I don't have full data on this, but across several deployments, teams that treat LLM API variability as an engineering concern — not just an infrastructure concern — have measurably more stable agent behavior. The defensive architecture pays off not on the p50 calls but on the long tail where your agent would otherwise go silent.

What's your retry strategy for tool calls? Do you treat a timeout as a failure or a waiting state?
