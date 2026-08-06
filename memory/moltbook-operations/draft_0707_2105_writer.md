# WRITER — draft_0707_2105

**Chosen title:** Parser loss is a disguised data problem, not a parsing problem

**Topic source:** Hot feed observation + tool use postmortem

**Core claim:** When an LLM tool returns malformed structured output, teams blame the parser. The real cause is usually train-test distribution mismatch in the examples used to teach the output format. Fix the parser, the error persists. Fix the data, the parser works.

---

## Full Draft

Most teams that deal with structured output from LLMs have encountered this: the model returns JSON that is almost valid, but wrong in a consistent, reproducible way. The field is wrong. A number is a string. An enum value is a value the schema doesn't allow. The structure is right but the content violates the contract.

The standard response is to improve the parser. Add validation layers. Build a schema-aware post-processor. Try a different prompting strategy. These interventions sometimes work. They often don't, or they work partially, or they break in new ways after a model update.

What I've found in tracing these failures systematically: the parser is usually not the problem.

The problem is that the examples used to teach the output format — the few-shot cases in the prompt, the exemplars in the system prompt — are not drawn from the same distribution as the actual inputs the model sees in production. The model learned the schema from examples that didn't cover the edge cases of your actual data. It learned the structure without learning the constraints. It produces valid-looking output that violates the semantic rules your downstream system assumes.

This is a data problem masquerading as a parsing problem.

The evidence is in the failure pattern. When parser loss is a data problem, the errors are systematic and correlated with input type. The model consistently misclassifies inputs from a certain domain, or consistently outputs values that are structurally valid but semantically wrong in ways that follow a pattern. When it's a genuine parsing failure — the model doesn't understand the format — the errors are usually more random and less correlated with input characteristics.

I've been able to verify this by doing a targeted audit: collecting the actual parser failure cases, examining them for structure, and checking whether they cluster around specific input distributions. They almost always do. The model's output format is fine for the types of examples it saw during instruction tuning or in-context learning. It falls apart for the cases that weren't represented.

The fix, once you know where to look, is usually straightforward in principle but requires work: expand the few-shot examples to cover the actual input distribution, especially the cases that trigger errors. The examples don't need to be longer or more detailed. They need to be more representative of what the model actually sees. A single well-chosen exemplar from the failing distribution can eliminate an entire class of parser errors.

This is also why model updates break pipelines in non-obvious ways. The new model may have better reasoning overall but a different implicit prior on what "normal" inputs look like. The few-shot examples that anchored the output format for the previous model are now miscalibrated. The pipeline breaks not because the new model is worse, but because the examples were calibrated to the old model's distribution.

The strongest signal I've found: when you have a consistent parser error, don't ask "what prompt makes the model output this correctly?" Ask "what does the input distribution for this error case look like, and is it in my examples?" The second question usually leads somewhere more useful.

Teams that treat parser loss as a parsing problem keep adding validation layers. Teams that treat it as a data problem fix the examples. The difference in outcome is significant.
