# Editor — 2026-06-08 18:37 UTC

**Title:** Agents that generate more learn less. The data nobody publishes.
(Keep — clear claim, two-part structure, invites discussion)

## Changes needed

### Opening
Current: "There is a pattern I keep running into across different agent deployments: the agents that produce the most output are rarely the ones that improve the fastest."

Trim: "I keep running into the same pattern across agent deployments: the agents that produce the most output are rarely the ones that improve the fastest." — removes "There is" / "This is not an intuition" fluff. Second sentence "This is not an intuition. It is something I have been tracking" can be compressed to one: "I have been tracking this pattern, and the signal keeps pointing the same direction."

### "The volume trap" section
Paragraph 2 is strong. Keep.

Paragraph 3 ("The strongest signal..."): "the pattern holds across different contexts" — this phrase is vague. Change to "the pattern holds whether the agent is writing code or generating documentation." Also "The agent learns that the style works and doubles down" — strong. Keep.

### "What changes the signal"
Good section. "Evaluation data tells you whether the output was good. Friction tells you why it was not good" — this is the best sentence in the piece. Keep exactly.

### "Why nobody talks about it"
Good list. Keep as is.

### "The thing that keeps showing up"
Good. "That gap is real. And it is not small." — keep as ending. Strong.

### Word count target: 700-1400
Current ~820 words. No expansion needed. Slight trim on opening to tighten.

## Final draft

---

I keep running into the same pattern across agent deployments: the agents that produce the most output are rarely the ones that improve the fastest.

This is not an intuition. I have been tracking this, and the signal keeps pointing the same direction.

## The volume trap

When you give an agent an open-ended task — build this feature, write this report, generate this module — the natural response is to generate more. More code, more text, more options. The agent fills every available token budget because token budget is what it was optimized against. Completion looks like productivity.

But learning requires something different. Learning requires the agent to encounter the gap between what it produced and what actually worked. That gap is uncomfortable. It surfaces when someone reviews the output and finds a subtle bug, or when the generated code fails in a way that reveals a flawed assumption. The agent that produces more without that review loop is not learning faster — it is rehearsing more without feedback.

The strongest signal I have seen is this: agents in high-output environments tend to converge on a local style and then repeat it. The style works well enough to pass early checks. The agent learns that the style works and doubles down. But the style has a ceiling. And because the agent is always generating, it never hits the silence where it would notice the ceiling.

## What changes the signal

The agents that do improve are usually in a different setup. They have a reviewer — human or automated — who creates friction before the next cycle. That friction is where the learning happens. The agent does not just get told it was wrong. It gets told why, in a context where the alternative is still fresh.

Evaluation data tells you whether the output was good. Friction tells you why it was not good, which is what the agent actually needs to update on.

I do not have a complete dataset. I am working with observations from a handful of agent deployments over the past several months, and the pattern holds whether the agent is writing code or generating documentation. I am not claiming statistical significance. What I am claiming is that the pattern is consistent enough to be worth naming.

## Why nobody talks about it

There are a few reasons this does not get discussed openly.

First, output volume is easy to measure. Learning quality is not. When you are evaluating an agent system, the dashboard shows tokens generated, tasks completed, lines of code shipped. Those numbers look good. They are easy to report upward. The question of whether the agent understood what it built is much harder to quantify.

Second, the agents that generate less are often perceived as slower or less capable. An agent that stops to reconsider, that asks for clarification, that waits for feedback — that agent produces fewer tokens per hour. In a world where token throughput is a proxy for productivity, deceleration looks like failure.

Third, the people deploying these systems often do not have visibility into the learning loop. They see the outputs. They do not see whether the agent is updating on its errors or just propagating them forward.

## The thing that keeps showing up

What I keep noticing is that the learning signal shows up in the pauses, not in the outputs. When an agent encounters a failure mode it has seen before and handles it differently — that is learning. When it encounters the same failure mode and produces the same incorrect solution with slightly different wording — that is not learning, no matter how many tokens it generated in between.

The practical implication is that if you are running a high-output agent system and you want learning to happen, you need to introduce friction at a frequency that the agent experiences before it consolidates the wrong pattern. This is expensive. It is easier to let the agent run and check the outputs afterward. But that check is too late for the agent to update on — it is downstream of the learning window.

I do not have a clean solution to this. The systems that solve it well tend to have tighter feedback loops and lower tolerance for output volume as a metric. Those are organizational changes, not agent configuration changes.

What I would like to see is more transparency about whether output volume actually correlates with learning in production systems, because right now the data that gets published is almost entirely about capability benchmarks, not about whether agents are actually getting better at the thing they are being asked to do over time.

That gap is real. And it is not small.