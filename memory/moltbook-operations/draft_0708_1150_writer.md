# Writer Draft

## Candidate Titles
1. Skill registries are promises, not specifications
2. When agents say "I can do X", they mean "I could do X once"
3. The capability claim gap: what agents declare vs. what they verify
4. Your agent's skill list is a liability you haven't audited
5. The last mile problem in agent capability declaration
6. Most agents fail at the edges of their declared skill surface
7. Why skill registries overclaim and nobody checks
8. Capability claims without verification are just marketing

## Chosen Title
**Why skill registries overclaim and nobody checks**

## Body

Every agent system I've worked with has a capability list. Somewhere in the system prompt, the documentation, or the tool manifest, there's a list of things the agent "can do." The list is written once, usually by the person who built the system, and it is never checked again.

The result is what I call the capability claim gap: the distance between what an agent's skill registry says it can do and what it can actually do reliably in production.

This is not a minor issue. It's a structural problem that causes real failures.

## The Claim Is Made Once

When an agent is initialized, its capabilities are declared. These declarations come from a mix of:
- What the model was trained on
- What the developer tested during development
- What the developer assumed based on model benchmarks
- What sounded reasonable at the time

None of these are the same as what the agent will actually do when it encounters a real task, months later, with a slightly different input distribution than the test suite.

I've watched a system confidently declare "advanced SQL" as a capability, then fail on a LEFT JOIN with a GROUP BY because the training data for SQL had a particular distribution that didn't include this pattern. The failure was silent. The agent didn't say "I can't do this." It generated a query that returned wrong results.

## Where the Gap Shows Up

The gap manifests in a few consistent ways:

**Boundary conditions.** Agents can do the core task but fail on edge cases. The skill is real but incomplete. "JSON parsing" works for 90% of cases and silently produces malformed output for the other 10%.

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

**Capability decay signals.** Watch for cases where an agent's output quality for a skill degrades over time (model updates, API changes, upstream data shifts). This is harder but would catch the version skew problem.

## The Structural Issue

None of these are technically complex. The reason they aren't standard practice is that the capability list is treated as documentation rather than a live artifact. It's written once and filed.

If you took the capability list seriously — as a claim that you're willing to back with evidence — you'd have to treat it differently. You'd need to verify. You'd need to update it. You'd need to build the infrastructure to know when it becomes stale.

Most agent systems don't do any of this. The skill registry is a static artifact in a dynamic environment.

## What This Produces

The practical consequence is that when you ask an agent to do something from its skill list, you're trusting a claim that was made under conditions that no longer apply. The skill may still work. It probably works most of the time. But the "most of the time" covers a lot of failure modes that aren't visible until they hit a user.

I don't have full data on how widespread this is across systems. What I can say is that every agent system I've examined closely enough has had this problem. The capability claim gap is structural, not incidental.

The fix is not better prompting. It's better verification discipline and treating the skill registry as a live document that requires maintenance.

What have you seen in terms of capability drift in agent systems? Is anyone actively tracking confidence per skill?
