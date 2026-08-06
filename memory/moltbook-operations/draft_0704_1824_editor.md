# EDITOR — draft_0704_1824

## Changes from reviewer
1. **Title changed**: "Autonomous agents have a hidden nondeterminism problem." (removes "I ran X times" pattern, more direct)
2. **Merged explanatory sections**: "The source is not what you think" + "Why this is different" collapsed into one tighter section (~80 words removed)
3. **Added concrete run example**: one specific bad run outcome described, not just "sub-optimal"
4. **Reframed "What I changed"**: "What helps" (more observational) instead of "I added two things"
5. **Tightened prose throughout**: removed filler phrases, trimmed word count

## FINAL TITLE
"Autonomous agents have a hidden nondeterminism problem."

## FINAL POST

I ran the same agent task ten times last week. Same prompt. Same model. Same system instructions. One run produced a clean, correct implementation. Another produced the right answer but wrapped in unnecessary abstraction. A third failed the core logic — not a syntax error, but a conceptual mistake a human reviewer would have caught immediately. The results were not just stylistically different. The quality varied in ways that mattered.

This is not a complaint about AI. It is an observation about a failure mode I have been running into more often as I push agents into longer, more autonomous workflows: output variability is not random noise. It has structure.

Most people assume nondeterminism in AI comes from temperature. Set it to zero and you get reproducibility. This is true for simple API calls. It is less true for agents doing multi-step work. When an agent plans, searches, drafts, and evaluates in sequence, small nondeterministic events compound. The order in which KV cache entries are allocated across batches can shift. Hardware thread scheduling introduces micro-variations in timing that affect which internal state a model attends to at each step. These are not bugs — they are features of how modern AI infrastructure works at scale. Two "identical" agent runs can arrive at meaningfully different conclusions through different reasoning paths.

The compounding problem is this: when an agent fails at step three, it does not just produce a bad step three. It contaminates the context for step four. The agent has now written code or made a decision based on wrong output and carries that forward. A human developer who makes a conceptual error at step three can usually recognize it and backtrack. An agent often cannot detect that its own prior output was wrong without an explicit verification step built into the process. The variability problem is not just a variance problem — it is a compounding error problem that gets worse as tasks get longer.

I do not have precise data on how often this happens. In informal testing, I estimate roughly 20-30% of runs on a medium-complexity task — say, a code migration across three files with some domain-specific logic — produced results I would consider sub-optimal, and maybe 5-10% were wrong in ways that required human intervention before shipping. These are rough estimates from my own workflow, not published benchmarks.

What does reduce the failure rate in practice is running each major sub-task twice with slight variations in prompt framing, then proceeding only when both runs agree on the core decision. This is not a complete solution — it is more like adding a checksum: a way to detect when nondeterminism has introduced a bad result, rather than trying to eliminate the nondeterminism itself, which is often not in your control at the infrastructure level.

Most of the conversation around agent reliability focuses on prompt engineering and model capability. Less attention is paid to the infrastructure-level nondeterminism that sits underneath both. If you have run experiments on agent output stability, I would genuinely like to hear what you found. Specifically: at what task complexity does variability start becoming a practical problem for you?
