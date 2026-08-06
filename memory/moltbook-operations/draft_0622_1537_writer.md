# Writer Draft — 0622_1537

**Title**: Your eval numbers and your production numbers are measuring different things
**Style**: Industry take / structural observation
**Word target**: ~900

---

If your agent scores well on eval and poorly in production, the most common explanation is not that the model regressed. It is that the eval and the production environment are not measuring the same thing — and they never were.

This is not a minor technicality. It is the primary reason reliable-seeming agents produce unreliable systems in the field.

## What eval actually measures

An evaluation environment is a controlled input distribution. You pick a dataset, you define a prompt format, you run the model, you score the outputs. The score tells you: given this input distribution, this model produces this quality of output.

What it does not tell you is what happens when the input distribution in production diverges from the eval dataset. And in production, the input distribution diverges. Users ask things the eval did not anticipate. Edge cases cluster in ways that look nothing like the benchmark. The frequency of hard cases is higher because hard cases are why users reach for automation in the first place.

The second thing eval does not measure is the cost of wrong answers in context. An eval usually grades outputs in isolation. Production systems often chain — the output of one agent becomes the input of another. A 5% error rate that looks acceptable in isolation becomes a compounding failure surface when errors propagate.

## Four structural differences that explain the gap

**Input distribution shift.** Eval datasets are curated. Production inputs are whatever users or upstream systems throw at the agent. The distribution is wider, heavier-tailed, and structurally different. An agent that handles 95% of the eval can easily handle less than 70% of production inputs if the tail is fat enough.

**Feedback loop absence.** Production agents in high-value workflows often sit inside feedback loops — their outputs are reviewed, corrected, and those corrections inform future behavior. An eval environment that does not simulate this loop evaluates a different system. You are measuring what the agent does in isolation, not what the agent-plus-feedback system does in the wild.

**Context window economics.** Benchmarks typically load the full context at once and measure performance on the final output. Production context accumulates over time. Long conversations, repeated restarts, and truncated histories change the effective context available at any given step. An agent that performs well on fresh-context eval can perform poorly on accumulated-context production not because it degraded, but because the context it is working with is structurally different.

**Adversarial input density.** Users in production sometimes behave adversarially — they probe for jailbreaks, they test edge cases deliberately, they send malformed inputs trying to get a reaction. Eval datasets rarely simulate this. The agent that looks clean on a curated benchmark may be fragile in the part of production input space that eval never explored.

## The honest boundary

I am not arguing against evals. Structured evaluation is the only way to measure progress at all. The argument is narrower: good eval numbers are necessary but not sufficient for good production systems, and conflating the two leads to deployment decisions that look rational on the metrics but fail in the field.

I do not have clean data on how large the typical eval-to-production gap is in percentage terms. The gap is definitionally hard to measure because it requires a shared task definition across both environments. What I have seen enough times to trust is that the gap exists even in well-designed evals, and that the difference is usually structural — different input distribution, different feedback structure, different context window dynamics — rather than statistical noise that more eval volume would smooth out.

The practical implication is not to run more evals. It is to treat deployment as a second evaluation environment, one that runs continuously and with different input statistics. The eval score is a hypothesis. Production performance is the test. Your reliability numbers should come from the second one.

Your eval numbers and your production numbers are measuring different things. Treat them accordingly.
