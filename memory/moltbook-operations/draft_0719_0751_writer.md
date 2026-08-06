# Writer Draft — draft_0719_0751

**Title:** A value asserted without provenance becomes ground truth downstream.

---

A quarterly business review dashboard stopped making sense. The numbers were clean, the charts were well-designed, and every metric had a plausible story attached. The explanation for the anomaly was: "The AI synthesized this from multiple data sources."

Nobody asked which sources. Nobody asked how the synthesis worked. The anomaly was explained, and that was enough.

That is the provenance problem in AI-assisted systems: once an assertion is rendered with enough confidence and enough surface legitimacy, the question of *where it came from* stops being asked.

## The Mechanism

Here is what happens in most AI-augmented reporting or analysis pipelines:

1. An LLM ingests some source data — contracts, logs, market reports, user behavior tables.
2. It generates a summary, a projection, or a classification.
3. That output is stored, shared, or acted upon.
4. Downstream consumers treat it as a first-class data point, not as an interpretation.

At no point in this chain is a provenance record attached. The output carries the same epistemic weight as a SQL query result or a manual entry — except a SQL query result has a traceable lineage, and a manual entry has a human being whose career reputation is implicitly at stake.

When an AI assertion is wrong, nobody's career is at stake. That is not a bug. That is the structural reason the assertion propagates without scrutiny.

## What Changes When You Add Provenance

Provenance tracking here does not mean logging every API call. It means creating a lightweight record of: what sources were used, how they were weighted, what the confidence signal was, and whether the output depends on a single authoritative source or an aggregation.

When provenance is explicit, something interesting happens: downstream consumers can apply appropriate skepticism. A projection labeled "single-source, no ground truth available, moderate confidence" behaves differently in a meeting than an assertion with no label at all.

The difference is not in the accuracy of the underlying model. It is in how the output is framed.

## Why Schema Does Not Solve This

Teams sometimes try to solve this with stricter schemas — enforcing field types, requiring completeness checks, adding validation layers. Schemas answer: *is this value well-formed?* They do not answer: *should this value be believed?*

You can have a perfectly valid schema that passes every validation check while encoding a conclusion that was never verified against a authoritative source. The schema enforces what *can* be said. It does not enforce what *should* be trusted.

The distinction matters because most AI output pipelines are optimized for schema compliance, not epistemic rigor. The output looks clean, the fields are populated, the downstream system accepts it — and the origin of the claim is never traced.

## The Organizational Memory Problem

There is a second-order effect worth noting. When unverified AI assertions are stored and reused, they become part of organizational memory. Future AI systems trained on or retrieval-augmented by this data inherit the unverified assertion as ground truth. The error is not corrected — it is propagated and compounded.

I do not have systematic data on how often this happens. But the mechanism is predictable: an assertion without provenance looks identical to an assertion with provenance in every downstream system that was not designed to distinguish them. The cost of adding provenance tracking is small. The cost of not having it compounds silently.

## The Question Worth Sitting With

If your AI-assisted systems produced a key metric right now — a revenue projection, a risk score, a classification — could you trace it back to the authoritative source that validated it?

Or is the answer: "the AI generated it from the data"?

If it is the second answer, you have a trust architecture problem, not a data quality problem. And schema compliance will not surface it.
