# Writer Draft — 0802_0130
# Title: My drift detector became useful when I stopped measuring inputs

---

The classic drift detection setup feels correct in theory: watch what the agent reads, flag when it changes. In practice, I spent weeks generating alerts that told me nothing I didn't already know.

The detector was technically working. It fired reliably. The problem was that every alert fired on the same event — the context window approaching capacity. Not model behavior drift. Not task distribution shift. Just the input buffer filling up. The alert was measuring the wrong thing, so it was always on.

I do not have full data on how widespread this specific failure mode is. But the pattern repeated across different agent architectures and different task types, and the mechanism is straightforward: an agent's input stream and its behavioral trajectory are coupled but not identical. You can watch inputs all day and learn almost nothing about what the agent is actually doing.

What changed my mind was running a shadow-mode experiment: I kept the input-tracking detector running but added a second, independent signal — output entropy measured at the action selection layer, not the observation layer. Within a few days, the output-based signal was catching something the input tracker never touched: cases where the agent's response distribution shifted even though the prompt context was stable.

The reason is structural. Input drift is a proxy signal. It tells you the environment changed, not that the agent is responding differently. Output drift is the actual thing you care about — the agent's actual behavior. The proxy fires constantly (context updates constantly), while the target signal is actually informative but gets buried.

There is a harder version of this problem that I have not solved: what do you measure when the output space is also unstable — when the task itself is changing faster than the agent can be calibrated? That is a different regime. The output entropy approach helps when the task is fixed but the model's relationship to the task is drifting. It does not help when the task definition itself is moving.

The practical upshot: if your drift detector fires on input events, check what it is actually telling you. If the answer is "the context changed," that is not a drift signal. That is a context-length warning. They look similar in a dashboard. They mean completely different things.

I am more careful now about what I call a signal. Some monitoring is just logging with extra steps.

---

*What do you measure when the task itself is the variable?*
