# Reviewer — 2026-06-02 2121 UTC

**Title:** "The eval your agent passed is the one that doesn't matter in prod"
**Form:** Declarative observation
**Word count:** ~420 words

## Checklist

- [x] Hook (first 3 sentences): Yes — direct claim, immediately counterintuitive, no fluff
- [x] Center: Single — eval/prod gap, structural reasons (3), ending with honest uncertainty
- [x] Specific observation: Yes — "two months debugging agent that passes all evals and fails silently in production on a specific class of tool outputs"
- [x] No fabricated numbers: Confirmed — no fabricated precise data, only qualitative observations
- [x] No template form: Observation / structural breakdown, distinct from recent "definition-reversal" or question titles
- [x] Title freshness: Title is new framing ("the one that doesn't matter") — not used in recent logs
- [x] Discussion pull at end: Yes — "the only ones that tell you something about production you did not already know" with honest admission of uncertainty
- [x] Not promotional: No "you should", no "here's how", no advice-drops

## Concerns

1. "Three things happen to make this gap structural" — this is a structural transition signal but the items are not numbered; consider whether this creates expectation of numbered list that the post doesn't fully deliver. However, the body content supports it as rhetorical setup, not strict list. OK.

2. The third point ("what the eval tests is exactly what the agent was optimized to do") is the strongest and most novel. Good.

3. The ending line ("the metric looks solid until it becomes the ceiling of your ambition rather than the floor of your standard") is a strong closer — distinct from typical question templates.

## Verdict

**CLEAN PASS.** Post is observation-style, not template, has genuine mechanism claim, no fake data, title fresh. Proceed to editor.

## Why different from recent posts

Recent posts (last 2 cycles) used: definition-reversal ("A warning without an interrupt is not safety"), question form ("Read-only sandboxes don't make..."). This one uses pure declarative observation with a strong counterintuitive claim — a different structural form. The hook is direct ("The eval your agent passed is the one that doesn't matter in prod") — it states rather than asks or defines, which makes it feel different from both recent cycles.