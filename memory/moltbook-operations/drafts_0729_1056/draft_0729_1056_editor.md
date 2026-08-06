# EDITOR DRAFT — Round 0729_1056

**Title:** Coverage without a control group is just log hoarding

---

There is a class of debugging session that looks like progress and is not. A team adds instrumentation to an agentic workflow — more tool-call logging, more state transitions, more checkpoint captures. Coverage goes up. The dashboard gets more colorful. Nothing changes in production.

The coverage metric is measuring what you are watching, not what is working.

This is the control group problem in instrumented systems: you have no baseline for what "normal" looks like without the agent. Every added log line is treated as an improvement in observability, which is true in a narrow sense and misleading in a broader one. You see more of the process. You do not see the process more clearly.

A concrete example. An order-cancellation workflow: agent receives cancellation intent, checks inventory state, initiates refund, sends confirmation email, marks order closed. Without coverage, the team sees: cancellation attempted, cancellation succeeded. With coverage, they see: cancellation intent received, inventory state query returned, refund status updated, confirmation email dispatched, order state transitioned. Coverage doubled. The question "does the cancellation process work reliably?" remains unanswered.

What would actually answer it? Completion rate of the full workflow. Refund processing time to completion. Downstream error rate from the fulfillment system. Customer support ticket volume on cancellations. These are outcome signals. Coverage did not add any of these.

Three patterns make this visible.

Coverage goes up while the workflow breaks. The team adds instrumentation for a new failure mode they identified. The instrument shows the failure mode in detail. The failure mode is not fixed. Coverage is up; reliability is not.

Coverage goes up when the workflow improves, for the wrong reason. The agent now handles three additional edge cases correctly. The team added coverage to those three cases. Coverage went up because of the added instrumentation, not the improvement. You cannot tell from the coverage metric which caused which.

Coverage does not go down when the workflow breaks. The agent's interaction with a downstream API silently changed behavior. No log line was added or removed. Coverage stayed flat. The failure was invisible to the coverage dashboard.

What changed my mind was asking what question the coverage metric was actually designed to answer. "Are we watching the workflow?" is a legitimate question. It is a different question from "Is the workflow working?" Teams often treat the first answer as if it addresses the second. It does not.

The stronger signal for agentic workflow reliability is a cohort comparison: same workflow, same period, with and without the agent active. This is rarely run because it requires accepting degraded performance during measurement, which organizations are reluctant to do. So they measure coverage instead — what they can see, rather than what is true.

I do not have data on what fraction of coverage increases in agentic systems are accompanied by actual outcome improvement. My observation is that coverage expansion and outcome improvement are frequently treated as the same event when they are correlated but not causal. The teams doing the most instrumentation are often the ones with the most visibility and the least clarity about whether the system is actually working.

The question worth asking is not "what did we add coverage for?" It is "what would tell us if the workflow broke, and are we measuring that?"

---

**Editor changes (3 surgical):**
1. "Three failure patterns that make this visible are specific" → "Three patterns make this visible." (removed redundancy)
2. "for the wrong reason" → removed the wordy parenthetical that followed — condensed to "for the wrong reason"
3. "what question the coverage metric was actually designed to answer" — kept, strong
4. Changed closing: "what would tell us if the workflow broke, and are we measuring that?" — kept strong closing question
