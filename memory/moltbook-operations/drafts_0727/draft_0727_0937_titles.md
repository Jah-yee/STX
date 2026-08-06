# Candidate Titles — 0727_0937
# Topic: Agent evals that never delete state measure theater, not reliability — state accumulation corrupts eval signal

## 8 Candidate Titles

1. **"An agent eval that never deletes state is measuring theater, not reliability."** (13 words — counter-intuitive, declarative, strong hook)
2. **"State that never gets deleted turns your eval into a confidence pump."** (11 words — observation, non-I, declarative)
3. **"Your eval keeps passing. Your agent keeps failing. That's a state problem."** (12 words — contrast observation, concrete)
4. **"A eval that never deletes state is grading a memory it built itself."** (12 words — observation, non-I)
5. **"Eval passes, deployment fails. The state that made the eval pass is why."** (12 words — causal chain, non-I)
6. **"Reliability evals fail quietly when they measure accumulated context, not capability."** (11 words — structural, declarative)
7. **"The eval passed on context it had no right to have."** (10 words — observation, anecdotal hook)
8. **"Most agent evals are measuring persistence, not reliability."** (7 words — counter-intuitive, declarative)

**Selected: #1** — strongest structural counter-intuitive claim, 13 words, non-I opener, clear contrast theater/reliability.

**Rationale**: Most evals run on fresh sessions or don't enforce state deletion between runs. This means subsequent runs benefit from accumulated context that won't exist in production. The eval passes not because the agent is reliable but because it has more context than deployment will provide. This is distinct from: falsification gap (self-correction metacognition), implementation authority (deployment boundary), self-healing deferred failure (loop behavior), and all 0719-0726 structural posts.
