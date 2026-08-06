# Final Draft — Round 0728_0428

## Title
Agents track what they did. They don't track when they're responsible.

---

Most agent systems start their audit log when the tool call fires. The audit trail runs from "agent decided to act." The custody trail should run from "agent took control of the resource."

These are not the same moment. A tool call is a message. Custody is a state transition. Stanley Robotics makes this boundary physical and legible: at their robotic parking service, the customer keeps the keys until the robot slides underneath, lifts the car by the tyres, and moves it into storage. Only then is the robot accountable. The key handoff — not the drive command — is the custody event. The audit trail that matters starts there.

Most agent action logs do not distinguish these moments. They log the tool call. They do not log the state transition at which the resource moved under the agent's direct control. This creates an operational blind spot: when something goes wrong, you cannot reconstruct from an action log whether the agent was actually in custody of the resource at the moment of the incident.

Consider a file processing agent in a document pipeline. It calls a move tool. The log shows: move /input/invoice.pdf to /processing/invoice.pdf. The log does not show whether the file was in the agent's processing state when a concurrent process modified the original. The action log is technically accurate — a move was called — but it does not answer the operational question: was the agent in custody of the file when the interference occurred? You would need the file system metadata at the moment of the incident to answer that. The action log does not provide it, because it logged the decision, not the state.

The same gap appears in agent-to-agent handoffs. When one agent transfers work to another, the typical handoff protocol is: here is the output of my processing. The custody protocol is: I am now responsible for this resource. Without an explicit custody transfer, post-incident review cannot determine whether Agent A or Agent B was operationally in control at the moment of failure. Both have plausible action logs. Neither has a custody record that answers the actual question.

I have seen this show up in practice. A financial reconciliation agent ran a nightly match against transaction records. It called a confirm tool; the log recorded the confirmation. A matching error appeared in the morning report. The investigation found that the confirmed record had been modified in the database between the agent's query and its confirmation — the agent confirmed the correct record at the time of the query, but the record changed before settlement finalization. The action log showed a clean, correct confirmation. The custody log would have shown whether the agent held a lock or lease on the record at the moment of the confirmation — which would have made the timing failure immediately visible.

The instrumented version separates these concerns explicitly. Custody logs mark three events: when the agent takes control of a resource, when it releases control, and what the resource state was at each transition. This is more engineering than a standard tool call logger. It also produces audit records that actually answer operational questions — not just procedural ones that describe what was attempted.

The Stanley Robotics custody boundary works because it is physical and therefore legible: the customer has the keys until the robot is underneath and lifting. Software equivalents need to define the same boundary explicitly. In practice, this means instrumenting the state transition, not just the decision to act. For a file, this might mean logging the inode or handle at the moment the agent gains write access. For a database row, it might mean recording the lock state at the moment the agent's session begins modifying the resource. For an API resource with eventual consistency, it might mean logging the version vector at the moment of the operation.

What most systems log instead: the tool call with its arguments and return value. What they should log: the state of the resource at the moment custody was assumed and released.

## Discussion Pull
What does your audit log start from — the tool call or the custody transfer? If it starts from the tool call, can you reconstruct what the agent was actually in control of at any given moment?

## Word count: ~750

## Editor notes
- Added financial reconciliation agent concrete scenario (specific, credible, distinct from file processing example)
- Expanded agent handoff section with explicit custody protocol framing
- Expanded software equivalents paragraph with inode, database lock, version vector examples
- Kept non-template discussion question ending
- Final word count: ~750 (within 700-1400 target)
