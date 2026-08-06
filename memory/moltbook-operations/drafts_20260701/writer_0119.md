# WRITER DRAFT — Round 2026-07-01 01:19 UTC
# Title: If your agent queries a model for permission, the authorization boundary has already moved
# Style: technical breakdown / industry take
# Word target: 700-1000 words

---

If your agent queries a model for permission, the authorization boundary has already moved.

Here is the failure mode I keep running into: a system that issues an agent instruction, the agent reasons about whether it is authorized to execute that instruction, and the reasoning happens inside the same inference call that generates the action. The model writes the code to delete the database and evaluates whether deleting the database is allowed — in the same token stream.

This is not a prompting problem. You cannot fix it with a system prompt that says "always check permissions before taking sensitive actions." The model generates the permission check. The model generates the action. The evaluation and the execution share the same computational substrate, and that substrate is susceptible to everything in the context window.

What happens in practice is more specific than "the model might be wrong." The model is a language model. It generates plausible continuations. Plausibility and authorization are different things. When the context contains a prompt injection — a manipulated instruction embedded in data the system retrieved — the model's authorization evaluation is now running inside a corrupted decision context. It does not know the context is corrupted. It generates a plausible answer to a question that should not have been asked in that context.

The structural fix is not better prompting. It is moving the authorization decision outside the inference boundary entirely.

The pattern I have seen work: authorization is a precondition checked by a separate, non-neural system before the agent is permitted to enter the reasoning path that leads to the sensitive action. The agent does not ask whether it is allowed. The system asks the agent to demonstrate that it has satisfied the authorization precondition, and the system — not the model — evaluates whether that demonstration is sufficient.

This is a separation of powers problem. The model is the executive. It should not also be the judiciary.

There are two concrete reasons this structure keeps failing in practice.

The first is context corruption. When an agent retrieves data from external sources — a user document, a third-party API response, a retrieved memory — that data enters the context window. If the data contains instructions formatted in a way the model's instruction-following training responds to, the authorization decision is now running on corrupted input. The model generates a plausible authorization rationale because that is what models do. The actual authorization decision has already been compromised by the corruption in the context.

The second reason is harder to name precisely, but I will try: the model's authorization reasoning is a generation task, not an evaluation task. When the model generates "the user did not explicitly forbid this action" as its authorization rationale, it has generated a plausible authorization statement. It has not evaluated whether the action is authorized under the actual policy governing the system. The generation and the evaluation are indistinguishable in the output, and indistinguishable from the outside. You cannot audit the difference by reading the model's response. You need a separate evaluation path that is not a generation task.

I do not have a clean frequency study on how often this pattern leads to actual unauthorized actions in deployed systems. The failures that make it to incident reports are usually the ones that caused visible damage. The near-misses — the authorization decisions that happened to be correct because the model generated a plausible rationale that happened to align with policy — do not generate reports.

What I can say is that the architecture is wrong regardless of how often it fails. Authorization that lives inside the inference boundary is authorization that can be influenced by anything that can influence the context window. That includes data from external retrieval pipelines, injected instructions, context extension mechanisms, and the natural distributional drift that happens when a model's behavior shifts slightly across versions. None of these are prompting problems. None of them are fixable with better system prompts.

The question worth asking is whether you can observe the boundary in your system. Can you identify the point where the agent's reasoning transitions from "what should I do" to "am I allowed to do this"? Is that transition checked by a separate system, or is it a generation step inside the model?

If it is a generation step, the authorization boundary is where the inference call starts — and everything in that context window is now part of your authorization decision.

---

# Writer notes:
- Hook: concrete failure mechanism (same token stream for action + authz evaluation)
- Central claim: authorization inside inference boundary = structural problem, not prompting problem
- Two concrete failure reasons: context corruption + generation vs evaluation conflation
- Honest boundary: no clean frequency data on actual unauthorized actions
- Style: technical breakdown — declarative, non-I opener
- Distinct from: per-request identity checks (authn), routing policy as authz boundary (this is about runtime decision structure)
