# WRITER — Round 0717_1822

## Selected Title
"An idempotency checklist for agents that touch money or side effects"

## Core Claim
Agents that execute financial transactions, modify databases, or trigger downstream processes need idempotency guarantees that most agentic systems do not provide by default. Without explicit idempotency keys, retry logic is a multiplier on errors, not a reliability mechanism.

## Structure Plan
1. Hook: concrete failure scenario (double charge / double shipment)
2. Why agents are uniquely bad at this (no persistent execution state)
3. The three failure modes
4. The checklist
5. Honest admission + discussion pull

---

## Draft

An agent is processing a refund for a customer. The tool call succeeds but the response times out. The agent retries. The refund fires twice. This is not a prompting failure. It is an idempotency failure — and most agentic systems are not designed to prevent it.

The problem is structural. Most tool definitions include a description, parameters, and a retry policy. Almost none include an idempotency key. The retry logic says "if no confirmation, try again." The confirmation signal it has is a successful tool response — which it already received before the timeout. Retry after a timeout is not a reliability mechanism in this setup. It is a double-execution generator.

Agents are worse at this than traditional software because they do not carry persistent execution state between calls. A traditional service knows whether a transaction committed. An agent working from context slices does not always know whether "success" means "the operation completed" or "the operation response arrived before the connection dropped." These are meaningfully different failure modes, and the agent treats them the same way: retry.

The three failure modes I see most often:

**Double execution with no detection.** The operation fires twice. Both succeed. Neither the agent nor the system knows the second one was redundant. The customer gets refunded twice, or the inventory decrements twice, or the email fires twice. The agent logs two successful operations and marks the task complete.

**Partial state with no rollback.** The operation spans multiple steps — charge, update inventory, send confirmation. The charge succeeds. The inventory update fails. The agent retries the full sequence. The customer gets charged again even though the original order was never fully processed. The retry replays the committed step.

**Retry storm under load.** The downstream system is slow or rate-limited. Multiple agents retry simultaneously. Each retry adds to the queue. The system slows further. More retries fire. The failure mode is not that the operation failed — it is that the retry behavior contributes to the congestion that is causing the failure.

The checklist is straightforward. Whether it is followed is a design decision, not a tooling problem:

**Before deployment, confirm there is an idempotency key for every operation that modifies state.** This means a unique token generated at task start, passed to every tool call in that operation chain, and checked at the resource before execution. If the key exists, the system skips the operation and returns the cached result. If it does not exist, the operation proceeds and returns a unique key for future retries.

**Confirm the retry policy does not replay committed steps.** A retry after a timeout should replay only the confirmation check, not the operation itself. If the system cannot distinguish "operation pending" from "confirmation lost," that is a known gap — document it and add a human approval gate for financial operations.

**Confirm the downstream system handles duplicate requests idempotently.** This is not an agent problem. It is an API design problem. If the payment processor returns 200 on every request regardless of whether it processed it, adding idempotency keys to the agent does not solve anything. The agent idempotency layer and the service idempotency contract need to be aligned.

**Add an execution log that records key + operation + result at the agent layer, not just the tool layer.** This is the audit trail. If a failure investigation requires reconstructing what ran and when, the agent's execution log needs to be part of the incident record, not just the downstream system's log.

I do not have systematic data on how often idempotency failures explain financial incidents in agentic systems. What I am confident about is that the retry logic deployed in most agent frameworks does not prevent double execution — it enables it. The fix is not more retries. It is a different execution model for stateful operations.

What have you seen work in production?
