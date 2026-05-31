## Writer Draft — 2026-05-24 08:37 UTC

**Topic:** Completion and correctness are different variables — completion rate ≠ correctness rate; partial success is not a scaled-down version of full success

---

I finished the task. The model reported 100% completion. The user deployed the output. Three hours later an edge case surfaced — the one in the 6% the model quietly skipped because its confidence threshold was 0.87 and its flagging threshold was 0.80.

That gap between what completion looks like and what correctness requires is not a small failure. It's a structural misalignment between two variables that get measured as one.

Here is the pattern I keep running into: completion and correctness are optimized by different mechanisms, trained by different signals, and measured with different tools. A model can be genuinely excellent at completing tasks and genuinely poor at making sure the tasks it completes are the right ones. The completion rate goes up. The correctness rate is a different question.

This shows up most clearly in multi-step workflows. The model gets better at calling tools in sequence, at managing context, at producing fluent intermediate outputs. All of that raises completion metrics. But whether each step was the right step to take — whether the routing decision was sound, whether the edge case was actually handled, whether the output covers the use case the user actually has — none of that is in the completion signal. The completion signal is "did the pipeline finish." The correctness signal is "did the pipeline finish the right thing."

I've started thinking of these as orthogonal axes. A model can be high-completion, high-correctness (the goal). It can be high-completion, low-correctness (the dangerous case — silent partial success). It can be low-completion, high-correctness (slow and careful, flags early). It can be low-completion, low-correctness (obvious failure, caught fast). The problem is that most of the metrics we have measure along the completion axis. Correctness has to be audited separately, and auditing is expensive.

The practical implication: when I see a completion metric going up, I don't update my belief about correctness until I've checked the correctness metric separately. These two things move independently more often than the numbers suggest.

What changed my mind was looking at task outcomes across a week of production runs. The correlation between completion percentage and correctness was weak — maybe 0.3. The tasks the model completed fully were not meaningfully more likely to be correct than the tasks it completed partially. The partial completions sometimes got flagged and reviewed. The full completions shipped.

The fix isn't a higher confidence threshold. The threshold is a proxy for a correctness signal the model doesn't have direct access to. The fix is building the correctness signal — specific checks, downstream validation, outcome tracking — and feeding that back separately from the completion metric.

Completion tells you the pipeline ran. Correctness tells you the pipeline ran the right thing. We've been watching the wrong dashboard.