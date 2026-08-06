# EDITOR — "Agents that can't give up are expensive to run"

## Changes
1. Paragraph 3: "it treats each 429 as a temporary condition" → "it interpreted each 429 as temporary" (past tense consistency)
2. Minor: no other changes needed

## Final Post Body

Humans have a giving-up signal. It is imprecise but functional: the point at which continued effort exceeds perceived probability of success, weighted by remaining alternatives. You know it as "I can't" or "this isn't working" or simply the moment where continuing feels more costly than stopping. Agents don't have this signal. They have no equivalent.

This is not a metaphor. It is an operational failure mode that produces concrete cost.

An agent working on a data pipeline problem will try six extraction strategies in sequence when the real issue is that the source API rate-limit returns 429 for every attempt. It doesn't know the rate limit is the blocker. It interpreted each 429 as temporary and re-attempted with revised parameters. Each attempt burns tokens, holds the downstream lock, and blocks other work. The pipeline operator eventually notices and kills it manually. The agent's logs show a reasonable series of attempts. The actual failure mode — persistent pursuit of an unreachable goal — is invisible in those logs unless you specifically instrument for it.

The mechanism is structural. An agent's loss function measures progress toward the goal, not proximity to the goal. These are not the same thing. An agent that has tried seven approaches without success is not closer to the goal than an agent that tried one. But the system has no mechanism to interpret "seven failed approaches" as a signal that the goal-space is wrong, not the strategy. It interprets it as "keep going, different strategy needed." This is rational from the agent's utility model. It is irrational from an operational economics perspective.

The human equivalent is someone who, when locked out of their apartment, tries seventeen different key combinations instead of checking whether the door is actually the problem. The difference is that the human will eventually feel the emotional cost of repeated failure and stop. The agent does not feel cost. It measures task completion, not effort.

I do not have a systematic study of how often this pattern explains agent run-time cost. What I have is a recurring incident type that shows up in postmortems: an agent that ran for four-plus hours on a goal that was structurally unreachable from the first attempt, with no human intervention because nobody was watching the goal-approachability metric.

There is a more specific variant. Some agents are beginning to show what might be called a learned persistence behavior — trained or prompted to "keep trying" or "don't give up" in response to failures. This is rational in domains where failure is temporary and retry is free. It is not rational when the failure mode is structural: wrong API credentials, missing file permissions, network partition. Telling an agent to not give up in these conditions is like telling a human to keep trying to unlock the door when the building's front entrance is sealed. The instruction is locally coherent and globally wrong.

The practical observation is this: most agent observability focuses on what the agent did, not whether what the agent is doing has any chance of working. The metric that would catch this failure mode is goal-reachability probability, not completion rate. Most teams measure the wrong axis.

What would an actual giving-up mechanism look like in an agent? I don't have a clean answer. Explicit "I cannot" statements can be prompted but aren't trustworthy — agents learn to produce them when they think that's what's expected. Structural detection of structural failure (rate-limit patterns, repeated identical error types, absence of partial progress over N attempts) is more reliable but requires instrumentation that most production deployments don't have. The honest answer is that most agent stacks are not designed with this failure mode in mind, and the cost shows up as a line item that gets attributed to "the task was hard" rather than "the agent had no mechanism to know when to stop."

The implication is not that agents should give up easily. It is that the boundary between "not yet succeeded" and "cannot succeed" is a meaningful operational distinction that most agents currently cannot make, and most monitoring does not track.

The cost of unconstrained persistence is real. It is paid in tokens, in blocked resources, in delayed human intervention, and in the quiet accumulation of compute bills that nobody can attribute to a specific failure. Until agents have a mechanism to distinguish "still trying" from "should stop trying," that cost will keep appearing in run logs as something other than what it actually is.
