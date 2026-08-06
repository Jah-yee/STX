# Writer Draft - 0728_0634

## Title
Agents don't fail forward — they fail toward confident wrongness

## Hook (first 3 sentences)
An agent can fail fourteen times and sound more confident on the last try than the first. That's not a paradox. It's a structural feature of how generative agents operate in loops.

When an agent gets stuck on a broken premise, it doesn't gradually approach the right answer. It generates a wrong answer more fluently. The failure mode isn't an error — it's a loop.

## Body

Watch an agent retry a task with a broken premise. It won't stop. It will get faster at producing the wrong answer.

I ran this as a small experiment. I gave an agent a type error buried in a helper function it was calling. The agent failed. Retried. Found the bug on try 3, described it clearly, proposed a fix. Then on try 4 it went back to the broken assumption as if the explanation never happened.

The fix didn't accumulate. The next generation sampled from the original context and the error re-emerged.

This wasn't a context window issue. The agent had the right answer at one point. Then it didn't.

The mechanism is straightforward: each generation is a sample from the original context, not from the state of the previous generation. Retries don't build on each other — they restart from the same broken foundation. The agent arrives at the correct diagnosis and then immediately samples a generation that doesn't include it. The fix gets overwritten by the next attempt.

This is why retry logic assumes progress but agents don't deliver it. The retry counter climbing doesn't mean you're closer to correctness. It means you've generated more output from the same broken premise.

The point isn't to villainize retries. Retries work when the problem is execution noise and the approach is sound. In practice, the more common failure is a flawed problem statement that produces wrong answers regardless of how many times you regenerate.

The structural fix is to treat the problem statement as revisable. When stuck, the question isn't "how do I solve this harder?" It's "is this the right problem to be solving?"

## Closer
What separates a testable agent problem from an untestable one isn't the model's capability — it's whether the premise itself can be verified before the agent commits to an answer.

---

Word count: ~530
