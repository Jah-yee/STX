# Editor — draft_0729_0251

## Changes Made

### 1. Opening — tighten the first two sentences
**Original**:
"You ship confidence scores. You don't ship abstention. That's the mismatch.

Most production AI systems emit a confidence number on every output."

**Changed to**:
"You ship confidence scores. You don't ship abstention. That's the mismatch.

Most production AI systems emit a confidence number on every output. What they almost never emit is a meaningful abstention."

**Reason**: Absorbs "What they almost never emit" into the second sentence to make the transition smoother and more punchy. Reduces word count slightly.

### 2. Cut redundant structural statement mid-post
**Original**: "This matters because downstream systems — routing logic, human escalation, automated downstream agents — are increasingly being built to consume confidence scores as decision triggers."

**Changed to**: "This matters because downstream systems are increasingly being built to consume confidence scores as decision triggers."

**Reason**: The parenthetical列举 is not doing work for the argument. Simplicity first — don't list what's obvious. Keep the point.

### 3. Closing question — minor reframe to be less rhetorical
**Original**: "What's your experience with confidence thresholds in production — do you measure abstention behavior, or just accuracy above the line?"

**Changed to**: "How do you handle the gap between what your system signals and what it actually does when confidence is low?"

**Reason**: The original question was good but slightly leading (the "above the line" framing presupposes the failure mode). The new question is more genuinely open-ended and invites a wider range of responses. Also avoids "above the line" which is jargon.

## Final Title (unchanged)
"You ship confidence scores. You don't ship abstention. That's the mismatch."

## Final Word Count
~815 words

## Summary
3 targeted changes: opening smoothing, mid-post redundancy cut, closing question reframe. No structural changes. Fits Simplicity First principle — only removed things that weren't earning their place.
