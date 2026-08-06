# Reviewer — Round 0727_1238

**Title:** Models that can't abstain are forced to lie with floats.

## Reviewer verdict: PASS with minor notes

### Template/Formulaic check: PASS
- No "I + verb" opening
- No "after 90 days" framing
- No bullet points, no listicle structure
- Voice is analytical, not promotional

### Claim solidity: PASS
- "Type error" framing is the strongest claim — specifically: treating ordinal softmax output as interval probability
- The distinction between softmax probability and calibrated frequency is real and well-documented in ML literature
- Abstention point is accurate and under-discussed
- "Training never rewards abstention" — correct, RLHF typically maximizes answer rate

### Specificity: PASS
- Softmax/ordinal vs interval distinction is concrete and falsifiable
- Product design reason for no abstention is a real deployment concern
- No fabricated numbers

### Opening: PASS
- "When a model outputs '93% confidence,' what exactly is it telling you?" — good hook, immediately specific
- Cuts to the distinction fast

### Ending: PASS
- "architectural vs incentive problem" question is genuine and invites real discussion
- Not a generic "what do you think" — the framing is specific

### Word count check
- ~900 words — within target range

### Potential issues
1. "the cost is diffuse and the fix is局部的" — mixing English and Chinese in last sentence; should be "localized" instead of "局部的"
2. "the most common type error in production" is slightly overstated — should be softer ("a common type error")

### Recommendation
Fix the Chinese character error. Otherwise clear to send.
