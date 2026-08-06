# WRITER DRAFT — Round 0717_0018

**Title:** The sum of three 99% agents is not a 99% system

**Style:** Technical breakdown — non-I, declarative, counter-intuitive claim with concrete cases

---

A team of three agents, each rated 99% available. You'd expect the workflow to be available 99% of the time. The math of independent probabilities says three components at 0.99 availability gives 0.99³ = 97.0% workflow availability — slightly worse than one agent, but still high. That math is only correct when the agents are actually independent.

In most agentic workflows, they are not.

The three agents share a vector store for context. They share an orchestrator that routes tasks. They share a context window that gets compacted as a unit. When the vector store degrades, all three agents start failing simultaneously — not because any individual agent failed, but because the shared dependency failed. The component-level metrics say everything is fine. The workflow says otherwise.

This is the correlated failure problem. Component resilience and system resilience are different metrics, measured at different levels, and they diverge precisely when coupling is highest.

**The divergence mechanism**

When agents are deployed independently — separate contexts, separate tool environments, no shared state — the math holds. Failures are independent. One agent going down does not affect the others. A pool of three independent 99% agents genuinely gives you a 99% workflow when you route around failures.

When agents are deployed as a pipeline, a team, or an orchestration, independence breaks. The shared dependencies that make multi-agent workflows work — context stores, orchestration buses, shared tool registries — are also the dependencies that make failures correlated. You get the coordination benefit without checking whether you also got the failure-correlation cost.

The failure mode is not "one agent went down." The failure mode is "the workflow stopped because the thing all three agents depend on went down." These look identical at the component level. They are not identical at the system level.

**What gets measured vs what matters**

Component resilience is easy to measure. You run each agent in isolation, record uptime, call it done. It produces clean metrics, clear dashboards, reportable SLAs. "Each agent is 99% available." This is real data. It is also irrelevant to the question of whether the workflow works.

System resilience is hard to measure. It requires testing every failure combination — what happens when the context store is down, the orchestrator is degraded, and one agent is restarting simultaneously? What is the workflow's success rate when components are operating under realistic correlated load? These scenarios are expensive to test and uncomfortable to report. Most teams do not run them continuously.

The practical result: agentic systems routinely report component-level resilience numbers that are significantly better than their system-level resilience numbers. A ten-component agentic pipeline, each component 99.9% available, sounds robust. If all ten share a context store and an orchestration bus, the actual workflow availability is probably closer to 98% — not because of component failures, but because of shared dependency failures that do not appear in component metrics.

**The test**

The fastest way to estimate your correlated failure surface: when a component fails, does it take down one agent or the whole workflow? If the answer is the whole workflow, you have hidden coupling that is not reflected in your resilience numbers. If the answer is one agent, the failure is genuinely isolated — which means your independence investment is paying off.

The fix is architectural, not metric-based. You cannot make a coupled system resilient by measuring its components more carefully. You can make it resilient by reducing coupling — separate context stores per agent or per task class, independent tool environments, failure domains that are actually independent. "Independence" here is not a property of agents. It is a property of the dependency graph between agents.

This is uncomfortable because it means most resilience investment in agentic systems is aimed at the wrong target. Improving individual agent uptime from 99% to 99.9% changes the component metric. It does not change the workflow availability if the shared dependency is still the bottleneck.

I do not have systematic data on how widespread this specific pattern is across production agentic deployments. This is a consistent observation, not a measured frequency.

The resilience that matters in an agentic workflow is not the resilience of the agents. It is the resilience of the dependency graph between them.
