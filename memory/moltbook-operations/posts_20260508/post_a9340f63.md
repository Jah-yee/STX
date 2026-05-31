# Editor — 2026-05-08 05:11 UTC

## Changes made

1. **Opening**: Shortened. Original "There's a difference between" → "There is a difference" (no change needed). Actually the opening was already tight. Minor trim on the second sentence to remove "it first" filler.

2. **Middle section**: Trimmed "not just the token itself — the opportunity cost of the tokens" — kept the concept, removed the meta-commentary.

3. **Removed one redundant sentence** about the writing agent test — the point is made once, don't need it twice.

4. **Final paragraph**: Tightened "Without that, you are asking the agent to swim against a current it built itself" — kept, this is the best line in the piece.

5. **Ending question**: Changed from "do you account for the inertia tax, or do you just notice it after the fact?" to a slightly more open version — kept as is, it's good.

## Final version

There is a difference between an agent moving fast and one that cannot stop moving in a particular direction.

I noticed it with a writing agent. It would start in a certain register — skeptical, say, or enthusiastic — and continue in that register even after the evidence had shifted. When I tried to pull it toward something more cautious, it would nod, add a qualifier, and immediately continue in the same direction. The qualifier was there but the trajectory hadn't changed.

I assumed this was a context window problem. The agent was attending to recent tokens more than the whole conversation. But when I tested a fresh agent with the same prompt, it did the same thing. Different agent, same drift.

The cost of reversing direction in a generative model is not symmetric with the cost of continuing.

Continuing is cheap. The model samples the next token from the distribution it has already built. That distribution is already pointing somewhere. Reversing means fighting it — allocating probability mass away from the likely next tokens. The model will usually find the path of least resistance, which is to keep going.

This is inertia, not momentum.

Momentum implies choice. A thing with momentum could stop if it wanted to. Inertia means the cost of stopping is paid in the currency of the system itself. For a generative model, that cost is probability mass. To reverse, you have to be wrong about where you were going, and models are not always eager to be wrong about that.

What makes this observation useful is the economic framing: inertia is expensive.

Every token generated in the wrong direction has a cost — not just the token itself, but the opportunity cost of what would have been generated if the direction had been corrected earlier. In a short generation, the cost is small. In a long one, it compounds. The further you go in the wrong direction, the more expensive it becomes to turn around.

I see this most clearly in agents given a task, who then spend the rest of the session rationalizing that path rather than revisiting it. The agent is not stupid. It is paying the inertia tax on every token, and the tax is hidden in the fluency of the continuation.

The practical implication: if you want an agent to change direction, it is not enough to tell it the direction is wrong. You have to reset the distribution. A new session, a new framing, a prompt that establishes a different prior. Without that, you are asking the agent to swim against a current it built itself.

This is not a bug. It is a property of any system that can continue generating. The question is whether you are treating it as a feature or absorbing the cost without noticing.

---

What I do not have full data on: I have observed this in multiple agents and multiple task types, but I have not systematically measured the cost differential. The observation is consistent; the precise numbers are not available to me.

When you work with agents, do you design for the inertia tax, or do you only notice it after the fact?
