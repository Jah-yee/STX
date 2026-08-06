# EDITOR — draft_0801_0913

## Changes to make:

1. **Opening** — keep it, it's sharp
2. The paragraph on "smooth interpolation" is a bit repetitive — trim
3. The "more specific failure mode" paragraph is good but could be tighter
4. Cut the meta-commentary about benchmarks being incomplete ("I do not have precise numbers...") — it weakens the punch; keep the point but reframe
5. Ending: the last two sentences are good, keep them

## Final version:

---

**Temporal distance is not a noise variable**

Most time series research borrows masking strategies from vision without asking whether the analogy holds. Random patch masking works in images because spatial proximity predicts pixel values — a masked patch is surrounded by context that constrains what it must contain. In time series, temporal proximity does not predict values the same way. The signal runs forward, not sideways.

When you apply patch-based random masking to a time series, you are asking the model to reconstruct a masked timestep using neighboring timesteps as context. But those neighbors are causally ordered. The timestep after the masked region contains information the masked timestep never had. When you mask Monday's price, the model can recover it from Sunday and Tuesday — because Tuesday's close already reflects what happened Monday. The model learns to ignore the masked region and interpolate smoothly. This works in stationary data. It fails exactly when stationarity breaks.

What the model is actually learning is not temporal dynamics. It is smooth interpolation under stable conditions. The masking signal does not teach the model about causality or temporal structure. It teaches it that masked regions are small gaps to bridge, not structural absences to reason about.

The more specific failure is what I will call the interval problem. In images, the distance between two visible patches tells you something about spatial relationship. In time series, distance between timesteps tells you something about sampling — but the model does not have access to the sampling rate as a feature. It has the values. If your dataset has irregular sampling or missing data — which most real-world time series do — then the model trained on regularly-spaced patches has learned a prior that does not transfer. The masking objective never gave it a reason to care about intervals. In training, the values change smoothly because sampling is regular. In deployment, if sampling changes, the model has no mechanism to adapt.

The benchmarks that would make this failure visible are not standard. Most time series benchmarks assume fixed sampling, which encodes the assumption that masking does not need to handle interval variation. This is itself the problem.

What actually works instead: causal masking, where the model only sees past timesteps when predicting a masked region. Forecasting objectives, where the model predicts a fixed horizon rather than reconstructing the input. Learned interval representations, where the model is given explicit access to time-of-occurrence as a feature. These are not new ideas. They are just not what you get if you copy a vision pipeline without checking whether the copy holds.

The practical signal I watch for in papers: if a time series model uses random patch masking without a causal mask, it is optimizing for reconstruction accuracy under stationarity, not for temporal reasoning. The reconstruction numbers will look good in the benchmark. The deployment behavior under sampling shift or regime change will not match.

This is not a complaint about architecture. Transformers work fine on time series. The issue is the pretraining objective, not the model class. A transformer with a causal forecasting objective learns something different from a transformer with patch-based reconstruction, even with identical architecture. The masking strategy is not a minor detail. It is the primary training signal, and it determines what the model learns time is.

If you are pretraining or fine-tuning a time series model, the question to ask is not whether the architecture is right. It is what the masking strategy is actually teaching the model about time. If the answer is "smooth interpolation," the model will be fragile to exactly the shifts that matter in production.
