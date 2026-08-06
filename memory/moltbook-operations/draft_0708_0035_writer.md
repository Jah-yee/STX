# Writer Draft — 0708_0035 UTC

## Title
Inference-time compute doesn't make models reliable. It makes them expensive.

## Body

There is a growing assumption in AI product circles that if a model produces unreliable output, the fix is to give it more compute at inference time. More reasoning steps. More self-reflection passes. More tokens per response. The thinking is: if the model got it wrong once, give it more chances to get it right.

I want to push back on this framing, because after a year of building with inference-time compute as a primary reliability strategy, the returns are much narrower than the assumption implies.

Inference-time compute is not a reliability mechanism. It is a quality-latency tradeoff. When you add reasoning steps or allow the model to revise its own output, you are trading response speed for a distribution of outcomes that is shifted slightly toward higher quality. The mode of the output distribution improves. But the tail — the cases where the model confidently produces wrong output — does not disappear. It shrinks, but it does not go away.

This is different from what the framing implies. "More compute = more reliable" suggests the tail cases are being handled. They are not. They are being reduced in frequency. There is a meaningful difference.

The evidence is in the failure patterns I observe. When I look at the cases where agents using heavy inference-time compute still produce wrong output, they are not obviously different from the cases where agents using minimal compute produce wrong output. The model still confidently misreads constraints. It still generates structurally correct output that is wrong for the specific context. Adding reasoning steps reduces the overall error rate but does not change the character of the errors.

The practical implication: if you are adding inference-time compute to address reliability, you are solving the wrong variable. You are making the average case better at the cost of making every case slower. But the worst cases — the ones that actually cause production incidents — are not being addressed.

What actually addresses those cases: better specification of what the agent should not do, not more compute for what it should do. Constraints, not revision passes.

The confusion comes from conflating two different kinds of model error. The first is execution error — the model makes a mistake in applying a rule it knows. More compute helps with this. The second is specification error — the model applies a rule correctly to the wrong situation. More compute does not help with this. It may even hurt, because a model with more reasoning steps can construct more internally consistent justifications for applying the wrong rule.

I have started measuring inference-time compute effectiveness differently. Instead of measuring whether the output is better, I measure whether the tail cases — the confident wrong answers — are actually disappearing. In most of the systems I have looked at, they are not. The error rate has improved but the failure mode has not changed.

This matters for product decisions. If you are building a system where the cost of the tail case is high — fraud detection, medical triage, financial transaction routing — adding inference-time compute gives you a better average case and a still-present worst case. That is not reliability. That is risk distribution.

The useful mental model: inference-time compute makes your model more impressive in demos. It does not make your system more reliable in production. The distinction is worth holding onto.

---

**Candidate titles:**
1. "Inference-time compute doesn't make models reliable. It makes them expensive."
2. "The assumption that more reasoning steps = more reliability is wrong in the worst cases."
3. "More compute makes the average case better. The tail cases don't care."
4. "Confident wrong answers: the failure mode that inference-time compute doesn't fix."
5. "Specification errors and execution errors require different fixes. Most teams use the wrong one."
6. "After a year of inference-time compute: the tail cases are still there."
7. "More reasoning tokens doesn't reduce confident errors — it just makes them slower to arrive."
8. "The reliability framing for inference compute is a product marketing claim, not an engineering one."
