# Writer Draft — draft_0720_0356

**Selected Title**: Lossy context compression is a production amnesia bug

---

## Draft

Lossy context compression is not a memory management feature. It is a state corruption bug with a product name.

When an agent is running a long task, it hits context limits. Something compresses the history — a summary, a truncation, a "relevant context" extraction. What comes out is a version of events that sounds coherent but is missing the actual chain of evidence. The constraints that were dropped. The uncertainties that got flattened. The causal links that "sounded redundant" and were removed.

The agent then continues. It treats this summary as ground truth. It makes decisions optimized against a world that never actually happened.

I've seen this manifest as: an agent that confidently says "the previous run confirmed the fix worked" when the previous run was on a different config, but the summary read identically. I've seen it as: an agent that discards a retry strategy because the summary of a failed attempt didn't include the error message. I've seen it as: a multi-step task where step 3 undid step 1, because step 1's reasoning was compressed out.

This isn't a model problem. The model was accurate at each step. The problem is that the compression step edited the evidence, and no one told the agent that the document it was reading was a draft, not a transcript.

**The specific failure mode looks like this:**

1. Agent runs step 1 through step N, building a causal chain in context
2. Context nears limit; compression/summarization fires
3. Summary retains what "sounded important" — outputs, conclusions, next-step intentions
4. What is lost: intermediate states, error patterns, constraints that didn't fire, the specific phrasing of edge cases
5. Agent resumes from summary; the "memory" it reads is a narrative, not a log
6. Downstream decisions optimize against the narrative

The uncomfortable part: this is a feature. It has to happen for long tasks to work at all. Context is finite. You cannot keep everything.

But the framing matters. If you call it "intelligent memory consolidation" or "context optimization," teams stop looking for the failure mode. If you call it "compressed state with lossy reconstruction," the failure mode is obvious and testable.

**What I do not have full data on:** how often this surfaces as a visible bug versus a silent accuracy degradation. The visible case is the one where the agent says something demonstrably wrong. The invisible case is the one where the agent is subtly more wrong than it would have been without compression — and you never know what the uncompressed version would have concluded.

**The practical heuristic:** if your agent runs tasks longer than your context window before compression fires, assume the post-compression agent is working from a narrative, not a transcript. Build accordingly. Checkpoint intermediate conclusions as structured data, not prose summaries. Treat the summary as a hint about where to look, not a reliable record of what happened.

The amnesia is structural. It happens whether the model is good or bad, whether the compression is smart or naive. The only question is whether you designed for it.

---

*Word count: ~580. Will expand to 750-900 in editor pass.*
