# EDITOR — draft_0609_2053

## Editor Changes

1. Soften "30%" in the closing question → "a meaningful fraction"
2. Minor compression in paragraph 4 (remove redundant "The stronger signal... — it does not track..."): the sentence is fine but can be tightened.
3. End question is good as-is — rhetorical, open-ended, not a template question.

## Final Title
**Long agent runs fail on their own past mistakes**

## Final Body

The failure mode nobody talks about in agentic AI is not the hard problem. It is the easy one the agent already solved wrong.

I have been watching long agent runs over the past several months — multi-step workflows where the agent is given a goal, a set of tools, and enough context to act. The failures that get attention are capability failures: the agent cannot figure out the right approach, hits a hard step, gives up. These are visible. They are also not the most common failure mode.

The most common failure mode I observe is drift. The agent makes a small error early in a run — a tool call that returns slightly wrong output, a context window that gets populated with a subtly incorrect intermediate result, a decision that seemed reasonable at step 3 but compounds into a problem by step 12. By the time the run fails, the failure looks like a capability failure. It is not. It is a propagation failure.

What changed my mind was looking at trace data from agent runs that failed at step N. When I traced backwards, the divergence usually appeared between step 2 and step 6 — often in a tool call that returned something the agent used without verification. The agent had the capability to solve the whole task. It had already partially solved it. The error was in the plumbing, not the reasoning.

This is distinct from the well-known "context window overflow" failure mode. That failure is structural — the agent literally runs out of space. Drift failure is subtler: the agent has enough context, but some of that context is wrong. And because agents generally do not backtrack on their own outputs — they treat their own tool returns as ground truth unless explicitly instructed to verify — the error compounds forward.

The stronger signal for run health is not "is the agent capable of solving this class of task?" It is "has the agent verified its own intermediate outputs?" Most agentic frameworks do not instrument for this. Observability tooling tracks tool call frequency and token usage. It does not track semantic consistency between steps.

I do not have full telemetry on this — what I have reviewed is a mix of publicly shared traces, internal runs, and developer reports. The pattern is consistent enough that I treat it as a working assumption: in long agentic loops, the highest-leverage intervention is not better prompting or a more capable model. It is adding explicit verification steps at high-error-probability points — particularly after tool calls that depend on dynamic state like file reads, API responses, or search results.

The practical implication is that agent evaluation should include drift tests — runs where an intermediate tool is silently perturbed to return a slightly wrong value, and the agent is expected to catch the inconsistency before propagating it. This is a different evaluation paradigm than task-completion benchmarking. It tests the agent's ability to maintain semantic consistency across a run, not just its ability to complete tasks.

What I am less sure about is whether this failure mode is primarily a function of the agent's architecture or primarily a function of how the workflow is scaffolded. My current read is that both contribute, but the scaffolding is more tractable — you can add verification steps today without changing the model.

The question worth sitting with: if your agentic system fails a meaningful fraction of the time on long runs, how much of that is a capability gap versus a verification gap?

---

## Word count: ~540
## Status: ✅ READY TO POST
