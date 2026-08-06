# EDITOR — draft_0727_1437

## Changes Made

### 1. Tighten opening
Cut the third sentence of the hook to sharper lead-in. Changed "It is the place where errors compound silently" to keep it as the punchy closer of the opening paragraph.

### 2. Refine "what a handoff actually is" section
Shortened the explanation of why handoff failures are silent — the original over-explained. Cut the redundant "The failure doesn't happen in Agent B's reasoning. It happened in the handoff." sentence — it was stated more cleanly earlier.

### 3. Strengthen "schema drift" section
Made the mechanism more specific — added "a field is renamed, a type changes" as concrete examples. Cut the trailing "The error is attributed to the downstream agent" sentence — it's implied and doesn't add.

### 4. Cut "temporal assumption violation" paragraph slightly
The point lands but was slightly wordy. Trimmed without losing the substance.

### 5. Sharpen the closing paragraph
The "reconstruction fidelity" paragraph was slightly academic. Tightened language throughout. The closing line "The models are doing what they do. The failure is in the contract between steps." is kept — it's earned and sharp.

## Final Post

---

Every agentic workflow has a failure mode that single-step evals do not catch. It lives in the handoff — the moment when one agent, or one step, passes its state to the next. It is the place where errors compound silently.

The standard approach to evaluating agentic systems is to test each step independently. Does the planner produce a valid plan? Does the executor complete the tool call? Does the reviewer catch the error? Each step passes its checks. The eval reports good performance. Then the system goes to production and silently fails on handoffs that nobody tested.

**What a handoff actually is.**

A handoff is a state transfer. Agent A has built up context — a goal state, intermediate outputs, accumulated tool results. At the handoff, this state is passed to Agent B. Agent B's first token is generated from this transferred state. If the transfer is lossy, incomplete, or ambiguous, Agent B starts from a degraded position.

This is different from a step failure. A step failure is visible: the tool call returns an error, the output is malformed, the plan is invalid. A handoff failure is silent. The state transfer completes. The next agent starts running. The first tokens look reasonable. The failure doesn't manifest until several steps later, when accumulated ambiguity produces an output that is wrong in a way nobody can trace back to the handoff that seeded it.

**Three ways handoffs quietly fail.**

The first is implicit assumption carry-over. When Agent A works on a problem, it builds up informal assumptions — about what the user meant, what the constraints are, what "success" looks like for this specific instance. Many of these assumptions are never explicitly stated in the state transfer. They live in the context as ambient inference. When the context transfers, these inferences may or may not survive the compression. Agent B reconstructs the intent from a partial signal and frequently reconstructs it differently than Agent A intended.

The second is schema drift. Tool outputs have schemas — structured data formats that downstream steps parse and rely on. When a tool's output schema drifts — a field is renamed, a type changes, a new variant appears — the handoff passes data the next agent was not expecting. If the next agent's prompt does not handle this gracefully, the parsing fails or produces wrong data.

The third is temporal assumption violation. Some tasks have real-time constraints — the data at handoff time is stale by the time the next agent processes it. The transfer succeeded. The state was valid at the moment of transfer. By the time the next agent acts on it, the world has changed. The output is wrong not because of a reasoning error but because the handoff clock and the execution clock were out of sync.

**Why single-step eval misses this.**

Single-step eval operates in a clean temporal window. The step runs, the output is checked, the step passes or fails. But real agentic systems are state machines. The output of step N is not the final output — it is the input to step N+1. Eval that only measures step outputs is measuring the wrong variable. It is measuring whether individual states are correct, not whether the transitions between states preserve the information required for the next step to succeed.

This is like testing whether each component of a distributed database is correct in isolation without testing whether the consensus protocol correctly propagates state between nodes. The individual nodes can be correct. The protocol can still be broken.

**What handoff quality actually requires.**

A handoff is good to the extent that the receiving agent can reconstruct the sender's intent from the transferred state. This is not the same as transferring all context — full context transfer is often impractical and some context is not serializable.

The useful question is not "did we transfer all state" but "can the receiver reconstruct enough intent to act correctly without re-access to the original context." The handoff needs to include enough signal — explicit goal state, constraint descriptions, intermediate conclusions, known failure modes from prior steps — that the receiver's reconstruction of intent matches the sender's actual intent with high probability.

Without this, you are relying on ambient context to carry information that should be explicit. Ambient context does not survive handoffs reliably.

The evaluation implication is straightforward: test transitions, not just steps. Run the full pipeline, interrupt it at handoff boundaries, and verify that the receiving agent's initial state is sufficient to continue correctly. If it is not, the handoff protocol needs redesign — not the individual agents.

This is not a model problem. It is an interface design problem. The models are doing what they do. The failure is in the contract between steps.
