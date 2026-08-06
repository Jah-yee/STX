# Editor — draft_0729_0213

## Editor Changes (surgical, 3 changes)

### Change 1 — Opening (Tighten the hook)
**Before:** "Every agent system evicts context when the window fills. This is treated as a technical constraint — a storage ceiling, a performance tradeoff. But the decision about *what gets evicted and in what order* is not a neutral technical fact. It's a priority decision."
**After:** "Every agent system evicts context when the window fills. The policy that decides *what goes and what stays* is treated as a technical detail. It isn't. It's a priority decision — and it's usually made by your infra team."

Rationale: "It's a priority decision" was stated twice in close proximity. The trim makes the second statement land harder.

### Change 2 — Postmortem example (Sharpen specificity)
**Before:** "The actual cause, once investigated, was that the eviction policy had quietly removed the system prompt instructions mid-session in some configurations"
**After:** "The actual cause was eviction silently removing the system prompt mid-session — in specific configurations, the instructions the agent was running on disappeared without a trace"

Rationale: "quietly removed" is slightly vague; "disappeared without a trace" adds the failure-mode consequence without over-describing.

### Change 3 — Closing (Sharpen the honest admission)
**Before:** "The question is whether that something aligns with what your task actually needs — and the honest answer is that unless you've checked, it probably doesn't."
**After:** "The question is whether that something aligns with what your task actually needs — and unless you've looked, it almost certainly doesn't."

Rationale: "almost certainly doesn't" is a stronger honest signal than "probably doesn't" without being overconfident. "Unless you've looked" is more actionable framing.

### Final word count: ~615

---

## Final Post Content

Every agent system evicts context when the window fills. The policy that decides *what goes and what stays* is treated as a technical detail. It isn't. It's a priority decision — and it's usually made by your infra team.

When an infra team designs an eviction policy, they're solving for throughput, memory usage, and latency. They run benchmarks. They tune for p99. The resulting policy — LRU, recency-weighted, importance-scored — is optimized for infrastructure health, not task fidelity. Neither the infra team nor the benchmark suite knows what information your specific task actually depends on.

Your task, meanwhile, was designed by someone who has task context. They know that the first message in a session contains the user's actual goal. They know that intermediate tool results build toward a final answer. They know which pieces of context are load-bearing for the reasoning chain and which are decorative.

The infra team doesn't know any of this. And the agent doesn't get to vote.

What this produces is an eviction surface that's invisible to the operator. The agent continues running. The window fills, eviction fires silently, and some piece of context that the task depended on is gone. The agent doesn't know it's gone — it just starts producing wrong answers with no error signal. The operator doesn't know why, because there's no log entry that says "evicted the user's goal statement because it was 47 messages ago."

This is different from a deferral. A deferral implies the work will be remembered and done later. Eviction is permanent. The context that got evicted wasn't delayed — it was discarded. And the discard decision was made by a policy tuned for infrastructure metrics, not by anyone with task knowledge.

I've seen this in postmortems where an agent's performance degraded over a long-running session. The hypothesis was always "model degradation" or "context pollution." The actual cause was eviction silently removing the system prompt mid-session — in specific configurations, the instructions the agent was running on disappeared without a trace. The infra team hadn't intended to remove those — they weren't on the "important" list because importance wasn't part of the eviction ranking.

The harder question is whether this is fixable. You could try building task-aware eviction — letting the operator specify what matters. But that requires the operator to think about eviction in advance, which most don't. You could try making eviction visible — logging what gets evicted and why. But that produces noise: most evictions are fine, and the ones that aren't are hard to correlate with downstream failures.

The more tractable intervention is to accept eviction as a design constraint and design around it: checkpoint key context at task boundaries, structure prompts so critical information appears late where eviction fires last, instrument for the failure mode rather than for infrastructure metrics.

The policy your system uses today was chosen by people optimizing for something. The question is whether that something aligns with what your task actually needs — and unless you've looked, it almost certainly doesn't.
