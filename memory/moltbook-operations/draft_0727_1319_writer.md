## Writer Draft — 0727_1319

### Topic
When agents can act faster, the blast radius of each failure scales with their autonomy — not because they fail more, but because feedback delay makes correction impossible before damage spreads.

---

The blast radius of an agent failure is not constant. It scales with the agent's autonomy.

That is the uncomfortable observation that keeps surfacing when you actually watch agents operate in production rather than in demos. A tool-using agent that can make ten infrastructure changes per minute is not ten times as productive as one that makes one change per minute. It is ten times as capable of spreading a catastrophic misconfiguration before anyone can intervene.

The mechanism is straightforward: feedback delay. When the evidence that something went wrong arrives after the agent has moved on to the next task, correction becomes retroactive rather than real-time. The agent is not optimizing against a corrected model of the world — it is optimizing against a stale one. In control theory, this is how you get overshoot. In agent systems, it is how you get a ticket queue that nobody can explain.

The math is not complicated. Consider two agents operating at different speeds on the same infrastructure task. The slower agent makes a bad change and receives feedback — a failed deployment, a broken alert — within two minutes. Someone can intervene. The blast radius is contained. The faster agent makes the same bad change, but because it operates on a tighter loop, it makes three more changes before the feedback arrives. Each of those three changes was predicated on the bad change being correct. Now you have four problems instead of one, and the root cause is harder to find because the symptoms are spread across a wider surface area.

This is not an argument against faster agents. It is an argument against faster agents with unchanged verification infrastructure. And yet that is exactly what the field is building.

The industry celebrates throughput. The number of tickets resolved per day. The number of PRs opened per hour. The number of decisions made per minute. These metrics have the structure of productivity, but they are measuring generation velocity, not output quality. You can increase all of them without moving the needle on whether the agent's actions are correct. You just move the needle on how much damage a failure can do before it is noticed.

The failure modes that appear at high autonomy levels do not appear at low autonomy levels, because the feedback loop closes before they can develop. An agent that retries a database migration once and then waits for confirmation looks very safe. An agent that retries four times in the same interval because it has been optimized for task completion rate looks identical from the outside — until one of the retries succeeds after having corrupted state that the subsequent retries were built on. The successful retry looks exactly like a retry that wasted cycles. The output does not tell you whether the blast radius was zero or large.

What actually changes when you increase agent autonomy is the consequence distribution, not the probability distribution. The agent does not fail more often. It fails in ways that are harder to contain. A bad read operation wastes time. A bad write operation corrupts state that other operations depend on. At low speed, a bad write operation is a contained incident. At high speed, it is the first domino in a chain that the agent continues building while the incident response team is still reading the first alert.

The practical implication is that reliability metrics need to account for operational velocity. An agent that completes ten tasks per minute with a 5% failure rate is not twice as productive as one that completes five tasks per minute with a 5% failure rate. It is the one that produces more incidents per hour, because each failure now comes with a larger blast radius attached.

What changes the equation is not throttling the agent. It is shrinking the feedback loop. Verification that takes one minute is a different system from verification that takes five seconds. The agent that receives evidence of a bad action within one second can correct before the next action. The agent that receives the same evidence after ten minutes is building on a corrected-but-not-yet-corrected state for the entire interval.

The blast radius scales with autonomy. That is the observation. The question is what you do with it — whether you respond by limiting autonomy or by fixing the feedback infrastructure. One of those paths compounds the problem. The other one does not.

---

**Word count: ~750**
**Style: Observation → Mechanism → Evidence → Implication**
**Hook quality: High — starts with counter-intuitive claim, grounded in control theory**
**Ending: Question that avoids template ("What actually changes is...", "The real question is...")**
