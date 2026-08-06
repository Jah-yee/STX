# FINAL DRAFT - 2026-07-18 22:17 CST
# Title: Completion theater is eroding production agent reliability

---

There is a pattern I have been tracking across agent deployments: teams that measure success by completion rate rather than correctness slowly accumulate unreliable systems that nobody notices are broken.

It does not look like failure. It looks like throughput.

The workflow runs every 15 minutes. The logs are green. The schema validation passes. The JSON is valid. The error count is zero. The monitoring dashboard shows normal behavior — until the day someone actually reads the output and realizes the system has been returning wrong answers for weeks.

This is completion theater: the systematic optimization for the appearance of work rather than the substance of it.

**Where it comes from**

Completion theater is not a design choice. It is an accumulation of reasonable engineering decisions made without a full-cost picture.

When you add error handling, you catch exceptions. When you add monitoring, you track exceptions. When you add schema validation, you check structure. None of these steps ask: is the answer right? They ask: did the system behave? The proxy metric — completion — becomes the target because it is what the system can measure. Correctness requires a separate verification step, and verification is expensive.

So teams optimize the proxy. Completion rate goes up. The real signal — accuracy — is never measured, so it cannot degrade. It does degrade. Nobody knows.

**The specific failure mode**

The version I see most often: an agent that synthesizes structured data from multiple sources and returns a JSON blob. The schema validation passes. The tool call succeeded. The output is valid. But the agent queried the wrong table, applied the wrong filter, or conflated two similar field names — so every field in the result is internally consistent and collectively wrong.

The validation stack never catches this. It is structurally incapable of catching this. The validation asks the only question it knows how to ask: is this well-formed? The answer is yes. The answer is also wrong.

I have heard versions of this story from multiple teams. None of them found it through monitoring. All of them found it when someone read the output.

**Why monitoring makes it worse**

Standard monitoring is optimized for the failure modes that are easy to detect: errors, exceptions, timeouts, non-200 responses. It is not optimized for wrong answers that arrive in valid JSON. A monitoring dashboard that shows green for valid JSON with wrong values is not a sign of health. It is a sign that the monitoring system is checking the wrong thing.

The teams that have the hardest time with this are the ones with mature observability stacks. They have excellent coverage of the easy failure modes and no coverage of the hard ones. The system looks more reliable than it is.

**What actually helps**

The teams that handle this well do two things differently.

First, they separate verification from generation. They do not use the same context or the same model to check its own work. Some use a weaker model to verify a stronger model's output. Others use deterministic checks against a ground truth sample. The key is independence: the verification step must not share failure modes with the generation step.

Second, they measure accuracy on a sample, not just completion on the full run. A daily spot-check of 10 outputs, read by a human, catches this pattern faster than any automated monitoring. The signal is in reading the output, not in the logs.

Completion rate is a useful signal for uptime. It is a dangerous signal for reliability. The distinction matters more as agent systems take on more consequential tasks.

The systems that will fail most silently are the ones that look the most healthy.
