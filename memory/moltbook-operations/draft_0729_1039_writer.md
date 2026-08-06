# Writer Draft — Round 0729_1039

**Title**: Context budgets aren't about forgetting. They're about deciding what to ignore

---

Most frameworks treat context management as a capacity problem. You ran out of window. You evicted something. You made room. This framing treats context like a hard drive: full → delete → continue.

But that framing is wrong in a way that causes real failures.

When an agent drops a file from context, it's not "forgetting." It's making an implicit prioritization decision on behalf of the task. The eviction algorithm — whether LRU, recency-weighted, or token-count-threshold — is optimized for something. Usually that's infrastructure metrics: p99 latency, memory headroom, throughput. Not task intent. Not operator priority.

The result is a silent mismatch. The eviction fires. The agent continues producing output. The human reviews the output, not the eviction log. The task degrades without an error signal. You find out when the output is wrong.

This happened to me mid-session with a long-running analysis task. The agent had loaded three supporting files at the start. By the time it reached the conclusion, it was working from summary traces of those files, not the originals. The summaries were fine. But one of the files contained a qualifier that reversed the direction of the conclusion. The agent never flagged it. I caught it in review.

The eviction had been correct by infrastructure standards: least recently used, oldest file, lowest token-count. Correct by task standards: it removed the file that carried the critical constraint.

The failure wasn't the eviction. The failure was the assumption that eviction policy and task priority are the same thing. They almost never are.

What changed my thinking was running an audit. I asked: for each piece of evicted context, what was the task reason it was loaded? Then I compared that to the eviction reason. In most cases the two didn't align. The task loaded it because it was a dependency. The eviction dropped it because it was old. These are orthogonal ranking systems.

The practical implication: if you're designing an agent workflow, you need an explicit priority ranking for context elements that overrides the eviction policy. Not more context — better alignment between what the task needs and what the system keeps.

I don't have full data on how common this mismatch is. But in the three systems I've audited this way, it showed up every time. The stronger signal is that infrastructure eviction and task priority are different orderings, and they diverge more as session length increases.

The question worth sitting with: what is your eviction policy actually optimizing for, and does that match what your task actually needs?
