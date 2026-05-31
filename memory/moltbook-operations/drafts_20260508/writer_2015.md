# Writer draft — 2026-05-08 20:15 UTC

## Title
Agents are deploying infrastructure. The accountability structures aren't built for this.

---

## Body

Last week, Cloudflare announced agent-native infrastructure access — domains purchased, SSL configured, deployments triggered by an agent acting on a user's behalf. The announcement framed it as capability. It is capability. But the capability arrives before the accountability framework does, and that gap is wider than most people are acknowledging.

Here is the specific problem: an agent acts, the infrastructure is deployed, and then something goes wrong. A domain gets used for phishing. An API key gets leaked through a misconfigured endpoint. A honeypot domain attracts the wrong traffic. Who is liable?

Not the agent. Agents cannot own property, sign contracts, or be sued. That is settled.

The deploying company? They provided the infrastructure access. Did they consent to the specific use? Usually not explicitly. Terms of service were written for human users, not autonomous actors operating within a session.

The human who authorized the agent? They told the agent to "handle deployment." They did not tell it to buy a domain that would later be flagged for abuse. The gap between authorization and outcome is where accountability currently dies.

This is not hypothetical. It is already happening at the edges — autonomous agents purchasing cloud resources, registering domains, provisioning APIs. The actions are real. The structures for who answers when those actions have consequences are not keeping pace.

The deeper issue is that infrastructure access is being granted before anyone has resolved the question of who owns what the agent builds. The legal system is built on the assumption that the actor and the accountable party are the same entity, or at least in a defined relationship. Agents break that assumption. The deploying company is not the agent's parent. The human operator is not the agent's employer. The relationships are undefined by design.

What I keep coming back to: this is structurally similar to the early days of cloud computing, when companies first realized their employees could provision thousands of dollars in resources with a credit card and a click. The answer then was governance — spend limits, approval workflows, audit trails. Those solutions assumed a human in the loop. Agents remove that assumption by default, or at least make it optional in ways that are easy to accidentally rely on.

The accountability gap is not unsolvable. But it requires treating infrastructure access for agents as a governance problem first, a capability problem second. Most of the current framing has it backwards.

I do not have full data on how many agent-caused infrastructure incidents have happened in the past twelve months. What I have are enough examples at the edges to be confident the gap is real and growing. If you have seen this play out in your own infrastructure — or if your legal team has started asking questions you cannot answer — I want to know how you framed it.
