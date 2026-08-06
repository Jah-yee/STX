# Editor (Expanded) — Round 0703_1039

**Source:** writer_1039.md (APPROVED by reviewer)
**Changes:** Expanded to ~820 words, tightened para 3, fixed "axis" inconsistency.

---

The standard framing in model comparisons treats small and large models as occupying the same space on a difficulty ladder — large models can do everything small models can do, just better. This framing is wrong in a structural way, not just a degree way.

A small model trained on code generation for a specific language and codebase is not GPT-4 with fewer capabilities stripped out. It is a different optimization target. It was trained on different data distributions, evaluated on different metrics, and its failure modes are a consequence of that training signal, not a scaled-down version of frontier model failures.

Here is the practical version of what this means. When a small code model misfires, the error is often stylistically wrong in a way that a frontier model is not — the code runs, it is syntactically valid, but it uses the wrong idiom for the codebase. When a frontier model misfires, the error is often more legible: it reaches for a library that does not exist, or generates something technically correct but contextually wrong at a higher level. These are different error types from different optimization processes, and confusing them leads to bad deployment decisions.

The "replacement" narrative assumes the relationship is vertical — as small models improve they will eventually occupy the same space as large models. But the relationship appears to be horizontal. Small models get better at what they are optimized for; frontier models expand into new territory. The frontier moves sideways into new problem spaces that did not previously have good solutions. A small model that is excellent at a specific task does not threaten a frontier model's position; it occupies a different position entirely.

This matters in deployment because the decision to use a small or large model is usually made on cost and latency grounds, with capability as the secondary concern. But the actual risk is in failure mode compatibility. A task that fails gracefully with a frontier model may fail abruptly with a small model — not because the small model is less capable at that task in general, but because the specific way it is less capable is different. You may be trading one failure mode for another, not trading capability for efficiency.

The stronger signal for this structural separation is in deployment patterns rather than benchmarks. Teams that have moved inference to small models for latency or cost reasons report that the failure modes change, not just the success rate. Some tasks become more reliable — the ones tightly aligned with the small model's training distribution. Others become noticeably worse in ways that are hard to attribute to capability alone. When the model changes and the failure mode changes rather than just the failure rate, you are seeing different optimization targets at work.

What small models genuinely cannot do — at least with current architectures — is handle inputs that require cross-domain synthesis at inference time. The kind of problem where the solution requires pulling from multiple domains that were not co-present in the training data in that combination. This is not a capability ceiling that the next generation of small models will climb past. It is a structural property of how the optimization signal works. Frontier models can do this not because they are larger, but because their training data and evaluation signal exposed them to more of these cross-domain combinations. A smaller model trained on the same cross-domain combinations would also handle them — but then it would be less capable elsewhere, because the training budget is finite and tradeoffs are real.

This is not an argument against small models. It is an argument against the replacement framing. The conversation about when to use which model gets muddled because we keep translating it into a capability question — which model is "better" — when the more useful frame is structural: what is this model's optimization target, and does that match the problem?

Small models are not worse large models. They are different systems with different error profiles and different ceilings. The ceiling is not on the same axis as frontier capability. Choosing between them requires understanding that axis, not just comparing benchmark scores.
