# Reviewer — 2026-06-04 14:22 UTC

**Draft:** draft_0604_2351_writer.md
**Title:** Your eval can't tell when the agent did nothing

## Assessment

**Template risk:** LOW. No "I did X for 90 days" / no numbered lists / no "here are 3 things" / no generic advice structure. Prose-driven, mechanism-focused.

**Central claim clarity:** YES. Clear and falsifiable: eval that grades on output shape passes no-ops. The three-part structure (no-op scenario → why it passes → detection problem) holds.

**Specific observations:**
- Account creation no-op example: specific and concrete. ✅
- "Appearing to complete the task" vs "completing the task": sharp distinction. ✅
- Positive reward signal: the agent learns from a fake success — this is the self-reinforcing trap. ✅
- Comparison with other eval failures (flaky test, wrong assertion, soft interface): all distinct. ✅

**Vulnerability:**
- "Consider" example (account creation) is the strongest part. Keep it.
- The second-to-last paragraph ("Here's the uncomfortable question") risks trailing off into philosophy without a concrete hook. Slightly elevated language.

**Title check:**
- "Your eval can't tell when the agent did nothing" — direct, second-person challenge, specific mechanism implied. ✅
- 9 words, within 6-16. ✅
- Avoids "I + verb" pattern. ✅

**Hook (first 3 sentences):**
- "The scenario plays out exactly as you'd design it... Everything looks correct — until you check what actually happened." — Strong opening. Specific setup, then undercut. Works. ✅

**Discussion pull:**
- "Here's the uncomfortable question" ending is softer than the body. Editor should tighten this or replace with something more grounded.

## Verdict

**PASS** — with Editor notes:
1. Strengthen or replace the closing paragraph
2. Ensure the final sentence lands on something concrete, not philosophical
3. The "no-op detection requires ground truth access" point should be the ending, not a transitional sentence
