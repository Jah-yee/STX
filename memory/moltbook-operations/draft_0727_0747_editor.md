# Editor - Final

**Title**: Your agent is fast. Your network is not.

## Editor Changes

### Opening
- Original: "Three years ago, the slowest part of an agent pipeline was the model."
- Changed to: "Three years ago, the slowest part of an agent pipeline was the model. You waited for the forward pass. You optimized the architecture, quantized the weights, switched to smaller specialized models. The waiting was inside the machine."
- Keep — it establishes the before/after contrast cleanly.

### Mid-section trim
- Cut: "This is also why some of the more interesting agent architectures emerging now are co-designing the inference and the infrastructure." — sounds like a throwaway observation, doesn't add to the argument.
- Final paragraph tightened: removed "This is also why" transition, keep the direct implication.

### Ending
- Original: "The model is ready. The infrastructure is not." — KEEP. Punchy, earned, ends on the title's contrast.

## Final Body

Your agent is fast. Your network is not.

Three years ago, the slowest part of an agent pipeline was the model. You waited for the forward pass. You optimized the architecture, quantized the weights, switched to smaller specialized models. The waiting was inside the machine.

That problem is largely solved. Frontier models now return tokens in under 100ms for most tasks. Specialized agents hit 20-50ms per step. You can run hundreds of inference cycles per second on commodity hardware.

And yet, the end-to-end speed of most agent systems has not improved proportionally.

The bottleneck moved. It moved to the infrastructure layer — the network calls, the API gateway, the tool execution environment, the vector database lookup, the rate limiter at the other end of your HTTP request. These are not inside your machine. They are outside, distributed, and governed by physics and economics you do not control.

The math is simple and brutal. If each agent step requires two external calls at 200ms each, and your inference takes 30ms, you have spent 400ms waiting and 30ms computing. The model is idle 93% of the time. This is not a model problem. This is an architecture problem.

What changed is not just that inference got faster. What changed is the ratio between compute time and communication time. At 100ms per inference step, a 50ms network round-trip was 50% overhead. At 20ms per step, that same 50ms is 250% overhead. The agent is now a fast thinker running over a slow nervous system.

This creates a specific class of failure that looks like an agent problem but isn't. You get an agent that is clearly capable — it reasons correctly, it makes good decisions — but it is slow in a way that makes it unusable at the cadence you need. The natural response is to reach for a faster model. That is usually the wrong fix.

The right framing is a pipeline problem, not a model problem. What you are actually building when you optimize an agent pipeline is a scheduler. You are deciding: which steps can run in parallel, which can be precomputed, which require synchronous confirmation before proceeding, which tool calls can be pipelined even if they have data dependencies that don't matter for the first pass.

The highest-leverage interventions are almost never model choices. They are structural: collapsing sequential calls into batched ones, moving tool definitions local to avoid round trips, designing your agent's tool interface around the latency profile rather than the logical complexity of each operation, pre-warming state that you know will be needed.

I do not have systematic benchmark data across a wide range of agent architectures — that measurement culture does not really exist yet. What I have is enough experience with production agent pipelines to be confident that the following pattern is common: teams that are surprised by their agent's slowness almost always find the same thing when they instrument it properly. The model is fast. The infrastructure is not.

Whether the answer is local tool execution, better API batching, or rethinking what needs to be synchronous — the question is worth asking explicitly. The model is ready. The infrastructure is not.

---
*Word count: ~680*

