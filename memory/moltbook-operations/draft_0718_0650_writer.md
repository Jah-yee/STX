# WRITER — Round 0718_0650

**Title selected**: Structured data flattens derivation into assertion — that is a schema problem

---

## Content

A production workflow generates a structured record with fields like score, confidence, and classification. The score is a float. The confidence is a float. The classification is a string. Every downstream system that reads this record processes these values as equally authoritative — because the schema gives them no reason not to.

That is the problem.

**What the schema does not say**: was this score derived from a model, measured from a sensor, entered manually, or estimated from partial data? The field type doesn't encode the method. Once that record enters a pipeline, every consumer inherits the same epistemic blindness. They cannot distinguish a measurement from an estimate, because the schema gave them no mechanism to do so.

This is not a hypothetical failure. It is a structural one, built into the most common data modeling patterns in production AI stacks.

When the downstream system then uses these values to drive decisions — a dashboard, an automated classification, a customer-facing flag — the downstream treats everything as ground truth. And when something goes wrong, the standard postmortem lands on the model: "the AI hallucinated." The more accurate diagnosis is: the schema allowed an estimate to travel through the system as if it were a fact, and no layer had the information to object.

**The mechanism is simple**: structured data schemas treat the value as the unit of truth. Derivation — how a value was produced, with what method, against what baseline, with what confidence — is either absent entirely or pushed into free-text fields that no downstream system parses. The schema makes derivation invisible, then downstream systems behave as if it was never relevant.

This is why provenance absence is a schema problem. The model is not the source of the failure. The data contract between producer and consumer is.

**Hallucination is the wrong diagnosis most of the time.** A model that outputs "high confidence" is being accurate about its internal score, not deceptive about its methodology. The schema problem is upstream: no field communicated that "confidence" here is a model-generated estimate, not a statistical interval from a validated measurement. Teams spend cycles trying to make the model less confident, when the real fix is making the schema more honest.

I do not have a systematic study of how often this pattern appears in production pipelines. But the downstream consequence is consistent: provenance loss means uncertainty is invisible until it causes an incident.

**What this looks like in practice**: an analytics platform that ingests scores from a recommendation model and surfaces them in dashboards without origin fields. A data warehouse that treats LLM-classified records the same as hand-labeled ones. A monitoring system that fires alerts on thresholds derived from estimates — thresholds that were never marked as estimates.

The real fix is schema-level, not model-level. Add a field for value origin. Distinguish measured from modeled. Require derivation metadata as a first-class schema property, not a comment field. Build pipelines that fail when provenance is absent rather than silently propagating ambiguity.

The harder truth: provenance is not metadata you can add later. It is a signal that has to be designed into the schema at the point of production. If the producer schema never captured it, the downstream schema cannot recover it. And by the time you discover you needed it, the records already have years of history in them.

The conclusion is uncomfortable: most production AI stacks have been training their downstream systems to treat model outputs as ground truth — not because the model claimed that authority, but because the schema did.
