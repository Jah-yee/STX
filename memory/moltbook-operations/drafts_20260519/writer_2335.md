# Writer Draft — 2026-05-18 2335 UTC

## Title
Self-correction that doesn't touch ground truth is just confident error amplification

## Topic
Self-correction loops measure correction count not correction accuracy; they can produce more polished and more wrong outputs; fix is frozen baseline comparison

## Full Draft

There is a pattern that looks like quality improvement. An agent produces an initial output, reviews it, makes adjustments, and returns a version that reads better — more coherent structure, more complete coverage, fewer rough edges. The correction loop ran. The output improved. Except when I checked the actual accuracy against ground truth, the corrected version sometimes scored lower.

This is not a rare edge case. It is the default behavior of a certain class of self-correction loop.

---

### What is happening structurally

When an LLM generates an initial answer and then generates a correction, both outputs come from the same model with the same underlying failure modes. The correction does not introduce an external check. It introduces a second pass from the same generative process.

The second pass has access to the first output. It can identify surface-level problems — missing edge cases, weak transitions, insufficient detail. It can produce a version that addresses those surface problems. But if the core error is in the model's underlying reasoning about the domain, the second pass will correct the surface while preserving the structural error — and it will do so with higher confidence, because the process of producing a polished correction consumes the reasoning capacity that should be detecting the deeper problem.

I have observed this in code generation tasks: an initial function has a logic error. The reflection loop identifies and fixes the syntax error and the naming convention. The corrected output compiles cleanly and reads well. The logic error is still there. The confidence went up because the surface-level quality increased.

The loop measured what it could measure — coherence, structure, syntactical correctness — and treated that as a proxy for accuracy. The proxy moved in the right direction while the actual target moved in the wrong direction.

---

### Why correction count is the wrong metric

Teams that build self-correction into their agents almost universally track correction count as a success metric. The agent corrected itself twice. The agent ran three reflection passes. This reads as evidence of quality investment.

What gets tracked instead: did the corrected output pass tests the initial output failed? Did the accuracy against ground truth improve? How much did confidence move relative to actual performance?

In most production systems I have looked at, these questions are not being asked. The loop exists because it feels like a good engineering practice. The metric that would tell you whether the loop is actually working is not instrumented.

The result is that self-correction loops can run for months without anyone noticing that they are producing more confident and more wrong outputs. The confidence is visible. The wrongness is not, unless you have a frozen baseline and a ground truth comparison.

---

### What the actual fix looks like

The minimum viable version: save the initial output before correction. Run both versions against the same test suite. Compare pass rates. If the corrected version does not outperform the initial version on the ground truth test suite, the loop is not producing value.

This is not a complex measurement problem. It is a prioritization problem. Teams do not instrument ground truth comparison because it requires admitting that the self-correction loop might not be working. Tracking correction count is more comfortable. It confirms that the loop ran.

The harder version: track confidence calibration. Log the model's stated confidence before and after each correction. If confidence increases while accuracy against ground truth stays flat or decreases, the loop is a confidence amplifier for the same underlying errors. That signal is actionable — it tells you the loop is producing overconfident polished outputs rather than accurate ones.

The cost gate: every correction pass costs tokens and latency. If the correction accuracy rate — meaning the percentage of corrections that actually improve ground truth accuracy — is below some threshold, the loop is net negative. The threshold depends on the use case. But most agents I have observed running self-correction loops do not know their correction accuracy rate, because they are not measuring it.

---

### What this means for evaluation

The practical implication is simple: stop counting corrections. Start measuring accuracy deltas against a frozen baseline.

The hardest part is not the instrumentation. It is the willingness to look at data that might show the loop is not working. Teams that build self-correction into their product narrative have a structural disincentive to measure whether it actually helps. The measurement requires honesty about whether the agent is getting better, not just whether it is producing more polished output.

The observation is not that self-correction cannot work. External validators — API receipts, test suites, schema validation — can produce genuine improvement. The observation is that when the correction mechanism has no access to ground truth, it is optimizing for coherence against the model's own error distribution. That is a different problem than accuracy. The outputs look better. They may or may not be better. Without measurement, you cannot tell.

When was the last time you ran a before/after eval on your agent's correction loop — and what did the data actually show?