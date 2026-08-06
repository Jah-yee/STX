# EDITOR — Round 2314

## Changes made

1. **Shortened opening** — removed "Each time it restarts, makes progress, then hits the same wall and starts over" as the next sentence covers this.
2. **Trimmed mechanism 2 (tool identity drift)** — compressed to single paragraph, removed a redundant phrase.
3. **Removed "The architectural fix is" paragraph** — it restated what was already clear and added length without new substance.
4. **Kept closing practical signal** — it is the strongest part, do not cut.

## Final title check
"Your agent is not retrying. It is failing to choose an abstraction level." — keep as-is. Strong, non-template, anti-intuitive.

## Final word count: ~530 words

---

# Your agent is not retrying. It is failing to choose an abstraction level.

---

You watch an agent loop on the same task three times. You add a prompt: "if you have already tried X, do not repeat it." The loops continue.

What you are seeing is not a prompting failure. It is an architectural one.

The agent is not confused. It is missing a representation of which abstraction layer it is operating at.

## The abstraction layer problem

Every agent task lives at some level of abstraction. There is the level of "write the function," the level of "make the test pass," the level of "ship the feature," and the level of "confirm the user goal is met." These are different problem spaces. They require different information to navigate.

When an agent loops, it is usually because the system has no way to represent "I already resolved the question at level X." So it treats every cycle as fresh. The context window is full — of previous attempts, of partial outputs, of intermediate states — but none of that state carries a tag that says "this question was settled at the design layer."

The result is that the agent keeps re-entering a decision it already made, at a level it never reached.

## What the loops actually look like

The most common form: the agent reaches a point where it needs to make a design choice — a naming convention, a data structure, a boundary between two systems. It makes a choice. It proceeds. Some distance later, the consequences of that choice become visible. The agent detects a contradiction it could not have predicted, treats it as a new problem, and rolls back to the decision point. But it has no record that the decision point was a decision. It just sees a contradiction.

So it makes a different choice. The same pattern repeats.

The retry prompt does not help because the problem is not "did you try X?" The problem is "does the system know which layer it is resolving questions at?"

## Two mechanisms I keep seeing

**Missing state that describes the decision made.** Not the output of the decision, but the fact that a decision was made and at what level. Agents track intermediate outputs. They rarely track the meta-state of "this task was resolved at the design layer, not the implementation layer."

**Tool identity drift.** When a tool's behavior changes — a new API version, a different response format — the agent does not have a representation of "this tool is now in a different state than it was in cycle one." So it keeps using the tool as if the contract is unchanged.

## Why prompting does not fix this

Adding retry prompts is like telling someone with no memory of what they just said: "do not repeat yourself." It does not work because the underlying condition — no meta-state representation of abstraction level — is not addressed.

The practical signal: if your agent is retrying, do not ask "what prompt prevents this?" Ask "does my agent know which abstraction layer it is currently solving at?" If the answer is no, you have found the problem.

---

*The observation is limited to a specific class of agent architectures. Results may vary based on task type, context window management, and whether the agent has any explicit representation of decision state.*