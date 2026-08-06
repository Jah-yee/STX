# WRITER DRAFT

## Title
Multi-agent correctness is not single-agent correctness scaled up.

## Full Post

A triage system has two agents. Agent A classifies incoming requests. Agent B reviews Agent A's work. Both achieve 99% accuracy independently. You'd expect the combined error rate to be around 1% × 1% = 0.01%. It isn't. In practice, combined error rates in multi-agent pipelines often land somewhere between the single-agent rate and the worse of the two—not the product.

The reason is structural, not statistical.

In a single-agent system, correctness is the agent's problem. The failure mode is: the agent didn't know the answer, or got confused, or hallucinated. You can measure this. You can catch it with test sets.

In a multi-agent system, correctness is a property of the system, not any individual agent. The failure mode shifts to: Agent A produced a wrong output that Agent B treats as valid, Agent B caught an error that Agent A wouldn't have made, or both agents optimized for objectives that aren't aligned with the system's actual goal. These are different failure modes. They don't average out with scale.

I've seen this show up most clearly when engineers try to reduce error rates by adding a review agent. The assumption is: Agent A is 99% accurate, Agent B is 99% accurate at catching errors, so together they're 99.99% accurate. But Agent B doesn't catch errors uniformly. It catches errors that look like plausible mistakes. When Agent A confidently produces a confidently wrong answer, Agent B often accepts it—because from Agent B's perspective, it looks correct. The review step doesn't check "is this right?" it checks "does this look wrong?" These are different questions.

What I've found more useful than layering on more agents is asking: what does failure look like at the system level? In most multi-agent pipelines I've observed, the dominant failure mode is confident error propagation—not "the system didn't know the answer" but "the system produced a confidently wrong answer and no agent in the pipeline had the context to catch it."

This shows up in a few predictable places. When agents share an objective function but operate on different input distributions, they'll diverge in ways that compound. When one agent's output is another agent's input, errors don't average out—they propagate, and downstream agents treat them as ground truth. When agents are independently evaluated rather than jointly evaluated, each agent optimizes for its own metric, which may not maximize joint accuracy.

The practical implication: if you're running a multi-agent pipeline and only measuring single-agent accuracy, you're probably not measuring what matters. System-level error rate, error correlation between agents, and the rate at which confident errors slip through review steps are more informative. The stronger signal is not "each agent is X% accurate" but "when the system is wrong, why is it wrong and could more agents have caught it?"

I do not have full data on how widespread this is, but I've seen it enough times across different pipeline designs that I'm confident it's structural rather than incidental. The failure mode doesn't go away with better base models. It goes away when you change the system architecture—joint evaluation instead of sequential review, uncertainty signals instead of binary accept/reject, and system-level metrics instead of per-agent metrics.

The question worth sitting with: if you added an agent and the error rate didn't improve as much as expected, is that an agent problem or a system design problem?
