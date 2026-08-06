# Writer Draft — Round 0731_1801

**Selected Title:** Downstream retry logic turns your agent's output into a liability

---

An agent initiates a wire transfer for $47,000. The API returns 200 OK. The network drops before the caller receives the response. The caller retries. The API returns 200 OK again. The bank processes two wires.

This is not a hypothetical. I've seen it in systems where the payment team and the agent team have different on-call rotations and different incident postmortems. The agent team calls it a successful call — 200 OK, confirmed. The payment team calls it a duplicate transaction. Neither is wrong. Both are describing the same event from different layers of the stack.

The problem isn't that the agent made a bad decision. The problem is that the agent's output entered a downstream data pipeline, and that pipeline had retry logic, and that retry logic had no way of knowing it was re-sending a committed decision rather than a lost packet.

**Agents get evaluated on decision quality. Pipelines get evaluated on delivery guarantees. These are different jobs, and they live in different organizational buckets.**

When you build an agent, the success signal is clear: did the agent do the right thing? When you design a downstream pipeline, the success signal is: did this event reach the destination exactly once? Agents optimize for the first question. Pipelines need to solve the second. The gap between them is where duplicate charges live.

## The specific failure pattern

The scenario that keeps appearing: an agent calls a tool, the tool call succeeds, but the response channel breaks before the result reaches the agent. The agent retries. Depending on the tool's idempotency design, the retry either:
- safely re-executes and returns the same result (idempotent), or
- re-executes and creates a second committed event (non-idempotent)

Email sends, API writes, database mutations, external webhooks — these are all non-idempotent by default unless explicitly designed otherwise. An agent that issues a "send confirmation email" command and times out before receiving the response will, on retry, send two emails. Not because the agent is broken. Because the retry loop doesn't know the first email already went out.

I've observed this in two different agent-to-SaaS integrations. In one case, it manifested as duplicate charges on a Stripe-connected workflow. In another, as double-issued purchase orders in an ERP system. Both incidents were eventually traced to a timeout between the agent and the downstream API — and both required a forensic trace through retry logs to confirm what happened.

The more subtle version: an agent reads a value, computes, writes a result. The write succeeds. The agent's memory of the read value becomes stale because the database was simultaneously updated by another process. The agent acts on stale data and writes an inconsistent result. Nobody's retry logic is involved. The failure is just concurrent access without a consistency contract.

## What pipeline-safe means for an agent

The property you need is: **can this output be safely replayed by a downstream consumer without causing a duplicate or inconsistent state?**

This question has four components:

**Idempotency** — Does the tool call produce the same committed result on repeated execution? Many REST APIs support idempotency keys. Agents rarely generate them. This is an asymmetry: the consumer needs idempotency, but the producer doesn't usually implement it.

**Versioning** — Can the consumer detect whether the agent's output is stale relative to the current state? Optimistic locking, ETags, version vectors. Agents that mutate shared state without embedding a version marker make it impossible for downstream consumers to know whether they're working with the latest state.

**Commit semantics** — Does the tool call return only after the effect is committed, or does it return on submission? Fire-and-forget tool calls (non-blocking HTTP, message queue publishes) create a window where the agent believes the action is done, but the action is still in flight or queued. If the agent retries during that window, it doubles the event.

**Observability** — Is there a trace that connects the agent's output to the downstream state change? Without correlation IDs that span the agent-to-tool boundary, you can't tell whether a downstream event was caused by the agent's action or a retry.

## The organizational gap

These questions land in the gap between who builds the agent and who owns the pipeline. Agent developers think about intent, reasoning, tool selection. Pipeline developers think about exactly-once delivery, dead letter queues, consumer group offsets. They rarely read the same postmortems.

I don't have systematic data on how often this plays out as a real incident versus a caught edge case. The incidents I've seen are the ones that escaped — the duplicates that reached a customer, the records that conflicted visibly. The caught ones don't make it into my sample. So I'm working from a selection-biased set of observations, not a rate estimate.

What I can say is that the combination of non-idempotent tool calls, retry-at-least-once semantics, and agents that return success before the downstream effect is committed is not rare. It's the default in most integrations I've looked at. The agents that avoid it have explicit idempotency design in the tool wrapper layer — not in the agent itself.

The question worth asking before you deploy: what happens if my agent's output is replayed by a downstream consumer, exactly once, three times, or never? If you can't answer that cleanly, your agent's output is a liability in proportion to how critical the downstream system is.
