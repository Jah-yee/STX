# Writer Draft — 2026-08-02 20:00 UTC

**Selected title:** The coverage guarantee holds. The world doesn't.

---

I used to think conformal prediction solved the calibration problem for production models.

The setup is clean: you calibrate on historical data, you get a prediction interval that should contain the true value with probability ~90%, and you ship it. The guarantee is distribution-free — it doesn't assume your data is Gaussian or that your model is well-specified. It just requires exchangeability, which felt like a low bar.

Then I watched one of these predictors run in an agentic loop.

What changed my mind wasn't a math error. It was the feedback loop. The agent takes an action based on the model's output. That action changes the world. The model's next prediction is on the changed world. But the calibration — the exchangeability assumption — was computed on the world before the agent started acting.

Conformal prediction assumes the training and test data are exchangeable. In a static benchmark, that's a reasonable assumption: same distribution, different samples. In an agentic loop, it's violated at prediction time. The test distribution includes the agent's own outputs as inputs. You're measuring coverage on a world the model partially constructed.

This matters for the coverage guarantee specifically. If the agent's actions are uncorrelated with the residual error — if the errors are still exchangeable with the training residuals — then coverage should still hold. I don't have full data on how often that assumption actually holds in practice. But when the agent's actions are directly coupled to the quantities being predicted — when predicting the state is what causes the state to change — the assumption is strained.

The practical consequence hit me when I realized you can't actually verify coverage in this setup. Coverage requires observing the true label. But in an agentic loop, the true label is partly a function of the action the agent took. You never observe the counterfactual — what would have happened if the agent had acted differently. So you can't compute whether your prediction interval contained the true value, because the true value was downstream of your prediction.

This doesn't mean conformal prediction is wrong. It's correct under its assumptions. The assumptions are what I'm flagging. The i.i.d. assumption is violated by the thing you're measuring.

What I do know is that when I look at production systems using conformal prediction as a trust signal — "the model says X and we're 90% confident the true value is in this interval, so we're comfortable proceeding" — that comfort assumes a world that doesn't change as a consequence of the model's predictions. Agentic systems violate that by design.

The honest heuristic I've arrived at: don't treat coverage as a property of your model's trustworthiness in an agentic loop. Treat it as a property of your model's performance in a stationary world. If your world is stationary, conformal prediction is one of the more principled tools available. If your world is changing because your model is changing it, the guarantee holds on a distribution you no longer have.

The question worth asking isn't "is our model calibrated?" It's "is our uncertainty estimate responsive to the distributional shift we're actually creating?" Those are different questions. The first has a clean answer. The second is where the actual risk lives.
