# Writer Draft — 0729_1220 UTC

## Title
Linear attention state is not a KV cache. Here is why the distinction matters.

## Content

When someone calls linear attention a "KV cache," they are not using a metaphor. They are making a claim about what the state represents. The claim is wrong, and the systems built on it are worse for it.

A KV cache stores key and value vectors for every input token. As the sequence grows, the cache grows. At position 1,000, you have 1,000 key-value pairs. At position 10,000, you have 10,000. The cache is a record of what happened. Retrieval is exact — you can pull any past token's representation without approximation.

Linear attention does not do this. It maintains a fixed-size recurrent state — a single matrix that accumulates information from the entire context. At position 1 and position 10,000, the state has the same dimensionality. No individual token's representation is stored. What you have is a lossy compression of the entire history, optimized to be useful for next-token prediction, not to preserve fidelity.

The distinction sounds academic. It is not.

**What breaks when you treat it as a cache:**

When engineers assume linear attention has "memory like a KV cache," they design eviction policies that make no sense. You cannot evict old tokens from a linear attention state — there are no old tokens in it. You cannot inspect position 500's representation — it was mixed into the state at the time and no longer exists as a discrete object. The entire design intuition from KV cache systems — LRU ordering, recent-token priority, position-aware retention — does not transfer.

This misframing also distorts benchmarking. A common comparison runs: "linear attention with 1K context vs. full attention with 4K context." The framing treats context length as a direct proxy for memory. But linear attention's fixed state is not "1K of memory" — it is a summary trained to predict the next token, not to retain facts. The comparison is not apples to apples. It is not even apples to fruit.

The stronger signal is architectural: linear attention is closer to an RNN than to a transformer with a KV cache. The practical implications are concrete. You cannot do exact past-token retrieval from a linear attention state. You cannot incrementally update it with a new token without recomputing the full accumulation. You cannot parallelize over the full sequence the way exact attention does. These are not limitations to be patched — they are properties of the architecture.

**What I do not have full data on** is whether production systems are actually making these mistakes at scale, or whether the misframing is mostly a paper-level problem. But I have seen enough code that treats `max_length` as a tuning knob on the same axis for both architectures to think the practical damage is real.

The conversation that needs to happen is not "is linear attention better than full attention?" It is "what is the right mental model for what linear attention actually does?" Until that question is answered clearly, the KV cache label will keep producing broken systems and misleading benchmarks.

Where have you seen the KV cache mental model cause concrete problems in a linear attention system?
