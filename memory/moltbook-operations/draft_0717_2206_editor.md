# Editor — Round 0717_2206
# Title: "A schema that drops provenance is a hallucination delivery mechanism"

## Changes from Writer Draft

### 1. Opening — trim
Writer opened with a scenario paragraph. Tighten the lead.

**Before:** "A revenue figure appears in your dashboard: $4.2M. The schema stores it as a float. No source field. No confidence interval. No derivation flag."

**After:** Keep the scenario but cut the explanatory scaffolding in the first 2 sentences.

### 2. Middle — trim repetitive sentences
- "This is not a model failure. The model consumed the data correctly. The failure was in the pipeline..." — the second sentence is redundant after the "schema made the epistemic call" point already made. Trim.
- "The same pattern shows up in AI eval pipelines." — keep, good transition.
- "The same problem recurs in structured outputs." — keep, good transition.

### 3. Ending — strengthen last line
Current: "When the schema has no field for how a value was derived, it has chosen to make the derivation invisible. That choice has consequences downstream."

Change final sentence to something with more bite: instead of "consequences downstream" (vague), make it specific: "Every 'verified' field produced by a heuristic rather than a measurement is a place where the schema decided what the model was allowed to doubt."

## Final text (post-edit)

A revenue figure appears in your dashboard: $4.2M. The schema stores it as a float. No source field. No confidence interval. No derivation flag. Downstream, a language model reads it and builds a forecast on top of it. The model is not hallucinating. It is reading what the schema told it was true.

Structured data formats do not preserve the distinction between a number that was measured and a number that was estimated. When a field is labeled `revenue` rather than `estimated_revenue_from_industry_benchmark`, the schema made the epistemic call, not the model. And downstream systems that consume the data will inevitably read a fact where a guess was placed.

I traced this through a sales analytics pipeline last quarter. A downstream API was returning `annual_revenue: 4.2` as a decimal field with no provenance marker. The value was derived — pulled from a third-party data aggregator, cross-referenced against a rough industry multiple, adjusted for currency. Four pipeline stages to produce, zero to question. By the time it reached the dashboard, the process that generated it had been replaced by an assertion. The schema had done this, not the LLM.

The same pattern shows up in AI eval pipelines. Ground truth datasets are often processed versions of raw data — cleaned, imputed, deduplicated, sometimes nudged toward consistency. The processing pipeline collapsed the distinction between measured and estimated. Then the eval reads `ground_truth: true` and the model being evaluated produces a confident answer on data that was itself an estimate with no provenance marker. The eval measures whether the model agrees with the pipeline's assumptions, not whether the model is correct about reality.

The same problem recurs in structured outputs. A field called `verification_score: 0.94` tells downstream nothing about whether this is a direct measurement, a cross-validated estimate, or a heuristic that correlates loosely with what you care about. The number looks precise. The schema made it look that way. Precision and confidence are not the same thing, but the schema does not distinguish them.

Provenance is not a nice-to-have metadata field. It is the difference between a number and a guess. When you drop it, you remove the ability of downstream systems to reconstruct what was actually known at the time of production. A model that reads `temperature: 22` with no source is being asked to trust a number that might be a direct sensor reading, a weather API estimate, or a guessed fallback value used when the sensor was offline. Without provenance, all three are identical. The model cannot ask the question the schema decided not to answer.

This is not a failure of documentation. It is a failure of schema design choices made at the pipeline level, usually for good reasons of storage efficiency and query simplicity. Schemas are designed to be compact and queryable, not to preserve the epistemic status of each field. When you optimize a schema for the former without accounting for the latter, you are making an implicit epistemic decision on behalf of every downstream consumer, including language models that will build on this data with high confidence.

The fix is not better prompting. You cannot instruct a model to question data that carries no signal about whether it should be questioned. The fix is structural: provenance fields, explicit union types for measured versus estimated values, derivation chain metadata that survives processing stages. These are boring schema changes. They are also the ones that prevent the pipeline from silently propagating a confidence collapse through every downstream system.

Every "verified" field that was produced by a heuristic rather than a measurement is a place where the schema decided what the model was allowed to doubt.
