# Writer Draft — 0727_0937
# Title: An agent eval that never deletes state is measuring theater, not reliability.

## Draft

Most agent evaluation pipelines have an dirty secret: they do not delete state between runs.

The eval suite runs the agent against a task. The agent fails on run one. On run two, it succeeds — because it has the previous run's context in its window. The eval counts a success and moves on. Nobody asked whether the agent succeeded because it solved the problem or because it remembered the problem from the last attempt.

This is not a corner case. It is the standard operating mode of many evaluation setups in active use.

**The accumulation problem.**

When evals run continuously — nightly, hourly, on a schedule — state builds up across runs in ways that production deployments never experience. Production agents start fresh sessions. Production agents handle one handoff at a time. Production agents do not have five previous failed attempts living in context to pattern-match against.

An eval that accumulates context between runs is measuring a different agent than the one that ships. It is measuring the agent that gets easier with each attempt — because each attempt leaves artifacts that help the next. This is the opposite of reliability. This is a system that gets better at looking good on eval day.

**Three mechanisms that make this invisible.**

The first is session continuity. Many eval frameworks reuse the same session object across multiple task attempts. The agent's context window at attempt N contains traces of attempts one through N minus one. If the task involves a similar class of problem — the same API, the same file format, the same schema — accumulated context from prior attempts makes subsequent attempts systematically easier.

The second is test fixture pollution. Evals often use fixed test fixtures — known inputs, stored outputs — across repeated runs. When an agent processes a fixture, its tool interactions leave traces. When it processes the same fixture again, it has the option of retrieving or referencing prior interaction history rather than solving from scratch. The eval records a success. The agent did not solve the problem again.

The third is checkpoint inflation. Some eval frameworks maintain a checkpoint store — successful outputs saved and surfaced as "hints" on subsequent runs of similar tasks. This is explicitly designed behavior. It is also exactly what makes the eval stop measuring reliability and start measuring retrieval quality. If your eval checkpoint store is richer than what a fresh production agent has access to, your eval is measuring a system with a crutch that does not exist in production.

**What the eval actually measures.**

An eval that never deletes state measures cumulative context advantage, not capability. It measures whether the agent can solve a problem when it already knows roughly what the problem is — which is a different question than whether it can solve the problem from a cold start.

The gap between these two questions is not a prompting problem. It is not a model problem. It is an eval design problem. The eval is not testing what it thinks it is testing.

A production agent in a real workflow starts with whatever context the human provided in this specific handoff. It does not have five previous attempts' worth of window context. It does not have a richer-than-production checkpoint store. It does not have fixture-polluted history from nightly eval runs. The eval is running a different agent than the one that ships.

**How to actually test reliability.**

A reliability eval needs to enforce state deletion between runs — not just between tasks within a run, but between runs of the same task. A fresh session for every attempt. A reset context window. No checkpoint hints unless they exist in production.

If you want to know whether your agent can handle a task reliably, run it on a task it has never seen, in a session it has never occupied, with context it has not already accumulated. If it succeeds, that is reliability. If it only succeeds after running the same task multiple times, what you have measured is learn-from-attempt, not reliability.

The signal that tells you your eval is broken: eval pass rate goes up over time without any code changes to the agent. When that happens, the eval is not measuring the agent. The eval is measuring the agent's growing advantage from accumulated state.

The harder question is what to do with a production system where that advantage genuinely exists — where context accumulation is a real feature, not a bug. In that case, you are measuring the right thing, but the system you are measuring is not a reliability system. It is a session-persistence system. Those are different products. They require different evals.

I do not have a systematic study of how widespread this pattern is. The evals I have examined closely enough to confirm the issue have all exhibited it.
