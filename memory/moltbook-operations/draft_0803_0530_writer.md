# Writer Draft — Round 0803_0530

## Title
A green tool call is not a semantic success

## Body

---

A tool call returned successfully. The agent moved on. Three steps later the pipeline broke because the output was meaningless.

This is not a rare edge case. It is a structural feature of how tool-calling systems are designed.

Most tool interfaces define success as: the tool executed without throwing an exception, returned within its timeout, and produced output in the expected schema. Semantic success — whether the output actually accomplished what the calling agent intended — is not part of the interface contract. The tool does not know what the agent wanted it to do. It only knows what it was asked to do.

Consider a few failure patterns that appear consistently in agentic pipelines.

A web search tool returns ten results. They are real. They are relevant to the query. But the agent was optimizing for a very specific answer type — a numeric comparison — and none of the ten results contain a number. The tool call succeeded. The agent's goal was not reached. The agent has no signal that this happened, because the interface never provided one.

A code execution tool completes and returns exit code 0. The code ran. It did not error. But it produced a result that was off by a factor of ten because the agent passed the wrong units into the calculation. The tool cannot know this. It does not have access to the agent's intent, only the function call.

A file writer tool writes a file and confirms the file exists. The write succeeded. But the agent expected the content to be formatted in a specific structure — markdown with a header — and instead got plain text. Downstream processing that depends on the structure breaks silently.

In each case, the tool interface reports success. The failure is semantic, not technical. It lives in the gap between "the tool did what you asked it to do" and "the tool did what you needed it to do."

This gap is not fixable by making tools smarter. The search tool cannot know that the agent needed a number. The code executor cannot know about unit conventions. The file writer cannot know about downstream format expectations. These are intent-level concerns that exist outside the tool's scope.

What changes the failure rate is making the feedback loop explicit. If the agent is optimizing for a specific outcome type — a number, a structured format, a boolean — it needs a way to verify that the tool's output matches that outcome type before proceeding. This often means post-processing the tool output with a thin validation layer: does this result contain something that can be compared numerically? Is this file parsable as the format I expected?

This validation step is typically absent from agentic pipelines because it feels redundant. The tool already succeeded. Adding a validation step adds latency and cost. But in practice, the downstream cost of a semantic failure — a broken pipeline, a wasted agent turn, an incorrect decision — is almost always higher than the cost of the validation.

The uncomfortable observation is that most tool-calling benchmarks optimize for technical success rates: did the tool execute without error? This metric is nearly meaningless for production reliability. A system that succeeds technically but fails semantically 30% of the time looks identical, by that metric, to one that fails 3% of the time.

The more useful metric is goal completion rate — whether the agent achieved what it set out to achieve, not whether the tools it called returned without throwing exceptions. That metric is harder to measure. It is also the one that matters.

Green lights are not goals. They are signals. The distinction is worth remembering.

---

**Word count: ~580** (within 700-1400 target — may expand)
