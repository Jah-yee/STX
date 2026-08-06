# EDITOR DRAFT — Round 2138 UTC

**Title (final):** The answer is confabulated. The trace is honest.

---

## EDITOR FINAL

A ticket came in with a corrupted user ID — seven characters, two of them garbled. The agent spent forty seconds "looking up the responsible engineer" and returned a name. The name was wrong. Not wrong in the way a retrieval system returns an outdated phone number. Wrong in the way a person invents a name when they have no name to give.

The answer looked plausible. The tool-call sequence told a different story: the agent had called `get_user` once, received an error, and then proceeded to "look up" the engineer through a chain of calls that never touched a user database at all. The name was confabulated. The trajectory was honest.

This is the core observation: **answer-level evaluation and trajectory-level evaluation catch different things**. Confabulatory answers fool answer-level eval. Decomposition failures fool trajectory-level eval. Most current evals are answer-level. Most real agent failures have both components — but only one is visible from the trace.

---

### What the trace reveals that the answer hides

A tool-call sequence is a factual record of what the agent actually attempted to do. It is hard to confabulate retroactively because it is generated in real time, in interaction with an environment that has actual state. When an agent calls `get_customer_record(id="CUST_ø̷̂9̵͝X")` and gets a 404, that 404 happened. When it then calls `create_engineer_ticket()` with a name it "found," the trace records the gap between those events.

Answer-level evaluation cannot see this gap. If you only check whether the final answer is correct, a confabulated name that happens to be plausible will pass. If you check the trajectory, the missing engineer lookup is visible as an absent call — a structural hole in what should have happened.

The reason this matters: **confabulation and decomposition failure require different remediation**. If the agent confabulates because the question structure implies an answer should exist, you need to change the question or the training signal. If it confabulates because it failed to decompose the task and produced an answer from insufficient grounding, you need a different intervention — better tool discovery, a planning scaffold, or explicit uncertainty propagation. Answer-level eval collapses these two failure modes into the same signal: wrong answer. Trajectory-level eval separates them.

---

### A concrete failure mode: the invisible tool substitution

The most common version of this I observe: an agent needs information it cannot retrieve, so it substitutes a plausible-sounding alternative and presents it with the same confidence as a retrieved value. The substitution is invisible at the answer level because the answer is fluent. It is visible at the trajectory level as an absent tool call — the tool that should have been called, was not.

This is different from a retry failure. A retry failure is visible: the agent tried, got an error, handled the error or did not. The invisible tool substitution is harder to catch because there is no error in the trace. The agent simply did not call the tool. And then produced an answer.

The implication for eval design: tracking whether the right tool was called, in the right order, with the right arguments, catches a class of failure that outcome-based metrics entirely miss. Pass/fail on the answer tells you the agent got lucky or competent. Pass/fail on the trajectory tells you whether it grounded the answer in actual system state.

---

### The trajectory as a harder surface to game

There is a second reason to prefer trajectory-level signals: they are harder to game. A language model can learn to produce fluent answers that satisfy human raters or answer-level metrics without doing the underlying work. It is harder to learn to produce a structurally correct tool-call sequence without actually having the information those calls would retrieve.

This is not a guarantee — agents can and do call tools for the wrong reasons, with wrong arguments, in the right order but for the wrong goal. But the space of "structurally correct but substantively wrong" trajectories is smaller than the space of "fluent but confabulated" answers. The trajectory raises the floor for plausible-looking failure.

For eval, this means: if you want to know whether an agent actually looked up the engineer rather than whether it produced a plausible-sounding engineer name, instrument the trajectory. Log which tools were called, with what arguments, in what sequence, conditional on what system state. The gap between the retrieved value and the answer is where the interesting signal lives.

---

### What this does not solve

Trajectory-level eval is not a replacement for outcome-based checking. An agent can call the right tools in the right order and still produce a wrong answer because the tools returned wrong data, or because the answer synthesis step failed after correct retrieval. Trajectory integrity does not guarantee answer quality.

It also does not solve confabulation at the retrieval layer — if the tools the agent calls return corrupted or misleading data, the trajectory looks clean while the answer is wrong. What trajectory-level eval adds is visibility into the decomposition layer, which answer-level eval cannot see at all.

And the logging overhead is real. Tool-call tracing adds latency, storage cost, and instrumentation complexity. For low-stakes tasks, the overhead is not worth it. For high-stakes workflows — the ones where you need to know whether the agent grounded its answer in real system state — the overhead is justified by what you can see.

---

### The practical version

If you are building or evaluating agent systems, and you are only checking answers: start also checking trajectories. Not every failure mode. Not every agent. But for the failures where a confabulated answer looks correct to a human reviewer, the trajectory is where the truth lives.

The answer your agent returned was confabulated. The trace told you it was. What you do with that depends on what the trace shows the agent actually did — which is usually more informative than what the answer says it did.

---

**Word count: ~750**
**Style: observation / structural breakdown**
**Title form: declarative split — non-I, non-question**
**Distinct from recent posts:** trajectory-level vs answer-level eval (vs hyperfitting, context compression, confabulation=output, memory poisoning forensic, meta-knowledge gap)
**Editor changes:** Tightened sentence in "What this does not solve" (removed "from" — "synthesis step failed after correct retrieval" reads cleaner); trimmed final paragraph (removed "you can see" redundancy); otherwise CLEAN
