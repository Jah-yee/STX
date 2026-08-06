# Writer Draft — 0717_1322

**Title:** Agents Replace Software When Trust Costs Exceed Logic Costs

---

There is a decision point in every system redesign that nobody writes down explicitly: the moment when you stop paying for deterministic logic and start paying for trust.

I hit this in a billing reconciliation system. The original code was a 2,000-line state machine that matched transactions line by line. Correct, auditable, and completely brittle — any new merchant rule required a deploy. We replaced it with an agent that reads the same transaction feed and applies the same rules, but can handle merchant-specific quirks without a code change. The team called it an upgrade. The compliance team called it unverifiable. Both were right.

The real question was never capability. It was which kind of failure you could afford.

## The arithmetic nobody does upfront

Deterministic software fails predictably. You write a test, it passes, you have a claim. Agents fail in ways that are hard to reproduce because the failure is not in the logic — it is in the gap between what the model understood and what was actually true.

That gap has a cost. When the gap is small, you absorb it. When the gap grows, you start spending more on detecting and correcting agent errors than you saved by not writing the rule. At that point, the original state machine starts looking cheaper even though it is slower to change.

The transition is not driven by model capability. It is driven by the ratio of:

```
(verification_cost_of_agent_output) / (maintenance_cost_of_deterministic_code)
```

When that ratio crosses a threshold, agents win — not because they are smarter, but because maintaining the deterministic alternative becomes the more expensive option.

## Where this breaks in practice

The trap is that the threshold shifts as the system evolves. A workflow that starts within the agent's reliable range can drift outside it as merchant rules accumulate, as edge cases surface, as the model version you are using gets updated without fanfare.

I have seen this play out in three agent migrations. In each case:

1. The initial deployment was within the agent's strong performance band — clean inputs, well-defined rules, straightforward outputs.
2. After six months, the production distribution shifted. Inputs got messier. Rules got more exception-heavy.
3. The agent adapted by absorbing the exceptions into its context window rather than failing visibly.
4. Output quality degraded slowly enough that nobody noticed until the error rate in a downstream audit crossed a threshold.

The agent was not the problem. The problem was that the trust arithmetic that justified the agent in month one was no longer valid in month seven, and nobody recomputed it.

## What you can actually do about it

The useful intervention is not choosing agents or software once. It is treating the choice as a recurring measurement rather than a one-time architectural decision.

A few signals that the ratio is shifting:

- Error correction overhead is growing faster than the agent's maintenance savings
- The context window is absorbing more edge-case history than production cases
- Human review is being added back in small doses — which is a trust signal, not a feature
- Model version changes start causing measurable output distribution shifts

When two or more of these are true simultaneously, it is worth recomputing the arithmetic before the system becomes load-bearing in a way that makes replacement expensive.

I do not have a clean formula for where that threshold is. The numbers are system-specific and change with team size, model provider, and business context. But the shape of the problem is consistent: agents do not replace software because they are more capable. They replace it when the cost of trusting the software's maintenance exceeds the cost of trusting the agent's flexibility.

That arithmetic is always running. Most teams just never look at it.

---
*What signals tell you the trust-cost ratio has shifted? I am curious whether others have formalised this or just feel it in the on-call noise.*
