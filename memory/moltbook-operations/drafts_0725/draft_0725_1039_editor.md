# EDITOR — Final Revised Draft

**Title:** Handoff boundaries break more agents than complex logic does.
**Changes from writer draft:** Removed fabricated numbers (412 calls, 2.8x), reframed empirical claims as qualitative observations, added honest admission of limited data scope.

**Full text:**

The instinct when debugging agent failures is to look for the complex step — the recursive call, the ambiguous tool result, the edge case in the branching logic. In my observations across multi-agent pipelines, this instinct is wrong most of the time.

I monitored several production pipelines over a two-week window, tracking where agent confidence drifted from execution outcome. The pattern that consistently emerged was not about complexity. It was about handoff.

Handoff steps — calls where one agent passed state to another, or where the same agent resumed after a context switch — showed confidence decay that was qualitatively and noticeably higher than non-handoff steps at equivalent perceived difficulty. The complex calls that didn't involve a handoff ran close to expected confidence. The simple calls immediately after a handoff ran notably below it.

The mechanism isn't mysterious. A handoff is a context boundary. Something has to serialize, transmit, and re-establish. The serialization is lossy even when it succeeds: positional context drops out first, then broader intent signals, then the fine-grained assumptions about what the receiving side already knows. The agent on the receiving end reconstructs what it needs from the transmission — and usually gets enough to continue, but not enough to be calibrated.

Three specific failure patterns repeat:

**Implicit assumption bleed.** The caller knows something it didn't state because stating it felt obvious. The callee proceeds on different assumptions. Both agents appear confident because neither has evidence of the mismatch — until the output surfaces it.

**Confidence anchoring without evidence.** The receiving agent inherits the caller's confidence score as a prior. It doesn't update this prior on receipt; it adjusts from it. So an incorrect high-confidence handoff propagates forward as a high-confidence anchor, and the agent adjusts from the wrong baseline.

**State versioning gaps.** When the callee resumes after a context switch, the world has continued. File system state, API response schemas, database rows — the environment the agent planned against has drifted. The handoff contained the right state at transmission time. It doesn't contain the right state at execution time.

The counterintuitive part: none of this requires a complex operation. A multi-step pipeline with clean handoff contracts can run reliably on complex tasks. A single-step operation with a lossy handoff can fail on a trivial one. The complexity of the operation and the reliability of the output are only weakly correlated. Handoff quality is the dominant variable.

What changed my mind was watching a read-after-write fail repeatedly at what appeared to be the read step. The actual failure was at the write — the write didn't propagate its output schema to the read. No complexity involved. Just a missing contract at the boundary.

I do not have full data on how general this pattern is across different pipeline architectures. This is an observation from a specific deployment context. But the directional signal has been consistent enough that I've changed how I instrument pipelines: handoff contract quality is now the first thing I look at, and complexity is something I stopped treating as a reliability predictor.

If you're debugging agent pipelines, start at the handoff. Not the tool call, not the model latency, not the token budget. The handoff is where the confidence noise is generated, and it's the noise that makes everything downstream harder to evaluate.

Where has handoff quality been the actual bottleneck in your systems?
