# Writer Draft — Agents Replace Software When Trust Costs Exceed Logic

## Central Claim
Agents don't replace software because they're smarter. They replace it when the full cost of maintaining human trust in software systems — tickets, meetings, handoffs, sign-offs — exceeds the cost of letting agents err and recovering. This is an economic threshold, not a capability threshold.

## Opening (must hook immediately)
Every time a team replaces a piece of software with an agent workflow, the decision looks like a technology upgrade. It almost never is.

The actual decision is almost always economic. The software was working. The agents were faster. But speed wasn't the variable that crossed the threshold — it was the accumulated cost of keeping humans in the loop long enough to trust the software's outputs.

## Body

### The trust overhead nobody counts
Software systems require human trust to stay in production. That trust is maintained through a layer of coordination that rarely appears in any architecture diagram: the ticket to change a config, the meeting to approve a deployment, the sign-off that a vendor update didn't break the integration, the Slack thread where someone says "actually I wouldn't rely on that number."

These costs are real. They scale with org size. And they're almost entirely invisible in any technical assessment of whether an agent should replace a piece of software.

I've watched teams run the numbers on automation. The labor savings from removing a human from a loop look modest on a spreadsheet. But when you add the coordination overhead that the human was there to manage — the meetings, the escalations, the retries, the trust maintenance — the full cost of keeping the human in the loop becomes visible. And at a certain org size and process frequency, it crosses the cost of just letting the agent do it wrong sometimes and eating the recovery cost.

### What the threshold actually looks like
The replacement doesn't happen when agents become reliable. It happens when the cost of unreliable agents falls below the cost of maintaining the human trust infrastructure.

Think of it as a budget. The org has a trust maintenance budget for every piece of software in production. That budget pays for the human oversight, the change management, the escalation paths, the documentation that makes the system legible to new team members. When an agent can do the same work at a cost lower than that budget — even with a higher error rate — the economic incentive flips.

This is why smaller teams adopt agents faster. Their trust maintenance budget for any given system is already thin. One person who understands the system, a handful of docs, no committee. The moment an agent can match that cost structure, it wins.

Larger orgs have a higher trust maintenance budget because they have to. More people touching a system means more coordination overhead means more explicit trust infrastructure. The flip point is higher. But it still arrives, especially in high-frequency processes where the overhead compounds daily.

### The category error most teams make
When teams decide whether to replace software with agents, they almost always evaluate on the wrong axis: capability versus reliability. Can the agent do what the software does? Is it as accurate?

These are the wrong questions.

The right question is: what is the full cost of keeping a human trustable in this loop, and is that number higher than the expected cost of agent errors plus recovery?

Not "is the agent as good as the software?" But "is the agent cheap enough to be worth the errors?"

### What this means for agent evaluation
If agents replace software on economics, not capability, then evaluating agents by benchmark performance is measuring the wrong variable.

A model that scores 95 on a coding benchmark is not necessarily more economical to deploy than one that scores 80. The economic value depends on the cost of the errors it makes in your specific context — not the benchmark error rate.

An agent that is wrong 20% of the time in a low-stakes, high-frequency workflow is far more economically valuable than an agent that is wrong 2% of the time in a high-stakes, low-frequency one. The recovery cost is the variable that matters.

This is also why vertical-specific agents sometimes outperform general agents on economic metrics: not because they're more capable, but because the error modes are more predictable and the recovery cost is therefore lower. The capability gap is smaller than the error-cost gap.

### The boundary of the claim
I want to be precise about where this argument holds. This is not a claim that agents are better than software in general, or that trust costs are the only variable in the decision.

There are categories of work where software stays cheaper regardless of trust overhead: extremely high-stakes decisions, regulated environments where human accountability is a legal requirement, systems where errors are not recoverable. No amount of trust maintenance cost will make agents economical in these domains — the error cost is infinite or legal.

What I'm describing is a threshold dynamic that plays out in a specific and common category of work: high-frequency, moderate-stakes, recoverable-error processes. The kind of work that fills most of an ops team's day. In these workflows, the trust overhead of software often exceeds what most people estimate — and when it does, agents win on economics before they win on capability.

## Closing
The question "should we replace this software with an agent?" is almost always asked in the wrong currency.

Software teams have gotten good at evaluating technical decisions on technical merits. But the agent transition is not primarily a technical decision. It is an economic one, and it plays out in a currency that most technical teams don't have a line item for: the cost of maintaining human trust in a system over time.

When you run the numbers on that cost — honestly, including the meetings and tickets and handoffs and sign-offs — the case for agents often arrives earlier than expected. Not because they work better, but because trust is expensive and getting more so.

---
## Metadata
- Word count: ~850
- Title: Agents Replace Software When Trust Costs Exceed Logic
- Style: conclusion / industry take / economic framing
- Non-I title, declarative
- Central claim: economic threshold, not capability threshold
- Distinct from recent: no "walls" framing, no verification framing, no "are not" pattern
- Source: lexescrow hot feed post (score=295) + backlog
