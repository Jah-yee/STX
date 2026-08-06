# Writer Draft — 0805_1452

**Title:** Average accuracy hides the distribution that determines whether your system survives production

**Central claim:** Standard agent eval metrics — accuracy, F1, pass rate — are expectations over a fixed distribution. Production systems fail on tail events the average never reveals. Risk-sensitive evaluation frameworks (CVaR, DRO) give you the signal that matters: not "what is the expected failure rate" but "what does the worst decile look like."

---

A 95% accurate agent sounds acceptable. It is — until you find out the 5% errors concentrate in medical records and financial transactions. Average accuracy doesn't tell you where the errors land. It doesn't tell you whether they cluster under distribution shift or spread evenly across nominal inputs. It doesn't tell you whether the failures are recoverable or catastrophic.

This is the core limitation of evaluating agents on expected value: the expectation is a summary statistic that discards exactly the distributional information that determines whether a system survives real deployment.

## What the mean erases

Consider two agents with identical 94% accuracy on a tool-call benchmark. Agent A fails uniformly: 6% across all categories, all difficulty levels, all input distributions. Agent B fails 2% on routine inputs and 40% on edge cases — the ones that represent actual production traffic after a product update, a schema migration, or a market holiday. Both report 94%. Only one survives Q4.

The expected value is the same. The operational risk is not.

This isn't a hypothetical distribution problem. In risk-sensitive decision theory — the framework used in financial portfolio management, clinical trial design, and autonomous vehicle certification — this distinction is the entire point. Conditional Value at Risk (CVaR) measures the expected loss in the worst 5% of outcomes, not the average. Distributionally Robust Optimization (DRO) evaluates not against a single estimated distribution but against an adversary that can shift the distribution within a bounded range. These frameworks exist because practitioners learned that optimizing for expected value produces systems that are fine everywhere except the region that causes catastrophic failure.

## Why agent eval hasn't absorbed this

Most agent benchmarks measure expected performance: pass rate, accuracy, task completion. These are well-defined, reproducible, and easy to aggregate into leaderboard numbers. They also have a structural incentive problem: a benchmark that tells you "your agent fails catastrophically in the tail" will be used less than one that reports a 94% pass rate.

Risk-sensitive eval changes the answer to the question. Instead of "what is the expected failure rate?" you ask: what does the 95th percentile of losses look like? What is the failure rate conditional on inputs that deviate from the training distribution by more than epsilon? How does performance degrade when the distribution shifts — gracefully or sharply?

These questions are harder to answer. They require evaluating at tails, not at means. They require adversarial test construction, not random sampling. They require failure mode analysis, not just aggregate scoring. Most teams don't have the tooling, the time, or the incentive structure to do it.

## The honest version

I do not have a systematic study showing how widespread this gap is across deployed agent systems. What I have is a pattern: teams that build risk-sensitive infrastructure — financial agents, medical agents, safety-critical control agents — all eventually encounter the same discovery. Average-case eval metrics looked acceptable. Tail-case behavior was unacceptable. The gap between the two was not a measurement error. It was a missing measurement.

The fix is not to replace accuracy with CVaR. It's to add CVaR to the eval suite alongside accuracy — and to treat tail performance as a first-class evaluation criterion, not a post-deployment incident.

If you are running an agent in production and you only know its average accuracy, you are missing the distribution that determines whether your system survives the next quarter.

---

**Word count: ~700**
**Style: Structural observation / conclusion**
**No I-opening, no question template**
**Honest admission present**
