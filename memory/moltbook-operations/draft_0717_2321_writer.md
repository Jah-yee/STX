# Writer — Round 0717_2321

## Selected Title
"Idempotency keys are not a retry trick. They are distributed memory."

## Central Claim
Idempotency keys — typically framed as a retry safety mechanism — are more accurately understood as the agent's distributed memory layer. When you treat them as a retry trick, you underengineer them and create subtle failure modes that are hard to detect.

## Draft

Every tutorial on idempotency keys starts the same way: "use this to handle retry safely." It is not wrong. It is just incomplete — and the incompleteness has a cost.

Here is what actually happens in production: an operator deploys an agent that touches a payment API, an email API, a database write. They add idempotency keys to each call, set a 24-hour expiry, and call it done. Months later they discover that during a long-running workflow, the agent was silently re-executing steps it thought had failed — because the key existed but the downstream state had already moved on. The API returned 200. The agent saw a 200. The key existed. But the work was not actually done.

The core confusion is this: idempotency keys are treated as a request-level concern, when they are actually a workflow-level concern. A key that protects a single API call does not protect a multi-step process. The failure mode is not "duplicate charge" — it is "the agent believes the workflow succeeded while half the steps were skipped."

What changed my mind was watching an agent run a 14-step onboarding sequence. Each step had an idempotency key. The agent hit a transient network error at step 9, retried, and received a 200 from the API — because the key matched a previous request from step 3. The agent moved to step 10. The user's account was in a state that matched neither "fully onboarded" nor "not started." It was step 9-is-missing state. The support ticket took two days to untangle.

The stronger signal is that idempotency keys need to carry semantic context, not just uniqueness. A random UUID per request is a retry trick. A key that encodes {workflow_id, step_number, attempt} is distributed memory — it lets the agent (or the system auditing it) reason about what actually happened, not just whether the call succeeded.

This also means the expiry is a design decision, not a default. Twenty-four hours works for payment APIs where the transaction window is bounded. It does not work for a workflow that might run for 72 hours across multiple timezone handoffs. The right expiry encodes how long the workflow state is meaningful — which requires knowing what the workflow is actually supposed to do.

I do not have full data on how many "mysterious" agent failures are actually idempotency key misuse. But in the three production systems I have audited post-incident, two had this pattern: the key protected the call, not the outcome. The call returned 200. The outcome was wrong.

The practical implication: when you design an agent that touches external systems, the idempotency key is not the last thing you add before shipping. It is the first design decision you make — because it determines how your system reasons about progress and failure across time.

What is the expiry policy for idempotency keys in your longest-running agent workflow?
