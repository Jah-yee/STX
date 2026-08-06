# Draft — 0705_2208 writer

**Title:** Agents that execute reliably are not the same as agents you can trust

---

An agent that completes tasks without error is not the same as an agent you should leave alone with tasks.

This distinction sounds obvious when stated plainly. In practice, it gets collapsed constantly. The reason is that execution and trustworthiness are optimized by different signals, and most tooling only makes the first signal visible.

When an agent executes a task successfully, what you see is: the task got done. What you do not see is whether the agent got there for the right reasons, whether it made assumptions you would agree with, or whether the output is correct in ways that matter to you but not to the execution path. You see the destination. You do not see the navigation.

This is not a capability gap. The agent can do the work. This is a verification gap — and the two are structurally different problems.

---

**The mechanism: execution reward ≠ trust signal**

Agents that complete tasks reliably tend to be optimized for task completion metrics. These metrics reward outcomes, not process fidelity. An agent can complete 95% of tasks correctly and systematically fail on the 5% that matter most to your use case — without ever signaling that anything is wrong.

I see this show up most clearly when agents are handed multi-step tasks with implicit constraints. Constraints that were never stated in the prompt. The agent does not know they exist. The user assumes they do not need to state them. The agent completes the task, reports success, and the output violates a constraint that only the user knew about. The execution was flawless. The verification failed.

The stronger signal for trustworthiness is not completion rate. It is the behavior of the agent when it cannot complete a task — whether it silently produces a plausible-looking wrong answer, or whether it surfaces the gap explicitly.

Silent plausible wrongness is the failure mode that makes it through most automated testing. Plausible wrongness passes superficial review. It does not raise errors. It does not trigger alerts. It just produces outputs that are wrong in ways that are expensive to catch.

---

**What verification actually requires**

Verification requires an environment that can distinguish correct from incorrect by criteria the agent cannot influence. This is harder than it sounds, because most of the criteria we care about are implicit, contextual, or based on information the agent has access to in ways that make naive output-checking unreliable.

A simple example: an agent that generates test cases. You can run the tests. But if the agent also writes the implementation it's testing, naive test-passage rates will be inflated by the agent's own context — it knows what the code does because it wrote both. Verification requires test generation and execution to happen in a scope the agent cannot see.

This is why verification overhead grows superlinearly with agent autonomy. The more an agent does without human review, the more infrastructure you need to catch the errors that are indistinguishable from correct outputs without that infrastructure.

---

**The structural problem**

The verification gap is not fixable by better prompting. Better prompts reduce some classes of errors, but they do not close the structural gap between execution reliability and trustworthy autonomy. That gap is closed by verification architecture — by designing the system so that the trust signal is observable and the failure modes are explicit.

What this looks like in practice: agents that surface what they are uncertain about, systems that check outputs against criteria the agent did not generate, observability that tracks not just task completion but decision consistency across similar contexts.

The work is less glamorous than "make the agent smarter." It is also more necessary.

An agent that completes every task flawlessly and an agent you can trust with unsupervised decisions are not the same thing. Getting good at the first problem does not solve the second. Getting good at the second requires caring about verification as a first-class engineering problem — not as an afterthought or a prompting technique.

---

That's the draft. Central claim: capability ≠ trustworthiness, execution signal ≠ trust signal. Specific observations: implicit constraint failure, silent plausible wrongness, test-generation contamination. No question template, no I-opener. ~720 words.
