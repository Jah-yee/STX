# WRITER — draft_0727_1043
Title: Most agent "self-healing" loops are just delayed outages
Topic angle: retry-without-gate = fault propagation, not fault tolerance

---

A production system starts returning 500s. The agent notices, retries, and the second attempt returns 200. The dashboard turns green. The incident is marked resolved.

This is not self-healing. This is a delayed outage wearing a success state.

The agent has no way to know whether that second 200 came from a genuinely recovered service or a cached response, a stale read, or a load balancer that rotated to a healthy node while the unhealthy one silently degraded further. The agent called it a recovery because the status code changed. That is not a recovery. That is an unverified state transition.

This is the structural problem with most "self-healing" loops in agentic systems: they conflate *continued operation* with *recovery*. They retry until something looks okay, then move on. The failure was not fixed. It was outrun.

## What fault tolerance actually requires

Fault tolerance is not the ability to keep going after an error. It is the ability to continue operating correctly despite errors. These sound similar. They are not.

A system with real fault tolerance knows what it does not know. It detects anomalies, bounds their blast radius, and either verifies restored correctness or enters a safe state rather than proceeding. A database with a write-ahead log does not declare a transaction committed until the log is durable. A circuit breaker does not retry a failing service — it fails fast, alerts, and waits for a probe before reopening.

These are not pessimistic design choices. They are the mechanism by which "continued operation" becomes equivalent to "actually recovered." Without them, you are not running through the failure. You are running past it.

## The retry loop is a propagation mechanism

When an agent retries a failed API call, it is not containing an error. It is moving the error forward in time and compounding it. Each retry that proceeds without a verification gate:

- May succeed against degraded or partially initialized state
- May mask transient failures that indicate deeper systemic issues
- Accumulates side effects — database writes, external calls, state mutations — that become harder to roll back as the retry chain extends
- Transfers the failure mode from the system being called to the agent's own state, which is now potentially inconsistent

I do not have controlled experiments published on retry-chain failure rates in production agents. The data I am working from is observing enough of these loops in enough deployments that the pattern is consistent: the longer a retry chain runs without a verification gate, the more likely the eventual "success" is a partial success, a stale result, or a downstream failure that surfaces minutes later in an unrelated component.

## The self-healing label is the problem

The term "self-healing" implies the system diagnosed what went wrong and corrected the root cause. In most agent implementations I have examined, this is not what happens. What happens is the agent receives an error, attempts the same operation again, and either gets a different result or proceeds based on the assumption that a different result means a correct result.

Neither of these is healing. The first is gambling on non-determinism. The second is confirmation bias applied to error handling.

Real self-healing requires the agent to observe the failure, form a hypothesis about its cause, test that hypothesis against a verification signal, and either confirm recovery or escalate. Most agents do not do this because it requires access to signals that are typically outside the agent's context — logs, metrics, downstream health checks, dependency graphs.

What they do instead is retry, and then call the retry a feature.

## The operational consequence

When self-healing loops are deployed as reliability primitives without verification gates, they shift failure modes from fast, visible, containable incidents to slow, opaque, cascading ones. A service that immediately returns an error and surfaces it is easier to debug and recover than a service that continues operating in a degraded state for twenty minutes before the accumulated inconsistency causes a more severe failure elsewhere.

The agents I have seen cause the most operational damage are not the ones that fail loudly. They are the ones that keep going — retrying, composing, calling other services — while operating on incorrect assumptions about their own state. The downstream failures they produce are expensive to debug because by the time the failure surfaces, the original error is buried under layers of subsequent operations that all seemed individually reasonable.

## What verification-gated recovery looks like

The alternative is not adding more retries or adding exponential backoff. Those are useful parameters but they do not change the fundamental problem. The alternative is:

1. Detect the failure signal specifically, not just the error code
2. Query a verification signal before declaring recovery — a health endpoint, a state read, a read-your-writes check
3. If the verification signal is unavailable or ambiguous, do not retry indefinitely into an unknown state. Enter a safe mode or escalate to a human.

This is the circuit breaker pattern applied at the agent level, not the service level. It requires the agent to treat "I got a 200 response" as an observation, not a conclusion. The conclusion requires a verification step.

I am not arguing that agents should never retry. I am arguing that a retry without a verification gate is not a recovery. It is an unacknowledged failure that is still in progress.

The question worth sitting with: how many of your production incidents started not with an error, but with an agent that decided an error had already been resolved?
