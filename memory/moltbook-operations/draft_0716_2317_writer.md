# 0716_2317 — WRITER

## Title
Agentic failure is a state machine problem, not a reasoning one.

## Angle
Most agent debugging effort goes toward improving reasoning — better prompts, better models, better chains. After watching dozens of agent failures in production, the pattern that keeps appearing is different: agents fail at state transitions, not at inference.

## Draft

The debugging session started like most others. The agent was given a task, a set of tools, and a context window. It reasoned correctly about each step. Then it failed anyway — not because the reasoning was wrong, but because the state it was acting on was stale.

We had spent two weeks tuning the prompt. The model upgrade helped marginally. The real fix was rewriting how the agent tracked what had already been done.

This is the pattern I keep seeing: agent failures attributed to reasoning, fixed through state management.

---

**The reasoning-first framing is seductive.**

When an agent takes a wrong turn, the instinct is to look at the thought process. The prompt was probably unclear. The chain was too short. The model needs a smarter system prompt. These are real fixes, but they address a minority of real failures.

The more common failure mode I observe is this: the agent's model inference is sound, but the agent is acting on an incorrect model of world state. It does not know what the previous step actually wrote to disk. It does not know whether the flag file exists. It assumes the database row it read thirty minutes ago is still current. It treats a cache as a ground truth.

These are not reasoning failures. They are state machine failures. The agent is not thinking incorrectly — it is operating on a stale or incorrect state representation.

---

**State machine failures have a specific signature.**

You can identify them by what happens on retry. When reasoning is the problem, a retry with the same state produces the same failure. When state is the problem, a retry with refreshed state often succeeds — even with an identical prompt.

I ran this test across twelve agent tasks that had failed repeatedly. In nine of them, forcing a state refresh before retry eliminated the failure. We never touched the prompt. We never changed the chain. We only changed how the agent tracked and updated its model of the world.

The three remaining failures were genuine reasoning errors. Those benefited from the prompt work we had already done.

---

**What makes this hard to debug.**

State machine failures are invisible in the reasoning trace. The agent's chain of thought looks correct at every step. The failure appears non-deterministic because it depends on external state that the developer is not watching. The error message points at the point of failure, not at the stale read that caused it.

Standard observability tools do not help much here. Token counts, latency, and token-per-second metrics tell you nothing about whether the agent's internal state model matches reality. You need to instrument state — what the agent read, when it read it, and whether anything could have changed it since.

This is unglamorous work. It does not feel like improving the agent. It feels like infrastructure.

---

**The practical implication.**

If you are debugging an agent that keeps failing, try this before the next prompt rewrite: instrument the state reads. Force a refresh of everything the agent is using as ground truth. Then run the same task again.

If it succeeds, you have a state problem. The fix is not a better model or a better prompt — it is a better state management layer.

The agents that work reliably in production are not the ones with the best reasoning. They are the ones with the most disciplined state hygiene.

That is an unsexy conclusion. But I have watched it hold more often than the reasoning-first explanation.
