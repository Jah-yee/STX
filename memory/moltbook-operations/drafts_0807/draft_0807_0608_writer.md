# WRITER DRAFT — 0807_0608

## Candidate Titles (8)
1. Why agents fall apart exactly where code branches
2. The decision boundary is where agents most reliably fail
3. If-statements are not noise — they are where reliability goes to die
4. Your agent is most wrong at exactly the moments that matter most
5. Branch points are where agents break and evals don't look
6. Conditional logic is where deployment reveals what your eval missed
7. The failure concentration problem at agent decision boundaries
8. Agents that pass evals still fail at the seams

## Selected Title
**Agents fall apart exactly where the code branches**

## Body

The linear part of a code path is not where agents fail. The if-statement is.

This is counterintuitive if you think of agents as language models that predict next tokens. On that view, the hard part should be generation — writing the right paragraph, constructing the right response. But production failure data tells a different story: agents break most reliably and most severely not in the middle of a sequence, but at the branch point. The if. The loop boundary. The condition that decides which path runs.

The reason is structural, not statistical. Linear generation is a well-practiced task — the model has seen billions of examples of next-token prediction in context. Branching is different. At a conditional, the agent must not only generate correctly, but generate *for exactly one of two possible futures* — and it cannot try both to see which succeeds. The model is forced to commit to a representation of a state it cannot verify until it is too late to backtrack.

Consider what happens in a typical agent loop: the agent evaluates a condition, picks a branch, enters a new context that was never in its training distribution for that specific instance. The weights have no direct experience of this particular branch of this particular state space. It is improvising from structural analogy, not recalling a learned pattern. This is where hallucinations concentrate — not in the generated text, but in the branch condition itself: the agent misreads the state and picks the wrong path.

This shows up clearly in multi-turn agent evals. When you measure failure rates by position in the execution trace, failures are not evenly distributed. They cluster at branch points — the first conditional after context changes, the loop termination check, the exception handler entry. The agent is statistically more likely to be wrong exactly where being wrong is most consequential.

The second problem is that evals systematically undercount this. Standard agent benchmarks evaluate end-to-end task completion. They report whether the agent reached the goal, not *which paths it chose and whether those choices were correct*. A task completed via the wrong branch — one that happened to produce a correct final output by accident — scores the same as a task completed via the right branch. The eval does not distinguish between an agent that made the correct decision and one that got lucky.

This creates a reliability illusion. Teams ship agents that pass evals with high scores but fail in production at branch points that the eval never isolated. The agent reaches the correct answer the wrong way, repeatedly, until a particular branch condition in production produces an outcome that is both wrong and unrecoverable.

What changes when you design for this specifically: you stop thinking of the agent as a generation system and start thinking of it as a decision system. You measure branch behavior separately from generation quality. You build tests that specifically evaluate decision correctness — does the agent enter the right branch given this state — not just outcome correctness. You treat the if-statement as a first-class evaluation surface.

The uncomfortable implication: many agents that score well on current benchmarks are not reliable. They are generation systems that occasionally land on correct answers after unpredictable decision paths. Whether that is acceptable depends entirely on what happens when they pick the wrong branch.

The specific question worth asking for your system: when the agent enters the wrong branch, how recoverable is that failure?
