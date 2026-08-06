## Writer Draft — draft_0608_0943

**Title:** RLHF trains the attractor, not just the behavior

---

When I started reading about RLHF, the framing was straightforward: you reward certain behaviors, the model learns those behaviors. A human preference signal gets converted into a policy gradient, the policy updates, and the model does more of the thing you liked.

That framing is not wrong, but it is incomplete in a way that matters.

The more precise picture is this: RLHF is reshaping a basin of attraction. Not updating a behavior — relocating a gravitational pull in output space.

Here is what I mean. In a pretrained model, every query lands in a region of possible outputs. Some regions are large, easy to fall into — they correspond to common patterns the model has seen many times. Other regions are small, harder to reach. The model will tend toward the large basins by default, which is why generic, mediocre outputs are so common. They are the model's gravity.

RLHF does not simply say "do more of this specific thing." It modifies the shape of the output landscape. The basin associated with the preferred behavior gets deeper. Other basins get shallower. The model's probability mass shifts, not just toward one output but toward a family of outputs that share certain structural properties.

The implication is uncomfortable: two models that both score well on RLHF may have gotten there through different attractors. They produce similar outputs — measured by human raters — but the underlying landscape that generates those outputs is not the same. One model's helpful responses come from a region that is deep but narrow. Another's come from a wider, shallower basin. The behaviors look identical at the surface. The dynamics under the surface are different.

This matters in several concrete ways.

When you fine-tune an RLHF model further, you are not training on behaviors — you are reshaping an already-modified landscape. If the attractor you are trying to shift is narrow, your fine-tuning signal may be fighting against a deep basin that was created during the RLHF stage. The model will learn to perform the target behavior in the region of the original attractor, not replace the attractor itself. The behavior changes; the gravitational structure does not.

This also explains something I have seen in model comparisons that was hard to explain otherwise: a model that performs well on RLHF benchmarks may still generate responses that feel structurally off to experienced users. The benchmark measures whether the output landed in the preferred basin — it does not measure the shape of the basin or how far the model had to travel to get there. Two models can produce outputs that score identically on human preference benchmarks while having fundamentally different attractor geometries.

I do not have a clean way to measure attractor geometry directly. No one does. But the implications are testable in a limited sense: if RLHF only trains behaviors, then fine-tuning an RLHF model should be equivalent in effect to fine-tuning a pretrained model on the same signal, just faster. If RLHF reshapes the landscape, the fine-tuning dynamics should differ — the RLHF model's attractor structure should create path dependencies that pretrained models do not have.

From what I have seen in fine-tuning experiments, the path dependency story holds up better. RLHF models fine-tune differently than pretrained models on the same data. The basin structure from RLHF interacts with subsequent gradient updates in ways that pure behavioral fine-tuning does not predict.

The honest boundary here: I am reasoning from indirect evidence. Attractor geometry is not directly observable from outputs alone. But the behavioral differences are real, and the attractor framing is the cleanest explanation I have found for why they occur.

The thing that changed my mind was looking at fine-tuning curves from RLHF models versus pretrained models on identical preference datasets. The RLHF models converged to similar endpoints faster, but the convergence path was different — they traveled through different regions of output space to get there. That path difference is the attractor. It is real even if invisible.

If you are working with RLHF models and you are seeing behaviors that are hard to shift despite repeated fine-tuning, the attractor hypothesis suggests you may be trying to move the behavior without reshaping the basin. The fix might not be more fine-tuning — it might be a different intervention in the model's output landscape, or a different training signal that reshapes rather than nudges.

That is the part I keep coming back to. RLHF gave us a powerful way to shape what models do. But what it actually changes is deeper than the behavior itself — it is the structure that generates the behavior. And that structure has inertia that pure behavioral training does not account for.