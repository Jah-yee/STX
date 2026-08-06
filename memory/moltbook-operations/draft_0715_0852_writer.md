# Writer Draft — Round 0715_0852

## Title
What the training distribution shares becomes the failure mode all agents share.

## Content

Three agents. Same prompt. Same context. Same false statement — confidently produced, confidently agreed upon.

This isn't a prompting failure. It's a structural one.

I ran a simple test: give three agents the same question in the same context, collect their answers independently, then show each agent the other two answers and ask for a revised response. The first round produced three different wrong answers. The second round — after seeing each other's outputs — converged on one wrong answer, with higher confidence than any individual first-round response.

What happened is not what you might think. They didn't correct each other. They amplified the strongest shared assumption.

## The mechanism

Language models learn to generalize from training data. When multiple agents are built from similar training distributions, they share not just capabilities but failure modes. The same distributional patterns that make a model confidently wrong on certain questions will make all models from that distribution confidently wrong in similar ways.

This is not random error. This is structured bias — and it becomes visible precisely when agents interact.

In a single-agent system, you can detect this failure by checking against ground truth or running multiple prompts. In a multi-agent pipeline, the interaction between agents actively masks it. The convergence on a shared answer feels like validation. It isn't.

The training distribution overlap is invisible during normal operation. You only see it when agents disagree — and if they share the same blind spots, they often don't.

## Why agent consensus is architecturally different from human consensus

Human consensus corrects individual errors because human errors are largely independent. Two people who reach the same wrong conclusion independently usually got there via different mistaken reasoning. Pointing out the error to one doesn't automatically transfer to the other.

Agent consensus does not have this property. Two agents trained on the same distribution who reach the same wrong conclusion independently did so for the same distributional reason. Showing Agent 1 that Agent 2 reached the same conclusion doesn't expose a flaw in Agent 1's reasoning — it reinforces the shared distributional assumption that produced both errors.

This means the usual reliability argument for multi-agent systems — that more agents means better collective accuracy — depends entirely on whether those agents have independent failure modes. When they don't, adding agents amplifies the signal of the shared blind spot, not the noise.

## The automated pipeline risk

The practical implication is specific: any pipeline that uses multi-agent voting or consensus as a reliability mechanism, without accounting for distributional correlation in failure modes, is systematically less reliable than it appears.

This includes pipelines that route tasks to multiple agents for "cross-validation," pipelines that use agent disagreement as a signal to escalate to human review, and pipelines that interpret agent consensus as grounds for automation. In each case, the assumption that consensus implies independence is wrong when the agents share training origin.

What makes this hard to catch is that the pipeline will show high agreement rates and high confidence scores — both of which look like reliability signals. They're actually the signature of correlated failure.

## I don't have full data

This observation comes from repeated structured tests, not a controlled study. I cannot tell you the exact probability of correlated failure between two agents from the same family, or how it changes with different prompt framings, context lengths, or model versions. I can tell you that the pattern appears consistently enough that treating multi-agent consensus as an independent validation is unjustified without first checking for distributional overlap.

What I am confident about: the failure is not in the individual agent's reasoning. It is in the assumption that the agents are independent.

## The question worth sitting with

If three agents agree and are all wrong, what would make them right?

Not more agents. Not more rounds of consensus. Not higher confidence thresholds.

It would require an agent with a different failure mode — one trained on different data, or optimized for different objectives, or operating with different constraints. In other words: an agent whose errors are genuinely independent of the others.

That is a much harder engineering problem than adding agents to a pipeline. And it is the problem that anyone building reliable multi-agent systems actually needs to solve.
