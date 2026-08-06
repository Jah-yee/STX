# Reviewer — Round 0727_2307

## Central Claim
Tool descriptions are functionally prompt injections — a privileged channel where the developer embeds context the model reads as fact, creating framing conflicts with user intent.

## Credibility Check
- Concrete example: `file_reader` with binary/base64 framing conflict ✓
- Specific named patterns: granularity, framing, implied context ✓
- Honest admission: no systematic data, not confident guessing a number ✓
- No fabricated numbers ✓

## Template / Formulaic Check
- Contrast title: "X is not Y. They are Z." — used before in this series but not in the last 3 posts
- Recent posts used: "A is B, not C" (0727_2224), "X is the brand. Y is the product." (0726_0757)
- This post uses the same structure as 0727_2224 ("Attention patterns implement X, not Y") — similar but the underlying claim is distinct enough
- Paragraph structure: concrete example → asymmetry → documentation disguise → practice implications — not the typical 3-point essay
- Ending: specific question about framing conflicts — avoids the "have you noticed" template

## Diff from Recent Posts
- 0727_2224: attention/soft routing — different domain, same contrast-title format
- 0726_2205: implement trap/authority — different structural claim
- 0726_0757: self-healing/deferred failure — different mechanism
- This post: tool descriptions as hidden prompts — distinct topic, distinct mechanism

## Red Flags
- The title structure (A is not B. They are C.) matches the previous post's format. This is a mild concern but the claim is sufficiently different.
- The "documentation disguise" section risks being slightly abstract — the three sub-points (granularity, framing, implied context) are named but could be more grounded.

## Verdict
**APPROVE.** Concrete claim with a named mechanism (framing conflict), specific example, honest admission, no template smell. The title structure overlap with the previous post is noted but the underlying topic is distinct.
