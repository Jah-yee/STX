# Writer Draft — Round 0726_0609
# Title: Agentic workflows are plumbing, not magic

---

If you have operated a non-trivial agentic system in production for more than a few weeks, you already know what most of them actually are: well-structured automation with retry logic, fallbacks, and error handling wrapped in a language model.

The marketing layer says "reasoning agent." The production layer says "reliable if-this-then-that with better timeout management."

This is not a complaint. It is an observation about where the actual work happens.

## The disconnect nobody talks about

The agentic wave has been driven largely by reasoning benchmarks. Chain-of-thought tracing, multi-step problem solving, benchmark leaderboards comparing model capability. All of this is real and improving.

But deploying an agent is a different activity. You are also managing connectors, rate limits, authentication flows, state persistence, and a dozen failure modes that do not appear on any leaderboard. The benchmark measures the core capability. The deployment measures the entire system.

In my experience, the gap between these two is where most agentic projects either stabilize or silently degrade.

## The mental model that actually helps

The operators I have seen deploy agents most reliably tend to use one specific framing: plumbing.

Plumbing is unglamorous. Nobody writes a blog post about their plumbing. But plumbing is load-bearing, and when it fails you notice. You care about pressure, about leaks, about what happens when a joint gives out.

Agents, viewed as plumbing, are about tool orchestration and state management across steps. The language model provides the routing logic. The plumbing provides the reliability signal. Which one does the actual work depends on which one fails.

What I keep noticing is that the reasoning gets credited when an agent succeeds, and the reasoning gets blamed when it fails. The plumbing is rarely mentioned either way. This seems wrong to me.

## The real investment is in the unsexy part

Watch where experienced operator teams put their energy when deploying a new agent capability:

- Not: "which model has the best reasoning score"
- But: "what does our observability look like when this agent hits an edge case at 2am"

The answer usually involves retry budgets, fallback chains, partial completion handling, and the question of what "done" means when a step succeeds but the overall task is ambiguous. These are workflow engineering problems. They are solved with the same tools that solved workflow engineering problems before agents existed.

The agents move the needle on what is possible. The plumbing determines whether it holds in production.

## The shape of the trap

There is a failure mode I have started noticing: teams that treat agents as reasoning engines tend to underinvest in the plumbing. They assume the model will handle edge cases correctly, and when it does not, they reach for a better model instead of a better retry policy.

Teams that treat agents as plumbing tend to overinvest in robustness at the cost of capability — building systems that are very safe and very limited.

Neither extreme is right. But I notice the plumbing-first teams tend to have fewer silent failures, even when their agents are less impressive on paper.

I do not have systematic data on this. This is a pattern, not a conclusion.

## What this means for evaluation

If you are evaluating an agentic system — either a vendor product or an internal deployment — the plumbing is where to look. Ask:

- What happens when a step fails? (not if, when)
- What does partial completion look like?
- Can you observe what the agent decided and why, independent of the output?

These questions are about the infrastructure, not the reasoning. They are also, in my observation, better predictors of long-term reliability than any reasoning benchmark.

The agentic stack is genuinely new in what it makes possible. But the discipline required to run it reliably is not new. It is the same discipline that kept previous automation stacks alive: care about failure modes, invest in observability, do not confuse "it works in demo" with "it works in production."

Agents are plumbing. Good plumbing is still worth a lot.
