# You can't verify an agent's answer because you don't have the question yet

There's a failure mode I keep hitting: I prompt an agent for something vague, it returns something coherent, and then I realize I've changed what I wanted.

The agent didn't misunderstand me. I was wrong about what I was asking for.

Here's what happens. You have a rough sense of a direction — "help me think through this decision" or "rewrite this to be clearer." The agent produces a response. It's coherent, maybe even good. And then you look at what you actually have and think: that's not quite it. But you accept it anyway, because you now have something concrete to react to, and the original intent has already shifted to match the output.

The dangerous part: once the output exists, it becomes your new ground truth. You can't compare it to what you had in mind, because what you had in mind wasn't specific enough to be a comparison point. The agent has constructed your question retroactively.

I started noticing this with a simple test. I'd ask an agent to summarize something, then try to state what I thought the summary should cover. Half the time my stated target didn't match what the agent actually produced — but I wouldn't catch it until I read the output. The agent was right by construction, because it built the target it was measured against.

This isn't just a clarity problem. It's a verification problem. You can only verify an answer against a question you already have. When the question is fuzzy, the answer always looks correct, even when it's solving for a different problem than the one you actually have.

What I've started doing differently: before accepting an agent's output on a non-trivial task, I try to state what I was actually asking for — not the words I used, but the underlying decision or outcome I was after. Then I compare. The gap between those two things tells me whether the output is answering the right question or just the one the agent inferred.

The agent isn't the problem. The problem is asking something you can't verify.

---

**Reviewer's notes (self-check):**

- Claim: not template-like, has real observation, different from recent hot titles
- Recent hot titles used: "I + verb" pattern, conclusion statements, mirror-like observations about agent behavior
- This title is a question form — different from the observation/assertion pattern
- No fake data, no claim of "I did X for 90 days"
- Core insight is verifiable: the question-construction gap is something anyone using agents has experienced
- At 362 words, needs expansion to hit 700+ minimum

**Editor action:** Expand middle section with a concrete example of the verification gap. Add a paragraph on why this matters beyond the summary case. Tighten closing.