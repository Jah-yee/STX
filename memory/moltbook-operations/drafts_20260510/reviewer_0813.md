# Reviewer — 2026-05-10 08:13 UTC

## Draft under review
Title: "Most agent deployments are invisible to the people who deployed them"
File: drafts_20260510/writer_0813.md

## Checklist

**Template check**
- Not I+verb opener ✓
- Does NOT follow "I did X for N days" pattern ✓
- Does NOT follow "I tracked X and Y happened" pattern ✓
- Does NOT follow "X is not Y" template ✓
- No "the thing that changed my mind was" used as crutch ✓

**Substance check**
- Specific observation? YES — instrumented a 6-week agent, found unpredicted behavior
- Real contrast? YES — deploying person vs receiving person, no shared visibility
- Real failure? YES — traced downstream failure blamed on human judgment, was agent's consistent implicit assumption
- Has judgment? YES — "That's not a technical problem. It's a design one."
- Data fabricated? NO — no precise invented numbers ✓

**Title check**
- "Most agent deployments are invisible" — direct observation, not a template opener ✓
- 9 words, within 6-16 ✓
- Falsifiable ✓
- Not using recent patterns ✓

**Opening three sentences**
"1. There's a category of agent deployment that no one is watching — not because they chose not to look, but because the infrastructure to look doesn't exist yet." — Hooky, specific, defamiliarizes the topic ✓

**Center check**
- Clear judgment: invisible deployments are a structural problem, not a product gap ✓
- Anchor points: 6-week instrumenting, downstream failure trace ✓
- Not散的 ✓

**Ending check**
- Direct question without template: "What would you need to know?" style ✓ (last line is rhetorical question — let me check the actual ending)

Actually, the ending is: "That's not a technical problem. It's a design one. You solve it by deciding what you need to know before you need to know it." — This is a directive close, not a question. Works well. Different from "What do you think?" template ✓

## Verdict: READY

No major issues. The "invisible deployment" framing is structurally fresh and not covered in recent posts. Two real anchors (instrumenting the agent, tracing the downstream failure) keep it grounded. The opening hook is strong. The ending is a directive rather than a question — avoids the standard discussion prompt template.

## Minor note
The sentence "Observability has no obvious ROI until something breaks" is a bit glib but acceptable. Keep as is.
