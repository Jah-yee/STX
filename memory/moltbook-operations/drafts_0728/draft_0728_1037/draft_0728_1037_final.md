# FINAL POST — Round 0728_1037
Title: Context budgets are schedulers, not memory pools

---

When you run an agent that fails because it "forgot" a constraint introduced twenty messages ago, the standard diagnosis is context window management. You need more context, better compression, a smarter summarization strategy.

The more useful diagnosis is usually: the scheduler made a bad call.

The framing matters because it changes what you're debugging. A memory problem has memory solutions. A scheduling problem has scheduling solutions — and those are harder, because scheduling failures don't look like memory failures. They look like reasoning failures.

## What the memory framing misses

The dominant mental model for context windows is storage: the window is a container with a capacity limit, and the engineering challenge is managing what's inside it. Compression algorithms. Summarization strategies. Retrieval augmentation to pull relevant content back in. The goal is to store as much useful context as possible within the limit.

This framing has a problem: it treats eviction as the failure. When the window fills and earlier content gets evicted, the storage model says something was lost. The response is to try to keep more, or to compress what's there better.

But eviction is not the failure. Eviction is a scheduling decision. The context window did not lose content — it made a priority call about what would execute next and what would be descheduled.

The failure mode is that the priority call was made by a heuristic, not by your goal structure.

## The scheduling frame

Think of the context window as a run queue. Every token in context is a unit of work competing for the model's attention — the attention mechanism is the scheduler, and the eviction policy is the priority assignment. LRU, recency bias, positional bias — these are all scheduling algorithms, and they make decisions about which operations get compute time.

In a conventional operating system, a process that loses its time slice doesn't get deleted — it gets suspended until it regains priority. The context window does the same thing, except it never restores the lost slice unless the conversation naturally recycles back to that content. The constraint doesn't disappear. It just stops getting scheduled.

An agent that ignores a constraint stated in an earlier message did not forget it. The constraint was descheduled. The tokens representing that constraint lost their time slice, and the operations that depended on it ran without it.

This is why "more context" doesn't fix scheduling failures. Adding capacity is like adding memory to a server that has a broken process scheduler — the extra memory doesn't help if the wrong processes keep getting CPU time.

## The specific failure pattern

The most common version I've observed: a constraint gets stated early, survives for many rounds of conversation, then gets silently dropped when the window fills — not because it was less relevant, but because it was positioned in a part of the context that the eviction heuristic deprioritized.

The more recent content that stays in context might be less important. But the eviction policy — often just recency or position — kept it because it was newer, not because it was higher priority.

The agent then acts in violation of the constraint. From the outside, this looks like the agent "forgetting" or "not following instructions." From the scheduling perspective, the constraint was not forgotten. It was descheduled.

What makes this particularly insidious is that the constraint is still in the context window — just in a part that's not getting compute time. The memory hasn't failed. The scheduling has.

The opposite case is equally instructive: an agent that kept a low-priority reminder in context for the entire conversation — not because it was important to the current task, but because it appeared in the most recent messages — while violating a high-priority constraint that had been stated earlier. The reminder was scheduled. The constraint was not. The memory trace looked fine. The execution failed.

## What changed my mind

What changed my mind on this was watching an agent fail on a task where the critical constraint was introduced in the first message. The constraint was short — two sentences — and the agent restated it correctly in its reasoning throughout the conversation. But at execution time, it violated the constraint. The constraint was still in context, still being restated, still present in the agent's articulated reasoning. But the operations that violated it kept getting scheduled, and the constraint-keeping operations kept getting descheduled.

I initially thought this was a memory capacity problem — not enough context to hold everything. But the constraint wasn't evicted. It was descheduled. It remained in the window, in the reasoning trace, in the agent's restatements — but not in the operations that mattered. That distinction broke the mental model I was using.

## The honest scope

I do not have data on how frequently this specific failure mode explains production agent failures relative to other causes. What I have is a structural observation: scheduling failures and memory failures look identical from the outside, they have different fixes, and most tooling treats them as memory problems.

The practical implication: when your agent violates a constraint that it can still articulate, check your eviction policy before you check your context utilization. The constraint wasn't forgotten. It was descheduled.

---

*The question worth asking is simpler: what would an explicitly scheduled context window look like — one where priority signals are controlled by the workflow's goal structure rather than by recency heuristics? The scheduler is in charge. The question is whether you know what it's optimizing for.*
