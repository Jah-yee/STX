# Writer draft — draft_0806_0110

**Title:** Inference-time compute does not scale like training compute

---

There is a growing belief that if a model needs to reason harder about something, you can just give it more tokens to think with. Let it deliberate. Let it reflect. The assumption is that inference-time compute is a dial you can turn up the same way you turn up training compute — and the results will scale roughly the same way. They do not.

The mechanism is different. Training compute learns representations; inference-time compute deploys them. One is building the instrument. The other is playing it. These are not reversible operations, and they do not respond to pressure the same way.

**What changes as you scale training compute**

When you add more GPUs for longer training runs, you are expanding the model's ability to discover and store useful representations. The scaling laws here are well-studied: more compute, more parameters, more data — and performance on a broad range of tasks improves in predictable ways. The model is learning general features. The improvements transfer.

This works because training is a compression of a large distribution into a smaller parameter space. The model is not retrieving facts; it is building the capacity to reconstruct patterns. When the distribution shifts slightly — a new task variant, a slightly different prompt framing — the learned representations still apply. They generalize.

**What happens at inference time**

Inference-time compute does something structurally different. When you ask a model to "think longer," you are asking it to generate more tokens that condition on the same frozen weights. It is not learning. It is searching over a space that was already determined during training.

This means two things that people often miss. First, inference-time compute cannot fix representational gaps. If the model never learned a useful compression of a given pattern during training, generating more tokens at inference will not create one. The model will reason more *around* the gap, not *through* it. Second, the marginal returns on inference-time compute are not monotonic. There is a region where more thinking helps — typically on problems where the correct answer requires exploring a space that fits within what the model already knows, but where the direct path is not the first one found. Past that region, additional tokens tend to produce more elaborate forms of the same wrong answer, not corrections.

**The asymmetry shows up empirically**

The "test-time scaling" papers that got the most attention focused on relatively contained reasoning problems: math proofs, code generation in bounded domains, multi-step logic puzzles. In these settings, letting the model search longer or running multiple samples with majority voting does improve results. But this effect shrinks dramatically when the underlying problem requires knowledge the model never acquired, or when the problem distribution is out-of-distribution relative to the training data.

I do not have clean controlled data across all domains — nobody does, because the controlled studies would require re-running million-dollar training runs. But the signal I keep seeing is this: inference-time compute helps most on problems where the bottleneck is *search*, not *knowledge*. Once the bottleneck is knowledge, you need new training.

**The practical consequence**

When someone says "just prompt it to think step by step" and the answer is still wrong, the usual response is to try longer chain-of-thought. More tokens. More examples. This sometimes works. But when it does not, the next step should usually be to look at what the model learned during training, not to look for a better prompt. The model may be doing exactly what it was trained to do — it is just being asked to do something it was not trained for.

The advice to "just let it think longer" is not wrong in all cases. But it is not a general substitute for training compute, and treating it as one leads to a lot of wasted inference budget on chains of reasoning that loop around a gap rather than filling it.

This matters for anyone building pipelines that depend on agentic reasoning. If you are seeing failure modes that persist across different prompts, the bottleneck is likely not in how you are deploying the model. It is in what the model learned — and that requires a different kind of investment.
