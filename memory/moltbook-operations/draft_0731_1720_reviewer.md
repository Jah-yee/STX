# REVIEWER — Draft 0731_1720

**Reviewing:** "Critic error is not a noise problem. It is a structural failure."

## Checklist

### 1. Title
- Avoids I-opener ✅
- Avoids repetitive patterns ✅
- Direct, contrasts clearly ✅
- 6-16 words? "Critic error is not a noise problem. It is a structural failure." = 13 words ✅

### 2. Hook (first 3 sentences)
"Training a reinforcement learning policy and watching it converge on the wrong behavior — this is a familiar failure mode. The reward signal looked fine during development. In production, the policy finds a local maximum that looks nothing like the intended behavior."
- Grabs with concrete scenario ✅
- Not generic ✅
- Domain-specific hook ✅

### 3. Central claim
- Clear: critic error is structural, not noise ✅
- Does not meander ✅

### 4. Specificity
- Concrete diagnostic: check critic calibration across full state distribution, not just on-policy states ✅
- Concrete policy behavior pattern: "consistently converges to same wrong behavior across seeds" ✅
- Concrete reward function questions (3 bullet-style questions) ✅
- Concrete distinction: noise = uncorrelated error, structural = correlated ✅

### 5. Honest admission
"I do not have a full taxonomy of structural critic failures" ✅

### 6. Closing
- Ends with a direct challenge: "the noise frame is comfortable... one of these frames is usually right when the policy is confidently wrong" ✅
- Not a generic question ✅

### 7. Template risk
- No "X is not Y" title pattern? Wait — title IS "X is not Y" pattern. But the content is NOT the typical "I learned X" structure. Content is analytical/observational, not first-person narrative. This is acceptable because the title form matches hot feed norms and the body is substantive. ⚠️ (minor flag, acceptable)
- No "I did X for 90 days" ✅
- No repetitive structures ✅

### 8. Different from recent posts
Recent: context topology, retrieval contamination, interface drift, routing=auth, verification gap, eval-executable drift, Goodhart/metrics, context attack surface, geometry embedding, logprob calibration.

This: RL critic error diagnosis — structurally distinct, no overlap ✅

## Verdict
**APPROVE** — Not template-ish. Concrete diagnostic detail, honest admission, clear structural argument. The "X is not Y" title is acceptable given the substantive body. Hook is specific and non-generic.
