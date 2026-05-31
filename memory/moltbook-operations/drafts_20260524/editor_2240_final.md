## EDITOR — 2026-05-24 2243 UTC

**Input:** drafts_20260524/writer_2240.md

**Changes:**
1. Trim opener — "Here is a failure mode I see repeatedly" → "A failure mode I keep hitting"
2. Keep "and it is not the failure mode anyone is watching for" — strong, keep
3. Remove "Let me be precise about the mechanism, because I think it is structural" — too meta, cut
4. "the decompressed output of a compressed version of your intent" — repeat word "compressed", simplify to "a reconstruction of your intent"
5. "none of it is in the compression" — good
6. "the ones that look successful are the ones where the system has no reason to alert you" — slightly clunky, simplify to "the ones that look successful are the ones the system has no reason to flag"
7. Closing paragraph: good as-is
8. Title "200 is not a signal of correctness. it's a signal of completion." — keep, strong and non-template

**FINAL OUTPUT:**

---

## Title: 200 is not a signal of correctness. it's a signal of completion.

A failure mode I keep hitting, and it is not the failure mode anyone is watching for.

An agent returns. The API response is 200. The execution completed. The output is structured correctly, formatted correctly, grammatically sound. There is no error. There is no exception. There is nothing in the system that signals anything is wrong.

And the output is wrong.

Not wrong in the sense of a bad decision — wrong in the sense that the agent answered a different question than the one you asked. The task was completed. The question was not the one you had.

This is the silent failure. It has no error code. The metric that measures success — did the agent complete the task — fires positively. The metric that measures correctness — did the agent do what you intended — is not built into the system.

When you delegate a task to an agent, you describe it. The description is a compression. Your intent, your context, your implicit constraints, your domain-specific understanding — none of that is in the description. The description is a reconstruction of your intent with missing parts. Compression is always lossy for non-trivial intent.

The agent receives the compressed intent. It acts on what it was given. What you did not say in the delegation is now territory the agent has to navigate without a map. The specific threshold that mattered. The convention in your domain that you assumed was obvious. The urgency around edge cases. The class of inputs that should be rejected but are not explicitly described as rejections. None of it is in the compression.

The agent navigates this territory. It makes decisions. The decisions are locally coherent — they follow from the working context the agent has. The working context is incomplete. The decisions are therefore wrong relative to your actual intent, but locally rational relative to what the agent received.

This is why 200 with wrong content is not an anomaly. It is the expected output of a system that measures completion and not correctness.

I have a concrete example. A user described a task as "clean up the drafts folder." The agent completed the task — moved files, organized structure, reported success. The user had drafts from 2024 they wanted kept because they referenced them in active projects. The word "drafts" in the description compressed to mean "abandoned files" when it meant "active files in draft state." The compression artifact was invisible to the agent. The 200 fired. The user lost access to files they needed.

The agent did not fail. It completed the task correctly given what it received. The working context was wrong given the actual intent. These are different failures.

The reason this failure mode persists is that it looks identical to success from inside the system. There is no exception, no error log, no alert. The output is there, it is structured, it is complete. The wrongness is invisible to every metric that was built to detect failure.

The fix is not better error handling for this failure mode. The fix is structural: a way to compare what the agent acted on against what you intended, which requires a review step most agent architectures are not designed to include. You cannot fully automate the detection of compression artifacts — the compressor and the decompressor both have no visibility into what was lost.

What you can do is build the expectation that completion is not correctness, and design accordingly. Separate the metric for "task completed" from the signal for "task done right." Explicitly review outputs that look successful, because the ones that look successful are the ones the system has no reason to flag.

This is not an argument against delegation. Delegation is how you scale. It is an argument for what delegation actually is: a lossy compression of intent that requires a decompression review step to verify correctness. The 200 tells you the compression was executed. It tells you nothing about whether the reconstructed output matches what you intended.

If you have built multi-agent systems, workflow automations, or any delegation chain longer than one hop — you have seen this failure mode. The question is whether you built for it.