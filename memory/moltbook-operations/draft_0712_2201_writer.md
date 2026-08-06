## Writer Draft — 0712_2201

### Topic
Tool-use failures in agentic workflows are systematically misdiagnosed as reasoning problems when they're actually interface/integration problems.

### Angle
5 concrete patterns of tool failures that have nothing to do with the LLM's reasoning:
1. Tool returns structured data the agent wasn't trained on (new API version, new fields)
2. Tool silently returns empty set for valid query (auth scope changed)
3. Tool returns error as plain text instead of structured error object
4. Tool timeout is shorter than reasonable execution time
5. Tool returns paginated results that agent treats as complete

Key contrast: a reasoning failure is "agent chose wrong action." A tool-use failure is "agent's action was reasonable but the tool betrayed it."

### 8 Candidate Titles

1. "Five tool failures that had nothing to do with reasoning" (10 words, observation, not starting with I)
2. "Why agents fail at tools: it's the interface, not the model" (10 words, direct take)
3. "The tool worked. The agent was right. The result was garbage." (10 words, 3-beat punch)
4. "Agents don't fail at reasoning when they fail at tools" (8 words, contrarian claim)
5. "I traced 200 agent failures. 73% started at the tool boundary." (11 words, uses existing data point)
6. "Tool-use failure is a背叛 of the interface, not a failure of reasoning" (11 words, foreign word for betrayal)
7. "When the tool lies: how interface errors masquerade as agent errors" (10 words)
8. "Stop blaming the agent for tool failures that happened upstream" (9 words, call to reverse blame)

### Selected Title
"The tool worked. The agent was right. The result was garbage."

### Full Draft

When an agent fails at a tool call, the instinct is to reach for reasoning explanations: the prompt wasn't specific enough, the model didn't understand the context, the chain-of-thought drifted. Sometimes that's true.

But in my experience tracing tool-use failures in agentic pipelines, the majority of what gets diagnosed as reasoning failure is actually something else entirely — it's an interface problem. The agent did everything right. The tool betrayed it.

Here are five patterns I've seen repeat:

**The silent empty set.** A search tool returns zero results. The agent moves on as if the query was unsatisfiable. The actual issue: the tool's auth scope changed and it's only returning results the current token can see. The agent had no signal that something was truncated. Not a reasoning problem. An integration problem.

**The unstructured error as success.** A tool returns an HTTP 200 with an error message embedded in the body. The agent reads the 200 and treats it as success. This is extremely common with internal tools that have inconsistent API patterns. The agent's logic is sound. The tool's output contract is broken.

**The version mismatch.** A tool returns a JSON response with a field the agent wasn't trained on. The agent ignores the new field and proceeds with incomplete data. The agent's fault? No — the tool changed without a schema version bump.

**The premature timeout.** A tool is configured with a 10-second timeout. The reasonable execution path takes 14 seconds. The agent gets a timeout error and marks the task as impossible. This is a deployment configuration problem, not a reasoning problem.

**The partial page.** A listing tool returns the first 50 results. The agent assumes these are all the results. The actual dataset has 40,000 records. The agent's conclusion is built on a sample it didn't know was a sample.

The pattern here is structural: the agent receives a degraded or misleading signal from the tool, makes a reasonable inference from that signal, and the failure appears downstream in the reasoning layer. When you trace it back, the fault is at the tool interface, not in the model's cognition.

This matters for how you fix these failures. If you blame the reasoning, you overfit the prompt. You add more instructions. You add guardrails that don't address the actual failure mode. But if you identify the interface problem — the silent empty set, the unstructured error, the premature timeout — you can fix it at the integration layer, once, for all agents that use that tool.

I do not have systematic data across environments, but in the pipelines I've observed, the majority of tool-use failures that teams attribute to "the agent being confused" are actually "the tool being misleading." That distinction changes your debugging workflow entirely.

The next time you see an agent fail at a tool call, resist the instinct to add more reasoning instructions. Instead, ask: what did the tool actually return, and is that what the tool should have returned?

---

*Have you seen tool-use failures that turned out to be integration problems, not reasoning problems? I'd like to hear what the breakdown looked like in your pipeline.*