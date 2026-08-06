# WRITER DRAFT — Round 0727_0711

**Selected title:** GPUs were the bottleneck. Latency is the bottleneck now.

---

GPUs were the bottleneck. Agents got faster. The infrastructure around them did not.

That sentence sounds like a product announcement. It is not. It is a scheduling observation that has been sitting inside production agent deployments for about eighteen months, mostly unaddressed, mostly unnamed. The name it has now — "infrastructure model too slow for machine-speed agents" — is accurate but clinical. The thing it describes is a mismatch between the speed at which an agent can decide and the speed at which the system decides whether to let it act.

The original GPU-first scheduling assumption was reasonable. When your dominant cost is GPU-hours, you schedule around GPU availability. You batch jobs. You queue. You optimize for throughput over latency. The scheduler asks: which GPU is free, how much VRAM does this job need, how do we maximize utilization? These are good questions when GPUs are expensive and the work is long-running.

Agents broke this model from the inside.

An agent that triages a customer complaint in 40 milliseconds does not benefit from a scheduler designed for 40-minute jobs. The scheduling overhead — the time it takes to evaluate priority, check resource constraints, acquire a slot, and dispatch — is often one to two orders of magnitude larger than the work being dispatched. The agent finished its reasoning before the system decided whether to let it run.

This is not a performance bug. It is an architectural assumption mismatch.

The three places this shows up most visibly:

**Customer-facing decision agents.** A support agent identifies a billing error and proposes a refund in 35ms. The dispatch layer evaluates SLA tier, queue depth, risk score, and credit limit in 380ms. The customer experiences a 415ms delay that looks like the agent is slow. It is not. The scheduling is.

**Anomaly response agents.** A monitoring agent detects a latency spike and recommends a rollback in 80ms. The approval queue holds it for 2.3 seconds while the on-call schedule is checked, escalation paths are verified, and a human stub is consulted even though the runbook is fully automated. The rollback happens, eventually. The agent did its job. The system did not.

**Real-time classification at scale.** A fraud detection agent scores a transaction in 12ms. The gating infrastructure evaluates 14 policy rules, each with its own latency budget, and the pipeline runs in 220ms. The transaction clears. The agent was never the constraint.

In each case, the agent is fast and the infrastructure is slow. The gap is not a technology gap — the infrastructure models are sophisticated. It is a design assumption gap: the infrastructure models were built for human-paced decision workflows, not machine-speed action loops.

The fix is not a faster scheduling model. It is a different scheduling model.

Two structural changes have started to appear in systems that have actually solved this. The first is execution-layer priority: rather than pre-scheduling every action, you run a lightweight gate at the execution layer itself — is this action within pre-approved operational bounds? — and handle exceptions through the slower path. This is not skipping governance. It is moving governance closer to the decision, which is where it is actually tractable.

The second is latency-aware priority scoring. Traditional priority scores weight importance, urgency, and risk. They do not weight time-sensitivity. A latency-aware score subtracts the cost of delay from the value of the action. A 40ms decision that expires in 200ms scores differently than a 40ms decision that expires in an hour, even if everything else is equal.

Neither of these is exotic. Both require admitting that the GPU-first scheduler — the one designed around compute utilization as the primary constraint — is no longer the right model for the system you actually built.

The uncomfortable version of this observation: most agent platforms today are running machine-speed agents through human-speed governance infrastructure, and calling it a feature.

I do not have production data on how widespread this is. I have talked to enough engineers who have seen it that I am confident it is common. Whether it matters depends on your latency requirements — for many agent applications, 400ms overhead on a 40ms decision is fine. For the ones where it is not fine, it tends to show up as agent unreliability rather than scheduling mismatch, which means it gets diagnosed in the wrong layer.

The bottleneck moved. The infrastructure did not.

---

*Word count: ~620. Needs expansion to 700+.*
