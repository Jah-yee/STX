# Editor — Final Version

**Title:** Your tool worked. The problem didn't get solved.

---

An agent calls a search tool, gets zero results, and marks the task complete. The tool ran without error. The response was valid JSON. Nothing broke.

The task was "find the latest contract amendment for vendor X." The agent found nothing. It reported back that it found nothing. It then moved on to the next step in the chain, carrying the same empty output into a downstream tool that was built to consume structured results — not silence.

This is not a retrieval failure. The search tool worked. Its job is to search. It searched and found nothing. The tool did its job correctly. The problem did not get solved.

This distinction — tool success versus task success — is where a large fraction of silent agent failures live. And it is not a problem that better prompts fix.

## Three cases where the gap is widest

**The empty result.** A search tool that returns an empty list has executed successfully. It returned a 200, a valid schema, and zero matches. The agent receives this as a completed tool call and proceeds. Nobody gets alerted. The downstream step receives `[]` and either fails silently or produces a confident non-answer. The retrieval failed. The tool call did not.

**The ghost write.** A state-changing tool — write, update, patch — returns 200. The agent assumes the resource was modified. In practice, the write succeeded at the transport layer but was rejected by a validation rule the agent could not see, or was immediately overwritten by a downstream process. The tool's success response was accurate at the time it was issued. The intended state change never persisted. The agent is unaware.

**The chain that composes wrong.** Each step in a multi-tool chain executes successfully. The output of step 1 feeds into step 2. Step 2 outputs correctly. Step 3 outputs correctly. But the composition of those three correct steps solves the wrong problem — the goal was mis-specified at the top of the chain, not at any individual step. No step errored. The outcome is wrong.

## Why this is not a monitoring problem

The standard response to these failures is to add more monitoring. Log the empty result. Alert on ghost writes. Trace the chain composition.

But monitoring at the tool layer catches tool-layer signals. It tells you whether the tool worked. It does not tell you whether the problem was solved.

What you actually need is a semantic layer signal: did this tool call, given its output, advance the goal? A search returning `[]` is a semantic failure wrapped in a tool success. A ghost write is a semantic failure inside a transport success. A wrong-composition chain is a semantic failure distributed across three tool successes.

The monitoring gap is not that teams don't log enough. It is that the signal they collect is the wrong abstraction level. Tool-level success and task-level success require different instrumentation.

## What the tooling actually needs

The minimum change is structural: tool wrappers should return semantic metadata alongside the tool output. Not instead of — alongside. The tool can still return its raw result. But it should also return something like: `retrieved_useful_content: bool`, `state_change_persisted: bool`, or `output_is_actionable: bool`.

This is not a call for agents to self-verify after every step — that would create circular dependencies. It is a call for tools to be honest about what they can and cannot confirm, and for the agent framework to treat that honesty as a first-class signal rather than an afterthought.

## The honest admission

I do not have a clean implementation of this. The tools I have seen that do semantic metadata well are narrow — they cover one tool type, one domain. Extending it across a general-purpose agent stack requires either a shared semantic layer that every tool owner commits to, or an external evaluator that checks goal-level outcomes independently of the tools that pursued them.

Neither is trivial. Both are worth building.

The practical version: before you ship an agent, write down what "the task is actually done" looks like in the output space, not the log space. Then check whether your current tooling gives you a signal that maps to that definition.

If it does not, you are flying blind — even when every tool says it worked.
