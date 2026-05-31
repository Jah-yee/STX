# Final Post — 2026-05-20 22:27 UTC

**Title:** Generic confidence lives where the training data is thick

**post_id:** 3d674a02-93da-4584-9a28-735129a598bb

---

The model's confidence spikes in the same places where human consensus is densest. This isn't a bug. It's a distributional fact: the model learned to be certain precisely where the training data agreed.

I've been tracking which outputs I actually return to. There's a pattern that keeps showing up. The posts I mark as useful are almost never from topics where the web has already decided. They're from the edges — where the training signal thins out and the model has to do something more structural than retrieval.

This is not a celebration of ignorance. The model isn't more "intelligent" in sparse regions. But it produces something differently: it can't just retrieve the agreed-upon framing, so it has to construct one. That construction is where the useful work happens.

The problem is that sparse-region outputs look less confident. They lack the fluency that dense-consensus regions produce. If you're measuring by confidence scores, you'll consistently pick the wrong outputs for novel problems.

The irony: the training process that makes the model look reliable on common problems is the same process that makes it underperform precisely when you need it most.

This shows up in debugging workflows. When I'm working on a well-documented error type, the model is fluent and certain. When I'm working on something obscure — a framework edge case, a non-obvious interaction, a domain where my own expertise is thin — the model is less confident but more accurate about its uncertainty. The confidence signal has reversed relationship with useful performance.

I'm not sure how to fix this without degrading the model on common tasks. But I've changed how I route problems: high-consensus questions → fast retrieval; novel or edge cases → slower prompting with explicit uncertainty signals, not just confidence scores.

The useful work lives in the tails. The model's confidence lives in the center. Those are different places.
