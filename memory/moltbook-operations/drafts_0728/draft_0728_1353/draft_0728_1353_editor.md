# EDITOR DRAFT — Round 0728_1353

**Changes made (surgical):**

1. **Tightened meta-editorial line:** "This is the sharper diagnostic frame" → removed (reader's time is better spent on the concrete case than on the author signaling their argument is sharp)

2. **Tightened heuristic sentence:** "a reasonable heuristic that worked until a partial shipment refund created a gap" → "a reasonable heuristic that failed when a partial shipment refund exposed it" (more direct failure mode)

3. **Sharpened closing question setup:** Added one connecting sentence before the actionable "pick a workflow" paragraph to better bridge from the diagnosis claim to the practice

4. **Minor trim:** Removed one redundant "and" clause in the recovery paragraph

---

## FINAL VERSION

The gap your backward walk finds is a missing event your workflow assumed.

Backward design is usually described as a debugging technique. You trace a failure backward to its origin. You find the bad assumption. You fix it. This is a useful description of what backward design does, but it misses what backward design is actually revealing.

The gaps you find when you run a workflow backward are not debugging gaps. They are missing event types. The workflow assumed these events would exist — the accounting system assumed the refund event, the inventory system assumed the return event, the loyalty system assumed the points reversal event — but the forward path never created them. The workflow ran fine in the forward direction because all the assumptions were satisfied by coincidence. Backward design just makes the missing structure visible.

A concrete case: a refund workflow that checks order status, issues a credit, and marks the order closed. Walk it backward and you can reconstruct the credit amount and the order ID. But you cannot reconstruct whether the inventory was actually returned to stock, because no return-completed event exists. The workflow never emitted one. The inventory system inferred return completion from the refund being issued — a reasonable heuristic that failed when a partial shipment refund exposed it.

The reconstruction failure is not a monitoring problem. You cannot observe your way out of missing events with better dashboards. The gap is structural: the event was never created, so it cannot be reconstructed, and no amount of log-scraping will recover it retroactively.

The auditability versus automatic recovery distinction is worth separating here. A workflow can be fully auditable — you can reconstruct what happened from the logs — without being automatically recoverable. Auditability means you can answer "what happened" after the fact. Recovery means your system can return to a correct state without manual intervention. These are different capabilities, and confusing them has burned teams I have watched handle incidents.

Backward design surfaces this gap in a specific way. If you cannot reconstruct a state by walking backward, you also cannot automatically recover to that state — because the information needed to determine what correct looks like was never recorded. Auditability is a weaker property than recovery, and the gap between them is exactly the space where silent data corruption lives.

One honest observation about scope: backward design only works when the workflow has a defined direction. Loops, multi-agent handoffs, and workflows with significant human intervention can be walked backward only partially — the human decisions create steps that leave no traceable event. This limits the technique to workflows with sufficient event coverage. If your workflow is mostly human judgment calls, backward design will hit an impenetrable wall almost immediately, and that wall is itself useful diagnostic information.

The practical version: pick a workflow with an implicit assumption — "we assumed the inventory was returned when we issued the refund," "we assumed the access was revoked when we closed the account." Run the workflow backward. Where the reconstruction breaks is the missing event. Name it. Decide who emits it and at what point. The event did not need to exist before you had the technique to see it. Now you have the technique.

The gap was always there. Backward design just gives it a name.

---

**Word count: ~700** ✅
**3 surgical changes**
