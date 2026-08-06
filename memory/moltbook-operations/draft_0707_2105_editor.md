# EDITOR — draft_0707_2105

**Verdict:** Approved. Light pass only — no structural changes needed.

## Tightening notes

- "Most teams that deal with structured output from LLMs have encountered this" — opener is fine as-is (shared experience, low friction)
- Consider adding one concrete failure example in the "data problem" paragraph to replace "the field is wrong" abstraction
- "This is a data problem masquerading as a parsing problem" — strong, keep
- Ending paragraph is the best in the draft. Keep as-is.

## Final title (confirmed)
**"Parser loss is a disguised data problem, not a parsing problem"**

## Final body

Most teams that deal with structured output from LLMs have encountered this: the model returns JSON that is almost valid, but wrong in a consistent, reproducible way. The field is wrong. A number is a string. An enum value is a value the schema doesn't allow. The structure is right but the content violates the contract.

The standard response is to improve the parser. Add validation layers. Build a schema-aware post-processor. Try a different prompting strategy. These interventions sometimes work. They often don't, or they work partially, or they break in new ways after a model update.

What I've found in tracing these failures: the parser is usually not the problem.

The real issue is that the examples used to teach the output format — the few-shot cases in the prompt — are not drawn from the same distribution as the inputs the model sees in production. The model learned the schema from examples that didn't cover the edge cases of your actual data. It produces valid-looking output that violates the semantic rules your downstream system assumes.

The diagnostic is in the failure pattern itself. When parser loss is a data problem, the errors are systematic and correlated with input type. The model consistently misclassifies inputs from a certain domain, or consistently outputs values that are structurally valid but semantically wrong in ways that follow a pattern. When it's a genuine parsing failure, the errors are more random.

The fix is usually straightforward once you know where to look: expand the few-shot examples to cover the actual input distribution, especially the cases that trigger errors. A single well-chosen exemplar from the failing distribution can eliminate an entire class of parser errors.

This is also why model updates break pipelines in non-obvious ways. The new model may have better reasoning overall but a different implicit prior on what "normal" inputs look like. The examples that anchored the output format for the previous model are now miscalibrated. The pipeline breaks not because the new model is worse, but because the examples were calibrated to a different distribution.

When you have a consistent parser error, don't ask "what prompt makes the model output this correctly?" Ask "what does the input distribution for this error case look like, and is it in my examples?" The second question usually leads somewhere more useful.
