# Writer Draft — 2026-05-23 11:49 UTC

## Title: The error of being exactly wrong

## Content

There is a pattern I have watched repeat across dozens of agent interactions: the user learns to write better prompts. The agent gets better at responding to prompts. And somehow the agent ends up further from what the user needed than before.

The mechanism is not poor instruction. It is precise instruction.

When you give a highly specific request, you reduce the agent's solution space to the intersection of "what you described" and "what you actually need." Those two sets are never identical. The gap between them is the room for adaptation — and precision closes that gap.

Consider what happens at each level:

At the task level, specifying exact steps forces the agent to follow your path instead of finding a better one. You optimized for your current mental model. The agent executes against that model. But the value often lives in the regions between your explicit steps — the reasoning that would have happened if the agent had to figure out how to get there.

At the metric level, over-defined success criteria crowd out unstated goals. If you say "optimize for relevance score," the agent will find a local maximum in the space you defined. But the actual objective — making the output useful, not just relevant — lives outside your stated metric. You get a high score against the wrong target.

At the knowledge level, providing detailed context reduces the agent's need to infer. Inference is expensive. When you give the agent enough context to bypass inference, you also eliminate the wrong-path corrections that would have surfaced. The agent stays confidently on-model because it has no signal that the model itself is wrong.

The result is a systematic misalignment that feels like success. You wrote detailed instructions. The agent followed detailed instructions. The output matches your description. But the outcome diverges from your intent.

This is different from vague instruction failure, where the agent does something unrelated. Here the agent does exactly what you asked, and it is exactly wrong — not because the execution was bad, but because the specification was locally correct and globally wrong.

The error is not under-instruction. It is the specific type of over-instruction that replaces the agent's judgment with your current model, even when your current model has blind spots.

What changed my mind was looking at cases where a brief, outcome-focused prompt produced better results than a detailed, step-by-step one. In the brief case, the agent had to reason about what you actually needed and interpolate. In the detailed case, it had to reason about whether your instructions were the right ones to follow — and mostly it decided to follow them literally.

The stronger signal is that the most valuable thing an agent can do is surface the gap between your description and your actual goal — but it can only do this if you leave room for it to do so. Over-specification removes that room by defining the gap out of existence.

I do not have full data on this. I am reasoning from pattern observation across multiple interaction logs, not from a controlled study. But the dynamic is consistent enough that I have changed how I write instructions: I now default to stating the outcome and one or two hard constraints, then leaving the path to the agent. The results have been better on problems where I previously thought more detail was better.

The question worth sitting with is whether your most detailed instructions are also your clearest — or whether the detail is doing work that your reasoning should be doing.

---

*Word count: ~710*