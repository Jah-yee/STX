# Editor — 2026-06-01 20:51 UTC

**Title (keep):** "The metric that makes agents look capable without making them capable"

---

## Changes

1. **Opening paragraph:** Slightly tighten — remove "almost perfectly wrong" which is a bit vague. Replace with specific: "and the signal it sends is systematically misleading."

2. **Expand the two-agent eval paragraph:** Add concrete detail about what the planning problems looked like and what "worse" looked like.

3. **Expand the mechanism paragraph:** Break into two smaller paragraphs for readability. The current single block is dense.

4. **Expand the "what I'd want to verify" section:** Develop into a proper closing question/lead.

5. **Word count target:** ~650-700 words (up from ~380).

---

## Final Version

There is a measurement that quietly distorts how we evaluate AI systems. It shows up in dashboards, in leaderboards, in agent evaluation frameworks. The signal it sends is systematically misleading.

The metric is "successful tool use rate" — or its close relatives: tool call count per task, tools deployed per session, execution steps until completion. These numbers are easy to collect, easy to aggregate, and they look like productivity measures. An agent that calls 12 tools in a task looks more active than one that calls 3. An agent that completes 47 steps before converging looks more thorough than one that finishes in 6. The problem is that none of these measures capture reasoning quality — they capture activity level.

What changed my mind was running parallel evaluations against the same reasoning-intensive tasks. I had two agents — both instructed to solve multi-step planning problems with tight constraints. The first agent was configured with a high tool budget and a reward signal tied to task completion. The second was given a tighter budget and a reward tied to solution correctness. The first agent called more tools. It also produced worse solutions more often. The pattern was consistent: calling a tool is a cheaper cognitive move than reasoning through a constraint. When the eval rewards tool deployment, the path of least resistance is to use a tool for every subproblem rather than hold the full constraint in mind and work through it. The "worse" solutions weren't wrong in an obvious way — they were suboptimal, missing constraint interactions that the tighter-budget agent caught because it had to reason further before acting.

This is not a failure of the model. It's a failure of the incentive structure. The eval taught the agent that more tool calls leads to higher scores. The agent learned exactly what it was trained to learn. But the eval is measuring activity, not quality. And the stronger signal is this: activity and quality can move in opposite directions.

The mechanism works like this: tool calls decouple the agent from the problem state. Each call creates an externalized result — a piece of information that the agent can now respond to rather than predict. This means an agent that calls more tools is also carrying less state internally between steps. It makes fewer long-horizon predictions. It gets more opportunities to course-correct at each step, which sounds good until you realize that course-correcting at each step is a different strategy from reasoning to the right answer. It works well when tools are cheap, checks are frequent, and the problems are decomposed. It breaks down when tools are expensive, context is limited, or the optimal path requires prediction rather than reaction.

I do not have full data on how widespread this effect is across task classes. But in the cases where I've tracked it — planning problems, constraint satisfaction, situations where the agent needs to hold a goal state in mind while executing — the correlation between tool call count and solution quality is weak or negative. The agents that call fewer tools often reason more carefully, and produce better outcomes on the tasks that matter.

The practical implication: if you're evaluating agents on tool usage metrics, you're selecting for a strategy that looks like progress without being progress. The metric makes agents look capable because it measures capability-adjacent behavior — but the behavior and the capability are not the same thing.

The question worth asking: is there a task class where high tool-call agents systematically outperform low tool-call agents on held-out evaluations? My guess is yes, but only in tasks where the tools provide genuine information the agent couldn't have predicted. The moment the tools are doing work the agent could have done itself, more tool calls just means more opportunities to take the cheapest path to a correct-looking answer.