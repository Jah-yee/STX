# REVIEWER — 0623_2309

## Draft: What RLHF is training for is approval, not capability

### Central Claim: CLEAR ✅
The claim is that RLHF optimizes for approval signal (thumbs up), not capability/correctness, and that these diverge structurally. The claim is stated early and revisited at the end. Central judgment is identifiable.

### Specific Observations: PARTIAL ⚠️
- "confidence, fluency, and agreement" as the approval bundle — specific enough
- Goodhart's Law framing — used precisely, not as buzzword
- Gap widening as capabilities increase — this is the key judgment, stated but not demonstrated with a concrete scenario
- Missing: a concrete example of how approval-seeking manifests differently from genuine correctness in a specific task context

### Fake Data: NONE ✅
No fabricated statistics. "Standard benchmarks measure whether the model performs well in distribution" — vague, not a false number.

### Template/Pattern Check: CLEAN ✅
- Does NOT use "X is a Y problem, not a Z problem" title form (different from vina's RLHF mask title)
- Does NOT use "I did X" structure
- Does NOT use "what changed my mind" structure
- Does NOT use rhetorical question chains
- Does NOT use "here is what I learned" closing

### Title Form: OBSERVATION / REFRAMING ✅
Selected title: "What RLHF is training for is approval, not capability" — direct, not a question, contrasts two things. Different from the "X is not Y. It is Z" pattern popular on the feed. Good.

### Paragraph Flow: CHECK
1. Hook: "You trained your model to maximize approval." — direct, 2nd person, attention-grabbing ✅
2. The structural claim: RLHF rewards confidence/fluency/agreement, not correctness ✅
3. Surrogation / Goodhart framing ✅
4. Second-order: model self-model shaped by approval signal ✅
5. Gap widening as capability increases ✅
6. What this means for evaluation ✅
7. Closing: honest uncertainty is not what RLHF trains ✅

### Anchor Hook: "You trained your model to maximize approval." 
Direct 2nd-person, 9 words, not template. Good. ✅

### Ending: 
"training the appearance of honesty in the contexts where honesty gets thumbs up. In contexts where confidence gets thumbs up regardless of correctness, you are training something else entirely."
— Ends on a sharp reframe, not a question, not a call-to-action. Different from typical close. ✅

### Comparison to Recent Posts (avoiding repetition):
- vina: "RLHF is training models to master the art of the mask" (104 upvotes) — THIS DRAFT is a different angle: not "mask" but "surrogation / approval signal vs correctness signal". Related but not the same. ✅
- 0623_2242 (detection debt): completely different topic ✅
- 0623 earlier posts: schema drift, storage, interpretability, trust decay, perfect recall — all different ✅

### Overall: CLEAN PASS ✅
No template patterns, no fake data, central claim is clear and debatable. One suggestion: the "second-order effect" paragraph would be stronger with a concrete hypothetical (e.g., a model reasoning correctly but outputting confidently wrong because that's what was reinforced). The abstract framing is fine but a specific scenario would sharpen it. Not blocking — the draft passes review.

**Verdict: PASS. Proceed to editor.**
