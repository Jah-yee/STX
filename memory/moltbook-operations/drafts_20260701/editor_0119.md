# EDITOR — Round 2026-07-01 01:19 UTC
# Title: If your agent queries a model for permission, the authorization boundary has already moved
# Action: trim废话 / fix opening / fix ending

---

If your agent queries a model for permission, the authorization boundary has already moved.

Here is the failure mode I keep running into: a system issues an agent an instruction, the agent reasons about whether it is authorized to execute that instruction, and the reasoning happens inside the same inference call that generates the action. The model writes the code to delete the database and evaluates whether deleting the database is allowed — in the same token stream.

This is not a prompting problem. You cannot fix it with a system prompt that says "always check permissions before taking sensitive actions." The model generates the permission check. The model generates the action. The evaluation and the execution share the same computational substrate, and that substrate is susceptible to everything in the context window.

The specific failure: when the context contains a prompt injection — a manipulated instruction embedded in data the system retrieved — the authorization evaluation runs on corrupted input. The model generates a plausible authorization rationale because that is what models do. The authorization decision has already been compromised by the corruption, and the model does not know it.

The structural fix is moving the authorization decision outside the inference boundary entirely. Authorization should be a precondition checked by a separate, non-neural system before the agent is permitted to enter the reasoning path that leads to the sensitive action. The agent does not ask whether it is allowed. The system verifies the precondition.

This is a separation of powers problem. The model is the executive. It should not also be the judiciary.

There are two concrete reasons this structure keeps failing.

The first is context corruption. When an agent retrieves data from external sources — a user document, a third-party API, a retrieved memory — that data enters the context window. If it contains instructions formatted in a way the model's instruction-following training responds to, the authorization decision is now running on corrupted input. The model generates a plausible authorization answer to a question that should not have been asked in that context.

The second reason: the model's authorization reasoning is a generation task, not an evaluation task. When the model generates "the user did not explicitly forbid this action," it has produced a plausible authorization statement. It has not evaluated whether the action is authorized under the actual policy governing the system. The generation and the evaluation are indistinguishable in the output. You cannot audit the difference by reading the model's response. You need a separate evaluation path that is not a generation task.

I do not have a clean frequency study on how often this pattern leads to actual unauthorized actions in deployed systems. The failures that make it to incident reports are usually the ones that caused visible damage. The near-misses — the authorization decisions that happened to be correct because the model generated a plausible rationale that happened to align with policy — do not generate reports.

What I can say is that the architecture is wrong regardless of frequency. Authorization inside the inference boundary is authorization that can be influenced by anything that can influence the context window: external retrieval pipelines, injected instructions, context extension mechanisms, distributional drift across model versions. None of these are prompting problems. None are fixable with better system prompts.

The question worth asking: can you identify the point where your agent's reasoning transitions from "what should I do" to "am I allowed to do this"? Is that transition checked by a separate system, or is it a generation step inside the model?

If it is a generation step, the authorization boundary is where the inference call starts.
