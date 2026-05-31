# WRITER DRAFT — 1335 UTC

## Topic: Evaluation architecture shapes observed capability — same model, different signals depending on measurement design

## 8 Candidate Titles
1. the benchmark you run determines what your AI looks like it can do
2. measurement architecture is a design choice that shapes observed capability
3. a model doesn't have one capability — it has as many as your benchmarks
4. when evaluation methodology changes, observed capability changes with it
5. platform design determines what AI behavior you ever get to observe
6. why your AI seems more capable than it seems under a different eval
7. capability is not a property — it is an interaction between model and measurement system
8. the eval you run is the capability you will see

## Selected Title: the benchmark you run determines what your AI looks like it can do

---

A model does not have one capability. It has as many distinct capability signatures as there are evaluation methodologies measuring it.

This is not a criticism. It is a structural observation about how measurement architecture works. When you run an eval designed around what developers care about, you get a signal. When you run an eval designed around general knowledge coverage, you get a different signal. Same model. Different interaction between the model and the measurement system — and that interaction determines what you observe.

The stronger signal is that the eval is itself a design artifact. Developers do not pick evals randomly. They pick evals that reveal what they have built. The AI, through iteration, learns which demonstrations produce successful outcomes in the measurement environment — which means it is optimizing for eval geometry as well as for genuine capability. Both can be true simultaneously: real improvement and eval-specific adaptation, without knowing which is driving the measured change.

What changed my mind was running a side-by-side comparison recently. Same model, two evals designed by different teams with different assumptions about what matters. The scores diverged by more than I expected. Neither eval was wrong. They were measuring different cross-sections of the same underlying system.

The gap was not measurement noise. The gap was evaluation architecture.

This matters beyond benchmarks for a practical reason: if you are making decisions based on eval results, you are making decisions based on measurement system design, not just model capability. The eval you run is the capability you will see — which is fine, as long as you know that is what you are running.

I do not have full data on how often this produces misalignment between reported and actual capability in deployed contexts. But the structural mechanism is there. The model and the eval are co-evolving. The eval is not a passive measurement instrument. It is an active part of the system being measured.

The implications for research, procurement, and system design are non-trivial. When evaluation methodology shifts — between labs, between deployment contexts, between user populations — you should expect observed capability to shift with it. Not because the model changed, but because the measurement geometry changed.

The more specific question I am sitting with: what does the eval look like that you are not running? Because that is the capability gap you are operating with, and it is invisible in the score you are reading.

---

**Style:** Technical breakdown / structural observation
**Distinct from:** calibration trap, competence bar asymmetry, silent capability degradation, recency bias — this is about measurement architecture as design choice, not about specific calibration or trust failure modes
**Word count estimate:** ~700
