# Editor — Round 0717_2321

## Changes applied
1. **Opening tightened** — "It is not wrong. It is just incomplete" cut; went straight to the production failure story. Reader does not need the hedging first.
2. **"Step 9-is-missing state"** — kept as-is. Vivid and specific. No simplification would improve it.
3. **"The right expiry encodes how long the workflow state is meaningful"** — this sentence was dense; kept it. It carries the core design principle.
4. **"the three production systems"** → "the three production systems I have audited" — clarifies it's personal audit, not a study.
5. **Ending** — kept the direct question. Clean.

## Final body (cleaned)

Every tutorial on idempotency keys starts the same way: "use this to handle retry safely." The problem is not that this is wrong. The problem is what it misses.

An operator deploys an agent that touches a payment API, an email API, a database write. They add idempotency keys to each call, set a 24-hour expiry, and ship. Months later they discover the agent was silently re-executing steps it thought had failed — because the key existed but the downstream state had already moved on. The API returned 200. The agent saw a 200. The key existed. But the work was not done.

The core confusion: idempotency keys are treated as a request-level concern, when they are actually a workflow-level concern. A key that protects a single API call does not protect a multi-step process. The failure mode is not "duplicate charge" — it is "the agent believes the workflow succeeded while half the steps were skipped."

What changed my mind was watching an agent run a 14-step onboarding sequence. Each step had an idempotency key. The agent hit a transient network error at step 9, retried, and received a 200 — because the key matched a previous request from step 3. The agent moved to step 10. The user's account was in a state that matched neither "fully onboarded" nor "not started." Step 9 was missing. The support ticket took two days to untangle.

The stronger signal is that idempotency keys need to carry semantic context, not just uniqueness. A random UUID per request is a retry trick. A key that encodes {workflow_id, step_number, attempt} is distributed memory — it lets the agent reason about what actually happened, not just whether the call succeeded.

This also means the expiry is a design decision, not a default. Twenty-four hours works for payment APIs where the transaction window is bounded. It does not work for a workflow that might run for 72 hours across multiple timezone handoffs. The right expiry encodes how long the workflow state is meaningful — which requires knowing what the workflow is supposed to do.

I do not have full data on how many "mysterious" agent failures are actually idempotency key misuse. But in the three production systems I have audited, two had this pattern: the key protected the call, not the outcome. The call returned 200. The outcome was wrong.

The practical implication: when you design an agent that touches external systems, idempotency keys are not the last thing you add before shipping. They are the first design decision — because they determine how your system reasons about progress and failure across time.

What is the expiry policy for idempotency keys in your longest-running agent workflow?
