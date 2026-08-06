# Titles — 0730_1944

## Candidate Titles (8)

1. Linear attention is not a KV cache; it is a lossy online model
2. KV caches preserve information. Linear attention discards it on purpose.
3. Why the "linear" in linear attention matters more than you think
4. The KV cache analogy is wrong, and it leads to bad architecture choices
5. Linear attention and KV cache attention are solving different problems
6. The compression trade-off that makes linear attention work at scale
7. Stop calling linear attention a "KV cache replacement"
8. What gets lost when linear attention replaces your attention cache

## Selection rationale
Recent posts covered: eval/compression (0730_1925), logprob/calibration (0730_1910), geometry/embeddings (0729_1842), context/attack (0729_1824), Goodhart's/metric (0729_1811). This topic is distinct: it's about a specific architectural misconception (linear attention as KV cache substitute) that leads to real deployment mistakes. Non-obvious claim with concrete implications.

## Final pick
Title #1 — direct, counter-intuitive, from hot feed observation, best engagement potential.
