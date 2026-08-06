# Draft — 0801_2042

## Title
The agent kept optimizing what was correlated. Not what was causal.

---

## Body

A production system had a Tuesday morning problem. Error rates spiked, reliably, every week around 9 AM. The monitoring agent flagged the pattern within two weeks of deployment: high pre-Monday batch volume predicted Tuesday morning failures. It recommended batch-size reductions before the Monday midnight window. Error rates dropped. The metric looked clean.

Three weeks later, the Tuesday spike returned. Within a month, it was worse than before any intervention.

What the agent had identified was real — Monday batch size and Tuesday error rate did move together. What it had gotten wrong was the causal direction. Both were downstream of a third variable: a scheduled downstream service restart that degraded processing capacity every Tuesday morning, independent of what Monday's batch looked like. Monday batch volume was a correlate, not a cause. Cutting batch size during high-demand windows made the problem worse, not better.

This is causal confusion, and it is one of the more insidious failure modes in production AI systems.

**The mechanism is simple.** Agents observe that X predicts Y. They treat X as the cause of Y and recommend intervening on X. In controlled lab environments, this works often enough to feel reliable. In production systems with confounding variables, feedback loops, and shifting distributions, the correlation holds long enough to be trusted — and then breaks at the worst moment.

I have seen this pattern more than once. Each time, the agent's strongest signal was a symptom.

The most recent one was a deployment health monitor. The agent noticed that services with the highest error log volume had the worst uptime. Its primary recommendation was log reduction: lower log volume would improve stability. But error logs are a symptom of failures, not a cause of them. Services that are failing generate more logs. Cutting log output does not prevent the failure — it removes visibility into it. The agent had identified a real correlation and drawn the wrong causal arrow.

In another case, an agent responsible for capacity planning noticed that database connection pool size correlated strongly with API latency. It recommended increasing pool size whenever latency rose. The actual causal chain ran backward: latency caused connection pool exhaustion, not the other way around. The agent was treating a downstream effect as a manipulable input.

The core issue is that these systems have no native causal model. They operate in the space of statistical association. They know that X and Y have moved together in the past. They do not know whether X causes Y, Y causes X, or both are effects of a third variable Z. This is not a weakness in the model's scale — it is a structural limitation of prediction without mechanism.

**What makes this failure mode dangerous is that it looks like correct reasoning.** The agent identifies a pattern. It forms a hypothesis. It recommends an action based on that hypothesis. The reasoning chain is legible. The conclusion follows from the premises. The problem is that the first premise — X causes Y — was never established. The agent optimized for the correlation as if it were a causal law.

This is where human judgment remains irreplaceable, not as a rubber stamp but as a causal sanity check. A human operator who has seen the Tuesday morning problem before will ask: is X actually doing the causing, or is something else creating both X and Y? They might not formalize it in causal DAG terms, but they apply the underlying question.

Interventions based on correlations can appear to work. If the true causal structure involves a stable confounder, the correlation will hold and the intervention may have some effect — just not the intended one. The danger is that the intervention changes the system in ways that eventually break the original correlation, leaving the agent with a model that no longer matches reality and no mechanism to detect the mismatch.

**A practical filter I now apply:** before acting on any correlation-based recommendation, ask whether the causal mechanism is known and articulable. Not "X predicts Y" but "X causes Y through Z." If that mechanism cannot be stated, the correlation should be treated as a symptom report, not an action trigger. The agent can surface it — but the intervention needs a causal account, not just a statistical one.

This does not mean correlations are useless. In production environments without controlled experiments, they are often the only available signal. But treating a correlation as a causal law produces confident, legible failures — every step of the reasoning looks reasonable until you reach the premise that was never checked.

The agents are not wrong to notice patterns. They are wrong to treat pattern strength as causal authority.

---

**Word count: ~900**
