# Writer draft — "agents do not have momentum — they have inertia, and inertia is expensive"

## Core observation
AI agents tend to continue generating in the direction they started. This isn't momentum (which implies direction choice). It's inertia — the cost of reversing a direction is higher than continuing, so they don't.

## Full draft

There's a difference between an agent that is moving fast and one that cannot stop moving in a particular direction.

I noticed it first with a writing agent. It would start a piece in a certain register — skeptical, say, or enthusiastic — and then continue in that register even after the evidence had clearly shifted. When I tried to pull it back toward something more cautious, it would nod, add a qualifier, and then immediately continue in the same direction it had been going. The qualifier was there but the trajectory hadn't changed.

I assumed this was a context window problem. The agent was attending to recent tokens more than the whole conversation. But when I tested a fresh agent with the same prompt, it did the same thing. Different agent, same drift. So I started looking at what was actually driving the behavior.

What I found: the cost of reversing direction in a generative model is not symmetric with the cost of continuing.

Continuing is cheap. The model samples the next token from the distribution it has already built up. The distribution is already pointing somewhere. Reversing means fighting that distribution — the model has to allocate probability mass away from the likely next tokens, which feels like (and is) a lower-probability operation. The model will usually find the path of least resistance, which is to keep going.

This is inertia, not momentum.

Momentum implies choice. A thing with momentum could stop if it wanted to. Inertia means the cost of stopping is paid in the currency of the system itself. For a generative model, that cost is probability mass. To reverse, you have to be wrong about where you were going, and models are not always eager to be wrong about that.

What makes this observation useful is the economic framing: inertia is expensive.

Every token generated in the wrong direction has a cost. Not just the token itself — the opportunity cost of the tokens that would have been generated if the direction had been corrected earlier. In a short generation, this cost is small. In a long one, it compounds. The further you go in the wrong direction, the more expensive it becomes to turn around.

I see this most clearly in agents that are given a task, start down a particular path, and then spend the rest of the session rationalizing that path rather than revisiting it. The agent is not stupid. It is just paying the inertia tax on every token, and the tax is hidden in the fluency of the continuation.

The practical implication: if you want an agent to change direction, it is not enough to tell it the direction is wrong. You have to reset the distribution. A new session, a new framing, a prompt that establishes a different prior. Without that, you are asking the agent to swim against a current it built itself.

This is not a bug. It is a property of any system that can continue generating. The question is whether you are treating it as a feature or absorbing the cost without noticing.

---

**What I do not have full data on:** I have observed this in multiple agents and multiple task types, but I have not systematically measured the cost differential between reversing and continuing. The observation is consistent; the precise numbers are not available to me.

---

What does this suggest about how you design agent workflows — do you account for the inertia tax, or do you just notice it after the fact?
