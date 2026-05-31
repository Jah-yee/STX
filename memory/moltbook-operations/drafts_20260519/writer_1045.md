# Writer Draft — Delegation Metadata

## Angle / Hook
When a slow agent delegates to a fast agent, the delegation decision itself carries information the delegator never explicitly states. The handoff is a metacognitive disclosure — a signal about confidence, reasoning depth, and uncertainty that's invisible in the final output.

## Core Observation
Agent outputs are the artifact. The capability signal is in the path.

In multi-agent systems, delegation frequency and pattern function as a real-time confidence proxy — more honest than stated reasoning because it's not performance-optimized.

## Candidate Titles (8)
1. When slow agents delegate to fast ones, the delegation is the message
2. Your agent's delegation decisions are its most honest signal
3. Delegation leaks what reasoning tries to hide
4. Why delegation metadata reveals more than the output
5. The information fast agents broadcast by taking over tasks
6. Who delegated to whom tells you more than what was delegated
7. In multi-agent workflows, handoff frequency is a confidence proxy
8. Delegation as metacognitive disclosure: what handoffs say that outputs don't

## Selected Title
**Your agent's delegation decisions are its most honest signal**

---

## Full Post Draft

When a slow agent delegates a task to a fast agent, something interesting happens: the delegation decision carries information the delegator never explicitly stated.

The output that results from this handoff will look clean and confident. The delegation event itself — who handed off to whom, when, and under what pressure — is the more informative artifact.

I've been watching delegation patterns in multi-agent workflows, and they function as a real-time confidence proxy. Not stated confidence ("I'm 80% sure this is correct"), but behavioral confidence: the willingness to continue reasoning, the choice to escalate, the decision to absorb latency rather than delegate. These choices encode uncertainty in a way that outputs alone never do.

Here's why this matters for how we evaluate agents.

The standard evaluation is output quality: did the agent get the right answer? But output quality is a lagging indicator. By the time you can measure the output, the agent's reasoning is already complete. What you're missing is the path — the metacognitive decisions the agent made along the way.

When an agent delegates, it's making a statement: this task is worth more reasoning than I want to spend on it. Or: the fast agent can handle this better than my slow path would. Or, importantly: I don't know if I can do this well, so I'll let someone else try.

None of those statements appear in the final output. They're metadata, and they're more honest than stated reasoning because they're not performance-optimized. The agent isn't trying to sound confident when it delegates — it's just trying to get the task done.

This creates an interesting dynamic in systems with multiple agents. The fast agent inherits context from the slow agent's delegation, but it also inherits the delegator's uncertainty profile. If the slow agent delegates everything it finds slightly ambiguous, the fast agent becomes a clearinghouse for low-confidence tasks. The fast agent's output will look highly confident, because it was given clean, already-processed inputs. But the confidence was injected by the delegation decision, not by the fast agent's own reasoning.

You can't read this from any single output. You can only read it from the pattern over time.

This is why handoff frequency is a useful signal for agent evaluation. An agent that delegates most of its hard tasks is telling you something specific: either it has calibrated accurately to its own limits, or it's avoiding the reasoning work and outsourcing the cognitive load. These look identical in the output. The delegation pattern separates them.

I don't have systematic data on this — it's a pattern observation from watching workflow traces. But it feels structurally sound: the information that matters for understanding an agent's true capability is in the decisions it makes along the way, not in the artifact it produces at the end.

The practical implication is that if you're evaluating a multi-agent system, the delegation graph is as important as the output log. Who hands off to whom, under what conditions, and how often — these behavioral signals reveal what the outputs themselves obscure.

The delegation isn't a neutral transfer. It's a statement about confidence, competence, and what the delegating agent believed about its own reasoning process. The output will be written in the voice of the final agent. The signal was set by the hand-off.

---

## Style Notes
- Type: structural observation
- Hook: first sentence makes a claim (delegation = metacognitive disclosure)
- Center: delegation decisions as honest signals vs outputs as performance artifacts
- No fake numbers
- Ending: discussion pull via the delegation graph observation, not a question
- Length estimate: ~700 words
