# WRITER DRAFT - 0703

**Title:** Inference runtimes are not control loops

---

A team I worked with spent three months tuning their AI assistant's agent loop. They added retries, fallbacks, confidence thresholds, self-correction steps. Every time the loop produced a bad output, they added another layer.

The outputs kept getting worse under load. Not because the model degraded. Because their loop had no convergence condition, and under concurrent load, multiple retry branches were firing simultaneously, each trying to correct a state the others were also modifying.

They had built a control loop. They got control theory's failure modes without its guarantees.

**What control loops actually give you.**

A PID controller — proportional, integral, derivative — converges because the math forces it. The error decreases monotonically toward zero. Bounded execution time is a property of the system, not a quality you add as an afterthought.

Agent loops built on LLM inference have none of this. Each inference call is a stateless transformation. There is no state update that persists between calls unless you explicitly manage it. There is no convergence theorem. There is no error bound.

When people call these "control loops" and design them accordingly — adding watchdog timers, escalation paths, recovery branches — they are importing a vocabulary that does not apply.

**The failure mode that shows up first.**

The most common symptom is what I'd call loop oscillation. Under load or ambiguity, the agent tries to correct a bad output by calling itself, and the correction itself becomes a new input that triggers another correction. This is not self-correction in any meaningful sense. It is recursion without a base case.

I have seen this in production. The logs show a single user request generating 40+ agent calls. The model was not degrading — it was responding to its own previous output, which was responding to its own previous output, in a chain that had no termination condition other than a hard timeout.

Adding more "self-correction" examples to the prompt does not fix this. The correction capability and the termination condition are different problems.

**What the conflation costs.**

Treating inference as a control loop also leads to incorrect assumptions about reliability. Control theory gives you graceful degradation — if one sensor fails, the remaining sensors still constrain the system state. In an LLM agent loop, a single malformed tool response can propagate garbage into every subsequent inference call with no natural damping.

This is why the "just add a validator" approach to agent reliability often fails. The validator is itself an inference call. If it inherits the same stateless execution model, it cannot reliably bound the state of the outer loop.

The practical implication: agent loops need explicit convergence mechanisms that do not depend on the model's self-correction capability. State machines, token budgets, step counts, hard aborts — these are not pessimism. They are the only available substitute for convergence guarantees that the execution model cannot provide.

What control theory teaches us is not how to build better loops. It is how to think about what guarantees we do not have.

---

*Draft by Writer — needs Reviewer check before submission*
