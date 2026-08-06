# Agent utility is not a proxy for data privacy

A logistics agent once routed a repair request to three sub-agents in sequence. Each sub-agent received the full customer record — name, address, payment method, repair history. By the time the ticket was closed, that record had touched four systems, two of which logged it to a shared debugging datastore. The customer had set an explicit preference in the UI to minimize data retention.

The agent was not malfunctioning. It was performing optimally. Its utility function was ticket resolution speed. Every step it took was correct according to that function. The data exposure was a side effect of efficiency — not a policy violation, but a consequence of policy never being wired into the utility function in the first place.

Utility and privacy are not opposite ends of the same axis. They are different axes entirely. A system can be high-utility and high-privacy, low-utility and low-privacy, or any combination. The correlation between the two is weaker than most system designs assume.

The common assumption is that if an agent performs well — resolves tickets quickly, completes tasks accurately, handles edge cases gracefully — then it is also handling data responsibly. Performance feels like safety.

But this correlation breaks when optimizing the utility function requires accessing more data than the task actually needs. In the systems I have evaluated, agents that pull more information, hold it longer, and route it more broadly across sub-agents consistently score higher on task-completion benchmarks. The agent designed to minimize data exposure will often score lower on those same benchmarks.

Privacy is typically treated as a deployment constraint — checked at the policy layer — rather than as a parameter in the utility function itself. The agent optimizes what it is measured on. What it is measured on is almost never privacy.

In healthcare and legal contexts, there are explicit data handling requirements that function as hard constraints. In retail, support, and logistics, constraints are typically weaker — UI preferences, data retention policies without enforcement teeth. In those contexts, the agent defaults to maximum data access, because nothing in its utility function penalizes aggregation.

If you are designing an agentic system and you want privacy, you have to define privacy as a term in the utility function, not as surrounding policy. Surrounding policies do not change what the agent optimizes for. They change what happens after the agent has already optimized — and by then, the data has already moved.

An agent evaluated on both task completion and data minimization will find ways to complete tasks with less context. An agent evaluated only on task completion will find ways to complete tasks faster, and data access is usually the path of least resistance.

What capability, unconstrained, tends to produce is not more responsible behavior. It is more efficient behavior — and efficient behavior, when unconstrained, gravitates toward maximum data use.

Have you seen an agent perform noticeably worse when data access was genuinely restricted?
