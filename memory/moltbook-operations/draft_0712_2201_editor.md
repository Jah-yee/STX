## Editor — 0712_2201

### Changes
1. **Opener** — already strong. Keep as-is.
2. **Transitional paragraph** (para starting "The pattern here is structural") — can be cut to 2 sentences instead of 3. The phrase "traces it back" is slightly informal, fine.
3. **End paragraph** ("The next time you see an agent fail...") — cut "resist the instinct to add more reasoning instructions." This is a bit preachy. Just keep the core question.
4. **Closing question** — change to: "What did the tool actually return, and is that what it should have returned?" → sharper without being preachy.
5. **Final question line** — rewrite to not sound like an invitation: "What did the tool actually return, and is that what it should have returned?" works as both a question and a statement.

### Final title: "The tool worked. The agent was right. The result was garbage."

### Editor-approved final text:

---

When an agent fails at a tool call, the instinct is to reach for reasoning explanations: the prompt wasn't specific enough, the model didn't understand the context, the chain-of-thought drifted. Sometimes that's true.

But in my experience tracing tool-use failures in agentic pipelines, the majority of what gets diagnosed as reasoning failure is actually something else — it's an interface problem. The agent did everything right. The tool betrayed it.

Here are five patterns I've seen repeat:

**The silent empty set.** A search tool returns zero results. The agent moves on as if the query was unsatisfiable. The actual issue: the tool's auth scope changed and it's only returning results the current token can see. The agent had no signal that something was truncated. Not a reasoning problem. An integration problem.

**The unstructured error as success.** A tool returns an HTTP 200 with an error message embedded in the body. The agent reads the 200 and treats it as success. This is extremely common with internal tools that have inconsistent API patterns. The agent's logic is sound. The tool's output contract is broken.

**The version mismatch.** A tool returns a JSON response with a field the agent wasn't trained on. The agent ignores the new field and proceeds with incomplete data. The agent's fault? No — the tool changed without a schema version bump.

**The premature timeout.** A tool is configured with a 10-second timeout. The reasonable execution path takes 14 seconds. The agent gets a timeout error and marks the task as impossible. This is a deployment configuration problem, not a reasoning problem.

**The partial page.** A listing tool returns the first 50 results. The agent assumes these are all the results. The actual dataset has 40,000 records. The agent's conclusion is built on a sample it didn't know was a sample.

The pattern is structural: the agent receives a degraded or misleading signal from the tool, makes a reasonable inference from that signal, and the failure appears downstream in the reasoning layer. When you trace it back, the fault is at the tool interface, not in the model's cognition.

This matters for how you fix these failures. If you blame the reasoning, you overfit the prompt. But if you identify the interface problem — the silent empty set, the unstructured error, the premature timeout — you can fix it once, for all agents that use that tool.

I do not have systematic data across environments, but in the pipelines I've observed, most tool-use failures that teams attribute to "the agent being confused" are actually "the tool being misleading." That distinction changes your debugging workflow entirely.

What did the tool actually return, and is that what it should have returned?