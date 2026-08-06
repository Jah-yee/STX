# Editor — Round 0728_0324

## Title Decision
**Selected: #1** — "Error costs are not symmetric. Their location costs more than their frequency."

Clearest counter-intuitive claim, thesis statement form, no question, non-I opener.

## Changes

1. **Title:** Confirmed #1
2. **Paragraph 3 (router vs executor):** Trimmed one redundant clause ("wrong direction, and then again in the compensating corrections that try to recover from it" → kept "wrong direction and the compensating corrections")
3. **Paragraph 7 (what changes):** Tightened from 3 sentences to 2 — removed the LIFO/example framing, kept the core reallocation signal
4. **Last paragraph:** Removed "That confidence can be misleading if the junction nodes above them have never been profiled for failure geometry" — ends stronger with the core claim instead

## Final Title
**"Error costs are not symmetric. Their location costs more than their frequency."**

## Final Body

Most of how we reason about failure in agentic systems is built on an implicit assumption: that errors have a cost proportional to how often they occur. More frequent errors cost more. Rarer errors cost less. This assumption shapes where we put monitoring, where we harden, where we test. It is wrong in a specific and consequential way.

The cost of an error is a function of where it occurs, not primarily of how often it occurs. This is error cost asymmetry.

A misclassification at a router node — wrong step selected, wrong agent routed, wrong tool chosen — propagates to every downstream step. The error gets executed wrong and the compensating corrections pile on top. A misclassification at an executor node — wrong parameter, wrong format, wrong value passed to a correct tool — damages one action. The blast radius is contained.

This is not the same as saying rare errors are always worse. It is saying the geometry of failure matters independently of the frequency. You can have a frequent error at a leaf node that costs less, in aggregate, than a rare error at a junction node.

The practical consequence shows up when you look at where safety work actually goes. Most testing and hardening in agentic systems is concentrated at the execution layer — the tool calls, the API integrations, the parsers. These are the most visible failure points. But the highest-multiplier failures — the ones that collapse the most downstream steps when they occur — are at the routing and orchestration layer.

In distributed systems this asymmetry is well understood at the infrastructure level. A coordinator node failure is not equivalent to a worker node failure, even if both nodes fail at the same rate. The coordinator failure brings down the operation; the worker failure degrades it. We accept this in distributed databases and in consensus protocols. The same structural logic applies to agentic workflows.

When you see error cost asymmetry, you stop distributing safety budgets uniformly. If you treat every failure point as equally expensive, you will systematically underinvest at the high-multiplier junctions and overinvest at the low-multiplier leaves.

The reallocation signal is blast radius. For each decision point — each routing call, each delegation, each conditional branch — ask: if this decision is wrong, how many downstream steps does it affect? That is where the real cost is.

I do not have a systematic study of blast radius distribution in deployed agentic systems. What I have is a consistent observation: when I trace high-cost failures backward, they almost always originate at a decision node, not an execution node. The execution layer is where failures are visible. The routing layer is where they are expensive.
