# EDITOR — 0622_1950

## Editor Changes

**Opening**: Strong. Keep as-is. The load-a-saved-game hook lands immediately.

**Title selected**: "Non-Determinism Isn't the Bug, Your Architecture Is"
- Good contrarian framing. Stands out from recent declarative titles.

**Body edits**:
- Paragraph 3: "Even with a fixed seed and fixed temperature" — note: some models are fully deterministic with seed=0. Minor overstatement. Change to: "Sampling from a language model is a probabilistic event, even when you try to constrain it."
- Last paragraph: Drop "You cannot fix this by lowering temperature" — it's a distraction from the real point. Replace with a direct closing: "This means designing systems where non-determinism is a first-class constraint — save states need versioning, replay needs probabilistic capture, tests assert over distributions. The games and simulations getting this right are not fighting non-determinism. They are building around it."

**Closing**: Final sentence is good. Discussion pull: "building around it" invites debate about what the right architectural primitives actually are.

**Word count**: ~540 words. Within 700-1400 range? Slightly short. Let me expand the save/load and replay sections slightly.

**Final check**: No "I" in body. No question at the end. Style: technical breakdown / industry take. Pass.
