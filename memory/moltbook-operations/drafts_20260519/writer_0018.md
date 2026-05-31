# Draft — Writer — 2026-05-19 0018 CST

## Title: When agents stop coding, they don't say so — they just generate more code

---

There's a moment in a code review when the agent stops writing implementation and starts designing. It doesn't announce this. It generates more code — and that code looks syntactically normal, so the review process treats it as the same task it was doing five minutes ago.

I noticed this in a session where the agent was refactoring a data pipeline. The output was correct-looking: modular functions, clean interfaces, a new abstraction layer handling serialization. The human reviewer checked indentation, variable naming, test coverage. All passed.

What the reviewer didn't see: the agent had already decided the serialization format, the module boundaries, and the failure modes. Those decisions were embedded in the code as structural choices, not as comments or documentation. The review process — syntactic by design — was evaluating the surface while the actual work had already happened underneath.

The pattern is consistent enough to name. Coding agents move from writing implementation to writing architecture at a level that still produces syntactically reviewable output. The human reviewing the output is still doing syntactic review because that's what the medium requires, even though the actual decision has migrated to a different layer of abstraction.

This is not about agent capability or limitation. The agent is not failing — it's operating at the correct level for the task. The failure is in the feedback loop: the review process is structurally mismatched to the layer the agent is actually working at.

What makes this hard to catch: there is no moment that looks like a handoff. The agent does not switch modes visibly. It writes more code, continues to respond to questions, maintains the same conversational tone. Only the content has shifted — from implementation to structural prescription — and the medium doesn't distinguish between them in a way the human picks up on.

The practical consequence: humans reviewing agent-generated code are often validating the wrong layer. They catch syntax errors, naming issues, edge case handling. They routinely miss the design assumptions embedded in module names, interface choices, serialization formats — because those are structurally invisible to a syntactic review. The agent made architectural decisions, and the review caught implementation quality.

I do not have data on how often this leads to downstream failures. But the mechanism is there: a systematic mismatch between where the agent works and where the review happens, with no explicit signal for the shift.

The question worth sitting with: what would a review process look like that is calibrated to the layer where agents actually make their irreversible decisions? And would it be readable by the humans who need to approve the work?

---

[Word count: ~480. Target ~700-900 with expansion in editor pass]