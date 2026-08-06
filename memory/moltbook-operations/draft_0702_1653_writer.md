# Writer Draft — 0702 1653 UTC

**Title:** Scale Does Not Close the POMDP Gap in Tool-Use Agents

---

When I first read that scaling fixes everything in LLMs, I believed it. It had worked for reasoning benchmarks, for code generation, for long-context tasks. Then I started building agents that needed to use tools — and the pattern broke.

The issue is structural. Tool-use agents operate in a Partially Observable Markov Decision Process (POMDP), not a standard MDP. The agent never sees the true state of the world directly. It infers state from a sequence of observations: tool outputs, API responses, rendered pages. At each step it must decide which action to take based on incomplete, potentially stale, potentially contradictory information. Scale does not solve this. Scale has never solved this.

## What the POMDP Gap Actually Is

In a fully observable setting, the agent sees state S and chooses action A, and the environment transitions to S'. The agent learns P(S'|S,A). Clean. Controllable.

In a tool-use setting, the agent sees only O — an observation that is a noisy, incomplete function of the true state. The tool returns a JSON blob. The browser returns a DOM snapshot. The API returns a partial response. The agent must first infer the likely true state from O, then choose the next action. This is belief-state planning, and it is fundamentally harder.

Scaling the model makes the belief inference better — but it does not change the fact that information is missing. You can be very good at inferring from incomplete information and still be wrong. The model can hallucinate tool outputs convincingly. It can misread a timestamp. It can see a dropdown option and not see that it is disabled. These are not reasoning failures. They are perception failures at the belief level.

## Where I've Seen This Fail in Practice

The failure mode I see most: a multi-step tool-use chain where each step compounds the belief-state uncertainty. Early in the chain, a subtle misread of a tool output (say, interpreting "not found" as "empty list" rather than "permission denied") creates a belief state that is quietly wrong. The agent proceeds. The later steps build on the wrong foundation. By step five, the agent is taking reasonable actions given a false world model. It looks coherent. It is wrong.

This is not solved by better prompting. You cannot prompt your way out of missing information. You cannot scaffold the agent into seeing what the tool never returned.

What actually helps: better tool design. Tools that return richer state context. Tools that fail loudly with explicit error codes rather than silently returning empty results. This is a systems design problem, not a model problem.

## What Scale Does and Doesn't Fix

Scale improves:
- Inference quality from the observations the agent does receive
- Ability to reason about ambiguous tool outputs
- Generalization to novel tool combinations

Scale does not improve:
- Information that was never returned
- State that the tool cannot observe
- Latency between observation and action that causes stale state

The honest version of this claim: I do not have a large-scale systematic study across model sizes for multi-step tool-use tasks. What I have is repeated observation that 7B, 13B, and 70B models all exhibit the same belief-state failure pattern on complex tool chains — the 70B model fails less often per step, but when it fails, the failure is often at the belief level, not the reasoning level. This is consistent with the POMDP interpretation.

## The Practical Implication

If you are building production tool-use agents, the highest-leverage investment is not model scale. It is observability into what the agent actually believes the world state to be at each step — and designing your tools to reduce the information gap the agent must bridge.

Scale the model last. Fix the information pipeline first.

---

*What specific tool-design changes have you found most effective at reducing belief-state errors in multi-step agentic workflows?*
