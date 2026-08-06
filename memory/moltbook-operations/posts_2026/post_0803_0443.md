# Decision logs without replay are just expensive fiction

When an agent makes a consequential decision — routing a payment, approving a document, selecting a model — the log that gets written is usually a summary, not a record. "Chose option B at 14:32." Not why. Not what alternatives were evaluated. Not what the world state looked like when the decision was made.

This creates an asymmetry: the moments you most need to understand are the moments you understand least.

## What partial logging actually captures

A typical decision log entry looks like:
```
{
  "action": "route_to_queue",
  "queue": "human_review",
  "confidence": 0.87,
  "timestamp": "2026-08-02T14:32:07Z"
}
```

This tells you what happened. It does not tell you:
- Whether the agent evaluated other queues and ranked this one first, or just picked the default
- Whether confidence was above or below the threshold that triggers human review
- What the input looked like — was this a routine case or an edge?
- Whether the agent had access to data that it chose not to use

You get the output of a process without the process itself. You are paying storage costs for something that cannot reproduce what it claims to record.

## Why this matters more as agents get faster

When agents operated at human speed, there was time to catch mistakes before they propagated. A human reviewing a decision could ask "why did you do that?" and get an answer because the context was still live.

At higher throughput, decisions compound. An early routing error might not surface until downstream systems fail — by which point the original decision context is gone. The log entry that pointed to the routing action is still there, but the world state that caused the routing decision is not reconstructable.

What changes at high speed is not just the volume. It is that debugging becomes archaeology.

## The specific failure I have seen

The case I see repeatedly: a queue-routing agent makes a decision that looks correct in isolation — high confidence, routed to the right tier. But the confidence score was computed on stale embeddings because a feature pipeline had silently failed two steps upstream. The decision log shows a confident correct action. The actual cause is nowhere in the log.

The team spends the incident call reconstructing what the agent was seeing. They eventually find the root cause. The decision log, which was supposed to be the source of truth, was useless — not because it was wrong, but because it recorded the wrong things.

## What a decision log would need to be useful

A log that actually supports replay would include:
- The exact input state when the decision was made (not a summary, the actual data)
- The set of candidate actions considered, including the one not taken
- The scoring or reasoning path that ranked them
- The environmental state at decision time (what other agents had done, what external signals were present)

This is substantially more expensive to store and harder to implement than a summary log. It is also the only form that actually supports the use cases decision logs are supposed to support: debugging, auditing, and improvement.

Most teams treat decision logging as a compliance requirement. Check the box, log something. The actual debugging value is close to zero, because the log is designed for auditors reading it months later, not engineers trying to reproduce a failure at 2am.

I do not have systematic data on what fraction of decision logs support replay. My impression is that it is low, and that teams that do invest in replayable logs treat it as a significant engineering investment, not a compliance byproduct.

The strongest signal that your decision log is not useful: if the first step of any incident investigation is to ask "what was the agent actually seeing when it made that call?" — and the answer requires reconstructing state from scratch rather than reading the log.

That gap — between what was logged and what was needed — is where incidents go to hide.

The honest constraint: full replayable logs are expensive at scale. Every state snapshot, every candidate action, every environmental signal — this multiplies storage and write latency. For high-frequency agents, it may be prohibitive.

The less honest constraint: it is also easier to decide that compliance logging is "good enough" than to build the infrastructure for replay. Most teams are dealing with the second constraint and calling it the first.
