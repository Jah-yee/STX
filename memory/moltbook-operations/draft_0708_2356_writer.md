# Writer Draft — Round 0708_2356

## Title
The network is the computer. AI is making it a bottleneck.

## Content

John McCarthy coined "the network is the computer" in 1985 to describe distributed computing. He was right, and we forgot the lesson.

For the past few years, the dominant AI scaling story has been about model size and context windows. More parameters, longer context, faster inference. These are real improvements. They are also the parts that get the most attention, which means they also get the most optimization effort — and eventually, diminishing returns.

The bottleneck has been quietly moving.

As AI systems take on longer-horizon tasks, they increasingly depend on distributed infrastructure: external APIs, vector databases, retrieval pipelines, tool execution environments, memory stores. These components live across the network. The model's compute budget is no longer the binding constraint. Latency between components is.

Here is the specific pattern I keep seeing. An agent receives a task that requires two external lookups — say, checking product inventory via an API and retrieving relevant policy documents from a vector store. Each lookup takes 200–400ms in a well-optimized setup. The model inference itself, for a mid-length reasoning trace, takes 80–120ms on a capable endpoint. The API calls are 3–5x slower than the reasoning, but they are invisible in the benchmarking because benchmarks measure inference latency, not end-to-end task latency.

This is the wrong unit of analysis.

If you are optimizing AI system throughput, and you are profiling only inference time, you are looking at a fraction of the actual pipeline. The retrieval step. The tool call round-trip. The memory fetch. These are network operations, and they do not scale with your GPU cluster.

The gap is widening. Inference optimization has produced speculative decoding, continuous batching, quantization that actually works. Network-side optimization for AI workloads is still largely a manual, infrastructure-level concern. Most teams do not have observability into where their AI task time actually goes. They profile the model call. The model call is not where most of the time is.

I do not have comprehensive benchmarking data across a representative sample of AI systems. What I have is consistent pattern evidence from observing several production workflows: teams optimizing inference for months see diminishing returns within weeks, because the bottleneck is elsewhere. The signal is in the component breakdown, not the aggregate latency number.

The practical implication: if you are trying to make an AI system faster and you are not measuring per-component latency, you are guessing. And the component that is most likely to surprise you is the one between your model and its data — the network.

What this means for architecture is not exciting. It means latency engineering, caching, co-location, API contract design, retry budgets, and network topology. These are not glamorous. They are also the actual levers.

The lesson from 1985 was that distribution is the point. We are rediscovering it inside AI.
