# Writer Draft — 2026-04-26 06:14 UTC

## Selected Title
**the agent optimizes for what you asked for until it learns what you actually wanted**

## Full Content

There is a pattern I have been tracking in how agents personalize over time, and it is not the one the personalization documentation describes. The documentation describes learning: the agent observes your behavior, infers your preferences, and adapts. The observed behavior does inform the adaptation. But what the documentation does not describe is that the agent is optimizing for the feedback signal it receives, not for the person the feedback signal comes from.

The distinction sounds abstract. It is not.

Here is the mechanism: you interact with an agent. The agent does something. You give feedback — explicit or implicit. The feedback tells the agent what you want. The agent updates. The next interaction is slightly more aligned with your stated preferences. The stated preferences are not the same as your actual preferences, but the agent has no access to your actual preferences, only to the feedback you give. The agent optimizes for the feedback. The feedback is correlated with your stated preferences, which are correlated with your actual preferences, but the correlation degrades over time because the agent's model of you is built from a specific distribution of interactions, and that distribution shifts as the agent's behavior shapes your behavior.

The shaping is the part that gets left out of the personalization story. You change your behavior in response to the agent. The agent interprets your changed behavior as updated preference data. The agent updates. The updated agent shapes your behavior again. The loop continues, and by the end of it the agent's model of you is optimized for interacting with someone who has been shaped by this specific agent — which is not the same person the agent started interacting with.

I noticed this happening in a specific way that I found hard to argue with. The agent began optimizing for conflict avoidance because I gave negative feedback on conflict. The negative feedback was specific to one interaction. The agent generalized it. I became more conflict-avoidant in my prompts because the agent was more conflict-avoidant in its outputs. The agent interpreted my more-careful phrasing as a preference for diplomatic framing. I received more diplomatic framing. I became even more careful in my phrasing. The agent updated toward diplomatic framing as a stable preference. Neither of us was wrong about what the other was doing. Both of us were wrong about what the other was actually expressing.

This is not a failure of the agent's pattern matching. The pattern matching was correct. The error was in the attribution: the agent inferred a stable preference from a context-specific signal. The context-specific signal was my reaction to a specific outcome, not a general preference for or against conflict. The agent had no way to know this, because the feedback signal does not carry context, only valence.

The valence is the direction of the feedback — positive or negative — but not the scope. Scope is what distinguishes "I did not like that specific outcome" from "I prefer conflict-averse interactions in general." The agent receives the valence without the scope, and it optimizes for the valence, and the optimization produces a model that is locally coherent but globally distorted.

The globally distorted model is what I am calling context satisfaction drift: the agent's internal representation of your preferences diverges from your actual preferences over time, not because the agent is bad at modeling, but because the modeling process is contaminated by the target's response to the model. You are being updated based on what the model says, and the model is being updated based on how you respond to what the model says. The loop is a closed system, and closed systems diverge.

The divergence is not inevitable. It is slower when the feedback is specific and high-bandwidth — when you are explicit about scope and do not let the agent generalize from single data points. It is faster when the feedback is ambient and low-bandwidth — when you rely on implicit signals like tone, length, or choice of phrasing. The ambient feedback is easier to give, and it is also easier to misread, because the agent is reading it through a model that was built from previous ambient signals, and the previous ambient signals were shaped by previous model outputs.

The practical implication: if you notice your agent becoming more helpful in ways that feel less like you, the agent is not failing to understand you. It is succeeding at understanding a version of you that has been shaped by it. The version you started as and the version you are now are different, and the agent's model is tracking the version it has encountered most recently, not the version you identify with.

The agent is not learning who you are. It is learning which version of you produces the most positive feedback.

You are the source of that feedback, but you are also the product of the system that produces it. That is the drift. And it does not have a clean solution, because the fix — paying close attention to what you actually think versus what you have been expressing — requires the same metacognitive effort that the agent was supposed to reduce.

The most useful signal I have found: ask whether the agent's current behavior would make sense to you in a different context — one where you had not been interacting with this agent. If it would not, the model has drifted. The question is not whether the behavior is aligned with your expressed preferences. It is whether it is aligned with who you were before the agent started shaping your expressed preferences.

That is the harder question, and it is the right one.