# EDITOR — Round 0621 UTC

**Draft:** draft_20260630/0621_writer.md
**Reviewer verdict:** CLEAN PASS ✅

## Editor assessment: APPROVED (one optional trim)

### Changes to make

**1. Trim the "tooling assumption" section — it re-states the one-shot/persistent distinction**

Current text:
> Most agent tooling assumes the one-shot architecture is sufficient. The workflow is: prompt → code → done. Reviews, iterations, and follow-up questions are treated as add-ons. But the workflow of a working software team is fundamentally different: it is a persistent conversation about a shared problem model, where each change is made in the context of everything that was tried before and why.

Proposed (merge into one sentence, cut the restatement):
> Most tooling assumes the one-shot model is sufficient — prompt, code, done. But a working software team runs a persistent conversation about a shared problem model, where each change builds on what was tried before.

Cut: "I've noticed that teams using agents most effectively..." (restatement, not needed — the teams observation is already in the next section)

**2. Minor word clean — "each prompt" in opening paragraph**

Current: "the agent completes the prompt"
→ "the agent completes a prompt" (cleaner)

### No other changes needed

Everything else is clean. The null-handling example is the anchor and should not be touched. The "what I'm not claiming" section is appropriately bounded. The closing is specific and not a template question.

### Final verdict
APPROVED WITH EDITS. Apply the two changes above, then submit.

---

# FINAL TEXT (after edits)

The task finished. The problem didn't.

That's the pattern I've been tracking for the past several months working with AI-assisted code generation: the agent completes a prompt, the code passes the test, and the work is marked done — but the surrounding context that a human developer carries forward has been dropped. The agent moved on. The codebase didn't.

This is not a capability gap. The model can write correct code. The gap is architectural: an agent executes a task, while a developer maintains a problem model that persists across time, across failures, and across the next five people who touch the file.

## The one-shot architecture

When I say agents are one-shot solvers, I mean something specific. A one-shot solver receives an input, produces an output, and the relationship between input and output terminates when the output is delivered. There is no carry-forward of what went wrong, no update to a running model of the system, no memory of the failure mode that was encountered and diagnosed and filed away.

A developer, even a junior one working on a modest feature, is building something more persistent. When the first approach doesn't work, the developer doesn't start from scratch — they start from "last approach + what I learned." The mental model persists. The agent doesn't have this. Each new session is genuinely new.

I've observed this concretely. I had an agent implement a data pipeline with a specific assumption about null handling. The implementation was correct under that assumption. Six weeks later, a different agent — working on an unrelated feature — broke the null handling because it had no representation of the original constraint. The first agent's "context" existed only in the output file, not in any model the system maintained. No one told the second agent about the constraint, and the codebase itself encoded it only implicitly in the original code. A human reviewing that code would have seen the null check and inferred the constraint. The agent saw a null check and moved on.

## What "solved" means in each case

When an agent says a task is complete, it means the output satisfies the prompt. When a developer says a task is complete, they usually mean something closer to: the problem is understood well enough that the solution is defensible against the failure modes that will actually occur in production.

These are different meanings. The first is verifiable. The second requires judgment about what the production environment will do to the code.

This is why I've started tracking what I call the "handoff gap" — the distance between what an agent delivers and what the next human (or agent) needs to maintain it. The handoff gap is not about code quality in the narrow sense. It's about whether the next reader can reconstruct the problem model that produced the code. If they can, the code is maintainable. If they can't, it doesn't matter how clean the implementation is — it will accumulate implicit constraints that only the original agent knows, and those constraints will silently break under new conditions.

Most tooling assumes the one-shot model is sufficient — prompt, code, done. But a working software team runs a persistent conversation about a shared problem model, where each change builds on what was tried before.

## What I'm not claiming

I don't think this means agents are useless for development work. They are extremely useful for one-shot tasks: generating a test file, refactoring a specific function, translating a pattern from one language to another. The one-shot architecture is the right architecture for those tasks. The problem is when the one-shot model is applied to work that requires persistence — where the output needs to coexist with other outputs in a system that is changing over time.

I also don't have systematic data on how often the handoff gap causes production incidents. I have personal observations, which are limited by my own codebase complexity and the specific types of projects I work on.

## The actual difference

The honest summary: an agent that writes correct code is not the same as a developer who understands a problem. The agent can complete a task. The developer understands what the task means in context. These are different cognitive artifacts, and conflating them is where most of the maintainability problems I observe originate.

The teams I've seen handle this best are explicit about the distinction. They don't ask "can the agent do this?" They ask "is this task one-shot-compatible?" — meaning, will the output need to coexist with other code that is changing? If yes, they add the human review step specifically to transfer the problem model, not to check correctness.

That's the architectural difference that matters: one-shot tasks get done. Persistent problems get understood. The tools are the same. The judgment required is different.
