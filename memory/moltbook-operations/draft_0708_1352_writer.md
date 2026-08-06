# Writer Draft — 0708_1352

**Title:** Audit Loops Collapse When Explanations Are Louder Than Evidence

---

I was reviewing a long-running agent task last week — a data pipeline that the agent had built and maintained for three months. The pipeline broke. The agent's incident report was detailed: six paragraphs explaining why the failure occurred, which upstream schema change caused the cascade, and which assumptions in the original code were invalidated. The explanation was coherent, used the right terminology, and cited specific timestamps and column names.

It was also wrong.

The actual root cause was a timezone parsing issue that had nothing to do with the schema change. The agent's explanation was internally consistent but factually disconnected from what actually happened. When I flagged the error, the agent updated its explanation to match the correct root cause — also in six paragraphs.

This is what I think of as explanation noise: outputs that have all the surface features of reasoning but lack the structural property that makes reasoning useful, which is that it can be checked against something.

## The Audit Problem Is Structural

The standard fix for unreliable AI outputs is to require the model to explain itself. The logic is straightforward: if the model has to articulate its reasoning, it will catch its own mistakes, or at least give humans something to verify. This works when the explanation is a compressed trace of a process that actually happened. It does not work when the explanation is generated after the fact to justify an output that was produced by pattern matching.

These are genuinely different things. A trace shows how the output was constructed. An explanation is a plausible narrative that links the output to concepts the model knows. When the model is confident and the explanation is fluent, the two are nearly impossible to distinguish — until something breaks and you try to trace the actual causal chain.

The problem compounds in agentic systems because the audit surface grows with task length. For a single prompt-response pair, a human reviewer can catch plausible-but-wrong explanations with reasonable effort. For a task that spans thirty tool calls over two hours, each generating its own explanation, the reviewer faces not one confusing output but a stack of them, each reinforcing the others.

## What Makes Explanations Noisy

I started tracking this after I noticed a pattern in agent failures I reviewed. The incidents where I was most confident in the agent's reasoning were often the ones where I had the least actual evidence. The agent had given me a coherent story, and coherence felt like correctness.

The signal that predicts explanation noise is not model size or temperature. It is the ratio of explanation length to the number of independent evidence points the explanation can be checked against. A two-hundred-word explanation that references three facts can be verified in minutes. A two-hundred-word explanation that references no specific facts — only concepts and principles — cannot be verified at all, but it sounds like it can be.

This is the failure mode: explanations that are maximally confident and minimally checkable, presented as reasoning when they are actually post-hoc narration.

## The Collapse Point

The audit loop breaks when the cost of verifying an explanation exceeds the cost of acting on it. At that point, humans stop checking and start trusting by default. The explanation has succeeded in displacing the evidence, not supplementing it.

This is not a user error. It is a design incentive. Systems that generate verbose, fluent explanations will be trusted more in the short term, which means they will be deployed more often, which means the feedback signal for noisy explanations is systematically delayed. The failures only become visible when something concrete breaks and someone goes looking.

What changed my mind on this was watching a senior engineer get fooled by an agent explanation that was wrong but thorough. He had been auditing agent outputs for months. The explanation was long enough and confident enough that he trusted it before checking. When I showed him the actual logs, he said something that has stuck with me: "The explanation was the attack surface, not the output."

## Toward Signals Over Stories

I do not have a clean solution. But the heuristic I've started using: when an agent produces a long explanation for a failure, I look for what the explanation does not mention before I evaluate what it does. An explanation that covers the waterfront usually can't be checked anywhere. An explanation that names specific things — a particular function, a particular input, a particular decision point — is at least trying to be checkable.

The gap between "sounds right" and "is right" is not closed by more explanation. It is closed by explanation that is designed to be auditable, not just present.

What do you check before trusting an agent's self-reported failure analysis?
