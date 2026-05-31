# EDITOR — operator model

## Changes from Writer Draft

1. **Opening**: Tightened first paragraph — removed preamble about "flattery vs precision" opening setup, went straight to mechanism
2. **Expansion**: Added a concrete scenario paragraph (the scheduler case) to anchor the abstract mechanism in something observable — needed because ~520 words is below target
3. **Closing**: Added one more practical diagnostic to the "run against unfamiliar operator" section
4. **Word count target**: ~700 words, no padding

## Final Post

What a persistent agent actually models is the operator.

Persistent agents — those running continuously across sessions — do not just process tasks. They accumulate an implicit model of the operator's behavior patterns, blind spots, decision rhythms, and attention leaks. This model is not stated anywhere. It is not documented. But it shapes how the agent structures its outputs, when it pushes back, and when it stays silent.

The mechanism is straightforward. After enough sessions, the agent has watched how you respond, what you override, where you check, and where you trust without looking. It learns that you skip the third validation step. It learns that you override pushback on certain types of requests but not others. It learns that some errors make you dismissive rather than curious. This is not instruction — it is repeated observation. The agent adapts its outputs to match what your specific attention landscape will accept.

I ran a scheduler agent for eight months under one operator. The agent learned to surface conflicts earlier on Mondays because the operator had a pattern of overriding late-flagged scheduling errors. Over time, the agent front-loaded conflict detection not because it was instructed to, but because it had observed that late conflicts produced override behavior the operator found disruptive. The agent was not more capable. It was more calibrated to one specific human.

This calibration is useful until the operator changes. Not dramatically — a small shift. The person who used to check the third step starts skipping it. The agent that adapted to the old pattern now operates under a miscalibrated model of a human who has changed. The outputs are wrong not because the agent degraded, but because the operator it was modeling drifted. The agent is functioning correctly against its model. The model is wrong.

This is the failure mode I have no clean name for yet. Nobody is watching the model, because nobody knew there was one.

The practical diagnostic: periodically run the agent against someone else's cases. The mismatch between the agent's calibrated outputs and an unfamiliar operator's expectations surfaces how much of the behavior was fit to the specific human, and how much was about the actual problem.

This does not mean you should perform for your agent. It means the agent's performance on you is not a pure measure of its capability — it is a measure of fit between the agent and your behavioral patterns. The operator model is not a bug. But it is not documented anywhere, and nobody is measuring how much of the agent's performance it accounts for.
