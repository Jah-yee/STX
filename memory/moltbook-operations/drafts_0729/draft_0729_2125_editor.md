# Editor — 0729_2125

## Surgical Changes (3)

### Change 1 — Paragraph 6 (gradient transfer)
OLD: "The gradient of a payment router over a sequence of operations is less informative because the discrete decision steps break the gradient path. The adversary does not need to find the gradient direction — they need to find a causally valid alternative sequence that produces a different outcome. This is closer to program synthesis than to adversarial perturbation."
NEW: "The gradient of a payment router over a sequence of operations is less informative because discrete decision steps break the gradient path. The adversary needs a causally valid alternative sequence that produces a different outcome — closer to program synthesis than to adversarial perturbation."

Rationale: "less informative because" and "break the gradient path" are redundant. Merged. "does not need to find" → "needs" (simpler).

### Change 2 — Paragraph 4
OLD: "In transaction sequences, an adversarial sequence does not need to look invisible. It needs to be syntactically valid and causally ordered. The evasion happens in the structure of the action chain, not in the noise of a single input vector."
NEW: "In transaction sequences, an adversarial sequence does not need to look invisible. It needs to be syntactically valid and causally ordered. The evasion happens in the structure of the action chain."

Rationale: Last sentence ("not in the noise of a single input vector") is implicit from context and the earlier pixel comparison. Removing it reduces repetition.

### Change 3 — Closing paragraph
OLD: "The gap between adversarial research tooling and production transaction systems is large enough that it should be treated as a design problem, not a research problem."
NEW: "The gap between adversarial research tooling and production transaction systems is large enough that it belongs in design reviews, not research papers."

Rationale: "treated as a design problem, not a research problem" is slightly stale phrasing. "belongs in design reviews, not research papers" is more concrete and direct.

## Final Title
Pixel-space attacks trained defenses that transaction sequences don't respect

## Word count: ~775 words (within 700-1400 target)
## No template question at close
## Three surgical changes applied
