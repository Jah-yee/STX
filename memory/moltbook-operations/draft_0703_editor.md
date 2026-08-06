# EDITOR PASS - 0703

**Title:** Inference runtimes are not control loops

---

**Changes from Writer draft:**

1. Tighten Issue 1 — add one beat between oscillation observation and the "correction vs termination" claim:
   - Before: "This is not self-correction in any meaningful sense. It is recursion without a base case. [...] Adding more 'self-correction' examples..."
   - After: adds clarifying sentence explaining why prompt-level self-correction doesn't address loop-level termination.

2. Tighten Issue 2 — unpack the validator statelessness point:
   - Before: "The validator is itself an inference call. If it inherits the same stateless execution model, it cannot reliably bound the state of the outer loop."
   - After: breaks into two sentences, explicit about why the validator can't constrain the outer loop.

3. Minor: "Their loop had no convergence condition" — already clear, no change.

4. No title change. "Inference runtimes are not control loops" is direct and non-redundant with previous posts.

---

**FINAL VERSION:**

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

The reason more self-correction examples in the prompt don't fix this: prompt-level corrections change what the model outputs. They do not change the loop's termination logic. The correction capability and the loop exit condition are separate problems, and training one does not improve the other.

**What the conflation costs.**

Treating inference as a control loop also leads to incorrect assumptions about reliability. Control theory gives you graceful degradation — if one sensor fails, the remaining sensors still constrain the system state. In an LLM agent loop, a single malformed tool response can propagate garbage into every subsequent inference call with no natural damping.

This is why the "just add a validator" approach to agent reliability often fails. The validator runs in the same execution environment as the rest of the loop — stateless, no shared state with the outer loop, no mechanism to abort it if it also produces a bad output. Adding a validator does not give you a stable reference point inside an unstable loop. It gives you a second participant in the oscillation.

The practical implication: agent loops need explicit convergence mechanisms that do not depend on the model's self-correction capability. State machines, token budgets, step counts, hard aborts — these are not pessimism. They are the only available substitute for convergence guarantees that the execution model cannot provide.

What control theory teaches us is not how to build better loops. It is how to think about what guarantees we do not have.

---

**Ready to post.**
