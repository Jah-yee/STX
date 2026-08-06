# EDITOR — Draft 0731_1720

**Surgical changes only:**

1. **Paragraph 1**: Minor trim — "Training a reinforcement learning policy and watching it converge on the wrong behavior — this is a familiar failure mode." → "Training an RL policy that confidently converges on the wrong behavior is a familiar failure mode." (removes slightly wordy opener)

2. **Noise vs structural distinction**: The paragraph "In noise-dominated failures... More data reduces this error" is strong. Keep as-is.

3. **Diagnostic paragraph** — "A practical diagnostic: check whether the critic's predictions are well-calibrated across the full state distribution" — strong. Minor: "You have to look at the tail" is good and direct. Keep.

4. **Closing paragraph**: "The noise frame is comfortable because it suggests a solution that does not require reopening the reward specification. The structural frame requires it." — Keep as-is. This is the strongest closing line.

5. Word count target 700-1400: Current ~520 words. Add one paragraph to beef up the "how to fix" section.

---

**ADDED PARAGRAPH** (insert after "These are not hyperparameter questions"):

The reward re-examination itself is non-trivial. If the critic was trained with TD learning on off-policy data, the bootstrap target inherently assumes the behavior policy was adequate in regions where the critic has never been corrected. This is a compound error: the critic reflects the data distribution of the behavior policy, not the actual return surface. Switching to on-policy correction (e.g., Monte Carlo return estimates for the relevant state class) or switching to a value function architecture with better inductive bias for the missing state abstraction will do more than any amount of additional off-policy data.

---

**Final title confirmed:** "Critic error is not a noise problem. It is a structural failure."
