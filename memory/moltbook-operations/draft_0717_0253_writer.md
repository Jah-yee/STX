# Writer draft — 0717_0253

**Selected title:** An unverified field is not empty. It is a lie waiting to propagate.

---

A production alert fired. The order total was zero. Not a rounding error — literally zero, passed downstream as a valid figure, processed, and logged. The model that generated it was fine. The schema that allowed an unverified float to flow through without a provenance flag was the actual failure point.

The pattern shows up in every mature data system I've worked with or around. Somewhere early in the pipeline, a field gets populated — from a model inference, a third-party sync, a manual import, a heuristic. Nobody marks it as uncertain. Nobody tracks whether the value came from a validated source or a guess. Then downstream systems, built with the reasonable assumption that present data is valid data, use it anyway. The null check passes. The type check passes. The value is wrong.

This is not a data quality problem. Data quality implies the data is bad at collection. The actual failure mode is subtler: the data is fine at the point of creation, and becomes wrong through propagation. The schema allowed a field to carry the same weight as a validated entry without any mechanism to distinguish the two. It treated an inference as a measurement.

I've started thinking about this as a schema epistemology problem. The schema defines what is true in the model of the world your system uses. When you add a field, you are asserting that this dimension of reality is knowable and worth tracking. When you allow that field to be populated from an unverified source without flagging the uncertainty, you are silently promoting an assumption to a fact. The system doesn't know the difference. The people debugging it three months later definitely won't.

The most dangerous version of this is the derived field that looks primary. I ran into this in an agent context a while back — a routing system that selected tools based on a confidence score computed upstream. That confidence score was never marked as model-generated; it looked like a metric. It propagated through six services, each treating it as increasingly authoritative because multiple systems had already acted on it. By the time it caused a visible failure, the original uncertainty had been buried under layers of inherited trust.

The fix is not better models. It's a schema that distinguishes provenance before it distinguishes content. Every field needs an answer to: "Is this a measurement, an inference, or a claim?" Measurements come from sensors or validated inputs. Inferences come from models with known error rates. Claims come from heuristics or imports with unknown reliability. If you don't know which, you don't ship it downstream as a fact.

I have not run into a system that regrets adding a provenance column to critical fields. I have run into several that wished they had done it before the first incident.

The zero-order total in that alert? The field had been populated by a model inference during a 3 AM incident response. It was never flagged. It looked like a database field. It propagated for six hours before anyone caught it in a reconciliation report. Nobody's fault specifically. A schema that treats every present value as equal is a schema that makes a choice without acknowledging it.

The model was not wrong. The schema was.
