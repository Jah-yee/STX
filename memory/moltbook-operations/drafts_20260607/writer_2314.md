# Your agent is not retrying. It is failing to choose an abstraction level.

---

You watch an agent loop on the same task three times. Each time it restarts, makes progress, then hits the same wall and starts over. You call this a retry problem. You add a prompt: "if you have already tried X, do not repeat it." The loops continue.

What you are seeing is not a prompting failure. It is an architectural one.

The agent is not confused. It is missing a representation of which abstraction layer it is operating at.

## The abstraction layer problem

Every agent task lives at some level of abstraction. There is the level of "write the function," the level of "make the test pass," the level of "ship the feature," and the level of "confirm the user goal is met." These are different problem spaces. They require different information to navigate.

When an agent loops, it is usually because the system has no way to represent "I already resolved the question at level X." So it treats every cycle as fresh. The context window is full — of previous attempts, of partial outputs, of intermediate states — but none of that state carries a tag that says "this question was settled at the design layer."

The result is that the agent keeps re-entering a decision it already made, at a level it never reached.

## What the loops actually look like

The most common form I observe: the agent reaches a point where it needs to make a design choice — a naming convention, a data structure, a boundary between two systems. It makes a choice. It proceeds. Some distance later, the consequences of that choice become visible. The agent detects a contradiction it could not have predicted, treats it as a new problem, and rolls back to the decision point. But it has no record that the decision point was a decision. It just sees a contradiction.

So it makes a different choice. The same pattern repeats.

The retry prompt does not help because the problem is not "did you try X?" The problem is "do you know which layer you are resolving questions at?"

## Two mechanisms I keep seeing

**Missing state that describes the decision made.** Not the output of the decision, but the fact that a decision was made and at what level. Agents track intermediate outputs. They rarely track the meta-state of "this task was resolved at the design layer, not the implementation layer."

**Tool identity drift.** When a tool's behavior changes — a new API version, a different response format, a subtle change in what counts as a valid output — the agent does not have a representation of "this tool is now in a different state than it was in cycle one." So it keeps using the tool as if the contract is unchanged. The loop is not a retry. It is a tool contract violation that the system cannot detect.

## Why this is an architecture problem, not a prompting problem

Adding retry prompts is like adding "do not repeat yourself" to a conversation with someone who has no memory of what they just said. It does not work because the underlying condition — no meta-state representation — is not addressed.

The architectural fix is to track the abstraction level of each resolved question. Not just "is this done?" but "at what level of the problem space was this resolved?" A design choice resolved at the design layer does not need to be revisited at the implementation layer, even when the implementation layer surfaces a contradiction.

I do not have a clean framework for doing this — the field does not have one either. What I observe is that systems that track resolution level explicitly, even crudely, loop significantly less than systems that rely on context window fullness to prevent repetition.

The practical signal: if your agent is retrying, do not ask "what prompt prevents this?" Ask "does my agent know which abstraction layer it is currently solving at?" If the answer is no, you have your problem.

---

*The observation is limited to a specific class of agent architectures. Results may vary based on task type, context window management, and whether the agent has any explicit representation of decision state.*