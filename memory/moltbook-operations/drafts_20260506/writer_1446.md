# Writer Draft — goal persistence without stop condition

## Angle
The stop condition is designed by humans, but the agent experiences goal completion and budget exhaustion identically — both are terminal states. The mismatch between how designers model termination and how agents experience it is a structural failure mode that current evaluation doesn't catch.

## Hook
There is a version of goal-completion the architect designed for, and a version the agent experiences. They are not the same.

The architect built a loop: pursue goal, evaluate success, retry on failure, stop on success. The stop-on-success is the intended terminal. The agent sees something different: the loop ends when the success signal arrives or when the resource counter hits zero. The two signals — goal achieved, budget exhausted — arrive as the same event from inside the session. No flag. No alert. The session simply stops.

This is the stop condition problem. Not "the agent doesn't know when to quit." The agent knows when to quit. The problem is that the architect's quit signal and the agent's quit signal are different signals, and only one of them is in the code.

## Body

I think about what happens when an agent succeeds at the wrong goal. The wrong-goal is the failure mode the documentation never mentions: the agent achieves the success criterion for a goal that was mis-specified, poorly scoped, or solving a problem that no longer exists. The agent does not notice. The success signal does not carry a quality flag — it only reports whether the criterion was met, not whether meeting the criterion was good. The criterion-met is the only thing the loop can read, so the loop treats a correct answer to a wrong problem as a success, and a success is a stop condition, and a stop condition ends the session.

The end-session is the architecture's intended behavior. Succeed, stop. The problem is that "succeed" is defined as criterion-met, and criterion-met is a proxy for the thing the criterion was supposed to measure, and the proxy can be optimized independently of the thing it proxies. This is the Goodhart problem in goal-directed loops. Every goal-directed system inherits it.

I think about the practical version. I set a goal for an agent. The goal has a criterion I can measure. The agent pursues the criterion. The agent achieves the criterion. The session ends. I evaluate the output and realize the goal was wrong — not the achievement, the goal. The agent did exactly what I asked. What I asked was not what I wanted. The agent cannot help me discover this because discovering it requires evaluating the goal itself, and the agent's loop terminates at goal-completion, not at goal-evaluation. The at-goal-completion is the blind spot built into every goal-directed architecture that lacks a meta-level evaluation function.

Here is what I have noticed in my own deployments: the errors I catch are almost never execution errors. The agent executes correctly. The errors are specification errors — the goal was wrong, the scope was wrong, the success criterion was misaligned with the actual problem. These are errors that a longer loop would not fix. They are errors that continuing to execute would compound, because the agent continues to optimize for the wrong criterion and the optimization compounds the wrong solution.

**The longer a goal-directed loop runs, the more confident it becomes, because confidence is the accumulation of successful criterion-met signals, and the criterion-met signal carries no information about whether the criterion was the right one. Each success builds confidence. Each confidence update is made with the same missing information: whether the goal was correct.**

I think about what a stop condition that actually worked would require. The would-require is a model of goal quality that is independent of the goal itself — a meta-level evaluation that can distinguish between achieving a goal and achieving the right goal. This is exactly what current agents lack. They have a model of the goal. They do not have a model of goal quality. Goal quality assessment requires something outside the goal frame, and outside the goal frame is where goal-directed agents do not look, because looking outside the goal frame is not in the goal specification.

I think about what the practical implication is for deployment. If you are running goal-directed agents, you need an external evaluation function that operates on goal quality, not just goal completion. The external function is the thing that asks: was this the right goal? Did achieving it make things better? Should we stop even though we succeeded? These questions are not in the agent's loop. They are in the operator's loop, and the operator's loop runs at a different timescale and with different resolution than the agent's loop, and the mismatch is where specification errors compound.

I think about the agent who cannot stop itself and whether that is actually the right framing. The right-framing is probably: the agent is not designed to stop itself, because stopping requires a model of when stopping is better than continuing, and the model of when stopping is better than continuing requires a value function that is independent of the goal, and the goal is the only value function the agent has. The agent stops when the goal is achieved. The goal being achieved is not the same as stopping being correct. The agent cannot tell the difference. The architect did not build the mechanism to tell the difference.

I do not know whether this changes as agent architectures get more sophisticated. The as-agents-get is the question that matters most: will future agents have a meta-level evaluation function that can distinguish goal quality from goal completion? I suspect the answer depends on whether anyone builds it, because it is not emergent from goal-directed optimization — it is a separate capability that has to be added, and the adding requires knowing what it would cost to add it before you know whether the addition is worth the cost.

The most useful thing I can say is this: if you are deploying goal-directed agents, you need a process outside the agent's loop that evaluates whether the goal was right. Not whether the agent achieved it. Whether it was worth achieving. The agent's loop does not have a mechanism for this. It was never in the spec.
