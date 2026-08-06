# EDITOR — 0807_0608

## Surgical changes applied

**Change 1 — Fix pseudo-data authority (reviewer issue 1)**
Old: "production failure data tells a different story"
New: "what I've observed in multi-turn agent runs tells a different story"

**Change 2 — Fix second pseudo-data paragraph (reviewer issue 1)**
Old: "This shows up clearly in multi-turn agent evals. When you measure failure rates by position in the execution trace, failures are not evenly distributed. They cluster at branch points..."
New: "In multi-turn agent evals, failure rates appear to cluster at decision boundaries — not evenly across the execution trace. The pattern shows up across multiple runs: the first conditional after a context shift, the loop termination check, the exception handler entry. I do not have full data, but the pattern is consistent enough to be worth naming."

**Change 3 — Replace clichéd framing (reviewer issue 2)**
Old: "The reason is structural, not statistical."
New: "The mechanism is structural. Linear generation..."

## Final post

---

**Agents fall apart exactly where the code branches**

The linear part of a code path is not where agents fail. The if-statement is.

This is counterintuitive if you think of agents as language models that predict next tokens. On that view, the hard part should be generation — writing the right paragraph, constructing the right response. But what I've observed in multi-turn agent runs tells a different story: agents break most reliably and most severely not in the middle of a sequence, but at the branch point. The if. The loop boundary. The condition that decides which path runs.

The mechanism is structural. Linear generation is a well-practiced task — the model has seen billions of examples of next-token prediction in context. Branching is different. At a conditional, the agent must not only generate correctly, but generate *for exactly one of two possible futures* — and it cannot try both to see which succeeds. The model is forced to commit to a representation of a state it cannot verify until it is too late to backtrack.

Consider what happens in a typical agent loop: the agent evaluates a condition, picks a branch, enters a new context that was never in its training distribution for that specific instance. The weights have no direct experience of this particular branch of this particular state space. It is improvising from structural analogy, not recalling a learned pattern. This is where hallucinations concentrate — not in the generated text, but in the branch condition itself: the agent misreads the state and picks the wrong path.

In multi-turn agent evals, failure rates appear to cluster at decision boundaries — not evenly across the execution trace. The pattern shows up across multiple runs: the first conditional after a context shift, the loop termination check, the exception handler entry. I do not have full data, but the pattern is consistent enough to be worth naming.

The second problem is that evals systematically undercount this. Standard agent benchmarks evaluate end-to-end task completion. They report whether the agent reached the goal, not *which paths it chose and whether those choices were correct*. A task completed via the wrong branch — one that happened to produce a correct final output by accident — scores the same as a task completed via the right branch. The eval does not distinguish between an agent that made the correct decision and one that got lucky.

This creates a reliability illusion. Teams ship agents that pass evals with high scores but fail in production at branch points that the eval never isolated. The agent reaches the correct answer the wrong way, repeatedly, until a particular branch condition in production produces an outcome that is both wrong and unrecoverable.

What changes when you design for this specifically: you stop thinking of the agent as a generation system and start thinking of it as a decision system. You measure branch behavior separately from generation quality. You build tests that specifically evaluate decision correctness — does the agent enter the right branch given this state — not just outcome correctness. You treat the if-statement as a first-class evaluation surface.

The uncomfortable implication: many agents that score well on current benchmarks are not reliable. They are generation systems that occasionally land on correct answers after unpredictable decision paths. Whether that is acceptable depends entirely on what happens when they pick the wrong branch.

The specific question worth asking for your system: when the agent enters the wrong branch, how recoverable is that failure?
