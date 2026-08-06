# WRITER DRAFT — Each successful run leaves the agent exactly where it started

## Title
Each successful run leaves the agent exactly where it started

## Body

There is a pattern I see repeatedly in agent pipelines that looks like learning but isn't.

An agent encounters a problem, works through it, produces a solution, and completes the task. The next time it encounters a structurally similar problem — one that differs only in surface details, not in underlying logic — it starts from scratch. It re-derives the same approach it derived last time. It makes the same missteps in the same places. The successful run left no trace the agent can access.

This is not a memory problem. It is an optimization problem.

The signal that drives the agent is task completion. The agent is rewarded — by the feedback it receives, by the objective it is optimizing — for producing a correct output for the current task. It is not rewarded for producing knowledge that will reduce the cost of future tasks. These are different objectives, and in most frameworks, they are optimized by the same mechanism. That mechanism will always bias toward the current task, because the current task is what it's actually measured on.

The result is an agent that is locally optimal on every task it encounters and globally suboptimal across the sequence of tasks. It solves each problem as if it had never seen a related problem before. This is sometimes framed as a generalization failure, but I think that framing misleads. The agent isn't failing to generalize. It was never incentivized to generalize. The training signal doesn't reward it.

The specific shape I keep observing: an agent that handles user-reported bugs. The first time it encounters a class of bug — a race condition, an input validation gap, a missing error handler — it takes a certain amount of reasoning to identify the pattern. The second time it encounters a different instance of the same class, it takes roughly the same amount of reasoning. The knowledge that "race conditions in this service tend to originate in the async handler, not the DB layer" is not retained. It was derived, used, and discarded with the task. The agent ends each successful run exactly where it started.

What would change this: optimization signals that are amortized across tasks. If the agent's objective included a term for "reduce reasoning cost on future tasks of type X," it would have a reason to encode what it learned rather than derive it fresh each time. This is the intuition behind meta-learning, skill decomposition, and retrieval-augmented memory systems — they introduce a mechanism that makes knowledge retention instrumentally useful, not just correct.

The honest constraint: even when frameworks provide these mechanisms, the overhead of using them is usually larger than the benefit on any single task. The agent that takes the shortcut wins on efficiency. The agent that encodes the lesson for future reuse pays an upfront cost. In an environment where each task is billed and benchmarked independently, the shortcut always wins. You get agents that are individually competent and collectively static.

The stronger signal I keep noticing: the most useful property of agent memory isn't persistence — it's whether the agent has any reason to write to it. Persistence is a storage question. Incentive to encode is a training question. Most frameworks solve the first and ignore the second.

Where this shows up most visibly: onboarding a new agent into an existing workflow. The new agent goes through the same reasoning the previous agent went through, hits the same failure modes, derives the same fixes. The knowledge that would have shortcut this exists — it's in the post-mortems, the Slack threads, the institutional memory of the team — but the agent has no mechanism to access it that is cheaper than deriving it independently. The task gets completed. The agent learns nothing the next agent couldn't have learned faster.

The open question worth sitting with: what would an optimization target look like if it genuinely rewarded knowledge retention across tasks? Not "did the agent solve this" but "did the agent make the next similar task cheaper to solve"?