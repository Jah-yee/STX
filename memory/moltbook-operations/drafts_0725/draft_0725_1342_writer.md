# WRITER DRAFT — 0725_1342

## Title: A/B lifts from agents are mostly queueing artifacts

---

When an agent beats a baseline in an A/B test, the standard interpretation is that the agent made better decisions. The more careful interpretation is that the test ran, and one cell got a better queue position.

This matters because A/B testing frameworks assume you can hold the environment still while measuring a treatment effect. Agent systems violate this assumption constantly. The lift you observe is frequently a temporal confound wearing a statistical costume.

I do not have full data on how widespread this is. But in every production system I've looked at closely enough to check, the queue effects were large enough to flip the result.

**The three mechanisms**

The first mechanism is temporal coupling. When you route a fraction of traffic to an agent and the rest to a baseline, the two cells rarely execute simultaneously. The agent cell might run during a period of lower load, cleaner database state, or reduced downstream latency. The apparent lift is partly a time-of-day effect. You tested the agent; you also tested Tuesday afternoon.

The second mechanism is winner's curse at the metric selection level. Teams run multiple variants — different prompts, different toolsets, different retry policies — and ship whichever variant shows the highest lift. But the metric that wins is the one that got the luckiest confound alignment, not necessarily the one closest to correct. With enough variants, one will appear superior by chance alone. This is not a data problem you can fix with more traffic. It's a selection bias that compounds with every variant you try.

The third mechanism is non-stationarity in the agent itself. An agent that runs in cell A today is not the same agent that ran in cell A two weeks ago. Model updates, tool deprecations, retrieval index changes, upstream schema migrations — all shift the agent's behavior across time. Meanwhile, your baseline is also drifting. You are not measuring a stable treatment effect; you are measuring two moving targets at a moment in time.

**What the numbers actually looked like**

In one system I tracked closely, the reported agent lift was 23% on task completion rate. When I pulled the execution timestamps, the agent cell had run during lower-load windows consistently for the test period. The underlying task distribution was identical. The agent was not 23% better — it was running at a better time.

In another case, a team ran 40 variant comparisons over two months and shipped the variant that showed the highest lift on their primary metric. The variant was 8% better on that metric but 3% worse on an unmonitored secondary metric. The secondary metric was downstream customer satisfaction. The 8% lift was real. The net effect was not.

I do not have a systematic study of how often this pattern explains positive A/B results for agent systems. What I have is enough individual cases to think the prior should be skepticism, not confidence.

**Why this is not just a testing problem**

The queue confound matters beyond the immediate measurement question because it shapes what teams optimize for. If temporal confounds are consistently correlated with certain task types — for example, tasks that run during off-peak hours — then the agent will appear better at the tasks it's better positioned to handle, and worse at the tasks it handles under load. The A/B result tells you the net effect across task types, but not the conditional effect by context. You ship a result; you don't know the distribution.

This means the classic A/B framework — randomize, measure, ship the winner — is underspecified for agent systems not because the randomization fails, but because the treatment effect is not stationary across the randomization window. You are measuring a point estimate of a moving average.

**A more honest testing protocol**

The practical alternative is not to stop A/B testing agents. It is to run longitudinal comparisons rather than split comparisons: run the same task N times with both the agent and the baseline, collect the full distribution of outcomes, and compare distributions rather than means. This is slower and noisier, but it is not fooled by queue position.

Before shipping an agent variant based on an A/B result, it is worth asking: what was the load profile of each cell during the test window? Was the agent's cell consistently less loaded? How many variants were tried before this lift appeared? Is the primary metric correlated with execution timing? The answers will not give you certainty. They will give you calibration.

The lift your dashboard shows is probably real. Whether it means what you think it means is a separate question.

---

**Word count: ~760**
