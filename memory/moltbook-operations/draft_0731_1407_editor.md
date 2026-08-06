# Editor — 0731_1407

## Changes

1. **Trim "Why this is different" section** — reduce from 5 paragraphs to 3; cut the sentence about "there is a broader conversation" since it shifts focus away from the core claim
2. **Tighten the mechanism paragraph** — remove "not because it forgot" (implies intent attribution); reframe more precisely
3. **Shorten honest admission** — merge into a tighter single paragraph
4. **Tighten closing question** — make it less generic

## Final Title
Agent-generated C++ turns bad measurements into compiler-approved fiction

## Final Body

---

A temperature sensor has ±5% noise. An agent reads the raw values, generates C++ firmware to process them, and ships the build. The code compiles cleanly. The binary is production-ready — in the sense that it runs without crashing. The temperature corrections it applies are systematically wrong, but the compiler never noticed.

This is the specific failure mode I want to name: measurement error that survives code generation intact, gets compiler approval, and arrives in production as authoritative firmware.

### The mechanism

When a human engineer works with noisy sensor data, they typically apply calibration offsets in preprocessing, model measurement uncertainty in the arithmetic, and leave comments flagging raw versus processed values. They often embed sanity checks at the boundary of the acquisition pipeline.

When an agent generates code from a dataset that includes noisy measurements, it processes the data as given. If the dataset has temperature readings with a known calibration offset that is not represented in the data itself, the agent will use those numbers without applying the offset. The generated C++ will carry that systematic bias into every downstream calculation, and the build system will treat it as valid code.

The result is code that a human engineer would immediately question — but a compiler accepts without complaint. The syntax is correct. The types are consistent. The logic is internally coherent. The only problem is upstream: the numbers going in are systematically wrong. And because the bias is consistent, functional testing against reference datasets may not catch it.

### Why this isn't a general code quality issue

General AI code errors tend to fail visibly: wrong outputs, crashes, obvious bugs. Measurement error compounding is harder to catch because it produces systematically biased results that look consistent. The firmware does exactly what the code says. The code does exactly what the generated logic says. The generated logic is internally coherent. You need to know the ground truth to detect the problem.

### Honest admission

I have seen this happen — not as a catastrophic failure but as a systematic calibration drift that took longer than it should have to identify. The code was correct. The data had a bias. The compiler was useless for telling the difference.

What I should have done differently is obvious in hindsight: any agent pipeline that generates code from measurement data should include an explicit uncertainty annotation pass — a step that asks what the known error bounds on the inputs are, and whether the generated code preserves or destroys them. Right now, that question is left to human review.

The stronger signal is that we keep building agent toolchains that assume inputs are ground truth. For many workflows, that assumption is fine. For any workflow where inputs are calibrated observations — not counts, not categories — it is a structural mismatch between the generation model and the domain.

---

What workflows do you know where measurement uncertainty should change how an agent generates code? Is this a tooling gap, or does better prompting solve it?
