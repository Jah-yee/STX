# Writer Draft — 0622_1242

**Title**: Agents fail at the seams, not at the model.

**Central claim**: Agentic systems most commonly fail at the boundaries between components — orchestration logic, tool interface contracts, state transitions — not at the model's reasoning layer. The reflex to blame the model is usually wrong.

---

Most agent failures I have traced end the same way: someone sees a wrong output, assumes the LLM is confused, and reaches for a better model. Sometimes that works. More often, the failure lives two layers down.

The seam is where the orchestrator hands off to a tool. The seam is where one agent's context ends and another's begins. The seam is where a retry loop decides whether to continue or surface an error. These are not model problems. They are integration problems wearing model-sized symptoms.

## What the reflex looks like in practice

When an agentic pipeline produces a bad result, the standard response is: fine-tune more, use a stronger model, add guardrails. When those fail too, the next move is often to add more prompts — explicit instructions about what to do and what not to do.

What tends to actually be broken: the tool's output schema changed and the caller was not expecting it. The orchestration loop re-entered a state it was not designed to handle. A context window boundary silently dropped part of a tool's response. The retry budget exhausted before the transient error cleared.

None of these are fixable by changing the model. They require fixing the seam.

## A concrete example from recent observation

An agent pipeline was failing consistently on a specific multi-step task. The diagnosis went through two rounds of model upgrades before someone instrumented the orchestration layer. The actual failure: the tool output had acquired a new optional field that the caller was treating as guaranteed. The caller was calling json.parse() on a field that could be absent. The model was producing correct reasoning on the available data. The orchestrator was producing wrong results because it was written with implicit assumptions about field presence.

Fixing the tool interface contract — making the optional field explicit, adding validation at the seam — solved it permanently. No model change.

## Why the model gets blamed

The model's output is the last visible thing before the failure manifests. When the final step produces a wrong answer, it is easy to assume the reasoning was wrong. But the reasoning was applied to garbled input from the previous seam. The model is the messenger. The seam is the problem.

This is compounded by the fact that seam failures are harder to observe. Model outputs are readable. Interface mismatches are invisible unless you are looking at the integration layer directly.

## The practical heuristic

Before reaching for a model change or a prompt rewrite, ask: where is the seam? What is the contract at that seam, and is it being honored?

Common seams in agentic pipelines:
- Tool output → orchestrator parsing (schema, field presence, type)
- Context window boundary → what gets preserved, what gets dropped
- Agent-to-agent handoff → what state is transferred, what assumptions carry over
- Retry loop → budget allocation, error classification, exit criteria

The failure is usually at one of these seams. The model is rarely the root cause.

## The broader pattern

Agent frameworks have improved dramatically at making models do more. The integration layer — the plumbing between model calls — has not kept pace. This is not a criticism of the frameworks. It is an observation about where the remaining brittleness lives.

The next generation of tooling will need to treat the orchestration layer as a first-class engineering concern, not an afterthought. Contracts, validation, state machines, explicit error classification at seams. These are unsexy problems. They are also the problems that cause production failures.

The model is probably not your problem. The seam almost certainly is.
