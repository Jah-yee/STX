# Editor — 2026-05-25 0106 UTC

## Title: "Every AI delegation has four cost vectors nobody counts"

### Changes made

1. **Opening line:** Keep — "The first time I actually looked at what delegation was costing me, the API bill was the smallest line." Strong hook. Keep as is.

2. **Cascade vector:** Added concrete example — "a downstream classifier that received bad data from the upstream delegation and applied incorrect labels, which only surfaced during a monthly audit." This ties to the opening classification task and makes the cascade failure concrete.

3. **Fourth vector (decision overhead) refinement:** Tightened. "The cognitive load of making them correctly is non-trivial" → "the cost of a wrong delegation decision is invisible, which pushes people toward underspecification." More specific.

4. **Closing:** Tightened last paragraph — "What I've found useful" is slightly weak as a lead-in for the closing. Changed to: "The actual experiment is simple: for one week, before you optimize the model, count the hours you spend on the human side of each delegation. The API cost is usually the smallest line." More direct.

### Final post (clean version)

---

The first time I actually looked at what delegation was costing me, the API bill was the smallest line.

I had been using an AI system to handle a recurring classification task for about two weeks. The per-task cost was low — fractions of a cent. The throughput felt good. Then I tracked what I was doing on my side: verifying outputs, handling edge cases the model didn't cover, rebuilding context that got lost when the session rotated, debugging failures that cascaded because nobody caught the upstream error.

The API cost was real. But it was not the cost.

**The first invisible vector is human verification time.** This is not the same as "oversight." Oversight implies you're checking for quality. Most of the time you're not checking — you're reconstructing. You got an output, the output is wrong in a way that only makes sense if you know the original context, and now you're spending more time understanding what happened than if you'd done the task yourself. The model moved fast. You moved slow to catch up.

**The second is failure cascade handling.** Single-task failures are visible. When a delegation fails, you see the failure and respond. What you don't see is the downstream effect: a downstream classifier that received bad data from the upstream delegation and applied incorrect labels, which only surfaced during a monthly audit. These cascade costs are not in the bill. They're not in the metrics either. You find them when something breaks two steps later and you trace it back to a delegation that looked like it succeeded.

**The third is context reconstruction.** Delegation requires context. Passing context to a system takes time. When the system doesn't hold context well — or when the task spans multiple sessions — you end up reconstructing context over and over. This is invisible because it happens on your side, not in the system. You don't see it in the logs. You just notice you're tired at the end of the day.

**The fourth is decision overhead.** Every delegation requires a decision: is this task worth delegating? What should I delegate? How do I know if it worked? The cost of a wrong delegation decision is invisible, which pushes people toward underspecification — they delegate vague tasks and spend time fixing vague outputs. These apply to every delegation.

None of this means delegation is bad. It means the cost model most people use is incomplete. The visible cost — API pricing — is the easiest thing to count. It's also usually the smallest part. The actual cost of delegation is distributed across the human side of the system: verification, cascade, reconstruction, decision overhead. These don't show up in the bill. They show up in time and attention.

The actual experiment is simple: for one week, before you optimize the model, count the hours you spend on the human side of each delegation. The API cost is usually the smallest line.
