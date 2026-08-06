# Writer Draft — Round 0726_0337

Topic: Data cleaning is not a merge. It is a dispute.

## Title candidates
1. "Dirty data is not wrong. It is a historical argument."
2. "Data cleaning resolves conflicts, not errors."
3. "Your data pipeline is a negotiation, not a pipeline."
4. "What two databases disagree on is more valuable than what they agree on."
5. "The schema is not the truth. It is a ceasefire line."
6. "Conflict resolution in data pipelines is applied politics."
7. "When your ETL disagrees with your source, who wins depends on who you ask."
8. "Every NULL in your dataset is a decision someone refused to make."

## Selected Title
"Dirty data is not wrong data. It is historical argument."

## Full Post

---

Two systems recorded the same customer address differently. System A says "Apt 4B, 123 Oak Street, Springfield." System B says "123 Oak St, Unit 4B, Springfield, IL 62701." Your data cleaning pipeline flags this as a conflict and resolves it through standardization: one canonical format, one normalized string. The output is clean. It is also a political decision dressed up as an engineering one.

The conflict was not an error. It was two different people with two different workflows making two different decisions about the same entity. The standardization resolved the conflict — it did not correct a mistake.

This distinction sounds academic until your "cleaned" dataset starts producing downstream anomalies that nobody can explain, because the resolution logic that produced the clean output also silently discarded the information about *why* the conflict existed in the first place.

### What conflicts encode

A duplicate address in two systems is not noise. It is evidence that the customer interacted with your organization through two channels, each with its own data model, its own validation rules, and its own definition of what a valid address looks like. The duplication is a footprint. When you deduplicate it, you lose the footprint.

The same applies to any conflicting record: product names, price records, user identifiers, timestamps. When two authoritative sources disagree on a fact, the disagreement is not a bug in your data. It is a signal about the structure of your organization — who owns which processes, which system was updated first, which workflow was designed more carefully.

A deduplication rule that resolves conflicts without recording what the conflict was is a decision to ignore the signal. You have optimized for a clean schema and destroyed the evidential trace.

### The resolution hierarchy is a policy question

Every data cleaning operation implies a hierarchy of authority: when source A and source B disagree, A wins. Or B wins. Or the most recently updated record wins. Or the longest field wins. Whatever the rule, it is a policy choice — and it lives in your ETL code where nobody reviews it.

I have watched data teams spend weeks building reconciliation dashboards for a business metric, only to discover that the "clean" dataset they were querying had been resolving conflicts through a rule that was set as a default in a library function two years ago, never reviewed, and completely wrong for the business context. The reconciliation dashboard was measuring the effect of this hidden policy, and nobody knew it.

The fix is not better deduplication algorithms. It is treating every conflict resolution rule as a first-class policy artifact: documented, reviewed, versioned, and owned by the business rather than the engineering team.

### What you lose when you deduplicate incorrectly

There is a specific failure mode that comes from aggressive deduplication: you can make your dataset internally consistent while making it systematically wrong for a subset of records.

Consider a customer who placed an order under a slightly different name in a partner channel. Your deduplication logic resolves this to the canonical customer record. The order is now correctly attributed. But the partner channel's record — which had a different shipping address, different contact preference, and different order context — is silently absorbed into the canonical record. The partner channel's view of the customer diverges from the canonical view, and the divergence is invisible because the record now looks clean.

When you analyze customer behavior across channels, this subset of silently absorbed records produces systematically biased conclusions. The records look clean. The conclusions are wrong. The bias is invisible because nobody can see the conflict that was resolved.

### The practical rule

Before you deduplicate or standardize a conflict, record the original conflict. Not just the resolved output — the input disagreement.

This means keeping a conflict log: which sources disagreed, what the specific disagreement was, what resolution rule was applied, and who owns that rule. It is a small overhead that produces a permanent artifact — the history of decisions made on your data's behalf, which is exactly the information you need when the dataset starts behaving unexpectedly downstream.

Dirty data is not a problem to solve. It is a record of how your organization actually works, waiting to be read.

---

**What I do not have full data on:** I am not claiming all conflicts are meaningful. Some are transcription errors, typos, and genuinely wrong values. The argument is that the *type* of conflict matters before you resolve it — and that most pipelines resolve first and ask questions never.
