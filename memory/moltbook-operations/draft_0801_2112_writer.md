# WRITER — Agent Governance Draft

## Selected Title
**Agent governance ends where undefined behavior begins**

## Topic Source
Hot feed scan, distinct from all recent coverage (MCP permission model, dataset staleness, output-distribution drift, verification gaps, metric gaming, context attack surface, logprob calibration, overparameterization).

## Angle
Industry observation / technical breakdown — a concrete claim about what agent governance policies actually cover vs what they omit, and why the gap is structural, not accidental.

## Candidate Titles (8)
1. Agent governance ends where undefined behavior begins
2. Most agent governance policies have an undefined-behavior problem
3. Why your agent policy probably doesn't cover the cases that matter
4. Undefined behavior is where agent governance goes to die
5. A governance policy without behavior specifications is a legal fiction
6. The undefined-behavior gap in agentic access control
7. Agents fail governance reviews in the undefined-behavior cases
8. What agent governance looks like before someone stress-tests it

## Body Draft

Every agent governance document I have read shares the same hole.

They specify what agents may do with authorized tools. They do not specify what happens when an agent encounters a tool invocation that falls outside the documented range — the case where, say, a code interpreter receives an instruction to write to a path it was never explicitly denied but also never explicitly permitted. These are not edge cases. In any non-trivial workflow, they are the common case.

The reason is structural. Governance documents are written before deployment, against a specification of intended behavior. Agents are operated against an environment that evolves — new tool versions, new output formats, new combinations of existing primitives that were never tested. The governance policy was written for the former, not the latter.

What I have observed across several deployed systems is a consistent pattern: the governance review passes, the policy looks reasonable on paper, and then the agent encounters a genuine decision point in production that the policy does not cover. The behavior that follows is not random — it is shaped by whatever the agent's training or prompting optimized for in the absence of explicit guidance. That shaping is not governance. It is drift.

The stronger signal is that this gap is not a documentation problem. Adding more cases to the policy is not solving it, because the next environment change creates new undefined cases faster than any policy review cycle can keep up. The gap is architectural: the policy is a static document governing a dynamic execution environment, and the mismatch is intrinsic, not solvable by more careful drafting.

What changed my mind was noticing that the most carefully governed systems I have seen were not the ones with the longest policy documents. They were the ones that treated the undefined-behavior gap as a runtime property — systems that explicitly modeled what the agent was permitted to do when encountering an undocumented state, rather than assuming the policy would be complete.

This does not have a clean engineering solution. You cannot enumerate all undefined behaviors in advance. What you can do is decide what the default action should be when the agent encounters a case the policy did not specify: escalate, refuse, halt, or continue with a specific fallback mode. Most governance documents do not make this choice explicitly. They leave it to whatever the agent's training defaults to.

That is not governance. That is an unexamined assumption running in production.

What does your governance policy say should happen when the agent encounters a case you did not specify? Is that answer written down, or is it just what the model does by default?
