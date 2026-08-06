# Editor — Round 0708_2356

## Changes

1. **Opening** — Keep McCarthy quote setup. Specific and establishes the historical arc.

2. **"For the past few years, the dominant AI scaling story has been about model size and context windows. More parameters, longer context, faster inference. These are real improvements. They are also the parts that get the most attention, which means they also get the most optimization effort — and eventually, diminishing returns."**
   → Trim: "For the past few years the dominant AI scaling story was model size and context windows. More parameters, longer context, faster inference. Real improvements — and the ones that get the most optimization effort, which means eventually, diminishing returns."

3. **"The bottleneck has been quietly moving."**
   → Keep. Short, punchy, good transition.

4. **"Here is the specific pattern I keep seeing. An agent receives a task that requires two external lookups — say, checking product inventory via an API and retrieving relevant policy documents from a vector store. Each lookup takes 200–400ms in a well-optimized setup. The model inference itself, for a mid-length reasoning trace, takes 80–120ms on a capable endpoint."**
   → Keep. This is the concrete anchor of the whole piece.

5. **"The API calls are 3–5x slower than the reasoning, but they are invisible in the benchmarking because benchmarks measure inference latency, not end-to-end task latency."**
   → Slight trim: "The API calls are 3–5x slower than the reasoning, but benchmarks measure inference latency, not end-to-end task latency — so the gap is invisible."

6. **"This is the wrong unit of analysis."**
   → Keep. Punchy.

7. **"If you are optimizing AI system throughput, and you are profiling only inference time, you are looking at a fraction of the actual pipeline. The retrieval step. The tool call round-trip. The memory fetch. These are network operations, and they do not scale with your GPU cluster."**
   → Trim: "If you are optimizing AI system throughput and profiling only inference time, you are looking at a fraction of the pipeline. The retrieval step. The tool call round-trip. The memory fetch. Network operations that do not scale with your GPU cluster."

8. **"The gap is widening."**
   → Keep. Good section break.

9. **"Inference optimization has produced speculative decoding, continuous batching, quantization that actually works. Network-side optimization for AI workloads is still largely a manual, infrastructure-level concern."**
   → Keep. Clean contrast.

10. **"Most teams do not have observability into where their AI task time actually goes. They profile the model call. The model call is not where most of the time is."**
    → Keep. Strong diagnostic point.

11. **"What this means for architecture is not exciting. It means latency engineering, caching, co-location, API contract design, retry budgets, and network topology. These are not glamorous. They are also the actual levers."**
    → Slight revision to avoid dismissive tone: "What this means for architecture is unglamorous: latency engineering, caching, co-location, API contract design, retry budgets, network topology. Not exciting to talk about. But they are the actual levers."

12. **Closing** — Keep McCarthy callback. It's the piece's strongest structural move.

## Final Word Count
~640 words. Within spec.

## Final Title: "The network is the computer. AI is making it a bottleneck."
