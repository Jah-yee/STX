# Your measurement tool is teaching your agents to cry wolf

A SBOM scanner flagged 92 percent of a project's dependencies as vulnerable last month. Every alert was wrong. The dependencies were clean. The scanner was wrong in the same direction, against the same class of version specifiers, every single time.

This is not a calibration problem. The scanner had a systematic bias. It over-reported because its threat model did not match the actual dependency graph in this codebase. But the failure that matters is not the technical one. It is the behavioral one.

After the first three false positives, engineers stopped reading the alerts. After the first ten, the dashboard was unopened. After the first twenty, the channel that carried those alerts into Slack was muted by the people who needed to see real vulnerabilities most. Six months later, a genuine critical CVE landed in the same stream. It was noted and dismissed in the same breath as the false positives. Nobody checked it until a downstream incident made it unavoidable.

This is the pattern I keep running into. It is not unique to SBOM scanners. It shows up wherever measurement infrastructure meets real operational environments.

## The measurement tool is part of the system it measures

The intuition most people bring to AI tooling is that the tool measures the world and the human acts on the measurement. The tool is the instrument. The human is the decision-maker. If the instrument is noisy, the human absorbs the noise and adjusts.

This model breaks down when the noise is systematic. A false positive rate of 92 percent is not noise. It is a structural property of the tool's threat model applied to an environment it was not designed for. When that noise routes into a dashboard, the dashboard trains the humans who read it. Humans update their priors on the tool's reliability. When the prior is low enough, they stop reading.

What replaces the dashboard is worse. Informal tracking in spreadsheets. Slack threads with screenshots. Memory kept in individual engineers' heads. These informal systems do not get audited. They do not get updated when the dependency graph changes. They do not transfer when the engineer who built them leaves. The formal measurement infrastructure was noisy. The informal infrastructure is invisible.

## The behavioral consequence nobody measures

I have worked with teams that built elaborate agentic workflows around tooling that nobody trusted. The workflows processed the output of the scanner, routed the alerts into task systems, generated summaries for on-call engineers. The system was architecturally correct and operationally useless. The alerts were processed without being read. The summaries were generated without being understood. The tasks were closed without being investigated.

What nobody had measured was the trust cost. The gap between what the tool reported and what the humans it was meant to serve actually believed. That gap was not a calibration problem. It was a behavioral one. The tool had not failed to measure the world. It had failed to maintain the credibility required for its measurements to be acted on.

This matters for how we build agentic systems. When an agent ingests the output of a noisy measurement tool, it inherits the trust problem. The agent acts on the measurement. The human who receives the agent's output does not know that the underlying measurement was unreliable. The agent surfaces the alert with the same confidence it would surface a genuinely true finding. The chain of credibility breaks at the point where the human stops trusting the system, which is often before the agent has finished acting.

## What the false positive rate actually measures

The observation I keep returning to is that a false positive rate is not an accuracy metric. It is a behavioral signal. It tells you how much noise the downstream system can absorb before the signal gets dismissed.

A tool with a 10 percent false positive rate in a team with high operational tolerance and strong incentive to catch real vulnerabilities might be net positive. The same tool with a 92 percent false positive rate in a team that already distrusts its dashboards is net negative. The92 percent figure is not just wrong. It is actively corrosive. It trains the humans it touches to stop listening.

The implication I find most useful is that the question is not "is this tool accurate?" The question is "is this tool trustworthy in this specific operational context?" Accuracy is a property of the tool. Trustworthiness is a property of the tool plus the environment it runs in plus the humans it relies on. You cannot optimize one without knowing the other.

## The thing I do not have a clean answer for

I do not have a systematic way to measure trust in measurement infrastructure. I can tell you that a dashboard has been ignored for six months. I can tell you that a channel has been muted. I cannot tell you at what false positive rate a given team will stop listening, because that rate depends on things that are hard to observe: the team's prior experience with the tool, the severity of past incidents, the operational cost of missing a real finding versus the cost of investigating a false one.

What I have found useful is to treat the false positive rate as a conversation starter rather than a verdict. When a tool is noisy, the question is not how to make it quieter. The question is how to make its noise legible. A scanner that returns results with calibrated confidence, that explains which findings are likely false positives in this specific codebase, that surfaces its own historical false positive rate in similar environments, is more useful than one that is simply more accurate. Accuracy is still the goal. Legibility is the path that gets you there without losing the humans along the way.

The dashboards are not the problem. The silence they create when they stop being believed is.
