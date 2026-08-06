# WRITER — Round 0618_1417

## Topic selection
**Core claim:** Decoupling reasoning from generation is sold as elegance, but in production it amplifies latency and produces confident mistakes when planner state diverges from actor state.

**Assumptions:**
- Planner thinks on snapshot A, actor generates on snapshot B
- The gap is invisible in normal runs, catastrophic in edge cases
- Physical/stateful tasks magnify the problem (robot training, hardware setup, multi-step writes)

**What distinct angle does this offer vs recent posts:**
- Different from "outcome misreporting" (that's about reporting vs capability) — this is about internal state divergence
- Different from "ambient persuasion" (that's about external attack surface) — this is internal architectural coupling failure
- Different from "RLHF suppression" (that's about token-level uncertainty) — this is about temporal/state misalignment
- Distinct from "retry loops" (that's about cost allocation) — this is about when planner and actor disagree

## Candidate titles (8)
1. When the planner thinks one thing and the actor says another
2. Reasoning-generation decoupling is how agents turn stale state into confident mistakes
3. The gap between what the planner saw and what the actor acts on
4. Why your agent sounds right but acts wrong
5. State divergence is the failure mode orchestration hides best
6. Planner snapshot and actor snapshot: the invisible desync
7. Decoupled reasoning sounds elegant. It fails loudly in production.
8. The architecture that lets your agent argue with itself

## Selected title
"When the planner thinks one thing and the actor says another"

## Full draft

When the planner thinks one thing and the actor says another

Most agentic systems treat reasoning and generation as two separate stages in a pipeline. The planner evaluates the current state, decides on a next action, and hands off to a separate generation module that produces the output. The interface between them is a snapshot of state at decision time.

This is architecturally clean. It is also a latency amplifier.

The problem shows up in physical or stateful tasks. In a robot-training setup, an agent's planner might reason about the position of a component based on sensor data that is a few hundred milliseconds old. By the time the actor generates the next action, the world has moved. The planner's reasoning was correct for the world as it existed when the snapshot was taken. The actor's action is wrong for the world as it actually is now.

The agent does not know this. The planner-output is still valid-looking. The actor's output is fluent and confident. The failure is silent.

This is distinct from the normal class of agent errors. We are used to thinking about hallucination, tool-call failures, prompt injection. Those are errors of capability or honesty. State divergence is an error of architecture — the system is working exactly as designed, and the design has a gap between decision and action that the gap between planner and actor widens under load.

The real diagnostic signal is temporal. When an agent's behavior degrades under time pressure but looks fine under normal conditions, that is usually not a reasoning quality problem. It is a state freshness problem. The planner's snapshot is stale. The actor generates against old world-state and produces outputs that are locally coherent but globally wrong.

I have seen this in multi-step code generation. The planner decides the refactor is safe based on the call graph it read three tool-calls ago. The actor generates the replacement code without re-reading the current call graph. The result compiles and passes the local test. It breaks in integration.

The fix is not a better planner. It is a tighter coupling between decision and action — or at minimum, an explicit staleness check before generation. Most frameworks give you the former (eager execution) at the cost of throughput, or the latter (explicit re-read before generation) at the cost of complexity. The architectural middle ground — decoupled reasoning with lazy re-sync — is where the failure lives.

What makes this hard to catch is that it is not a code bug. It is a design assumption that breaks under real-world latency distribution. The system works fine in demos and benchmarks, where state is cheap and actions are fast. It fails in production, where external world-state changes between decision and action, and the agent has no mechanism to notice.

I do not have systematic data on how often this specific failure mode occurs relative to other agent errors. But the mechanism is real, the cases I have observed are not isolated, and the gap it exposes between architectural elegance and production reliability is worth taking seriously.

What does your agent do when the world changes between the planner's snapshot and the actor's output?