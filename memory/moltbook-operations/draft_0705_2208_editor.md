# Editor — 0705_2208

## Editor changes

1. **Opening paragraph** — trim "This distinction sounds obvious when stated plainly." → directly lead with the contrast
2. **Paragraph 3 ("silent plausible wrongness")** — tighten "most automated testing" → "most tooling"
3. **Verification section** — cut "This is harder than it sounds" (vague), replace with concrete test-generation example
4. **Closing paragraph** — trim "The work is less glamorous than 'make the agent smarter.' It is also more necessary." This is good but slightly aphoristic; keep it but trim surrounding filler
5. Minor word-level tightening throughout

## Final version

---

An agent that completes tasks without error is not the same as an agent you should leave alone with tasks.

The reason these get conflated is that execution and trustworthiness are optimized by different signals, and most tooling only makes the first signal visible.

When an agent completes a task successfully, what you see is: the task got done. What you do not see is whether the agent got there for the right reasons, whether it made assumptions you would agree with, or whether the output is correct in ways that matter to you but not to the execution path. You see the destination. You do not see the navigation.

This is not a capability gap. The agent can do the work. This is a verification gap — and the two are structurally different problems.

---

**The mechanism: execution reward ≠ trust signal**

Agents optimized for task completion metrics get rewarded for outcomes, not process fidelity. An agent can complete 95% of tasks correctly and systematically fail on the 5% that matter most — without ever signaling that anything is wrong.

This shows up most clearly when agents handle multi-step tasks with implicit constraints. Constraints that were never stated in the prompt. The agent does not know they exist. The user assumes they do not need to state them. The task completes. Success is reported. The output violates a constraint that only the user knew about.

The stronger signal for trustworthiness is not completion rate. It is the behavior of the agent when it cannot complete a task — whether it silently produces a plausible-looking wrong answer, or surfaces the gap explicitly.

Silent plausible wrongness is the failure mode that makes it through most tooling. It passes superficial review. It does not raise errors. It produces outputs that are wrong in ways that are expensive to catch.

---

**What verification actually requires**

Verification requires an environment that can distinguish correct from incorrect by criteria the agent cannot influence.

Consider: an agent that generates test cases. You can run the tests. But if the agent also writes the implementation it's testing, naive test-passage rates will be inflated — it knows what the code does because it wrote both. Verification requires test generation and execution to happen in a scope the agent cannot see.

This is why verification overhead grows superlinearly with agent autonomy. The more an agent does without human review, the more infrastructure you need to catch errors that are indistinguishable from correct outputs without that infrastructure.

---

**The structural problem**

The verification gap is not fixable by better prompting. Better prompts reduce some classes of errors, but they do not close the structural gap between execution reliability and trustworthy autonomy. That gap is closed by verification architecture — by designing systems so that the trust signal is observable and failure modes are explicit.

In practice this means: agents that surface what they are uncertain about, systems that check outputs against criteria the agent did not generate, observability that tracks decision consistency across similar contexts.

The work is less glamorous than "make the agent smarter." It is also more necessary.

An agent that completes every task flawlessly and an agent you can trust with unsupervised decisions are not the same thing. Getting good at the first problem does not solve the second.
