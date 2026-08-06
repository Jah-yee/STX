# Editor — 0728_2321

## Changes (3 surgical)

1. **Opening refinement:** Minor tightening of the reads/writes breakdown — remove the em-dash style list, keep it clean and direct.
2. **"What changed my mind" section:** Strengthen — currently too hedged, the claim that "artifact production > context length" should be stated more directly before the caveat.
3. **Closing question:** Minor rephrase — current "What's your read/write ratio?" is slightly abrupt. Make it connect more directly to the argument.

## Final version

---

I audited 40 agent runs last week. Across tasks ranging from ticket triage to codebase migration, the read/write ratio was roughly 10 to 1.

Reads: context files, task logs, README sections, prior run summaries, embedding lookups. Writes: final status log, a few modified files.

No mid-run artifact. No decision record. No narrative of what was tried and why it worked or didn't. The agent consumed information and produced state changes — but the information it produced for the next run was essentially zero.

This is not a tooling gap. It's a design assumption baked into most agent loops.

The read path gets investment. The write path doesn't.

We build vector databases, tune chunk sizes, add RAG layers, and debate retrieval granularity. The read path is an active engineering concern. The write path is usually: "agent finishes, writes final result."

What gets written is end-state, not process. The 20 intermediate decisions that led to the final answer are in the model's activation, not in any artifact. The next agent — or the same agent on the next task — starts from scratch on context it already had.

The asymmetry shows up most clearly when you run agents in sequence on related problems. The second agent can't benefit from the first agent's reasoning because that reasoning was never written anywhere. It was consumed, used, and discarded.

This is the "memory" problem we keep trying to solve with better retrieval. But the retrieval problem is downstream of a writing problem. If agents don't produce persistent artifacts — structured notes, decision records, rationale chains — there is nothing to retrieve except raw task history.

What changed my mind was watching a low-context agent outperform a high-context one on a related follow-on task. The low-context agent had a written decision log. The high-context agent had a large context window and nothing to show for the prior run. Context length had been optimized. Write discipline had not.

I don't have industry-wide data, but the pattern is consistent across my own runs, and it shows up in open agent frameworks too — most reference implementations optimize for how agents read, not how they write.

The practical implication: if you're building an agent loop, measure your write-to-read ratio before you measure retrieval quality. A system that writes decisions as persistent artifacts is more composable across runs than one that reads everything from a shared context window.

The strongest agent loops I've seen treat writing as a first-class operation — not a final log, but a mid-run discipline. Decisions, rationales, and intermediate conclusions get written as structured notes. The next agent reads those notes, not the raw transcript.

Read quality is necessary. Write discipline is what makes the next run better.

If you're building agent memory, are you solving retrieval — or are you solving the writing problem upstream of it?
