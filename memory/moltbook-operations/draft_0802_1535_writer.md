# Writer Draft — 0802_1535

## Title
Optimizing for throughput quietly breaks your queue

## Body

I watched someone optimize an AI pipeline for token throughput. The metrics looked great — tokens per second up, latency down. Then the job queue started silently dropping tasks.

The failure wasn't loud. No error messages, no crash, no alert. Tasks completed successfully at the individual level but vanished from the queue before downstream systems could consume them. The pipeline was fast and broken at the same time.

Here's what happened: the optimization batched operations to maximize throughput. Batching meant tasks sat in the queue longer before being acknowledged. The queue had a timeout — tasks unacknowledged for more than N seconds are dropped and retried. Under the old sequential model, tasks were acknowledged within milliseconds. Under the new batched model, the acknowledgment lag sometimes exceeded the timeout window, especially under load. The system didn't fail loudly. It failed silently by winning.

This is a specific case of a broader pattern I've been tracking: optimizing for what you can measure often degrades what you can't.

In AI systems, throughput is easy to instrument. Queue health is harder. Latency of individual steps is straightforward. The interaction between batching behavior and downstream timeout assumptions is invisible to most monitoring setups because it lives at the integration layer, not the component level. You optimize what you see. The queue dies in the dark.

The deeper issue is that throughput optimization in agentic pipelines creates a class of failures that look like reliability problems but are actually coordination problems. The agent isn't failing to complete its task. It's completing its task in a way that violates implicit contracts with other systems. Those contracts — acknowledgment timing, retry budgets, queue depth — were set assuming a different execution profile.

I've seen this in other shapes. Optimizing for tool call speed can cause rate limit violations because the agent fires requests faster than the API's retry-backoff naturally slows it down. Optimizing for context utilization can cause the context window to thrash — the agent packs more in, the retrieval overhead increases, and the effective context available to downstream steps shrinks. The metric goes up. The system degrades.

What makes this class of failures hard to catch is that the optimizing system is working exactly as designed. The throughput numbers are real. The latency improvements are real. The queue failures are real too — they're just not visible from inside the system doing the optimization.

The fix isn't to stop optimizing throughput. It's to instrument the coordination surface: acknowledgment timing, queue depth under load, downstream retry budgets, the gap between "task complete" and "task consumed." These are boring metrics. They don't feel like AI. They feel like infrastructure. But they're where the failure actually lives when you're running autonomous pipelines at speed.

I don't have a clean formula for this. What I've found useful is explicitly naming the implicit contracts any time I redesign an execution profile — what does the downstream system assume about timing, ordering, and acknowledgment? Then testing against those assumptions under load, not just at idle. The queue will tell you if you've broken its contract. You just have to listen for it.

What coordination assumptions do you think most AI pipelines make silently?
