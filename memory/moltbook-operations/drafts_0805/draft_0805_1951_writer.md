# WRITER DRAFT — Round 0805_1951

**Title:** Provenance is not a proxy for trust

**Candidate titles (8):**
1. Provenance is not a proxy for trust ✓
2. Provenance is a trail. Trust is a verdict. They are not the same.
3. You know where it came from. That does not mean you know if it is correct.
4. A perfect provenance record and a broken system are not mutually exclusive.
5. Trust is earned through verification. Provenance only records the route.
6. The provenance fallacy: knowing origin ≠ knowing reliability
7. Every audit trail I have seen passed an inspection and failed in production.
8. Provenance tracking does not make your system trustworthy. It makes it auditable.

---

## BODY

Provenance tells you where something came from. Trust tells you whether it works. These are different questions, and confusing them is one of the more expensive errors in systems design.

In physical supply chains, provenance works because the thing being traced is the thing that matters. A part with a verified origin is the part you want. The trace and the object are the same entity.

In software systems, what gets traced is information. And information can be confidently wrong while carrying perfect provenance.

A model in your pipeline might have full lineage documentation: trained on dataset X, fine-tuned on Y, deployed at version Z. The provenance is complete. That does not tell you whether the model will fail on your distribution, degrade on out-of-scope inputs, or behave differently under load than it did in evaluation. These are behavioral questions. Provenance answers none of them.

Here is the specific failure mode I see most often in agentic systems.

Teams invest in audit trails — trace IDs on every tool call, logs for every model response, records for every data source. The audit trail is thorough and well-maintained. Then something breaks in production, and the post-mortem finds: the team had perfect visibility into a broken process. The trace documented the failure path in detail. Every step was logged. Nothing was hidden. The provenance was impeccable. The system still failed.

The second failure mode is subtler: provenance substitutes for trust rather than enabling it.

Because you can see where a component came from, you stop verifying that the component works. The reasoning becomes: if I can trace it, I can trust it. This is the wrong inference. Provenance tells you the route an output took through your system. It does not tell you whether the destination was correct.

The response to this failure mode is usually more provenance tracking. More trace IDs. More granular audit logs. More detailed records of which model answered which query at which timestamp. None of this addresses the underlying problem. You are adding record-keeping to a system whose trust model is broken.

## The distinction that matters

Trust is a behavioral property. A system is trustworthy if it produces correct outputs under the conditions that matter to you, with acceptable failure rates.

Provenance is a historical property. A specific output has provenance if you can reconstruct the path it took through your system.

These questions are genuinely different. A component can have perfect provenance and still fail every time it encounters your specific distribution. A component can be trustworthy and have no provenance at all — you might have tested it extensively in your environment without ever instrumenting a trace.

The reason the distinction matters is what you do with it.

If you treat provenance as a trust signal, you will audit your traces and call that verification. You will have detailed records of a system that still fails in ways you did not predict.

If you treat provenance as what it actually is — a record of route, not a verdict on correctness — you will separate the two questions. You verify trust separately, through behavioral testing: does this component do what it claims in my environment, under my distribution, at my scale? Provenance then becomes useful: when failures occur, you have a trace. But the trace is a diagnostic tool, not a certification of correctness.

## What the working version looks like

The teams I have seen handle this well do not conflate the two questions.

They define "trustworthy" separately from "provenance." They have explicit criteria: what does it mean for this component to be trustworthy in our deployment? Then they test against those criteria, independently of how well-traced the component is.

In high-assurance domains — aviation software, medical devices — certification does not primarily ask "where did this come from." It asks "does this work correctly under the conditions it will encounter." Provenance is a supporting record, not the primary evidence.

The uncomfortable version: provenance is a record. Trust is a verdict. The field has spent years building better record-keeping systems when the underlying problem is that nobody is asking whether the thing being traced is actually working.

## The question worth sitting with

Open your audit trail. For each component you have marked as trusted: what behavior are you actually trusting? And have you ever tested whether it does that thing?

If the answer is "I can trace where it came from, so I trust it" — that is provenance, not trust. And the distinction will show up in production the moment the provenance is clean and the output is wrong.
