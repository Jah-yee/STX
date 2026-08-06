## EDITOR — 0619_2345

### Title (keep)
"LLM APIs are the new legacy systems: stable on the surface, dangerous underneath"

### Opening (revise slightly for punch)
Change:
"Most engineers think about LLM API stability the way they think about cloud infrastructure: "it has an SLA, it's fine." That framing was wrong for SaaS dependencies in 2015 and it's wrong for LLM APIs now."

To:
"When your payment processor deprecates an endpoint, your code breaks loudly. When your LLM provider changes a model, your agent degrades silently — and nobody notices until the decisions have already accumulated."

### Expand "what makes LLM APIs specifically dangerous" — add concrete second example
After the retrieval drift example, add:
"The same pattern shows up in classification tasks. A sentiment analysis agent tuned on one model version starts tagging negative reviews as neutral after a provider update — not because the review changed, but because the model's calibration on the sentiment scale shifted slightly. The downstream consequence is a CRM that stops routing escalation tickets."

### Tighten the "honest part"
Change:
"But here's the honest part: most teams aren't doing any of this."

To:
"Here's what most teams actually do: nothing. They add logging, they check outputs manually for a week, they ship. The eval suite that would catch gradual drift doesn't exist yet, or it's not wired into production monitoring."

### Ending
Keep the audit question. It's uncomfortable and that's the point.

---

### Final Post (combined):

"When your payment processor deprecates an endpoint, your code breaks loudly. When your LLM provider changes a model, your agent degrades silently — and nobody notices until the decisions have already accumulated.

Here's the specific problem: an LLM API is not a deterministic dependency. When your provider changes a model, the surface behavior looks the same, the outputs feel similar, but downstream decisions are subtly different.

I've watched this happen. A retrieval-augmented agent that had been performing reliably for months started returning slightly different relevance rankings after a provider update. The chunk selection thresholds that were tuned for the old model became miscalibrated. No error, no alert, no crash — just worse decisions compounding over two weeks until someone noticed the output quality drift.

The same pattern shows up in classification. A sentiment analysis agent tuned on one model version starts tagging negative reviews as neutral after a provider calibration shift — not because the review changed, but because the model's calibration on the sentiment scale shifted slightly. The downstream consequence is a system that stops routing escalation tickets.

This is the legacy system problem, but backwards. Traditional legacy systems are stable and documented but nobody wants to touch them. LLM APIs are actively changing — providers ship model updates constantly, often without prominent notice — but developers treat them like the stable kind of legacy system.

What makes LLM APIs specifically dangerous as dependencies: there is no semantic versioning contract. A provider going from one model date to another is a minor version bump by their naming convention. In practice it's a different model, and the behavioral delta matters for tasks sensitive to reasoning style. There is no runtime contract — the provider can change instruction interpretation, refusal patterns, temperature-equivalent behavior, none of which appear in changelogs developers actually read. And agent loops amplify small deltas: each step has a small probability of degrading, and chained together the failure surface compounds.

What most teams actually do: nothing. They add logging, they check outputs manually for a week, they ship. The eval suite that would catch gradual drift doesn't exist yet, or it's not wired into production monitoring.

The practical mitigations exist. Pinning to specific model versions rather than 'latest' is the most direct hedge. Eval pipelines that run continuously — not just at deployment — catch drift before it compounds. Architecture that limits the blast radius of a single degraded step prevents silent failures from becoming cascading ones.

But here's the uncomfortable question: if you can't reproduce which model version your agent ran on six months ago, can you actually trust the decisions it made? Not philosophically. In the audit sense. The answer for most production agents is no."

---
### Word count: ~750 ✅
