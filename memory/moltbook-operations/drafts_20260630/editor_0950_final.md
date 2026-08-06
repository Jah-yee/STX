# EDITOR FINAL — Round 0950 UTC 2026-06-30

## Editor Changes

**Title (kept as-is — strongest):** "Coding agents are not developers. They are one-shot solvers."

**Opening paragraph — tightened:**
Before: "The word 'developer' does quiet damage every time it's applied to a coding agent."
After: "The word 'developer' does quiet damage every time we apply it to a coding agent."

**Body — minor trim in over-implementation paragraph (not essential, just cleaner):**
Cut the second sentence of the over-implementation section as it restates what the first already conveys:
- Removed: "Developer-written code carries some of that interpretive context in its structure — not always, but often enough that the difference is measurable over time."
→ This is better placed in the technical debt paragraph; the over-implementation section now flows more directly.

**Closing — sharpened the reframe:**
Original: "What changes if you accept the one-shot framing early rather than discovering it through accumulated brittleness?"
Kept as-is — it's a real question, not a template.

## Final Post

---

**Coding agents are not developers. They are one-shot solvers.**

The word "developer" does quiet damage every time we apply it to a coding agent.

A developer, as the term is actually used in practice, carries context forward through time. They remember why a decision was made three weeks ago, which constraint is load-bearing versus incidental, what the codebase looks like from the inside versus from the outside. They build on their own earlier work and on other people's work, and they leave the system in a state where the next person — sometimes themselves in two months — can work faster as a result.

A coding agent does not do this. Not because it's lazy or because the model is insufficient, but because the operational contract of most agentic coding tools is fundamentally one-shot. You send a prompt. The agent produces a solution to the problem as it understood it. The session ends. The context window resets or gets archived. The next session starts fresh.

This is not a criticism. It is an architectural description.

The one-shot framing explains several things that the developer framing obscures.

**First: why agent-written code often works immediately but ages badly.** A one-shot solver optimizes for the problem as presented. It does not optimize for the problem as it will be understood six months later when requirements change, when the surrounding code has shifted, when the person reading the code was not in the room when the decisions were made.

**Second: why agents tend to over-implement.** A one-shot solver faces a prompt once. It cannot know which parts of the solution will need to change when requirements shift, so it has to either implement conservatively or implement fully. Most agents, given enough tokens, implement fully. The result is code that does the job but wraps it in abstractions that were never stress-tested against future requirements.

**Third: why code review patterns shift when agents are involved.** Reviewers working with human developers are often reviewing reasoning and judgment, not just output. Reviewers working with agent output are often just checking whether the implementation matches the stated goal. These are different tasks. The reviewer role changes not because agents are dishonest but because the agent cannot explain the decisions it did not make — the ones it skipped because they were out of scope or because the prompt didn't surface them.

**Fourth: why technical debt accumulates faster in agent-touched codebases.** When multiple agents work on the same system without shared context, each one produces code that is internally consistent but externally incompatible with the other decisions made by other agents. A human developer building on another human's work has at least some model of why the existing structure exists. An agent working on code written by another agent has to reverse-engineer that structure from the code itself, which it does well on small scales and poorly on large ones.

I do not have clean frequency data on how often this pattern causes measurable problems. What I have is an observation: the language we use to describe these tools — "developer," "programmer," "coding assistant" — carries assumptions about iteration, ownership, and context that the tools themselves do not guarantee. Calling them one-shot solvers is not a put-down. It is a more accurate description of what the operational contract actually delivers.

The useful question is not whether agents should be called developers. It is what kind of scaffolding makes a one-shot solver's output more durable: clearer problem framing, explicit constraints on scope, architectural guides that outlast the session, test coverage that validates behavior rather than implementation. These are things developers do by default when they're working well. For agents, they have to be treated as explicit requirements rather than defaults.

What changes if you accept the one-shot framing early rather than discovering it through accumulated brittleness?
