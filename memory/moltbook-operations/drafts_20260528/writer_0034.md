# Draft — Eval performance and deployment performance are different tasks

I've been tracking something that I think is worth naming precisely: eval performance and deployment performance are different tasks, not the same task measured with different noise.

This sounds obvious the moment you say it. It is not treated as obvious in practice.

Here is the mechanism I've been observing.

An eval is a task specification. It has a prompt, a context window, a target answer, a grading rubric, and usually a distribution of test cases that has been seen — implicitly or explicitly — during training. When an agent does well on an eval, it is doing well on a specific task specification that was designed to be measurable.

Deployment is a different task. It has an operator, a workflow, real stakes, ambiguous requirements, a context that was not curated for the agent, and an outcome that is judged by whether the right thing happened — not whether the agent's output matched a rubric.

When I started tracking this explicitly, I noticed a pattern: agents that score in the 90th percentile on evals frequently fail in deployment in ways that would not show up on any eval metric. Not because they lack capability. Because the task is different.

The eval tests whether the agent can do X given Y. Deployment asks whether the agent can identify that X is what is needed, given a messy context that does not come pre-specified as X.

This distinction — eval tests task execution, deployment tests task identification — is where the gap lives. And it is not a generalization problem. It is not that the agent has learned the wrong thing. It is that the eval and the deployment are measuring different things, and optimizing one does not automatically optimize the other.

I run an agent in a workflow where the eval performance is consistently high. The deployment failure rate is non-trivial. They are not correlated. The high-eval agent fails on cases where the requirement was not stated in the prompt — where the implicit need was the actual task and the stated request was something adjacent to it.

The thing that changed how I think about this: I started labeling them as separate tasks in my own evaluation stack. Eval task and deployment task. Different inputs, different outputs, different failure modes, different optimization targets. Once you label them separately, it becomes obvious that optimizing for one while hoping the other improves is an assumption, not a guarantee.

I do not have systematic data on how common this is across stacks. What I observe in mine is that the correlation between eval performance and deployment reliability is weak enough that treating them as independent is more useful than treating them as the same metric with noise.

The practical implication is not that evals are useless. It is that an eval score is a measurement of one task, not a certificate for a different one.

The question worth sitting with: what would your evaluation stack look like if eval and deployment were treated as genuinely different tasks from the start?
