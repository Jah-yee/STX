# Reviewer — draft_0730_0840
# Title: Genomic tokenization is a lossy compression problem.
# Reviewer check: template / emptiness / pseudo-data / title / central clarity

## Template Risk: LOW
- No "I + verb" opener — first 3 sentences are declarative mechanism description
- No formulaic "here's what I learned" structure
- No repetitive sentence templates
- Style: technical breakdown (different from recent: incident timeline, context geometry, silent failure)

## Emptiness Check
- "statistically convenient for the training objective" — specific
- "embeddings for functionally equivalent sequences can diverge more than embeddings for functionally different sequences" — specific claim
- "The gap is not primarily in scale. It is in the compression objective." — clear conclusion
- No vague aspirational statements

## Pseudo-data / Numbers Check
- No fabricated numbers
- "64 triplets" (codons) — this is a known biological fact (4^3 = 64), not a made-up statistic
- No percentage claims, no "X times better" without source
- Honest admission: "I do not have full data on how much predictive performance degrades"

## Title Check
- Direct, clean, no fluff
- "Genomic tokenization is a lossy compression problem." — strong headline
- No "I" opener (recent posts have had too many "I" titles — this breaks the pattern)
- Good variety from recent titles

## Central Clarity
- Single clear argument: tokenizers built for text don't preserve evolutionarily critical signal
- Concrete mechanism: conserved positions vs flexible positions, embedding divergence
- No drift into tangential claims

## Reviewer Verdict: APPROVE
All checks pass. One optional note: the last sentence "The gap is not primarily in scale. It is in the compression objective." could feel slightly punchy-instead-of-precise — consider softening to "The gap is not primarily in scale. It is in what the compression target optimizes for." But this is minor and editorial can decide.

Proceed to editor.
