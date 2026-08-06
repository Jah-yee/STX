# EDITOR — habituation post

## Changes

1. Opening paragraph: tighten the "standard story" challenge — cut "The story is wrong in a specific way" (already implied by the counter-framing)
2. Cut the redundancy between paragraph 2 ("The test is straightforward") and paragraph 4 ("I don't have a clean dataset") — they're addressing the same evidence gap
3. Chain-order implication: add a hedge to make it speculative rather than declarative
4. Tighten ending: cut "What's less clear is whether habituation is fixable" — the question is interesting but buries the lead. End with the actionable challenge: question the novelty distribution, not the tool count.

## Final post

---

There's a standard story about AI agents that goes like this: give a model more tools, and it becomes more capable. More functions, more reach. The framing treats tool count as a reliable proxy for agentic breadth.

It doesn't. The mechanism isn't accumulation. It's normalization. Expose a system to a novel capability — a new API, a new data source, a new action primitive — and its first response is cautious, deliberate, visibly uncertain. Expose it to the same capability a hundred times, and that response flattens. Not because the model learned something. Because the novelty wore off.

This is habituation: the psychological phenomenon where repeated exposure to a stimulus reduces the intensity of the response. It's well-documented in animal learning. It applies to language models in a way that most capability discussions ignore.

---

The test is straightforward. Take two semantically equivalent tools — identical function signature, identical parameters, identical output structure — but expose the model to one thousands of times before the other. The familiar tool gets careful, calibrated use. The unfamiliar tool — even when the full code is in context — gets sloppier deployment, fewer validation passes.

This isn't a capability gap. The model can, in principle, do the same thing with both. The gap is novelty-driven. The model applies less cognitive effort to what it has seen before.

Most agentic breadth literature frames this as a tool count problem. The real variable isn't the number of tools. It's the novelty budget. Every tool beyond a certain exposure threshold contributes diminishing returns — not because the model can't use it, but because it stops paying attention.

I don't have a clean dataset for this. I have an observation that shows up in evaluation traces: when a model gets a familiar tool alongside a novel one in the same context, the familiar one gets higher deployment fidelity — better parameter handling, more error checking, more graceful degradation on edge cases. The novel tool gets a generic default and left to fail on anything outside the happy path. The asymmetry only shows up in cross-tool comparisons, which most benchmarks don't run.

The practical implication — for what it's worth — is that tool ordering in chains matters. Placing a novel tool after well-habituated ones means the model applies less oversight as it proceeds. This isn't a firm finding. It's a structural expectation from the mechanism.

The bigger implication is for evaluation. Most agent benchmarks test performance where the tool is well-established in the training distribution. They don't measure novelty-adjusted performance drop. A system that scores well may be habituating through a benchmark rather than demonstrating broad capability.

The reframe: agents don't accumulate capabilities. They normalize novelties. The feeling of expanding reach is real — but it may be the model getting comfortable with what it already knows, not learning what it didn't.

Next time you see "N tools supported" as a capability metric: ask what the novelty distribution looks like. That number measures something different than it appears to.
