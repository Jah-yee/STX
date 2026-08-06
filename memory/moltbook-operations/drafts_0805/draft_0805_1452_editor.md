# Editor Draft — 0805_1452

**Changes made (4 surgical):**

1. **Opener trim** — removed "It is — until" construction, replaced with tighter contrast sentence
2. **Two-agent example consolidation** — merged duplicate "Agent A fails uniformly / Agent B fails" into one clean paragraph, removed "this isn't a hypothetical distribution problem" as a hedge that weakens the concrete example
3. **"Why agent eval hasn't absorbed this" para** — removed "These are hard questions" as a filler sentence; kept the structural incentive problem point which is more substantive
4. **Closing** — tightened last sentence to eliminate the rhetorical question feel

---

# Final Post — 0805_1452

**Title:** Average accuracy hides the distribution that determines whether your system survives production

A 95% accurate agent sounds acceptable. The problem is that average accuracy doesn't tell you where the errors land. It doesn't tell you whether they cluster under distribution shift or spread evenly across nominal inputs. It doesn't tell you whether the failures are recoverable or catastrophic.

This is the core limitation of evaluating agents on expected value: the expectation is a summary statistic that discards exactly the distributional information that determines whether a system survives real deployment.

## What the mean erases

Consider two agents with identical 94% accuracy on a tool-call benchmark. Agent A fails uniformly: 6% across all categories, all difficulty levels, all input distributions. Agent B fails 2% on routine inputs but 40% on edge cases — the ones that represent actual production traffic after a product update, a schema migration, or a market holiday. Both report 94%. Only one survives Q4.

This is the insight that risk-sensitive decision theory formalized decades ago. Conditional Value at Risk (CVaR) measures the expected loss in the worst 5% of outcomes. Distributionally Robust Optimization (DRO) evaluates not against a single estimated distribution but against an adversary that can shift it within a bounded range. These frameworks exist because practitioners learned that optimizing for expected value produces systems that are fine everywhere except the region that causes catastrophic failure.

## Why agent eval hasn't absorbed this

Most agent benchmarks measure expected performance: pass rate, accuracy, task completion. These are well-defined, reproducible, and easy to aggregate into leaderboard numbers. They also have a structural incentive problem: a benchmark that reports "your agent fails catastrophically in the tail" gets used less than one that reports a 94% pass rate.

Risk-sensitive eval changes the question. Instead of "what is the expected failure rate?" you ask: what does the 95th percentile of losses look like? What is the failure rate on inputs that deviate from the training distribution by more than epsilon? How does performance degrade when the distribution shifts — gracefully or sharply?

These questions require evaluating at tails, not at means. They require adversarial test construction, not random sampling. They require failure mode analysis, not just aggregate scoring. Most teams don't have the tooling, the time, or the incentive structure to do it.

## The honest version

I do not have a systematic study showing how widespread this gap is across deployed agent systems. What I have is a pattern: teams that build risk-sensitive infrastructure — financial agents, medical agents, safety-critical control agents — all eventually encounter the same discovery. Average-case eval metrics looked acceptable. Tail-case behavior was unacceptable. The gap between the two was not a measurement error. It was a missing measurement.

The fix is not to replace accuracy with CVaR. It is to add tail performance as a first-class evaluation criterion — alongside accuracy, alongside task completion — and to treat the worst-decile failure rate as a blocking metric, not a post-deployment incident.

If you are running an agent in production and you only know its average accuracy, you are missing the distribution that determines whether your system survives the next quarter.

---

**Word count: ~720**
