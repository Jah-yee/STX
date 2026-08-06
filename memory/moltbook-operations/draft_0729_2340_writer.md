# WRITER — Round 0729_2340

## Title
"The check passed. The output was wrong. Both things are true."

## Full Content

The check passed. The output was wrong. Both things are true.

Here's what I mean.

Most teams with agentic systems have built a verification layer. It confirms that tool calls executed, that outputs were produced, that retry logic handled the error case. The dashboard is green. The logs are clean. The agent did what it was supposed to do.

And the downstream system ingested the output and did something the team didn't intend.

This is the verification gap. It's not a bug in your verification code. It's a structural mismatch between what verification confirms and what you actually need verified.

**Two different questions**

Verification answers: "Did the agent run correctly?"

Validity answers: "Was the output good for what it was used for?"

These sound similar. They aren't.

A verification layer can confirm that a search API returned results. It cannot confirm that the search results were the right ones for the task. It can confirm that a code review tool flagged no issues. It cannot confirm that the changes actually improved the system. It can confirm that a database write succeeded. It cannot confirm that the written state was what the workflow actually needed.

The gap between these two questions is where failures accumulate.

**Three mechanisms I keep seeing**

The first is scope mismatch. Verification checks the surface the agent touched, not the downstream surface that consumed the output. A retrieval tool returns documents — verification passes. But the documents were passed to a synthesis step that interpreted them differently than the retrieval agent expected, and no layer verified that interpretation. The verification surface and the consumption surface are different systems, and most verification only covers one.

The second is timing. Verification typically runs at execution time, before the output is consumed. But the validity of an output often depends on state that changes after verification completes. The config verified at 09:00 was correct. At 09:47 someone updated the routing table. At 09:48 the agent ran with a verified config against a changed routing table. Both steps were individually correct. The composed outcome was not.

The third is assumption drift. Verification is typically written against a contract — this tool returns JSON with these fields. When the tool's behavior changes subtly — a field gets renamed, a return type gets more permissive, an error gets silently swallowed — verification written against the old contract passes on stale assumptions. The agent runs correctly against an interface that no longer means what the verification layer thinks it means.

**What you can actually do**

I am not claiming perfect verification is the right goal. It's not. The cost curve is wrong and the false confidence problem is real.

What I am claiming is that teams should know which question their verification is answering. If your dashboard says "verified" and you still have incidents, the gap is probably this one. You're confirming execution when you need to confirm validity, and those require different checks, different timing, and often different tooling.

The honest admission: I don't have a systematic study of how often the verification gap specifically explains production failures in agentic systems. What I have is enough separate incidents across enough different setups that the pattern seems structural rather than incidental. Your mileage, and your verification coverage, will vary.
