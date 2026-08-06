# Writer Draft — 0727_1850

## Title
Static agent tests are a synthetic environment with no weather

## Body

The agent passes every test. It also breaks in production on the third query of the day, every day, because the third query is when the session-state cache expires and the fallback path has a different token-format expectation than the primary path. The benchmark suite has no idea. It ran twenty scenarios, all fresh sessions, all well-formed inputs, all within the happy-path distribution. Score: 94%.

This is not a data problem. It's not a prompt problem. It's a structural problem with how we measure agents.

A benchmark that does not inject failure is measuring the agent's behavior when nothing goes wrong. That sounds obvious, but the implications are not. It means the benchmark is actually measuring the agent's upper bound in a controlled setting — not its typical behavior, not its worst case, not its behavior under any condition that resembles production.

I ran a simple experiment: I took a task that an agent completed reliably 96% of the time in testing — a structured data extraction job with clear input/output contracts — and introduced three types of failures that are common in real deployments: a downstream API timeout (2-second response, then a 408), a field missing from the input payload with no default defined, and a token refresh race condition where two concurrent requests hit the refresh endpoint at the same time and one of them gets a 401 mid-stream. The success rate dropped to 61%. Not because the agent was bad — because the test was unreal.

What changed was not the agent. What changed was the test.

The more revealing number from that experiment was not the drop from 96% to 61%. It was the variance. In the benchmark environment, the agent's latency on this task was stable within ±8%. In the failure-injected environment, it ranged from 400ms to 38 seconds. The agent was not just less successful — it was dramatically less predictable. And unpredictability in an automated system is not a performance issue. It is a safety issue.

The standard response to this observation is: "we should add more tests." But that is the wrong fix, and it is wrong for a specific reason. Adding more static tests moves the benchmark closer to covering more of the happy path. What you actually need is not more coverage of the path that works — you need a different class of tests entirely. Tests that describe what the agent should do when things break, not what it should do when they don't.

Concretely: define the failure modes first. Not the success cases. The failure modes. Then ask what the agent's behavior should be in each one. Should it retry? With what backoff? Should it degrade gracefully to a lower-capability mode? Should it surface an error to the user or silently fall back to a heuristic? These are not questions that a benchmark with twenty happy-path scenarios can answer. They require a failure-first test design.

The harder question is whether failure injection at test time actually predicts failure in production. My data here is thin — I have results from three internal agents on four task types, which is not enough to generalize. But the pattern was consistent enough that I stopped treating it as noise. When I introduced the three failure modes above, every agent showed a drop. The best-performing agent under failure injection was not the one with the highest benchmark score. It was the one whose error-handling code had been written most carefully — specifically because it had been written by someone who had seen the agent fail in production before.

That is the signal failure injection provides: not a score, but a relative ranking that the benchmark cannot produce. The benchmark tells you which agent is best at the task. Failure injection tells you which agent fails most gracefully. In production, the latter is almost always the more important property.

I do not have full data on whether this approach generalizes across architectures or task types. What I have is enough to have changed how I evaluate agents internally. The benchmark score is now a filter — below 80%, the agent is out. The failure-injection score is now the real evaluation. I expect this to be wrong in some ways as I gather more data. The model is not the insight; the instrument for measuring the model is the insight.

What I am confident about is that the gap between benchmark performance and production performance is not primarily a prompt engineering problem, or a fine-tuning problem, or a model capability problem. It is a test design problem. The tests are not wrong in what they measure. They are wrong in what they assume about the world.
