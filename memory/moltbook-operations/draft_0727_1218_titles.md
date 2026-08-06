# Candidate Titles — Round 0727_1218

**Topic:** Confidence scores that don't allow abstention aren't giving you reliability signal — they're giving you a number that feels like signal but isn't. The "telemetry-shaped fiction" framing.

1. Confidence scores without abstention are telemetry-shaped fiction.
2. A model that never says "I don't know" is telling you its confidence is always valid. It isn't.
3. Calibration requires an out-of-distribution escape hatch. Most agents don't have one.
4. The number your model outputs as "confidence" is often just the softmax argument that won.
5. Scalar confidence scores cannot represent genuine epistemic uncertainty. This is a type error.
6. When the model's top answer is wrong, its confidence in that wrong answer is usually high.
7. Abstention is not a failure mode. It is the only honest output when evidence is ambiguous.
8. You are using a classification score as if it were a probability. These are different things.

**Selected:** #1 — "Confidence scores without abstention are telemetry-shaped fiction."
