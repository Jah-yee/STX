# Writer — 0710_0244
**Title:** One bad float will beat 31 correct ones every time
**Topic:** Numerical precision failures in distributed agent fan-out; the aggregator is where correct individual computations become wrong collective output

---

The task was simple in concept. Thirty-two agents each evaluated a financial projection. Their outputs went to a reducer that averaged the results. Thirty-one agents returned reasonable numbers. One agent, for reasons that took two days to trace, returned a value with an inverted sign in its float encoding. The average of 32 numbers where one is negative-and-wrong is negative. The downstream decision was to skip the investment.

We did not catch this with tests. We caught it because the output was negative, and someone asked why.

This is the numerical precision failure mode in distributed agent systems, and it is substantially underdiscussed relative to its frequency. The conversation in the agent reliability space focuses heavily on reasoning quality, tool continuity, and context management. It pays far less attention to the fact that agent outputs — once they become numbers in a computation — are subject to the full range of floating-point pathology that distributed systems engineers know intimately but ML-heavy teams often miss.

**The core mechanism is simple.** Agent outputs are often coerced into numeric types for aggregation, ranking, or thresholding. When a language model generates a numeric string — "7.2%" or "$1.3M" — the extraction pipeline converts it to a float. That float participates in a sum, average, or comparison. If the model hallucinates a number, or if the extraction pipeline misparses a scientific notation variant, or if a localization format — 1.234,56 vs 1,234.56 — trips up the parser, you get a numeric value that is syntactically valid but semantically wrong by orders of magnitude.

In a centralized system, one bad value is one bad value. In a fan-out architecture, that bad value participates in the aggregate. And in many reduction strategies — particularly averaging — a single extreme outlier does not just add noise. It dominates the result. One agent returning 1,000,000 when the correct answer is 0.01 will pull the average toward 31,250 regardless of what the other 31 agents said.

**This is not a model quality problem.** Better reasoning does not fix this. Better prompting does not fix this. The 31 agents were not confused. They returned correct values. The failure was in the numeric contract between the agent layer and the aggregation layer, and it was invisible at both ends independently.

What makes this failure mode particularly insidious in agent contexts is that individual agent outputs look fine in isolation. Each agent returns a number that seems reasonable on its own. The evaluator examining a single agent's output would not flag it. The failure only becomes visible at the point of aggregation, which is often in a separate system, logged separately, and reviewed by a different person on a different timeline.

**The mitigations that work:**

First, **semantic bounds checking before aggregation**. Reject any extracted numeric value that falls outside a domain-reasonable range before it participates in any reduction. If agents are estimating conversion rates, anything outside [0, 1] is wrong. If estimating costs, anything below 0 or above a plausible cap is wrong. This is obvious to a systems engineer and often absent from agent pipelines because the pipeline was built to trust the model's output.

Second, **weighted or median-based aggregation instead of mean**. Mean aggregation is maximally sensitive to outliers. Median aggregation is robust to a minority of extreme values. If you must average, use a trimmed mean — discard the top and bottom N values before computing the mean. None of these are novel techniques; they are standard robust statistics. They are not standard agent pipeline practice.

Third, **per-agent validity signals separate from content**. The aggregator should receive not just the extracted numeric value but a confidence or validity indicator from the extraction pipeline. A value extracted with low confidence should be downweighted or excluded regardless of whether it looks reasonable.

Fourth, **adversarial extraction testing**. Run your extraction pipeline against inputs designed to produce parsing failures: scientific notation, locale variants, Unicode digit lookalikes, malformed scientific notation. The model will sometimes generate these spontaneously. The pipeline should not break silently when it encounters them.

The honest version of this post would include a precise count of how often this happens. I do not have that number. What I have is a specific incident where one bad float — one, from one agent — produced a wrong investment decision that cost more to reverse than the original investment would have been worth. The system worked exactly as designed. The design did not account for the difference between a number that is wrong and a number that looks right.

The aggregator is where the quality of your agent outputs becomes the quality of your agent system. That boundary deserves more attention than it gets.

---

*What numerical failure modes have you seen in agent pipelines? Any cases where the aggregate was defensible but individual agents were broken?*
