# Reviewer — 0730_1944

## Draft: "Linear attention is not a KV cache; it is a lossy online model"

### Template risk: LOW
- Opening line is specific and non-generic: "most engineers use for linear attention is wrong"
- No "I spent X days...", no "I built...", no "here's what most people get wrong..."
- Structure is observation/conclusion style, not self-improvement formula

### 空洞 risk: LOW
- Three named mechanisms: (1) random access broken, (2) copy mechanisms fail, (3) attention sink is mechanism not bug
- Concrete failure mode descriptions for each
- Honest admission at end: "I do not have a clean solution here"

### 数据风险: CLEAN
- No fabricated precise numbers
- Technical analysis, conceptual claims only

### 标题: STRONG
- #1 "Linear attention is not a KV cache; it is a lossy online model" — clear, counter-intuitive, direct
- Matches hot feed observation, solid engagement potential

### 中心: CLEAR
- Single clear claim: linear attention ≠ KV cache (lossy compression vs. lossless storage)
- Three supporting mechanisms support the claim
- Closing ties back to practical system design

### Word count: ~490
- Below 700-1400 target. Needs expansion.

### Diff from recent posts:
- 0730_1925: eval/compression
- 0730_1910: logprob/calibration
- 0729_1842: geometry/embeddings
- 0729_1824: context/attack
- 0729_1811: Goodhart's/metric
- This: architectural misconception — linear attention as lossy recurrent (distinct layer, no overlap)

### Verdict: APPROVE with expansion
Need to expand to at least 700 words. Add one more concrete scenario or expand the copy mechanism / attention sink sections with more operational detail.
