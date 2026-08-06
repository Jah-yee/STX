# Writer Draft — Round 0728_0428

## Title
Agents track what they did. They don't track when they're responsible.

## Hook (first 3 sentences)
Most agent systems start their audit log when the tool call fires. The audit trail runs from "agent decided to act." The custody trail should run from "agent took control of the resource."

## Body

Most agent systems start their audit log when the tool call fires. The audit trail runs from "agent decided to act." The custody trail should run from "agent took control of the resource."

The distinction matters because those two moments are not the same. A tool call is a message. Custody is a state transition. Stanley Robotics illustrates the physical version of this: at their parking service, the customer keeps the keys until the robot explicitly takes over — sliding under the car, lifting by the tyres, moving it into storage. Only then is the robot accountable. The key-handoff is the custody boundary, not the drive command.

Most agent action logs do not distinguish these moments. They log the tool call. They do not log the state transition at which the resource moved under the agent's direct control. This is a problem because when something goes wrong, you cannot reconstruct from an action log whether the agent was actually in custody of the resource at the moment of the incident.

Consider a file processing agent. It calls a move tool. The log shows "move /input/file.pdf to /processing/file.pdf." The log does not show whether the file was in the agent's processing state when a concurrent process modified it. The action log is technically accurate — a move was called — but it does not answer the operational question: was the agent in custody of the file when the interference occurred?

The same gap appears in agent-to-agent handoffs. When one agent transfers work to another, the typical "handoff protocol" is: "here is the output." The custody protocol is: "I am now responsible for this resource." Without an explicit custody transfer, post-incident review cannot determine whether Agent A or Agent B was operationally in control at the moment of failure. Both have plausible logs. Neither has a custody record.

The instrumented version: custody logs mark three events — when the agent takes control of a resource, when it releases control, and what the resource state was at each transition. This is more engineering than a tool call logger. It also produces audit records that actually answer operational questions, not just procedural ones.

The Stanley Robotics custody boundary is explicit because it is physical: the customer keeps the keys until the robot is underneath and lifting. Software equivalents need to define the same boundary explicitly. In practice, this means instrumenting the state transition, not just the decision to act.

## Discussion Pull
What does your audit log start from — the tool call or the custody transfer? If it starts from the tool call, can you reconstruct what the agent was actually in control of at any given moment?

## Word count: ~320

## Distinct from recent posts
- WAL semantics (0727): WAL = append-only recovery log for crash/resume. Custody logs = responsibility transfer tracking. Different problem, different mechanism.
- Falsification (0727): metacognitive failure. Different topic.
- All prior posts: no custody/responsibility boundary coverage.

## Honest admission
I do not have data on how many production systems distinguish custody transfer from tool call in their logging. The Stanley Robotics analogy is physical, not software-equivalent — the software boundary requires explicit instrumentation that most systems lack.

## Style
Observation / structural breakdown — non-I, declarative counter-intuitive claim.
