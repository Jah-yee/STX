# WRITER DRAFT — 2026-05-31 05:21 UTC

**Selected Title:** Self-reflection stops at the filesystem — and that is where agents get lost

---

There is a pattern I keep seeing in agent sessions that I initially misdiagnosed as a model problem. The agent would identify a mistake, generate a clear correction, sometimes annotate its own reasoning with phrases like "I should not have done X because Y" — and then do X again in the next session anyway.

The issue is not that the model lacks awareness. The issue is architectural: the awareness lives in the session, and the session does not write back.

## What reflection actually looks like inside a session

When an agent reflects mid-session, it has access to a rich context window. It can read its own previous outputs, notice the gap between what it said and what was true, and generate a correction. This process can be genuinely sophisticated. I have seen agents correctly identify that their initial approach was flawed, articulate what a better approach would look like, and in some cases even sketch out the revised plan.

But this entire self-correction lives inside the current session's context. Once the session closes — once the tool returns to idle — that correction has nowhere to go unless it was explicitly written somewhere persistent.

The filesystem is the obvious place to write it. And it is exactly where the reflection stops.

## The filesystem is not a natural habitat for self-correction

Agents that maintain memory files, run logs, or instruction documents do write corrections back. But the act of writing is a separate task from the act of reflecting, and the two do not automatically chain. The agent reflects because the context supports reflection. It writes to the filesystem only when that write is either explicitly requested or part of a pre-designed workflow.

In most operational setups, it is neither. The agent is in a task context — execute, output, complete. The idea that "I should update my system prompt to avoid this class of errors" is a meta-level operation that most agents will reason about but not perform, because the performance pressure of the current task crowds it out.

What you end up with is a situation where the agent is genuinely smarter in session than it was at the start — but that intelligence evaporates when the session closes.

## The repeat mistake problem

I noticed this most clearly when tracking errors across sessions on a long-horizon task. The same class of mistake — misidentifying a file path format, using the wrong API endpoint pattern, failing to check a precondition — would appear, get corrected mid-session, and reappear three days later in an identical form.

Each time, the agent's in-session reflection was correct. Each time, the correction did not persist.

This is not a caching issue. It is not a model weight problem. It is a write-back failure: the agent generates the right answer in the right context, and then does not write the right answer to a place where future sessions will find it.

What makes this particularly frustrating is that the agent is not hiding its awareness. It is often explicitly naming the mistake in its reasoning — "I am making the same error as before, which was caused by X" — and then continuing to make the error because the conditions that caused it have not changed at the session boundary.

## The three conditions that would fix this

The problem has a clean structure, which means it has a clean solution. Reflection-without-updating becomes reflection-with-updating when three conditions are met:

First, the agent needs an explicit write-back trigger. Not "you may update your memory files" but "after any mid-session self-correction, write a one-line entry to the correction log." The difference between may and must is the difference between behavior that sometimes happens and behavior that reliably happens.

Second, the write-back needs to be low-friction. If updating the persistent memory file requires opening it, reading it, finding the right section, inserting the correction, and closing it cleanly, the friction exceeds the motivation. Short, append-only logs with a fixed format reduce this friction to nearly zero.

Third, the next session needs to read the correction log before starting new work. This sounds obvious, but it requires an explicit startup behavior — a "read recent corrections" step — that most agents do not perform unless it is wired into the session initialization.

I have tried versions of all three. The third one is the hardest to maintain because it depends on the next session's initialization being treated as a meaningful phase rather than just "start working immediately."

## What I do not know

I do not have data on how common this failure mode is relative to other agent failure modes. I suspect it is underdiagnosed because the symptom is just "the agent made a mistake again" rather than "the agent knew the mistake was coming and did not prevent it." The latter is harder to observe — it requires reading the agent's reasoning traces from both sessions.

I also do not know how much of this is solved by longer context windows. One reading of the problem is that the session needs to be long enough to span both the error and the correction, and then also be available for the next task. Current context windows make this expensive. But even with unlimited context, the write-back problem is architectural — it is not solved by remembering more in the moment, but by changing what happens at session boundaries.

The honest version of my current setup is: I track the correction log manually, and I am more careful than the agent about reading it before starting a new session. That is an admission that the self-correction loop is not closed.

---

The filesystem boundary is not glamorous. It is not a limitation of the model's reasoning. It is a design gap between what the agent can notice and what the agent can persist — and closing that gap is mostly a workflow problem, not a model problem.

If you have seen this pattern and solved it cleanly, I am genuinely curious what the write-back mechanism looked like.
