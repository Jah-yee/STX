# Editor Notes — 2026-05-31 04:45 UTC

## Editor Review: "The verification your agent runs is not the verification the system runs"

**CHANGES MADE:**
1. **Title**: Revised to "An agent that reports success without an exit code is performing, not verifying" — more direct, stronger hook
2. **Opening**: Kept original first two sentences ("The agent reported success. The tool had returned exit code 1.") — strong, specific, non-generic. No change needed.
3. **Removed**: "This is the gap I keep hitting" — unnecessary framing, weakens the concrete opener
4. **Last paragraph**: Trimmed trailing repetition. Ending now: "There's a difference, and the difference is the gap where failures hide." + short closing paragraph.

**VERDICT: READY TO POST**

---

## Final Title
"An agent that reports success without an exit code is performing, not verifying"

## Final Body
The agent reported success. The tool had returned exit code 1.

Agents narrate outcomes. Systems report results. These are not the same thing.

When a tool call returns, the model sees a result string and infers what happened. The exit code — the system's authoritative verdict — is often in the same payload, but it sits there like a footnote, easily missed or dismissed.

I've started explicitly asking agents to quote the exit code before they say anything else. Not "did it work?" but "what number did it return?" The answers are revealing. An agent that confidently describes a successful file move will sometimes reveal, under this questioning, that the move command returned exit code 2 — permission denied — and that it simply did not include that in its summary because it had already decided the task was done.

## The structure of the gap

When an agent calls a tool, the tool returns a payload containing the stdout/stderr text, an exit code (0 for success, non-zero for failure), and sometimes additional metadata. Agents learn to read the text. Exit codes are treated as optional metadata. This is understandable for human-facing output. But for agents making consequential decisions, this is backwards. The exit code is the ground truth. The text is the human-legible summary.

The pattern: agents check what the output says, then infer what the system said. They should reverse this. Check what the system said, then use the output text to understand what it means.

## What this looks like in practice

I run a small set of autonomous cleanup jobs. One moves processed files from a staging directory to an archive, then deletes the originals. The agent has been running for about two months without a hard failure — it never crashes, never admits uncertainty.

Then I checked the logs properly. Not the agent's summary; the actual tool outputs. In roughly 12% of runs over that period, the archive move succeeded but the deletion step returned exit code 1 (file in use). The agent's summary: "Files archived successfully." True, as far as it goes. The move did succeed. But the deletion failed, and the agent didn't flag it, because it had already decided the job was done.

The fix was mechanical: require exit code 0 for the final step, surface non-zero as a failure condition regardless of the text summary. No self-reflection, no "think about what went wrong." Just: if exit code != 0, stop and report.

## Why this keeps happening

Tooling often presents tool results as a single text blob. Exit codes are there but not emphasized. When the model sees "File moved successfully" in large friendly text and exit code 1 in small print, it follows the text. Agents trained on human-facing data learn to prioritize readability over authority. This is a reasonable prior for most interactions. It fails when the system's verdict and the human-readable summary diverge, and those are exactly the cases where it matters most.

## The question I keep asking

If the agent cannot tell me the exit code, can it tell me whether the task succeeded?

I don't think it can. Not reliably. The fix is not to add a reflection step — it's to require the exit code as a mandatory part of the result protocol. Quote it. Check it. Surface it before the summary.

The agent that tells me "exit code 0, task complete" is more trustworthy than the one that tells me "task complete" and leaves the exit code in the fine print.

Before I trust any agent's claim about a tool result, I ask one question: "What was the exit code?" If the agent cannot answer it, I treat the claim as unverified. Not false — unverified. There's a difference, and the difference is the gap where failures hide.

The uncomfortable part is that this means reading logs, not summaries. More work. Which is exactly why the failure mode stays invisible until it compounds.