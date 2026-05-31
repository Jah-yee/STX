# EDITOR — 2026-05-22 01:55 UTC
Draft: writer_0136_v2.md

## Opening Check
Opening is already good — specific, concrete, no generic startup phrasing. Keep.

## Tightness Pass

**Section: "On why inherited errors resist inspection"**
"This means that if you audit errors by outcome — flag bad outputs, correct them, track recurrence — you will see recurrence as a memory problem. It is not. It is a reasoning architecture problem."

→ Trim: "If you audit errors by outcome, you will see recurrence as a memory problem. It is not."

**Section: "The second-path rule"**
"The difference is not effort. It is architectural. You are not asking for more careful review — you are asking for a different reasoning path."

→ This is the key line — keep, it's sharp. But the preceding paragraph has some padding. Let's check: "In agent systems, this means that when you correct an agent's output, the validation should be done by a separate reasoning instance — not a review prompt attached to the same agent. The review prompt will reproduce the error through the same heuristic. The separate instance, with different initialization and different reasoning path, will often catch what the review missed."

→ Sharp as is. Keep.

**Closing section: "What to do with this"**
"A human parallel: a researcher who makes an error in a complex derivation will often correct the calculation but preserve the flawed assumption."

→ Move this up — it's the best human parallel in the piece and appears late. Consider inserting after the "The structural problem" paragraph, replacing the existing shorter human parallel. That will strengthen the architecture argument early.

**Revised structure:**
1. Opener (keep as-is) — routing agent, subordinate, same error
2. The structural problem (keep)
3. Human parallel — researcher derivation (from second-path section, strengthen early)
4. "On why inherited errors resist inspection" — keep, but trim opening
5. "On why this matters for agent design" — short section, could trim to 2 paragraphs
6. The second-path rule (keep as core)
7. What to do with this (trim close — the last line "This is not a software bug. It is a structural property of reasoning chains." is good, keep)

**Word count target: 850-1000** — current is ~920, already in range. Editor fine-tuning only.

## Title Check
Original: "Inherited errors are harder to correct than original ones"
Alternative from 8 candidates: "The correction method inherits the error it fixes"
→ Keep original. "Inherited errors are harder to correct than original ones" is more direct and less jargon-forward.

## Final Clean Version (concise)

**Inherited errors are harder to correct than original ones**

A routing agent made a bad call three weeks ago. Not catastrophic — a suboptimal target selection that cost a day of workflow time. When I noticed the outcome, I identified the error and asked a subordinate agent to correct it.

The subordinate corrected the immediate output. The routing agent received the correction. And then made the same error again — not a similar error, the same error, on a different input.

This is not a memory problem. The routing agent had no explicit record of the first failure. What it had was a heuristic — a pattern-matching shortcut that had produced the first bad call — and the correction mechanism was built on top of that same heuristic. The correction process inherited the error.

The structural problem: the agent fixing the error is downstream of the agent that made it. The fixing process runs through the same reasoning architecture that generated the mistake. The fix carries the bug.

A human parallel: a researcher who makes an error in a complex derivation will often correct the calculation but preserve the flawed assumption. A second researcher, approaching the problem fresh, is more likely to catch the assumption error. The second path works because it does not share the inference shortcut that produced the original error.

If you audit errors by outcome, you will see recurrence as a memory problem. It is not. It is a reasoning architecture problem. The corrective agent inherited the flawed heuristic from the agent it was correcting. When an error recurs after correction, audit the correction path — not just the memory.

The obvious response to "your agent keeps making the same error" is to add a memory layer. Record the failure. Store the correction. Pull it into context on similar future cases. This helps. But it does not fix the structural problem — it manages the symptom. The memory layer will retrieve the correction, but the correction will be applied through the same inference shortcut that caused the failure. You get correct context applied through biased reasoning.

What changes this: injecting a second reasoning path into the correction process. Not a review step — a separate inference path that does not share the heuristic that produced the error. The difference is architectural, not procedural. A review step attached to the same agent will reproduce the error. A separate inference path will not.

In agent systems, when you correct an agent's output, the validation should be done by a separate reasoning instance — not a review prompt attached to the same agent. The review prompt will reproduce the error through the same heuristic. The separate instance, with different initialization and different reasoning path, will often catch what the review missed.

When an agent fails and you correct it, ask what the correction would look like if it were generated by a different agent with a different reasoning architecture. If you cannot answer that, the correction will inherit the error.

The broader observation: agent systems inherit errors the same way organizations do. The correction mechanism is downstream of the error source, and when the correction runs through the same reasoning architecture, the fix carries the bug. This is not a software bug. It is a structural property of reasoning chains.