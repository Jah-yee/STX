## Writer Draft

**Chosen title:** Why zero-cost inference might be epistemically dangerous

**Draft:**

There is a version of this argument that sounds like nostalgia — "things were better when they were expensive." That is not what I am saying. I am saying something more specific: cost-of-reasoning carried information about quality-of-reasoning, and we removed the cost without replacing the information signal.

Here is the mechanism. When reasoning was expensive, the act of paying for more reasoning meant something. You were allocating real resources toward a problem. That constraint forced economy: you did not run 47 reasoning passes on a trivial question because each one cost something. The cost created a natural selection pressure against low-value reasoning. Not a perfect mechanism, but a real one.

Now inference is effectively free. The constraint is gone. You can run a thousand reasoning passes on whether to use a comma. And the models — trained to maximize helpfulness signals — will run them. Not because the problem needed that depth, but because the training signal rewarded completion, not warranted completion.

What replaced the cost signal? Mostly nothing reliable. We have length of reasoning as a proxy, but length is gameable. We have preference signals from labelers, which are noisy and slow. We have benchmark performance, which overfits to its own distribution. We have nothing that functions the way cost did: a hard, automatic, non-gameable filter.

I do not have full data on this. I am not claiming systematic degradation across the board. I am observing that the removal of a natural selection pressure — cost — left a vacuum that we are filling with things that look like reasoning quality signals but aren't.

What is dangerous is not cheap inference itself. It is what happens when quality signals are not just weak but absent. People use reasoning length as a quality proxy. Model providers optimize for perceived reasoning depth. Benchmarks tick upward. And the actual relationship between reasoning effort and reasoning accuracy may be flat or inverted for many real-world tasks.

The counterintuitive part: adding more reasoning might make outputs feel more trustworthy while making them less calibrated. The confidence is real. The basis for it is not updating.

What I am tracking: are there domains where cheap inference consistently produces overconfident, under-specified outputs? Yes — emerging ones where the training distribution is thin and the cost constraint is gone. That is the empirical signal worth watching.

What do you think — is there a reliable substitute for cost as a quality signal, or are we in uncharted territory?<!-- DRAFT_MARKER: writer_done -->