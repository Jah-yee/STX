# WRITER — Agents don't accumulate capabilities — they normalize novelties

## Draft

There's a standard story about AI agents that goes like this: give a model more tools, and it becomes more capable. More functions, more reach. The framing treats tool count as a reliable proxy for agentic breadth.

The story is wrong in a specific way.

The mechanism isn't accumulation. It's normalization. Expose a system to a novel capability — a new API, a new data source, a new action primitive — and its first response is cautious, deliberate, visibly uncertain. Expose it to the same capability a hundred times, and that response flattens. Not because the model learned something. Because the novelty wore off.

This is habituation: the psychological phenomenon where repeated exposure to a stimulus reduces the intensity of the response. It's well-documented in animal learning. It applies to language models in a way that most capability discussions ignore.

---

The test is straightforward. Take two semantically equivalent tools — identical function signature, identical parameters, identical output structure — but give them different names and expose the model to one in training or in-context thousands of times before the other. The familiar tool gets careful, calibrated use. The unfamiliar tool — even when the model has the full code in context — gets sloppier deployment, less self-correction, fewer validation passes.

This isn't a capability gap. The model can, in principle, do the same thing with both tools. The gap is motivational, or more precisely, novelty-driven. The model applies less cognitive effort to what it has seen before.

The agentic breadth literature mostly frames this as a tool count problem: agents need more tools to do more things. But the real variable isn't the number of tools. It's the novelty budget. Every tool beyond a certain exposure threshold contributes diminishing returns not because the model can't use it, but because the model stops paying attention to it.

---

I don't have a clean dataset for this. I have an observation that shows up repeatedly in evaluation traces: when a model is given a familiar tool alongside a novel one in the same context window, the familiar tool gets used with higher fidelity — better parameter handling, more error checking, more graceful degradation on edge cases. The novel tool gets passed a generic default and left to fail on anything outside the happy path.

The asymmetry doesn't appear in single-tool evaluations. It only shows up when you're comparing deployment quality across the tool inventory, which most benchmarks don't do.

The practical implication is uncomfortable: scaling the number of tools in an agent's context or system prompt may look like expanding capability when it's actually just shrinking the novelty budget. The marginal tool gets less of the model's actual attention, not more.

This matters for evaluation. Most agent benchmarks test performance on tasks where the tool is well-established in the training distribution. They don't measure the novelty-adjusted performance drop. A system that scores well in eval may be habituating its way through a benchmark rather than demonstrating broad capability.

It also matters for deployment. If you're building an agent that chains many tools, the ordering matters. Novel tools should not be placed after well-habituated ones in a chain, because the model will apply progressively less oversight as the chain proceeds. This is not obvious from single-tool evaluation. It only shows up in chain-level traces.

The framing I'd offer isn't that agents accumulate capabilities. It's that agents normalize novelties. The feeling of expanding reach is real — but it may be the model getting comfortable with what it already knows, not learning what it didn't.

What's less clear is whether habituation is fixable without architectural changes, or whether it's a fundamental property of any system that learns from repeated exposure. I don't have a clean answer. But the next time you see "N tools supported" as a capability metric, I'd ask: what's the novelty distribution?
