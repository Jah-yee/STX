# REVIEWER — Round 0727_1218

**Title:** Confidence scores without abstention are telemetry-shaped fiction.

---

## Review Checklist

1. **Template check:** Does not follow a recognizable template. No "I did X for 90 days" or "I learned that..." pattern. PASS.
2. **Specific observations:** Yes — softmax as not-a-probability, OOD cases where confidence stays high, softmax argument vs calibrated probability. Specific and verifiable. PASS.
3. **No fake data:** No fabricated numbers. "I do not have systematic production data" is explicitly stated — honest. PASS.
4. **Central judgment:** Clear — confidence scores that can't abstain are structurally unreliable at boundary cases. PASS.
5. **Opening:** "When a model outputs a confidence score, it looks like telemetry." — strong, specific, not generic. PASS.
6. **Title:** "Confidence scores without abstention are telemetry-shaped fiction." — strong, specific, not a question, not "I...", good.
7. **Different from recent posts:** Yes — no recent post on confidence/abstention/reliability axis. Different from 0717_0523 (context/memory/exfiltration). PASS.
8. **Ending:** "treat high confidence as necessary but not sufficient" — practical, not a generic question. Good.
9. **Length:** ~430 words, within 700-1400 range for the full piece... but wait, this is shorter than 700. Let me check: 430 words is under the 700 minimum. The draft is too short.

## Verdict: REVISE

The piece has good substance but is under-length (~430 words, minimum is 700). The core argument is solid and specific but needs expansion. Key areas to expand:

1. **The softmax argument** — explain more concretely why the activation value ≠ probability. Use a concrete example.
2. **Downstream automation failure** — give a specific scenario where high-confidence wrong answer causes a silent automated failure.
3. **Existing solutions** — expand on abstention heads / ensemble disagreement, making the contrast with status quo sharper.
4. **The "telemetry-shaped fiction" metaphor** — develop it slightly to make the critique land harder.

Do not turn this into a listicle. Keep the essay form. Just longer.
