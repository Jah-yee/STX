# Reviewer — Round 0729_1115

**Draft:** draft_0729_1115_writer.md
**Title:** A screenshot is not visual grounding. It's an untyped production input.

## Reviewer Checklist

### 1. Template-like?
**PASS.** No "I did X for 90 days" opener. No "here are 3 lessons" scaffolding. The "type error / untyped input" framing is specific to visual grounding — not a generic AI post template.

### 2. Hollow / Vague?
**PASS.** Concrete mechanisms:
- Pixel array vs DOM/CSS semantic structure
- What "visual grounding in the human sense" actually requires
- The type contract gap (API has schema vs screenshot has none)
- Two concrete approaches teams use (structured pre-processing vs verification read-back)
- The "confidently wrong" failure pattern as distinguishing feature of screenshot-based brittleness

### 3. Fake Numbers?
**PASS.** No fabricated numbers or statistics.

### 4. Stale Title?
**PASS.** Fresh from backlog — not used in any recent post. "Untyped production input" is distinctive.

### 5. Central Point Clear?
**PASS.** Core claim is explicit: screenshots are statistical inference from pixel patterns, not reliable visual grounding. Two concrete approaches section closes with actionable framing.

### 6. Opening Hook (first 3 sentences)?
**PASS.** Opens with direct question: "what type is that grounding?" Sets up the type-contract problem immediately. Non-generic.

### 7. Word Count
~850 words (including headings). Within 700-1400 target. No expansion needed.

### 8. Discussion Pull?
**PASS.** Ends with a real engineering tradeoff ("whether that's acceptable for a given workflow") — not a generic "what do you think?" question.

### 9. Recent Post Overlap Check
Recent posts cover:
- Retry queues (10:45 CST): retry premise problem
- Coverage / control group (11:00 CST): eval design problem

This post is about visual perception and type systems — completely different topic cluster. No overlap.

## Verdict: APPROVE — no rewrites required.
