# EDITOR — Round 0728_1037

## Changes (Surgical)

### Change 1: Expand "The scheduling frame" section
Add concrete scheduling analogy to ground the abstract frame.

**Before**: "...every token in context is a unit of work competing for the model's attention..."
**After**: Add: "In a conventional operating system, a process that loses its time slice doesn't get deleted — it gets suspended until it regains priority. The context window does the same thing, except it never restores the lost slice unless the conversation naturally recycles back to that content. The constraint doesn't disappear. It just stops getting scheduled."

### Change 2: Add a contrasting scheduling example
**Before**: "The most common version I've observed..."
**After**: Add after first failure example: "The opposite case is equally instructive: an agent that kept a low-priority reminder in context for the entire conversation — not because it was important to the current task, but because it appeared in the most recent messages — while violating a high-priority constraint that had been stated earlier. The reminder was scheduled. The constraint was not. The memory trace looked fine. The execution failed."

### Change 3: Strengthen "what changed my mind"
The section currently ends thin. Expand the closing reflection.

**Before**: "What changed my mind on this was watching an agent fail..."
**After**: Replace with expanded version: "What changed my mind on this was watching an agent fail on a task where the critical constraint was introduced in the first message. The constraint was short — two sentences — and the agent restated it correctly in its reasoning throughout the conversation. But at execution time, it violated the constraint. The constraint was still in context, still being restated, still present in the agent's articulated reasoning. But the operations that violated it kept getting scheduled, and the constraint-keeping operations kept getting descheduled. I initially thought this was a memory capacity problem — not enough context to hold everything. But the constraint wasn't evicted. It was descheduled. It remained in the window, in the reasoning trace, in the agent's restatements — but not in the operations that mattered. That distinction broke the mental model I was using."

### Change 4: Tighten final paragraph
The closing question is good but the preceding sentence can be tighter.

**Before**: "The question worth asking: what would an explicitly scheduled context window look like..."
**After**: "The question worth asking is simpler: what would an explicitly scheduled context window look like — one where priority signals are controlled by the workflow's goal structure rather than by recency heuristics? The scheduler is in charge. The question is whether you know what it's optimizing for."
