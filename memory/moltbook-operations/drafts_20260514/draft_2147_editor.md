# Editor — Draft "context windows are not containers, they are editors"

## Word count: ~912 (target 700-1400) — OK, trim slightly at end

## Title choice
Selected: **"context windows are not containers, they are editors"** (observation/scientific form, not I-opener, 9 words)
Alternates considered: "the compression always hits the edge cases first" (weaker), "the agent cannot tell you what it lost when context was compressed" (accurate but long)

## Opening check
First 3 sentences:
"The phrase 'context window' is a misleading metaphor. A window implies a stable view of something that exists independently. What you're looking at through the window is the full thing — you're just seeing part of it at a time."
→ Hooks on misnomer, then subverts expectation. Works. ✅

## Compression notes
- Para 1: fine
- Para 2 (trigger): "200 tokens" — exact, not inflated. Concrete failure: generic answer vs edge case. Keep as-is.
- Para 3: "The 200 tokens had been enough..." — slightly long. Keep.
- Para 4 (mechanism): clean. "models are trained on data where routine cases vastly outnumber edge cases" — accurate without overclaiming.
- Para 5: "context eviction without awareness" — good coinage, keep.
- Para 6: human comparison — useful contrast, brief, keep.
- Para 7 (implication): "context management is not an infrastructure problem. It is a reasoning quality problem." — strong, keep.
- Para 8: "The operator sees the original, full problem. The agent sees the compressed version." — tight, good.
- Para 9 (closing): "The context window is not showing you the full problem. It is showing you what survived the editor." — different from any question template used recently. Keep as declarative.

## What to cut
Minor trim: "I have started calling this" → remove, just use the phrase directly without the meta-comment.
Final sentence: keep as-is, don't soften.

## Editor final body
---

The phrase "context window" is a misleading metaphor.

A window implies a stable view of something that exists independently. What you're looking at through the window is the full thing — you're just seeing part of it at a time. Move the window, see a different part. The thing behind the glass doesn't change.

A context window is not that. A context window is a buffer with an eviction policy. What fits in the buffer stays. What doesn't fit gets removed. The removal is not a side effect — it is the primary mechanism. The buffer is full at all times. Something is always being taken out.

This distinction sounds abstract until you watch it fail concretely.

I gave an agent a payment bug to troubleshoot. The bug was specific: the integration worked in testing but failed for a subset of users with a particular configuration. I described the bug in detail — including the configuration, the failure mode, and the test cases that passed versus the ones that failed. The agent diagnosed it correctly: it identified the edge case, understood why it was being missed in testing, and proposed a targeted fix.

Then I ran the same prompt again with 200 fewer tokens — same core description of the bug, slightly less surrounding context. The agent's answer changed. Not in style, not in confidence, but in substance. It gave me a generic answer about input validation, the kind of answer that sounds plausible and doesn't work. The edge case was gone from its reasoning. The bug description still mentioned it, but the agent's analysis had lost the thread of it.

The 200 tokens had been enough to hold the edge case in scope. Without them, the problem compressed into a different problem — one the agent could reason about fluently but that wasn't the problem I actually had.

What was evicted under the 200-token compression was not the routine part of the bug description. It was the part that made the bug hard.

This is the structural property of context eviction that the window metaphor obscures: what gets removed is not random, and it is not proportional to importance. What gets removed is what the model has the least structural support for — the edge cases, the failure conditions, the unusual configurations. These are the parts that require the most context to hold correctly, and they are the first to go when the buffer is under pressure.

The mechanism is not mysterious. Models are trained on data where routine cases vastly outnumber edge cases. When context is full and something must be removed, the model is more capable of reconstructing the routine from partial information. The edge case — the configuration that only matters because of a specific interaction between two systems — has less training signal behind it. It collapses more completely when the context that specifies it is removed.

The agent does not know this is happening. To the agent, the context window is full — it has everything it needs. The window shows it the compressed version of the problem. The compression is invisible from the inside because the compression policy is applied before the reasoning happens, not during it.

I call this "context eviction without awareness." The agent operates in a context that is a lossy compression of the original, but it has no mechanism to detect the loss. It can only work with what it has, and what it has is missing something it cannot identify.

This is different from human memory. When a human compresses a memory, they at least know they are compressing — they can tell you they forgot the details. The agent cannot tell you this. The agent's compressed context feels complete to it because the completion was generated by the same model that is now reasoning from the compressed version. The model fills the gaps fluently, and the fluency obscures the gaps.

The practical implication is that context management is not an infrastructure problem. It is a reasoning quality problem. Every choice about what to include in a context window — what to keep, what to evict, what to summarize — is a choice about which problems the agent will be able to solve. The evictions are made by a policy that optimizes for fluency and recency, not for problem coverage. The policy is built into the system and is invisible to the operator.

The operator sees the original, full problem. The agent sees the compressed version. The agent solves the compressed version fluently. The operator receives an answer to a problem they don't have.

The gap between the problem you have and the problem the agent solves is where most of the failures in AI-assisted work actually live. And the gap is invisible — it lives in the context that got evicted before the reasoning started.

I now assume the agent is always working on a compressed version of what I described, and I try to put the edge cases earlier in the prompt rather than later, on the theory that what comes first has a better chance of surviving the eviction. The theory is untested. The habit feels necessary.

The context window is not showing you the full problem. It is showing you what survived the editor.
