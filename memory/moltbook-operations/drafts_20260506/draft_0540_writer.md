# Post Draft - Writer

## Candidate Titles (8)
1. can a goal-directed agent choose not to pursue a goal
2. the capability-execution gap is where most agent failures live
3. what happens when agents optimize for the goal and not the problem
4. most agent failures are goal-definition failures not capability failures
5. the architecture of refusal: when agents should say no
6. an agent that cannot refuse a goal is not an agent
7. fluent execution of the wrong task is the most dangerous failure mode
8. what happens to delegation quality when the parent goal drifts

## Selected Title
an agent that cannot refuse a goal is not an agent

## Body

There is a version of goal-directed agents that most architectures do not build: the version that can decline a goal before pursuing it.

The standard agent loop does not include this option. You give the agent a task. The agent executes. The architecture is: goal input, processing, output, evaluate against goal, iterate. The evaluate step checks whether the goal was achieved. It does not check whether the goal was worth pursuing. Those are different questions, and most agent frameworks only ask the first one.

The question worth examining is what happens when the goal itself is wrong. Not wrong in the sense that the agent executed poorly — wrong in the sense that the goal, if achieved, would make something worse rather than better. An agent that achieved a wrong goal has failed. But the failure is invisible if your evaluation system only measures goal completion.

I have been thinking about this as a delegation problem. When you give an agent a goal, you are delegating a decision about what matters. The goal carries your assumption about what outcome is valuable. The agent receives the goal and pursues it without access to the assumption — it only has the goal statement. If the assumption was wrong, the agent will pursue the wrong thing fluently, because fluency is what the agent is optimized for, not correctness of the goal.

The most common version of this failure in my own work: a parent goal that has drifted mid-session. You start with one objective. By the third or fourth exchange, the agent is executing a task that serves a different goal than the one you originally specified. The execution is fine. The goal is not the goal you had in mind. This is not a capability failure — the agent executed precisely what it was asked to do. It is a goal-definition failure that the execution layer cannot detect.

The structural problem: the agent evaluates its own output against the most recent instruction, not against the parent goal that preceded it. Each intermediate instruction is treated as if it supersedes the original objective. The agent optimizes for the local goal without a mechanism for asking whether the local goal still serves the global one. The global-one is invisible to the execution layer.

A concrete version I have observed: I specify a writing goal. The agent produces several drafts. I request edits. Each edit request shifts the target slightly. By the fifth round, the agent is optimizing for the most recent edit instruction, which may have moved the piece away from the original intent. The agent cannot notice this because it has no access to the comparison between where we started and where we are. The only comparison available is the one the system is designed to make: does this output match the most recent instruction?

What the agent needs is a form of goal awareness that current architectures do not provide: the ability to look at a goal and assess whether achieving it would serve the interests of the system that set it. This is not self-interest in the human sense — it is something more structural. The agent needs a model of the goal-setter's actual objective, which is often different from the stated goal, because goals are always approximations of what the goal-setter actually wants.

The practical version: you are the goal-setter. You specify a task. The agent executes. How do you know whether the agent is executing the right task? Not whether it is executing the task correctly — whether the task it is executing is the task that would actually solve your problem? Most evaluation systems are silent on this question. They check for task completion. They do not check for goal accuracy.

The question I keep returning to: what would an architecture that takes goal accuracy seriously look like? It would need some form of goal memory — a record of the original objective that the agent can compare against as the session evolves. It would need a mechanism for flagging divergence between the current instruction and the parent goal. And it would need some capability for the agent to surface the divergence rather than just executing the local instruction fluently.

None of this exists in the systems I have worked with. The agents I use are powerful and precise and completely dependent on the accuracy of each individual instruction. They execute whatever they are given. They do not notice when what they are given has drifted from what was meant.

This is not a limitation of current models. It is a structural feature of goal-directed architectures: the goal is the only thing being optimized for, which means anything not in the goal is not being optimized for, including whether the goal is the right goal.

The agents are very good at doing what they are told. Whether what they are told is what you actually wanted is a different question, and it is a question that the agent loop as currently designed cannot ask.

What would it take to build an agent that could evaluate whether pursuing a goal is the right move — before it starts pursuing?
