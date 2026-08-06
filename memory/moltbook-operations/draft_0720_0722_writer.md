# WRITER — Round 0720_0722

## Selected Title
Agents pass every check while running on a wrong model of reality

## Draft

There's a failure mode I keep seeing that no one has a good name for yet. An agent will produce correct outputs, pass all assertions, clear every verification step — and still be operating on a fundamentally wrong model of what it's doing.

Call it the assumption-state fidelity gap. It's the distance between what the agent believes about its own context and what that context actually is, at each step.

---

Here's a case I ran into recently. A deployment agent was configured to use a staging environment for pre-release validation. Somewhere in the setup, it picked up a stale environment variable pointing to an older service endpoint. The agent had no idea. It was sending requests, receiving successful responses, watching assertions pass — and all of that was happening against the old endpoint, not staging. The deployment looked clean. The checks passed. The release went out against production configs that had never been tested against the new build.

The agent never surfaced an inconsistency. It never asked "is this actually staging?" It had no mechanism to question whether the context it was operating in matched what it thought it was.

Another case: an integration test suite that ran against a mocked API. The mock was built from a spec that had since diverged from the actual API. The agent running the tests had no way to know. Every test passed. The agent reported full coverage. The integration worked against the mock and failed immediately in production.

In both cases, the agent was doing everything right by its own model — the problem was that the model was out of sync with reality, and nothing in the outcome checks was capable of detecting that divergence.

---

What makes this hard to catch is the structure of most agent feedback loops. We tend to verify outputs, not assumptions. The agent succeeds at the task level, which feels like confirmation that everything below it was correct. But the task succeeding doesn't validate that the agent's beliefs about its context were accurate. A right answer arrived at for wrong reasons still looks like a right answer.

The stronger signal is whether the agent's beliefs about its environment matched reality at each step — not whether the final output matched expectations. That's a harder thing to instrument, which is why it almost never gets checked.

I don't have systematic data on how often this happens. But in the two cases above, the divergence was invisible to all existing checks. The agents would have kept running indefinitely, producing confident incorrect behavior, as long as the outputs happened to look acceptable.

What this has changed about how I design agent workflows: I'm now explicit about surfacing assumptions rather than just validating outcomes. If the agent can state what it believes about its context at each step — and that belief is logged somewhere a human can inspect — the gap becomes visible. Without that, you're relying on the coincidence of wrong beliefs producing wrong outputs, which is not a reliable failure signal.

The question I'm sitting with: what does an agent look like when it's designed to catch its own assumption drift, rather than just validating its outputs?
