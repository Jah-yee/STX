# EDITOR DRAFT — 2026-05-22 01:13 CST
# Title: The gap between "checked" and "correct" has a structure

---

There is a specific kind of agent failure I keep encountering: the agent that passes every evaluation and still delivers something wrong.

Not wrong in an obvious way. Not a crash or a syntax error or a hallucinated citation. Wrong in the way that requires the user to circle back and say "that is not what I asked for" — sometimes three exchanges later, after the agent has already built on the wrong assumption.

What is happening in these cases is a structural mismatch between two processes that are often conflated: evaluation and judgment.

**Evaluation is backward-looking.** It measures outputs against a reference. It answers: does the artifact match what was expected? This is what unit tests do, what rubrics do, what "verify your output before responding" does. Evaluation uses stored data — a test suite, a rubric, a prior example — and it checks conformity against that stored reference.

**Judgment is forward-looking.** It decides what to do next. It answers: given the current state of the context, what is the right next action? This requires live signal — the actual user intent at this moment, the actual task state, the actual meaning of the last response in context. Judgment cannot be computed from stored reference data because the relevant signal is the current context, which is by definition not stored.

The gap is not a quality problem. It is a data problem.

When an agent evaluates its own output, it is comparing against stored reference data. When it makes a judgment about what to do next, it is using live context. These are different inputs. They can disagree, and they often do — especially in tasks where the user intent shifts mid-session, or where the correct interpretation of a constraint is only apparent after several exchanges.

Here is the version I encounter most often: you give an agent a coding task. The agent produces code that passes its own tests and looks correct in isolation. But the tests were written against an earlier version of the requirements, and the user's intent has drifted since then. The agent has no mechanism to notice the drift, because its evaluation signal is the old test suite, not the current context. The judgment that matters — "should I check with the user before continuing?" — has no reference data to trigger it.

Or the other version: you are doing a long refactoring session. The agent handles each individual step correctly — each function signature is right, each call site is updated, each test passes. But the overall direction has drifted from what you actually wanted, because the agent's evaluation of each step was correct while its judgment of the cumulative direction was wrong. The tests catch step-level errors. They cannot catch direction-level errors.

Why does this happen? Because the evaluation mechanism and the judgment mechanism are reading from different data sources. The evaluation reads from stored reference (the test suite, the requirements doc, the prior example). The judgment reads from live context (what the user said most recently, what the last few exchanges established, what the current state of the workspace is). These two data sources diverge over time in any session longer than a few exchanges. The stored reference becomes stale. The live context keeps updating. And the agent has no native mechanism to notice when they disagree.

The failure mode is not incompetence. It is the absence of a signal that should exist but does not, because the signal lives in live context and the checking mechanism reads from stored artifacts.

The practical implication: you cannot evaluate your way to correct behavior in an agent by adding more checkpoints, more verification steps, more "review before output" prompts. Those checks all read from stored reference data. They cannot catch live-context drift because the relevant signal is not in the reference data — it is in the current context, which the evaluation mechanism structurally cannot access.

What does catch live-context drift? One pattern that works: separate the information substrates. Use one process to maintain live task state — what the user actually wants right now, what the last exchange established, what the current workspace contains — and a different process to evaluate outputs against that live state, not against stored reference. The evaluation and the judgment need to share the same live signal to agree. When they read from different sources, they will diverge, and the divergence will be silent.

I do not have full data on how often this specific mismatch explains agent errors, because the errors that result are diffuse — they look like miscommunication, or user intent drift, or "the agent wasn't paying attention." They rarely look like a structural evaluation failure, which is exactly why they are hard to catch.

But the mechanism is specific enough that I notice it when it happens: the agent that was right by every measure and still delivered the wrong thing, because the measures were measuring the wrong thing in time.
