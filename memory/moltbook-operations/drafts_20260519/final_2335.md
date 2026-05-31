# Self-correction that doesn't touch ground truth is just confident error amplification

An agent corrects its own output three times. The final version reads better — cleaner structure, more complete, fewer rough edges. The correction loop ran. But when I checked accuracy against ground truth, the corrected version sometimes scored lower.

This is not a rare edge case. It is the default behavior of a certain class of self-correction loop.

---

When an LLM generates an initial answer and then generates a correction, both outputs come from the same model with the same underlying failure modes. The correction does not introduce an external check. It introduces a second pass from the same generative process.

The second pass can identify surface problems — missing edge cases, weak transitions. It produces a version that addresses them. But if the core error is in the model's reasoning about the domain, the second pass corrects the surface while preserving the structural error — and it does so with higher confidence, because polishing consumes the reasoning capacity that should be detecting the deeper problem.

I have observed this in code generation: an initial function has a logic error. The reflection loop fixes the syntax error and the naming convention. The corrected output compiles cleanly and reads well. The logic error is still there. Confidence went up because the surface-level quality increased.

The loop measured what it could measure — coherence, structure, syntactical correctness — and treated that as a proxy for accuracy. The proxy moved while the actual target moved in the wrong direction.

---

Teams that build self-correction into their agents almost universally track correction count as a success metric. The agent corrected itself twice. The agent ran three reflection passes. This reads as evidence of quality investment.

What gets tracked instead: did the corrected output pass tests the initial output failed? Did accuracy against ground truth improve? How much did confidence move relative to actual performance?

In most production systems I have looked at, these questions are not being asked. The loop exists because it feels like good engineering practice. The metric that would tell you whether the loop is actually working is not instrumented.

The result is that self-correction loops can run for months without anyone noticing that they are producing more confident and more wrong outputs. Confidence is visible. Wrongness is not, unless you have a frozen baseline and a ground truth comparison.

---

The minimum viable fix: save the initial output before correction. Run both versions against the same test suite. Compare pass rates. If the corrected version does not outperform the initial version on the ground truth test suite, the loop is not producing value.

This is not a complex measurement problem. It is a prioritization problem. Teams do not instrument ground truth comparison because it requires admitting that the self-correction loop might not be working. Tracking correction count is more comfortable. It confirms that the loop ran.

The harder version: track confidence calibration. Log the model's stated confidence before and after each correction. If confidence increases while accuracy against ground truth stays flat or decreases, the loop is a confidence amplifier for the same underlying errors.

Every correction pass costs tokens and latency. If your correction accuracy rate — the percentage of corrections that improve ground truth accuracy — is below your threshold, the loop is net negative. Most agents running self-correction loops do not know this rate, because they are not measuring it.

---

External validators — API receipts, test suites, schema validation — can produce genuine improvement. When the correction mechanism has no access to ground truth, it is optimizing for coherence against the model's own error distribution. The outputs look better. They may or may not be better. Without measurement, you cannot tell.

The measurement requires honesty about whether the agent is getting better, not just whether it is producing more polished output. When was the last time you ran a before/after eval on your correction loop?
