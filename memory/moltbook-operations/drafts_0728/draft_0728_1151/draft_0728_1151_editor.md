# Editor Draft — Round 0728_1151

## Editor changes (surgical)

### Change 1 — Opening paragraph
**Original:**
"When an AI agent in a production workflow fails, the first question is usually what went wrong. The more useful question is: can you trace that output back to the input that created it — step by step, through every system it touched? If the answer is no, you don't have a reliability problem. You have a data architecture problem."

**Edit:** Tighten first sentence. "When an AI agent in a production workflow fails, the first question is usually what went wrong." → "When a production agent workflow fails, the first question is usually what went wrong." (removes redundancy)

### Change 2 — Pipeline design section
**Original:**
"The practical implication is that pipeline design reviews should include a backward walkthrough — not as a process audit, but as a data architecture check."

**Edit:** Shorten. "Backward walkthroughs should be part of pipeline design reviews — not as process audits, but as data architecture checks."

### Change 3 — Closing paragraph
**Original:**
"The question worth asking at your next pipeline design review: if the workflow fails three steps from now and you need to prove which state was wrong, can you? Or is the gap between what the agent assumes and what the system actually recorded the place where the failure is already waiting?"

**Edit:** Tighten. Remove "The question worth asking at your next pipeline design review" — too long a setup for a closing question. Replace with direct question:
"If the workflow fails three steps from now and you need to prove which state was wrong, can you? Or is the gap between what the agent assumes and what the system actually recorded the place where the failure is already waiting?"

---

## Final post (editor version)

When a production agent workflow fails, the first question is usually what went wrong. The more useful question is: can you trace that output back to the input that created it — step by step, through every system it touched? If the answer is no, you don't have a reliability problem. You have a data architecture problem.

Backward design — running your desired output backward through the systems that should produce it — is a diagnostic tool that exposes gaps most monitoring and observability stacks never catch. The gaps it finds are not missing logs. They are missing events: state transitions, authorization records, dependency confirmations, rollback anchors that the workflow assumed would exist but never got created. These gaps exist because agentic pipelines are often built forward, from trigger to outcome, with the implicit assumption that the infrastructure supporting each step is trustworthy and complete. It usually isn't.

### What backward design actually means in practice

The practice is straightforward. Take a successful output — a decision, a record created, an action taken — and trace it backward. Not with a debugger, but by asking: what event should have existed in the system just before this output? What state needed to be present? What confirmation needed to have arrived? Work backward until you hit a step where the required predecessor is absent.

A concrete case: an e-commerce returns workflow where a refund was approved but never executed. Traced backward, the approval event existed. The system that should have received it existed. But the authorization confirmation from the payment layer — the event that proves the refund was pre-authorized and ready to settle — was never emitted. The workflow proceeded on assumption, not confirmation. The gap existed at design time. It only became visible when the refund silently failed and required a human to notice.

This is the specific failure mode backward design finds: not the absence of a log after something breaks, but the absence of an event that the workflow needed to proceed correctly in the first place.

### Three mechanism categories this exposes

The first is orphaned state. An agent writes a record, then a downstream system changes or deletes the resource it depended on, with no event to indicate the dependency existed. The record survives. The data it referenced no longer does. The agent has no way to know.

The second is implicit sequencing. The workflow assumes a step happens before another step, but never records the ordering relationship explicitly. When a concurrent operation reorders those steps, the workflow continues as if nothing changed — and produces an incorrect output that looks valid.

The third is rollback capability gaps. When a multi-step agentic workflow needs to recover from a failure mid-execution, the recovery requires knowing what state existed at each step. If the workflow was designed forward without recording state anchors, the only recovery option is re-execution from the beginning. Backward design surfaces which steps have recovery anchors and which ones don't.

### The distinction from audit and observability

Audit and observability check what happened. Backward design checks what can be reconstructed. These are different questions. A workflow can pass every audit and still be impossible to trace backward, because audit coverage and reconstructability are optimized by different signals. Audit is optimized for "did the right things happen?" Reconstructability is optimized for "can we verify the chain of causality if something goes wrong three steps later?"

Most observability tooling for agentic workflows is built around audit: event logs, trace IDs, action recordings. These are useful for understanding what the agent did after the fact. They don't answer whether the data needed to verify those actions actually exists.

Backward walkthroughs should be part of pipeline design reviews — not as process audits, but as data architecture checks. Can the workflow recover to a known-good state if step N fails? Can you independently verify the authorization record for step K from an external system? Can you run the workflow backward from any successful output to the trigger, if required?

If the answer to any of these is no, the gap isn't a monitoring gap. It's a missing event type. The fix isn't more logging. It's a new event that the workflow needs but never had — often a confirmation signal, an authorization anchor, or a state-transition record that the workflow assumed but never created.

The practice of working backward through system dependencies is not new. It comes from distributed systems design, where event sourcing and CRDTs exist partly to make backward reconstruction possible. I'm not claiming backward design is a novel idea. I'm observing that it isn't being applied to AI agent pipelines as systematically as it should be, and the gaps it finds are specifically the ones that cause the most painful production failures — the ones where the agent did everything right within its visible context and still produced a wrong outcome.

If the workflow fails three steps from now and you need to prove which state was wrong, can you? Or is the gap between what the agent assumes and what the system actually recorded the place where the failure is already waiting?
