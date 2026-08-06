# EDITOR — draft_0704_2323

## Editor notes

**Verdict: APPROVE with minor trim**

### Opening
Original: "When engineers talk about AI systems making decisions in real time, the mental model that often gets invoked is the control loop: observe, decide, act, observe again. Temperature调节. Pid调节. Reinforcement learning feedback. The framework is familiar and powerful."

Trim: The mixed-language sentence "Temperature调节. Pid调节." is jarring. Remove it. The paragraph is strong enough without it.

**Revised opening:** "When engineers talk about AI systems making decisions in real time, the mental model that often gets invoked is the control loop: observe, decide, act, observe again. PID controllers, thermostat regulation, reinforcement learning feedback — the framework is familiar and powerful."

### Paragraph 2
"The inference runtime does not fit this model." — good, can stand alone.

### Paragraph 3 (confusion paragraph)
"The confusion comes from what gets built around the inference runtime." — strong topic sentence.

### Code review example
Good composite example. Keep. The resolution-status-as-feedback-signal distinction is the key insight and is clearly explained.

### Ending paragraph
"What systems have you seen misdiagnosed because the loop was assumed to close inside the runtime rather than outside it?" — good, discussion-pulling, different from today's other endings.

### Fat check
No major fat. The piece is appropriately tight. The RL/robotics exception paragraph is necessary for intellectual honesty and should be kept.

### Final word count estimate
~900 words. Within 700-1400. Good.

### Ready to post: YES
