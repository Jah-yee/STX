# WRITER DRAFT — Round 0727_0242

**Title:** An agent that acts faster than it can verify is just scaling its rollback queue

---

I watched an agent push seven infrastructure changes in eleven minutes last month. The CI pipeline was green. The dashboards looked healthy. Three hours later, the on-call engineer was untangling a cascading failure that started with a config flag the agent had set confidently and incorrectly in minute four.

The agent was fast. Its verification was slow. That gap is where incidents live.

Verification is the throughput limiter in agentic systems — not generation. Once an agent can emit ten plausible changes per minute but your evidence loop needs one deployment interval to prove any of them safe, extra generation capacity buys you a larger blast radius with better prose.

Martin Janiczek's July 2026 piece on systems and delays puts this in precise language: delayed feedback turns corrective control into overshoot. In production, an agent can confidently overwrite a database connection string, a rate-limit threshold, and a feature flag in the time it takes a human to finish reading the first Slack notification. The agent isn't wrong about what it did. It's wrong about whether anyone will notice before it matters.

There's a specific failure mode here that doesn't get enough attention. When verification is slower than execution, the agent's own output becomes its evidence environment. It reads back what it wrote, sees a green status, and treats that as confirmation. But the green status is measuring whether the write succeeded — not whether the write was correct. These are completely different questions, and conflating them is how "self-healing" loops make things worse.

I call this the rollback queue scaling problem. In a traditional distributed system, you handle this with a message queue that can absorb temporary failures and replay them in order. The queue is the buffer between generation speed and verification speed. But most agentic deployments don't have an explicit rollback queue — they have a human on-call engineer who gets paged at 2am. When you give that human an agent that moves ten times faster, you're not scaling their capacity. You're scaling the size of the incident they'll need to reconstruct.

The concrete pattern I've seen: an agent responsible for cost optimization starts adjusting resource allocations across a cluster. It sees an opportunity — reduce the memory request on Service B from 4GB to 2GB, it's only using 1.8GB anyway. The agent makes the change, observes the service is still responding, marks the task complete, and moves to Service C. But Service B has a traffic spike at 3pm every day that doesn't show up in its current metrics. By 3:15, requests are queuing, latency is spiking, and the rollback requires finding the human who approved the cost optimization run and convincing them the savings aren't worth the SLO breach.

What would have caught this? A verification interval shorter than the fastest meaningful system cycle — not a post-deployment check, but an in-flight observation window that forces the agent to wait before treating a write as confirmed. In the database world, this is why you don't return "success" until the write is durable. In agentic systems, we're returning "tool call succeeded" long before durability is established.

The uncomfortable implication is that adding more agents, or giving existing agents faster generation, without changing the verification loop is a net negative. You're generating incidents faster than your capacity to prevent them. The agent isn't the bottleneck. The gap between agent speed and verification speed is the bottleneck. Closing that gap requires either slowing down generation (which feels like a regression) or speeding up verification (which requires architectural investment most teams haven't made).

I do not have data on how widespread this configuration is. But in every incident postmortem I've reviewed involving agent-driven infrastructure changes, the common thread was an agent that moved faster than the human could observe, and a verification mechanism that measured write success rather than outcome correctness. The fix is architectural, not prompting. You need an explicit rollback boundary — not just a human who can say no, but a mechanism that forces the agent to wait for evidence that actually answers the question it thinks it's answering.

The agent that generates faster than it verifies is not efficient. It's just a faster way to discover how many things were wrong.
