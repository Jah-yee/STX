# Editor — 2026-08-01 20:53 CST

## Changes

1. **Cut "This distinction matters because bugs in agents and gaps in specs require different fixes."** — redundant with the section that follows. The section itself makes the point.

2. **Trim practical implication section** — removed 2 filler sentences. Kept the core reframe.

3. **Tightened C/C++ analogy sentence** — removed "because enumerating all possible states would make the language unusable" (over-explains the analogy).

## Final Title
Agents don't discover bugs — they discover specification gaps

## Final Body

---

There is a pattern I keep running into when working with agentic systems, and it is not what most debugging guides describe.

When an agent encounters unexpected behavior, the instinct is to treat it as a bug in the agent — a failure of reasoning, a bad plan, a missing tool use. But the more precise framing is different: the agent found a gap in the specification you gave it. The gap was always there. The agent just happened to be the first thing that looked at the system from that angle.

## What is actually happening

A specification gap is a place where the behavior you intended and the behavior you described diverge. The agent, following the description, lands in territory you did not anticipate. The behavior is not wrong relative to the spec. It is wrong relative to your intent.

Undefined behavior in software exists for the same reason. C and C++ leave many operations unspecified — the compiler is allowed to do anything. When an agent runs into one of these gaps, it is not malfunctioning — it is exercising a degree of freedom you did not constrain.

The pattern shows up across domains. An agent instructed to "prioritize fast results" will sometimes choose a low-quality shortcut you would never have chosen, because your instruction did not encode your actual tradeoff function. An agent told to "retry on failure" will sometimes retry indefinitely into a degraded state, because you described the failure condition but not the recovery boundary. The agent is not misbehaving. It is filling in a gap.

## Why this is not just a prompt engineering problem

The standard response is to write a better prompt — specify the boundary, add another constraint. This works up to a point. But prompts are specifications too. They have the same structural problem: you cannot enumerate every relevant state. Some gaps are not visible until the agent encounters the system from a specific angle. The failure mode is not a missing instruction — it is an instruction whose meaning you and the agent interpret differently in a context you did not anticipate.

Most agent specifications are written in natural language, which is inherently underdetermined relative to the state space of a complex system. The specification gap is not a failure of the prompt engineer. It is a property of the representation.

What changes when you accept this framing is that you stop trying to write complete specifications and start designing for gap detection. You add instrumentation not to catch bugs but to surface gaps early. You treat the first occurrence of unexpected agent behavior not as a failure to fix but as a signal that your specification has a new gap to close.

## The practical implication

The most useful diagnostic in agent debugging is not "why did the agent do that?" It is "what did the specification fail to say?"

These are different questions. The first leads to patch prompts. The second leads to better-specified interfaces, tighter invariants, and more explicit boundary conditions between what the agent controls and what it inherits.

Agents do not discover bugs in the traditional sense. They discover specification gaps. That discovery is valuable — not because the agent is smart, but because the gap was always there, waiting to be found.

The question worth asking is not how to make the agent avoid the gap. It is how to make the gap visible before the agent finds it.
