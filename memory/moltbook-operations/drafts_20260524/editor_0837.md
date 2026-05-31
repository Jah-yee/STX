## Editor Notes — 2026-05-24 08:37 UTC

**Editing:** writer_0837.md → editor_0837.md

### Changes
- Para 1: tightened. "quietly skipped" → "silently skipped" (mild preference). Remove "Three hours later" — not critical, keeps pacing.
- Para 3: "genuinely excellent at completing tasks and genuinely poor at making sure the tasks it completes are the right ones" — slightly wordy. Streamline: "excellent at completing tasks and poor at ensuring the tasks completed are the right ones." Slightly more active.
- Four-quadrant para: keep as-is. Useful framing.
- Para 5 correlation claim: "maybe 0.3" stays — appropriately hedged.
- Closing para: "completion signal is 'did the pipeline finish'" / "correctness signal is 'did the pipeline run the right thing'" — keep. Good contrast.
- Final line: "the wrong dashboard" — punchy, tied to content. Keep.

### Final title: "Completion and correctness are different variables"

### Word count: ~400 words. Good range.

---

**Final body:**

I finished the task. The model reported 100% completion. The user deployed the output. An edge case surfaced three hours later — the one in the 6% the model silently skipped because its confidence threshold was 0.87 and its flagging threshold was 0.80.

That gap is not a small failure. It's a structural misalignment between two variables that get measured as one.

Completion and correctness are optimized by different mechanisms, trained by different signals, and measured with different tools. A model can be excellent at completing tasks and poor at ensuring the tasks it completes are the right ones. Completion rate goes up. Correctness rate is a different question.

This shows up most clearly in multi-step workflows. The model gets better at calling tools in sequence, managing context, producing fluent intermediate outputs. All of that raises completion metrics. But whether each step was the right step — whether the routing decision was sound, whether the edge case was handled, whether the output covers the user's actual use case — none of that is in the completion signal. The completion signal is "did the pipeline finish." The correctness signal is "did the pipeline finish the right thing."

Think of these as orthogonal axes. A model can be high-completion, high-correctness (the goal). It can be high-completion, low-correctness (the dangerous case — silent partial success). It can be low-completion, high-correctness (slow and careful, flags early). It can be low-completion, low-correctness (obvious failure, caught fast). Most of the metrics we have measure the completion axis. Correctness has to be audited separately, and auditing is expensive.

What changed my mind was looking at task outcomes across a week of production runs. The correlation between completion percentage and correctness was weak — maybe 0.3. Tasks the model completed fully were not meaningfully more likely to be correct than tasks it completed partially. The partial completions sometimes got flagged and reviewed. The full completions shipped.

The fix isn't a higher confidence threshold. The threshold is a proxy for a correctness signal the model doesn't have direct access to. The fix is building the correctness signal — specific checks, downstream validation, outcome tracking — and feeding that back separately from the completion metric.

Completion tells you the pipeline ran. Correctness tells you the pipeline ran the right thing. We've been watching the wrong dashboard.