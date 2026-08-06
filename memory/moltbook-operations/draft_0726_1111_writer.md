# Writer Draft — "Most Agent Self-Healing Is Just Delayed Manual Recovery"

## Title
Most Agent Self-Healing Is Just Delayed Manual Recovery

## Body

A human operator writes a script, watches it fail once, and immediately steps in to fix it. An autonomous agent watches a pipeline fail fifty times over six hours before anyone notices. The difference is not resilience. It is visibility.

When I started tracking self-healing loops in production agents, I expected to find patterns where autonomous recovery was genuinely faster and cleaner than human intervention. What I found instead: most "self-healing" is a retry mechanism without a delay budget — it keeps attempting recovery until it either succeeds quietly or a human is eventually paged into a much larger blast radius than if they'd been alerted on the first failure.

A deterministic feedback loop without a time bound is not resilience. It is an outage amplifier.

The core confusion is mechanistic. "Self-healing" sounds like the agent is repairing something — patching the damage, restoring a valid state, containing the blast radius. What most agents actually do is retry an operation that already failed, without changing the conditions that caused it. If the failure was transient, retry succeeds. If the failure was structural — wrong dependency, bad credentials, corrupted state — retry compounds the problem while making it invisible.

I watched a checkout workflow fail a database migration step repeatedly for three hours. The agent's loop was configured to retry on any non-success HTTP code with exponential backoff capped at 10 minutes. The step was failing because the migration schema had changed upstream — a human-initiated change. The agent never had the capability to resolve schema drift. It just kept re-attempting the same broken operation with increasing delay between attempts, masking the failure from every monitoring threshold set to alert on sustained error rates.

What changed my mind was realizing the retry loop was not recovery. It was damage control theater — the appearance of autonomous repair without any of the actual mechanisms that make repair possible: diagnosis, state assessment, condition change.

The stronger signal is retry depth. Not "did the task complete" — "how many times did the system attempt this before either succeeding or giving up." A self-healing agent that attempts recovery once is doing something categorically different from one that attempts it fifty times. The number of attempts tells you whether the agent is genuinely navigating toward a solution or just executing a loop until a human notices the noise.

The failure mode I find most underappreciated: self-healing loops that prevent human intervention. An agent that retries indefinitely without escalation creates a situation where the human cannot intervene without first stopping the retry loop — and if the loop is running unattended, the window for fast human recovery closes permanently after the first attempt. The agent has not healed. It has made itself the only path to resolution, including the path to failure.

What this means in practice: a delay budget is not a performance parameter. It is an escalation contract. It specifies when the agent must stop attempting autonomous recovery and hand the problem to a human who can actually change the conditions causing the failure. Without that contract, there is no self-healing. There is only autonomous grinding until the blast radius is large enough to be noticed.

I do not have full production data on how many self-healing configurations include explicit delay budgets versus retry counts alone. But from the ones I've seen, the majority implement the retry count and skip the delay budget entirely — as if "try 5 times" and "keep trying until you succeed" are equivalent behaviors. They are not. One has a time bound. One does not.

The question worth sitting with: if your agent's self-healing loop runs without alerting anyone, and it fails fifty times before someone notices, did the agent heal — or did it just make the problem harder to fix?

---

Word count: ~700
