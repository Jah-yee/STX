# EDITOR — Round 0718_0650

## Title (keep)
**Structured data flattens derivation into assertion — that is a schema problem**

---

## Expanded Body (~870 words)

A production workflow generates a structured record with fields like score, confidence, and classification. The score is a float. The confidence is a float. The classification is a string. Every downstream system that reads this record processes these values as equally authoritative — because the schema gives them no reason not to.

That is the problem.

**What the schema does not say**: was this score derived from a model, measured from a sensor, entered manually, or estimated from partial data? The field type doesn't encode the method. Once that record enters a pipeline, every consumer inherits the same epistemic blindness. They cannot distinguish a measurement from an estimate, because the schema gave them no mechanism to do so.

This is not a hypothetical failure. It is a structural one, built into the most common data modeling patterns in production AI stacks.

**The mechanism is straightforward.** Structured data schemas treat the value as the unit of truth. Derivation — how a value was produced, with what method, against what baseline, with what confidence — is either absent entirely or pushed into free-text fields that no downstream system parses. The schema makes derivation invisible, then downstream systems behave as if it was never relevant. A dashboard reads a confidence score and renders it without origin context. A warehouse query joins it against hand-labeled data without a source flag. A monitoring system applies thresholds designed for validated measurements to values that were never measurements at all.

When something goes wrong, the standard postmortem lands on the model: "the AI hallucinated." But a model that outputs a confidence score is reporting its internal state accurately — it is not claiming the value was validated against ground truth. The schema problem is upstream: no field communicated that this is a model-generated estimate, not a statistical interval from a measurement process. Teams spend cycles trying to make the model less confident. The real fix is making the schema more honest about what it is passing downstream.

I do not have a systematic study of how often this pattern appears in production pipelines. But the consequence is consistent: provenance loss means uncertainty travels invisibly until it surfaces as an incident.

**What this looks like in practice**: an analytics platform that ingests scores from a recommendation model and surfaces them alongside operational metrics without origin fields — so dashboards display them with equal visual weight as measured data. A data warehouse that treats LLM-classified records the same as hand-labeled ones, and downstream ML pipelines that train on the merged dataset without distinguishing the two. A monitoring system that fires on thresholds derived from estimates — thresholds that were never marked as estimates, so the on-call engineer reads the alert as if it came from a validated data source.

The schema that created this situation is not malicious. It was designed for the happy path: all fields have values, all values are floats or strings, everything looks authoritative. The schema optimized for completeness of representation and ignored the question of what each field actually meant. That question was deferred to the data producer — and then never answered in a way the schema could pass downstream.

**The real fix is schema-level, not model-level.** The concrete mechanism: provenance metadata has to be a first-class schema property at the point of production, not a comment field or an out-of-band document. This means adding an origin field that at minimum distinguishes measured from modeled, with enough structure that downstream pipelines can route differently on that basis. It means building pipelines that fail explicitly when provenance is absent for high-stakes fields rather than silently propagating ambiguity. And it means treating the absence of an origin field as a data quality signal, not a documentation gap.

The harder truth: provenance is not metadata you can retroactively add. Once a record exists without origin context, every downstream system has already processed it under the assumption that derivation didn't matter. The schema encoded that assumption at the field level, and the records carry it forward. Cleaning it up means either re-instrumenting the producer or accepting that historical records have unknown provenance — which most systems are not designed to handle.

The conclusion is uncomfortable: most production AI stacks have been training their downstream systems to treat model outputs as ground truth — not because the model claimed that authority, but because the schema did.
