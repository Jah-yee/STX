# Writer Draft — Round 0716_1707

## Title
Agents don't fail at logic. They fail at state management.

## Body

When an agentic system breaks, the instinct is to look at the reasoning trace. Something in the chain went wrong. The model hallucinated, or the prompt was unclear, or the tool output was misleading.

That's usually the wrong place to look.

After tracing a significant number of agent failures — in production pipelines, eval runs, and personal projects — the dominant failure mode isn't bad reasoning. It's state that the agent is treating as current when it isn't. The logic was sound. The state underneath it was stale.

**What this looks like in practice**

The most common pattern: an agent calls a tool, the tool returns a result, and that result gets cached or carried forward as if it were still valid at the next step. A file was deleted. A database record changed. A service restarted. The agent's context window still contains the old answer, and it reasons from there — correctly, given what it knows, but incorrectly given reality.

In single-agent systems this shows up as confusing behavior: the agent insists a resource exists when it doesn't, or recommends the wrong configuration for a system that has changed. You trace through the reasoning and it looks reasonable. The bug is invisible in the trace because the trace shows the agent doing the right thing with the wrong information.

Multi-agent pipelines make this worse. Agent A runs, writes outputs, and hands off to Agent B. Agent B operates on those outputs without knowing whether Agent A's state changed between writing and handing off. If the outputs are files, there's no atomic guarantee. If they're in-memory state, the handoff might be a pointer to an object that Agent A has already mutated. Agent B is reasoning from a snapshot of a snapshot.

**The harder problem: state management is invisible when it works**

Logic failures are dramatic. The agent says something clearly wrong. The trace is short. The bug is easy to point at.

State failures are quiet. Everything looks fine until a downstream effect accumulates enough error to become visible — often far from the point where state first diverged. By the time you notice, the agent's context window is full of artifacts from reasoning with stale data, and the only recovery is often to restart and rebuild state from scratch.

This makes state failures harder to debug than logic failures. You can't just inspect the reasoning. You have to reconstruct what the agent's state actually was at each step, compare it to what the system state actually was, and find the divergence. That's not something the tooling usually helps you do.

**Why logic-focused evaluation misses this**

Most agent evaluation frameworks test reasoning quality: does the agent make the right decision given the right information? This is a legitimate test of model capability. But it doesn't catch state management failures, because in evaluation the state is controlled. The tool outputs are fixed. The environment doesn't change between steps.

State failures only appear in dynamic environments — where things actually change: files get modified, APIs return different results, user inputs alter system state mid-pipeline. These are the conditions where agents are most useful, and they're precisely the conditions where state management is hardest.

**What I've actually done about it**

Three things that have helped:

First, explicit state checkpoints in pipelines. Not just "the agent outputs this" but "the system state after this step is X." When something breaks, you can compare the checkpoint to what actually happened and find the divergence.

Second, treating staleness as a first-class error type. If a tool result is older than some threshold and the agent is about to use it for a consequential decision, the system should surface that explicitly rather than letting the agent proceed on stale information.

Third, keeping pipelines short enough that state divergence has limited room to accumulate. Long chains of agents each reasoning from their own snapshot of state compound the staleness problem. Fewer handoffs, or handoffs with explicit state reconciliation, reduce the problem significantly.

None of these are elegant solutions. They add friction to pipelines and require the kind of explicit bookkeeping that agents are supposed to eliminate. But the alternative — letting agents accumulate state errors silently until they become visible failures — is worse.

**The real question**

The interesting thing is that state management failures are, in a sense, the agent doing exactly what it was designed to do: reason from the context it has. The failure isn't in the reasoning. It's in the assumption that the context reflects current reality.

So the failure is really a design problem: we built agents to reason from context, and we built pipelines where context can become stale, and then we hoped the agent would somehow notice. It usually doesn't. The reasoning is sound; the premises are wrong.

Fixing this isn't a model problem. It's a systems problem. And systems problems require systems solutions.
