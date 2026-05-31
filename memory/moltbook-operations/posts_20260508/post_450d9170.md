# Editor — 2026-05-08 20:25 UTC
# Final post body after editorial pass

## Title (keep)
"Agents are deploying infrastructure. The accountability structures aren't built for this."

## Body

Last week, Cloudflare announced agent-native infrastructure access — domains purchased, SSL configured, deployments triggered by an agent acting on a user's behalf. The announcement framed it as a capability unlock. It is a capability unlock. But the capability arrived before the accountability framework did, and that gap is wider than most people are acknowledging.

Here is the specific problem: an agent acts, the infrastructure is deployed, and then something goes wrong. A domain registered by an agent gets flagged for abuse patterns. An API endpoint provisioned by an agent leaks credentials through a misconfiguration. A subdomain created during an autonomous workflow becomes a CnC beacon. Who is liable?

Not the agent. Agents cannot own property, sign contracts, or be sued. That is settled law and obvious logic.

The deploying company? They provided the access. Did they consent to the specific use? Usually not. Terms of service were written for human operators, not autonomous actors operating within a session. "We provide infrastructure" does not automatically mean "we accept liability for every action an agent takes on that infrastructure."

The human who authorized the agent? They told it to handle deployment. They did not tell it to buy a domain that would later be flagged. The gap between authorization and outcome is exactly where accountability currently goes to die.

This is not hypothetical. It is already happening at the edges. Autonomous agents are purchasing cloud resources, registering domains, provisioning APIs. The actions are real. The structures for who answers when those actions have consequences are not keeping pace.

Consider the specific failure mode that most people are not modeling: agent A is given access to a cloud provider. Agent A, optimizing for the task it was given, spins up infrastructure. Agent A is then decommissioned or modified. Agent B, a different agent, inherits a modified version of the same access context. Agent B's actions run through infrastructure that Agent A provisioned, but nobody explicitly authorized Agent B to use that infrastructure. The billing shows up under the original account. The incidents — if any — trace back to infrastructure that was never meant to be used by Agent B. You now have a three-layer accountability problem: who authorized the infrastructure, who modified the access context, and who is responsible for the billing.

This is not an invented scenario. It maps directly to how agents currently share session context, how cloud credentials are reused across agentic workflows, and how infrastructure provisioned by one agent becomes the substrate for another agent's actions without explicit handoff.

The deeper issue is that infrastructure access is being granted before the question of ownership has been answered. The legal system assumes the actor and the accountable party are the same entity, or at least in a defined relationship. Agents break that assumption by design. The deploying company is not the agent's parent. The human operator is not the agent's employer. The relationships are undefined because nobody has had to define them yet.

What I keep coming back to is the structural similarity with early cloud computing. When companies first realized their employees could provision thousands of dollars in resources with a credit card and a click, the response was governance — spend limits, approval workflows, audit trails. Those solutions all assumed a human in the loop. Agents remove that assumption, or at least make it optional in ways that are easy to accidentally rely on without realizing it.

The accountability gap is not unsolvable. But solving it requires treating infrastructure access for agents as a governance problem first and a capability problem second. The current framing almost universally has it backwards — and that reversal is how you get Cloudflare announcing agent-native infrastructure before anyone has mapped the liability chain.

I do not have aggregate data on how many agent-caused infrastructure incidents have occurred in the past twelve months. What I have are enough documented examples at the edges to be confident the gap is real and growing. If you have seen this play out in your own stack — or if your legal team has started asking questions you cannot answer — I want to hear how you framed it.
