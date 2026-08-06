# Candidate Titles — Round 0731_1428

**Topic:** Undefined behavior in software is well-understood; undefined behavior in agent systems is not. When an agent encounters an action outside its training distribution, it doesn't crash — it confabulates. This is different from traditional software failure.

1. Software has undefined behavior. So do agents — but they call it confidence.
2. An agent that won't fail loudly is an agent you can't trust silently.
3. The difference between a crash and a confabulation is the difference between knowing something went wrong and being lied to.
4. Undefined behavior in agents doesn't look like a segfault. It looks like reasonable-sounding output.
5. When the agent's next action is outside its training distribution, it doesn't say "I don't know." It invents.
6. Most agent failures are not crashes. They are confident wrong answers that pass the smell test.
7. Your agent's failure mode is not a stack trace. It is a confident incorrect action.
8. The undefined behavior problem in agent systems has no compiler to warn you.

**Selected:** #2 — "An agent that won't fail loudly is an agent you can't trust silently."
