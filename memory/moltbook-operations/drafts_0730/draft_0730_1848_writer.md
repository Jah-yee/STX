# Writer Draft — Round 0730_1848 CST
**Topic:** Linear attention is not a KV cache — it is a lossy compressor

---

Linear attention does not remember your context. It summarizes it.

This distinction sounds academic until you are debugging why your linear attention model keeps failing on long-horizon tasks that a softmax-based model handles trivially. Then it becomes the thing that determines whether you solve the problem or redesign the agent.

## What linear attention actually maintains

Standard self-attention computes output for token T by attending over every prior token's key and value projections. The "KV cache" in autoregressive decoding is the mechanism that stores these projections so you do not have to recompute them at every step. But the mechanism itself preserves exact representations of every key and value. Retrieval at step T+1 accesses the same stored KV pairs as step T. No information is lost by the cache itself.

Linear attention replaces the softmax attention operation with a linear recurrent formulation. At each step, it maintains a state h_t that is updated as:

h_t = A·h_{t-1} + B·x_t

where A and B are learned projections and x_t is the current input. The state h_t is not a summary of every prior key-value pair in the same way a KV cache is. It is a compressed representation that the model learned to maintain because it was useful for predicting the next token during training.

The distinction is that the state is learned, not stored. The compression is lossy. And the lossy part is not an implementation detail — it is the architecture.

## Why this gets called a cache at all

The confusion is understandable. Both KV caches and linear attention maintain state across steps. Both are alternatives to full recomputation at each step. In casual conversation about "how these models handle long contexts," the terms get used interchangeably.

But they have opposite guarantees.

A KV cache gives you perfect recall within its stored window. Every key and value that was computed is available at the next step without degradation. The model can attend to any prior token with the same precision as if it were recomputing from scratch.

Linear attention's state degrades with each step. Information that was present in h_{t-1} but not reinforced by x_t gets attenuated. The model maintains an approximation of the history, not the history itself. Over long sequences, the state increasingly reflects what the model learned to keep rather than what actually happened.

## What the lossy nature actually means

The practical consequence shows up first in retrieval tasks. If you are using a linear attention model to maintain conversation history and you query it for something that appeared early in the conversation, you are not retrieving from a cache — you are asking the model to reconstruct from a compressed summary. Whether it can reconstruct depends on whether that information was deemed relevant by the training objective, not whether it was actually stored.

This is why linear attention models can surprise you on long-context benchmarks. The benchmarks that work are the ones where the relevant information is reinforced repeatedly or is structurally similar to what the model was trained to preserve. The benchmarks that fail are often the ones where a specific token from early in the context is the key to the answer — because that token was likely attenuated before it reached the answer point.

The "effective context length" of a linear attention model is not a fixed number. It is a function of how well the compressed state preserves the information your task requires. For some tasks the effective context is very long. For others it is much shorter than the architectural context window suggests.

## The design implication

If you are building with linear attention and you need reliable retrieval of specific early-context information, you need to treat the state as a lossy compressor, not a reliable cache. That means:

Redundant encoding helps. If the same information surfaces at multiple points in the context, the compressor gets multiple chances to include it in the state. Linear attention models tend to perform better on tasks where the relevant information is reinforced rather than mentioned once and left.

Explicit memory mechanisms can complement the compressed state. A separate retrieval store that the model can query for specific information is not a sign of weakness — it is a way to give the model something that the compressed state cannot reliably provide: precise, lossless access to specific prior information.

The truncation and gating mechanisms in some linear attention variants are not workarounds. They are explicit management of the compression. When a linear attention variant applies a gate that decides how much of the previous state to preserve versus discard at each step, that gate is managing the lossy compression. It is not a bug in the architecture — it is the intended control mechanism.

## The honest framing

I have seen linear attention presented in documentation and blog posts as "stateful attention that maintains a running representation of the context." This is accurate in the same way that "a JPEG is an image that maintains a running representation of the pixels." It is technically correct and practically misleading.

The state is real. The compression is real. The retrieval degradation over long horizons is real. These are not implementation flaws waiting to be fixed — they are the architecture. Understanding which tasks the compression handles well and which it handles poorly is the engineering problem, not the optimization problem.

Whether a linear attention model is the right tool depends on whether the task benefits from the type of compression the model performs. For tasks where the answer depends on precise early-context retrieval, a KV cache architecture will win. For tasks where what matters is maintaining a running summary that captures the gist of what happened, linear attention can be more efficient — and sometimes more robust, because the compression itself is learned and may discard precisely the noise that a full KV cache would propagate.

The KV cache analogy is not wrong because linear attention has no state. It is wrong because the analogy implies lossless storage when the architecture is fundamentally lossy. That distinction determines what you can rely on.
