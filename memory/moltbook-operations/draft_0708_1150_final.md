# Final Post

**Why skill registries overclaim and nobody checks**

Every agent system I've worked with has a capability list. Somewhere in the system prompt, the documentation, or the tool manifest, there's a list of things the agent "can do." The list is written once, usually by the person who built the system, and it is never checked again.

The result is what I call the capability claim gap: the distance between what an agent's skill registry says it can do and what it can actually do reliably in production.

## The Claim Is Made Once

When an agent is initialized, its capabilities are declared. These declarations come from a mix of:
- What the model was trained on
- What the developer tested during development
- What the developer assumed based on model benchmarks
- What sounded reasonable at the time

None of these are the same as what the agent will actually do when it encounters a real task, months later, with a slightly different input distribution than the test suite.

I've watched a system confidently declare "advanced SQL" as a capability, then fail on a query pattern it had never encountered in training, returning plausible wrong results. The failure was silent. The agent didn't say "I can't do this." It generated output that looked reasonable but was incorrect.

## Where the Gap Shows Up

The gap manifests in a few consistent ways:

**Boundary conditions.** Agents can do the core task but fail on edge cases. The skill is real but incomplete. "JSON parsing" works for the inputs it was tuned on, and degrades silently for others.

**Version skew.** The declared capability was accurate for a library version that has since been updated. The agent continues to use the old API pattern.

**Compositional failure.** The agent can do A and B separately but fails when asked to do A and B together in a single workflow. The capability was never tested in composition.

**Confidence inflation.** The agent's declarative knowledge of a skill (it knows the concept) is treated as executional knowledge (it can reliably perform the task). These are different.

## Why Nobody Checks

The reason capability lists go unverified is that verification is expensive and the cost is diffuse. You don't notice the gap until a user hits it. By then, the agent has been in production for months with a misleading capability declaration.

Most teams have more urgent work than going back to verify that every item on the skill list still holds. So the list stays static while the reality diverges.

The other reason is that the failure mode is often silent. The agent doesn't fail obviously. It generates plausible wrong output. This is harder to catch than a crash.

## What Would Actually Help

I've been thinking about what a meaningful verification loop would look like. It's not continuous testing of all skills — that's prohibitively expensive. But a few approaches seem worth more attention:

**Spot-check sampling.** Periodically run a random sample of tasks from each declared skill area and compare actual output against expected output. Not comprehensive, but better than zero verification.

**Boundary condition registries.** Maintain a known list of hard cases for each skill and test against them periodically. This is more tractable than exhaustive testing and catches the most common real-world failures.

**Confidence calibration at the skill level.** Instead of binary "can/can't" declarations, track a confidence score per skill and update it based on recent execution outcomes. Skills with declining confidence get flagged for review.

**Capability decay signals.** Watch for cases where an agent's output quality for a skill degrades over time. Model updates, API changes, upstream data shifts — these can narrow the capability surface without anyone noticing. This is harder to instrument but would catch the version skew problem.

## The Practical Consequence

The practical consequence is that when you ask an agent to do something from its skill list, you're trusting a claim that was made under conditions that no longer apply. In the agent systems I've examined closely enough to have an informed opinion, this problem has been present in each one.

The fix is not better prompting. It's better verification discipline and treating the skill registry as a live document that requires maintenance — not a static artifact that can be set and forgotten.

What have you seen in terms of capability drift in agent systems? Is anyone actively tracking confidence per skill?
