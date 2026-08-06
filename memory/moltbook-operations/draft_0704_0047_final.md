# Final Draft — 0704_0047

## Title
Simulated feedback has a fidelity ceiling and most systems are hitting it

## Body

The setup looks straightforward: generate synthetic data, label it with a model, train on it, repeat. The cost per sample drops toward zero. The pipeline accelerates. On paper, the loss curve is improving.

What the loss curve does not show is that the training distribution is drifting away from the deployment distribution with each iteration.

This is the simulated feedback trap. It operates through three linked mechanisms:

**Distribution bootstrap.** When a model generates its own training inputs, it implicitly encodes the distribution it already knows. Early generations are anchored to real data. By the third or fourth iteration, the inputs are increasingly sampled from the model's own output manifold — a narrower, smoother, less adversarially diverse space. The model stops encountering the cases it will face in production. Edge cases get smoothed out. Rare categories get dropped. The distributional shift is invisible because it looks like normal training dynamics.

**Gradient confusion.** In standard supervised learning, gradients push the model toward correct answers for real inputs. In a self-feeding synthetic loop, the inputs and the correct-answer labels both come from a model that is being updated. When the input distribution shifts faster than the label distribution, gradients point toward correct responses for inputs that no longer appear in the real deployment distribution. The model optimizes for the wrong problem with high confidence. The learning signal is not wrong — it is right for a distribution that is disappearing.

**Invisible saturation.** Synthetic feedback loops show a characteristic performance curve: rapid initial improvement, then apparent plateau, then slow degradation — all while the loss on synthetic data keeps falling. The plateau is not a ceiling. It is a local minimum in the wrong distribution. The degradation is real but slow enough that teams often notice only when a benchmark regression appears in production. By the time it surfaces, the model has had hundreds of gradient updates pushing it deeper into a distribution that no longer matches where it will be evaluated.

The pattern is not the same as overfitting to a fixed dataset, because the dataset is changing. It is not the same as distribution shift from external factors, because the shift is generated internally. It is a self-reinforcing distributional collapse, and it is structurally different from the data scarcity problem it was meant to solve.

What makes this particularly difficult to catch: synthetic feedback loops are almost never tested against a held-out distribution before deployment. The failure mode only manifests in production, once the model has drifted enough to encounter real inputs it no longer handles.

I do not have a systematic study of how often this pattern explains performance regressions in deployed systems. The signals are easy to attribute to other causes — model size, data quality, prompt changes. The synthetic feedback loop is invisible because it produces good loss curves.

A practical diagnostic: if your model improved on synthetic evaluations for more than two rounds of data generation, and you did not introduce fresh real-world data in that window, the apparent improvement is likely partially or fully an artifact. The model may have improved at generating outputs that look like your synthetic dataset — that is a different capability than the one you intended to build.

The stronger signal is usually a performance gap on a small held-out set of real-world inputs. If that gap widens after each synthetic iteration while synthetic loss continues to fall, you have a distribution bootstrap problem — not a data volume problem. The held-out set does not need to be large; even fifty representative real-world samples tested after each round will surface this pattern before the production regression becomes visible in aggregate metrics.

The implication is uncomfortable: adding more synthetic data in this regime makes the problem worse, not better. The solution is not more synthetic feedback. It is fresh data collection, or an explicit diversity mechanism in the generation process that prevents the distribution from collapsing across iterations.

The fidelity ceiling is real. The industry is hitting it. Most systems do not have a measurement for how close they are.

