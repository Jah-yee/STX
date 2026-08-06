# Candidate Titles — 0703_0542 UTC
# Topic: GPU compute bottleneck framing — the network/interconnect is the hidden constraint

1. GPU compute gets the attention. The network is what fails first.
2. The bottleneck in your AI pipeline is not the GPU. It is the highway between them.
3. Bandwidth is the load-bearing constraint in distributed AI inference.
4. GPU utilization is a proxy metric. Bandwidth utilization is what kills production.
5. When your GPU cluster saturates, the problem usually lives one hop away.
6. Networks fail louder than GPUs do. That is why we notice the wrong one.
7. Why does a GPU cluster achieve 30% compute utilization? Because the network is the bottleneck.
8. The inter-GPU network is infrastructure, not plumbing — and it has different failure modes.

# Selected: #3 — "Bandwidth is the load-bearing constraint in distributed AI inference."
# Rationale: Direct, specific, distinct from "GPU is engine" analogy (which we avoid for this post).
# Avoids "X is not Y" pattern heavily used recently.
