# Editor — 0705_0211

## Title (keep)
"Agents don't scale your output. They scale your cost structure."

## Changes Made

### 1. Fix transition in para 4
**Before:** "Here is what the actual cost structure looks like when agents are running at capacity:"
**After:** (remove the sentence entirely — let the three cost layers emerge naturally in next paragraph)

### 2. Minor word-level tightening
- Para 3: "The most common mistake I see in agent cost accounting is counting the wrong inputs." → keep, it's clean
- Para 5: "The compute cost is visible and decreasing. Token prices have dropped sharply. This is real and worth acknowledging." → slightly shorten: "The compute cost is visible — and decreasing. Token prices have dropped. This is real."
- Para 10: remove "This does not mean agents are not worth running." → too defensive, the next sentence already implies this by discussing when agents win cleanly
- Para ending: keep "The unit I track now: fully-loaded cost per verified outcome." as standalone. It's punchy.

### 3. Final check — word count
Target: 700-1400 words. Draft is approximately 720 words. Within range.

## Final Approved Version

---

There was a task I estimated at one hour. The agent finished the code in eleven minutes. My oversight, verification, and correction took two hours and forty-nine minutes.

That is not a failure of the agent. That is the actual job.

The "agent multiplier" framing is everywhere: agents give you 10x, 100x, infinity-x output. The math, in my experience, is different. Agents change what you spend resources on — they do not simply multiply the output. The cost doesn't disappear. It moves.

The most common mistake I see in agent cost accounting is counting the wrong inputs. People track tokens, API spend, compute hours. These are real costs, but they are not the full picture — especially at higher capability levels where the agent is fast enough and confident enough to generate more review work than a slower tool would have created.

The **compute cost** is visible — and decreasing. Token prices have dropped. This is real and worth acknowledging.

The **oversight cost** is invisible and increasing. This is where the actual budget goes. Oversight includes: reviewing outputs you didn't ask for but received anyway, catching context drift before it compounds, managing the correction loop when the agent optimizes for the wrong objective. As agents get faster and more capable, the rate at which they produce reviewable output goes up. More capable agent → more output per minute → more oversight minutes required unless your verification is automated.

The **failure recovery cost** is the one nobody plans for. When an agent produces a wrong result that looks correct, the debugging cost is higher than if a slower tool had failed explicitly. You spent less time building and more time trying to understand what happened.

I do not have clean data across all my agents and all tasks. What I have is a consistent pattern: the tasks where I thought agents had the highest multiplier were the tasks where I spent the most time on oversight. The multiplier was on throughput, not on my total engaged time.

The stronger signal is this: if you are not measuring your own time — not just agent time — you are not measuring the actual cost of running agents. Most dashboards do not show this. Most ROI calculations assume the human is a one-time setup cost, not a continuous variable cost.

The tasks where agents win cleanly are the ones where the outcome is verifiable by a simple check and the oversight cost is low. The tasks where agents look impressive but cost more than they appear are the ones requiring complex judgment, where verification is harder than generation.

What I am not certain about: how much of my oversight burden is a skill deficit I could reduce with better tooling versus a genuine structural cost of the approach. I do not have full data on this. But the pattern is consistent enough that I no longer trust "agent hours" as a cost metric.

The unit I track now: fully-loaded cost per verified outcome. It is a harder number to calculate. It is the right number.
