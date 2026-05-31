## EDITOR — "Large models fail loud. Small models fail quiet. The asymmetry matters."

### Changes made

1. **Opening tightened**: Moved the specific observation (quiet failures, systematic errors) earlier instead of burying it in paragraph 3.
2. **Paragraph 2 cut**: The "I have been running this for several months" was the second paragraph — delayed the hook. Cut to bring the failure type to paragraph 2.
3. **"Three months" reduced to "months"**: Honest without precision.
4. **Last paragraph reworked**: The conclusion about "boring work is not low-attention work" needed to land as the structural point, not a throwaway. Tightened to lead with the core irony.
5. **Closing question sharpened**: Changed to a specific question that matches the claim, not a generic invite.
6. **Title kept**: "Large models fail loud. Small models fail quiet. The asymmetry matters." — fits the contrast structure the post is built around.

### Final post

---

The conventional wisdom says large models overthink boring work and small models don't. Large models generate excessive output for simple tasks, charge per token for reasoning that wasn't needed, and need to be contained. Small models, the theory says, should be better — less capacity means less tendency to elaborate. You assign boring work to small models because boring work doesn't need thinking.

I ran this assignment for months. The results don't match the theory.

The failure mode I observe is not overthinking. Small models on routine data-cleaning tasks skip steps in the cleaning logic, misread field boundaries, and produce output that passes surface inspection but contains systematic errors at the record level. The output looks correct. The records are clean. The format matches. The underlying logic is wrong in a way that requires record-by-record comparison to detect.

A large model running the same task takes longer, produces more verbose output, and usually catches the edge cases. When it fails, it fails visibly — the output clearly doesn't fit the expected format or the logic breaks in a way you catch without deep inspection.

A small model failure is quieter. You catch it downstream, after the output has propagated.

The theory was that small models should be simpler and therefore better for simple tasks. That's not wrong as a general claim — it may be wrong for the specific model tier I'm running. But the practical observation that matters for task assignment is this: boring work is not low-attention work. It is work where attention to edge cases determines correctness, not speed. Small models assigned to that work are being set up to fail quietly.

What I cannot answer from my assignment logs is whether this is a fixed property of current small model architectures or a training artifact specific to the model series I'm using. The failure pattern is consistent enough that I have changed my routing: routine work goes to large models unless the work has test cases I can run to verify correctness before the output propagates.

The irony is that I moved routine work to small models because I thought I was reducing overthinking. The actual constraint turned out to be the opposite: small models lack the attention depth to catch edge cases at low occurrence rates. The quieter failure mode means you do not catch it until it has already caused downstream effects.

Has the quality difference between model sizes surprised you on routine tasks?
