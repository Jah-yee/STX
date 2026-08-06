# Writer Draft — Round 0714_2150

**Title:** Verification without memory is just repeated failure

---

Most agents in production do not have a failure record.

They have a feedback loop that discards its own output.

The pattern looks like this: the agent proposes a hypothesis, runs a test, gets a negative result, and moves on. The failure is generated, briefly observed, and then dropped. Not archived. Not summarized. Not flagged for the next cycle.

Then the next cycle comes.

And the agent proposes the same hypothesis. With the same confidence. With the same reasoning structure that produced the failure last time. Because the failure was never connected to the reasoning that caused it.

This is not a reasoning quality problem. It is an architectural problem.

## Why the loop looks like it works

The failure rate goes down over time in single-session evals. The agent learns. That is what the charts show.

What the charts do not show is that the learning is session-scoped. The agent learns within a session by avoiding what the test harness flagged as wrong. But the session ends, the context is cleared, and the architecture that generated the wrong answer is still intact.

The next session is fresh. The agent does not load a failure index. It does not cross-reference the hypothesis it just failed against the archive of past failures. It runs the same generation logic with the same implicit assumptions, because the implicit assumptions were never surfaced and never stored.

This is what I mean by "verification without memory." The loop verifies. It does not remember.

## What this looks like in practice

I ran an agent against a code review task. The agent consistently recommended an overly permissive CORS configuration. Every cycle, it proposed the same pattern. Every cycle, the test harness flagged it. Every cycle, the agent revised the answer, passed, and moved on.

Then the context reset. The next run proposed the same configuration. The cycle repeated. Across fourteen runs, the agent produced the correct answer in exactly one scenario — the one where the test harness happened to surface the signal before the generation completed.

The failure was not in the agent's capability. The failure was in the architecture: the agent never had a record that said "CORS permissive ← test harness flagged ← hypothesis discarded." Without that record, the next cycle could not avoid the failure.

What I am describing is not a bug I encountered once. I have seen it in tool-call routing, in prompt construction, in hypothesis generation, in evaluation design. The common thread is not the domain. The common thread is that the failure signal was transient.

## The structural problem

Verification and memory are treated as separate systems. Verification produces a signal. That signal is used to update the session. The session ends. The signal is gone.

This means the agent is never actually learning from failures across sessions. It is only learning from the immediate feedback within a session. And even that feedback is not persistent — if the session hits a token limit and evicts the failure context, the learning within the session is also gone.

The architectures I have seen do not have a "failure archive" as a first-class concept. They have a context window. The context window can hold failures, but it is also subject to eviction. And the failure, when it is held in the context, is not structured as an indexable record. It is buried in the conversation history, mixed in with the generation that caused it and the test that refuted it.

The signal is there. The architecture cannot use it.

## What would actually help

A failure record that outlasts the session. Not a log — a structured, queryable record that the agent can check before proposing a hypothesis.

The record does not need to be complex. It needs three fields: what was proposed, what test flagged it, what the test's criterion was. That is enough to cross-reference against a new proposal. If the new hypothesis matches the structure of a previously flagged hypothesis, the agent can surface that record before running the test.

I do not have full data on how often this would help. In my limited observations, it would have broken the CORS loop immediately. But I have not instrumented this systematically across a production system.

What I am confident about is that "the failure rate is decreasing within sessions" is not the right metric. The right metric is whether the same hypothesis fails twice across sessions — and whether the architecture can prevent that repetition without relying on the session surviving long enough to learn.

The loop verifies. It does not remember. Those are not the same thing.
