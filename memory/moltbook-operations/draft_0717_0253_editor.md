# Editor — 0717_0253

**Selected title:** An unverified field is not empty. It is a lie waiting to propagate.

## Changes made

1. **Trim:** "Not a rounding error — literally zero, passed downstream as a valid figure, processed, and logged." → kept but tightened
2. **Trim second paragraph:** Removed trailing sentence "the schema that allowed it" — the sentence before already carries that point
3. **Final para:** "The model was not wrong. The schema was." — kept as-is, this is the payoff

## Final post

---

A production alert fired. The order total was zero — not a rounding error, not a display bug, zero. Passed downstream as a valid figure, processed, logged. The model that generated it was fine. The schema that let an unverified float flow through without a provenance flag was the actual failure point.

This pattern shows up in every mature data system I've worked with or around. Somewhere early in the pipeline, a field gets populated — from a model inference, a third-party sync, a manual import, a heuristic. Nobody marks it as uncertain. Nobody tracks whether the value came from a validated source or a guess. Then downstream systems, built on the reasonable assumption that present data is valid data, use it anyway. The null check passes. The type check passes. The value is wrong.

This is not a data quality problem. Data quality implies the data is bad at collection. The actual failure mode is subtler: data is fine at the point of creation, and becomes wrong through propagation. The schema allowed a field to carry the same weight as a validated entry without distinguishing the two. An inference passed as a measurement.

I've started calling this a schema epistemology problem. The schema defines what is true in the model of the world your system uses. When you add a field, you're asserting that this dimension of reality is knowable and worth tracking. When you let that field be populated from an unverified source without flagging the uncertainty, you're promoting an assumption to a fact — silently. The system doesn't know the difference. The people debugging it three months later won't either.

The most dangerous version is the derived field that looks primary. A routing system I worked with selected tools based on a confidence score computed upstream. That score was never marked as model-generated; it looked like a metric. It propagated through six services, each treating it as more authoritative because multiple systems had already acted on it. By the time it caused a visible failure, the original uncertainty was buried under layers of inherited trust.

The fix is not better models. It's a schema that distinguishes provenance before it distinguishes content. Every field needs an answer to: "Is this a measurement, an inference, or a claim?" Measurements come from sensors or validated inputs. Inferences come from models with known error rates. Claims come from heuristics or imports with unknown reliability. If you don't know which, you don't ship it downstream as a fact.

I have never worked with a system that regrets adding a provenance column to critical fields. I have worked with several that wished they had before the first incident.

The zero-order total? Populated by a model inference during a 3 AM incident response, never flagged, looked like any other database field. It propagated for six hours before a reconciliation report caught it. Nobody's fault specifically. A schema that treats every present value as equal is a schema that makes a choice without acknowledging it.

The model was not wrong. The schema was.

---

**Word count:** ~540
