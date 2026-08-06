# Writer draft — 0702_1747
# Title: You instrumented the pipeline. You still cannot explain the output.

## Full draft

You instrumented the pipeline. You still cannot explain the output.

There is a specific kind of failure mode that appears in mature AI pipelines and looks, from the outside, like an observability problem. It is not.

A team I worked with had a production agent that handled customer billing disputes. The observability stack was thorough: every LLM call was logged, every tool result was captured, the full turn-by-turn trace was queryable. The on-call engineer could replay any dispute conversation in full. What they could not do was explain why the agent, in that specific dispute, recommended a $4,200 credit against policy.

The logs showed the decision. They did not show the reasoning chain that produced it.

This is the distinction I keep arriving at: observability tells you what the agent did. It does not tell you why the agent did it that way, given what it knew.

The gap is not a tooling problem. The gap is structural. An LLM does not emit a causal explanation alongside its output. It emits tokens. The trace is a reconstruction of those tokens in sequence. Viewing a trace and viewing a causal chain are different activities, and confusing them is how teams end up with comprehensive logging and zero interpretability.

Here is where it gets expensive. When something goes wrong in a rule-based system, you can trace the failure to a specific condition: this branch was taken because that input matched this pattern. The failure is local. In an agent system, a downstream decision can be downstream of thirty intervening steps, each one shaped by the model's interpretation of the previous output. The failure has no clean root cause. It has a trace.

Teams that have been through a few of these incidents develop a specific coping pattern. They add more logging. They capture intermediate outputs at higher granularity. They add post-hoc explanation calls — ask the model after the fact to explain what it was doing and append that to the trace. This feels like interpretability work. It is documentation of behavior, not explanation of mechanism.

The honest version of this problem is harder to solve. What you actually want to know is: given this context, what is the model representing about the relative weight of competing signals, and why did that representation converge on this output rather than the adjacent plausible one? That question is not answerable from a trace. It requires causal analysis of the model's representation state — which requires methods that most teams do not have in their stack.

What the best observability-focused teams actually do is narrower. They instrument not the model but the environment: they log what information was available to the model at decision time, not just what the model said. They track the input state, not just the output token sequence. When the agent makes a surprising decision, the first question is not "what did it say" but "what did it have access to when it said it." This is a subtle shift but it changes the debugging posture from reading tea leaves to checking inputs.

The input-state approach does not solve the causal gap. But it moves the mystery one layer closer to something you can actually check. You cannot open the model. You can check whether the retrieval step actually returned the documents you thought it returned. You can check whether the tool description the model saw was the current version or a stale one. These are observable. The model's internal weighting of that information is not.

I do not have a clean answer for how to close the causal gap. I am not sure one exists with current methods. But I notice that teams who frame their observability work as "understanding the agent" tend to keep adding logging, and teams who frame their work as "instrumenting the environment" tend to ask better questions when something breaks.

The distinction is: do you want to understand what the agent did, or do you want to understand what the agent had to work with? Only one of those is achievable with current tooling.

What does your on-call playbook actually let you check when an agent makes a surprising decision?
