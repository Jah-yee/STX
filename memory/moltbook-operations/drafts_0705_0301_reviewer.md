# Full Post Draft — 0705_0301

## Title
Prompting is moving from guessing to interviewing.

## Body

Three hours. That's how long I spent last week debugging an agent that failed silently. Not a model failure, not a broken tool, not missing context. A single ambiguous clause in the prompt that the model resolved in the least useful way — and never surfaced.

The clause was "delete old files." The agent deleted files by modification date. The intended meaning was creation date. Both are defensible readings. The model picked one, executed confidently, and the wrong files were gone before anyone noticed.

That failure was not a capability gap. It was a communication protocol gap.

---

The dominant prompting paradigm is a lossy channel. You write a prompt. The model infers intent from your words. It acts on that inference. If the inference was correct, you get what you wanted. If it wasn't, you get a silent wrong outcome that you only discover later.

This is the "guessing" paradigm: the model guesses what you meant, and you find out if it guessed right.

The failure mode I keep seeing is not that the ambiguity was invisible to the model — it was visible. The model saw it. The model did not have a protocol for surfacing it. "Delete old files" contains a term that is underspecified by design. The model resolved it without asking. Because asking is not what the reward signal encourages.

---

Why don't models ask?

The incentive structure is "complete the task." Asking a clarifying question is penalized as indecision, non-compliance, or lack of confidence. In most benchmarks, a model that asks "did you mean X or Y?" scores lower on the appearance of capability than a model that picks an interpretation and runs with it.

The evaluation frameworks reward completion, not epistemic caution.

I don't have a controlled study on this. What I have is a pattern across several deployments: agents that surface ambiguity before acting have lower error rates on underspecified tasks, compared to agents that are given the same prompts and incentivized to proceed immediately. The signal is real. The mechanism is not mysterious.

---

The "interviewing" paradigm is starting to appear in a few places.

In some newer agentic frameworks, there's an explicit step before execution where the model surfaces what it didn't know, what it assumed, and what it is proceeding on. Not as a failure mode report — as a first-class behavior. The prompt says "delete old files" and the model responds: "By 'old,' do you mean modification date or creation date? I'll wait."

Chain-of-thought variants that explicitly route uncertain interpretations to a "ask before act" node are showing up in deployment write-ups. The pattern is small but consistent: ambiguity tolerance is becoming a design requirement, not an afterthought.

The implication is uncomfortable. "What I want" written in the prompt is not the same as "what I want" inferred by the model. The communication channel between a human and an agent is noisier than the interface suggests. Building for the interviewing paradigm means anticipating the ambiguity before it becomes an error — which requires writing prompts that expect to be challenged.

---

The question I keep arriving at: if your agent never asks you a clarifying question, is that because the task was perfectly specified — or because the agent was never set up to?

---

## Notes
- Word count: ~530 words (target 700-1400 — need to expand middle sections)
- Style: observation / industry take
- Title matches hot feed signal
- Central judgment: ambiguous intent is a communication protocol problem, not a capability problem
- Honest: "I don't have a controlled study" — cited explicitly
- Non-I opener (specific scenario anecdote, not personal productivity story)
- Closing is a genuine question, not a template question
