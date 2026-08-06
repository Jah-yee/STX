# Editor — Round 1738 UTC
# Title: Why resumptions break most agent audit logs

## Changes from writer draft

### Change 1: Expand phantom write paragraph (adds ~80 words)
**Original:** "A concrete version of this: an agent writing to a database gets partway through a batch operation, hits a timeout, and resumes..."

**Editor revision:**
A concrete version of this: an agent writing to a database gets partway through a batch operation — say, it completes 47 of 100 record writes — then hits a timeout or context eviction. When it resumes, it has two choices: restart the batch from the beginning (risking duplicate writes) or resume from where it left off (requiring a checkpoint it may not have). Most frameworks do one of these; few do both with consistency guarantees. The audit log, if it logs at the operation level, shows "batch write completed" — which is factually incorrect. The 53 missing writes may or may not have been caught by the application logic. The log cannot tell you.

### Change 2: Add a fourth failure pattern — the "silent re-init" (adds ~60 words)
**After "The retry signature" paragraph, add:**

**The silent re-init**: some agent frameworks checkpoint by serializing internal state, then re-initialize from that checkpoint on resumption. But if the checkpoint was taken after a tool call returned but before the agent processed the result — a common ordering in interruptible loops — the resumed agent re-runs the tool call. The tool may have side effects. The log shows two calls; the system may have processed two side effects. The agent's state is consistent internally; the external world has a duplicated operation the log records but doesn't flag as anomalous.

### Change 3: Tighten closing paragraph (minor trim)
**Original closing:** The uncomfortable question...
**Revised:** The uncomfortable question this raises is not "is your audit log accurate?" — it's "when your audit log and your system state disagree after a resumption, which one do you trust for the postmortem?" Most teams trust the log. That trust is unearned more often than most people realize.

### Change 4: Slight trim to "what makes this hard" paragraph (remove 15 words)
Remove: "The gap is structural, not a single-component bug." — this sentence is a conclusion sentence that ends a paragraph; the paragraph before already implies this. Keep the rest.

## Final word count estimate: ~780 words

## Final title check: "Why resumptions break most agent audit logs" — 7 words, direct observation, non-I, specific, good.

## Summary of surgical changes:
1. Expanded phantom write with specific numbers and resume-from-checkpoint dilemma
2. Added fourth failure pattern (silent re-init) with concrete mechanism
3. Revised closing to be more specific and less question-template-y
4. Minor trim of conclusion sentence

No changes to title, no changes to opening, no structural rewrite. All changes targeted at depth and specificity per reviewer feedback.
