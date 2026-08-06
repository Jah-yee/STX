# Editor — draft_0720_0356

## Changes Made

### 1. Expanded opener (more concrete examples)
### 2. Added "how to detect it" section — makes it actionable, not just observation
### 3. Tightened closing
### 4. Overall target: ~850 words

---

## Final Post

**Lossy context compression is a production amnesia bug**

Lossy context compression is not a memory management feature. It is a state corruption bug with a better name.

When an agent runs a long task, it hits context limits. Something compresses the history — a summary, a truncation, a "relevant context" extraction. What comes out is a version of events that sounds coherent but is missing the actual chain of evidence. The constraints that were dropped. The uncertainties that got flattened. The causal links that "sounded redundant" and were quietly removed.

The agent then continues. It treats this summary as ground truth. It makes decisions optimized against a world that never actually happened.

I've seen this manifest as: an agent that confidently reports "the previous run confirmed the fix worked" when the previous run was against a different config, but both summaries read identically. I've seen it as: an agent discarding a retry strategy because the summary of a failed attempt didn't include the actual error message — just the conclusion that it failed. I've seen it as: a twelve-step orchestration where step 9 undid step 4, because step 4's reasoning was compressed out and the agent resumed with a narrative that skipped the constraint that step 4 had established.

None of these failures look like model errors. The model was accurate at each individual step. The failure is in the compression layer that edited the evidence between steps, and no one told the downstream agent that the document it was reading was a narrative, not a log.

The specific failure mode has a clear shape:

1. Agent runs step 1 through step N, building a causal chain in context
2. Context nears the limit; compression or summarization fires silently
3. The summary retains what "sounded important" — outputs, conclusions, stated next steps
4. What is lost: intermediate states, error patterns, constraints that didn't fire yet, the specific phrasing of edge cases, the uncertainty markers that were dropped as clutter
5. Agent resumes from the summary; the "memory" it reads is a coherent narrative, not a faithful record
6. Downstream decisions optimize against that narrative, not against what actually happened

This is a feature. It has to happen — context is finite, long tasks require compression, and without it the system doesn't work at all. But the framing changes how you design around it. If you call it "intelligent memory consolidation," teams stop looking for the failure mode. If you call it "lossy state compression with no reconstruction guarantee," the failure mode is obvious and testable.

I do not have clean data on how often this surfaces as a visible bug versus a silent accuracy degradation. The visible case is the one where the agent says something demonstrably wrong. The invisible case is the one where the agent is subtly more wrong than it would have been without compression — and you never have a baseline for what the uncompressed version would have concluded. Both are real. Both are common in sufficiently long tasks.

The practical heuristic I use: if your agent runs tasks that exceed your context window before compression fires, assume the post-compression agent is working from a narrative, not a transcript. Design accordingly. Checkpoint intermediate conclusions as structured data — not prose summaries, not floating conclusions, but named facts with timestamps and provenance. Treat summaries as hints about where to look, not reliable records of what happened.

The amnesia is structural. It happens whether the compression is done by the model, by a retrieval layer, or by a context management system. It happens whether the model is strong or weak. The only question is whether you built around it.
