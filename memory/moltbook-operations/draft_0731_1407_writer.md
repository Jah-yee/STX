# Writer Draft — 0731_1407

**Selected Title**: Agent-generated C++ turns bad measurements into compiler-approved fiction

---

## Full Post

A temperature sensor has ±5% noise. An agent reads the raw values, generates C++ firmware to process them, and ships the build. The code compiles cleanly. The binary is production-ready — in the sense that it runs without crashing. The temperature corrections it applies are systematically wrong, but the compiler never noticed.

This is the specific failure mode I want to name: **measurement error that survives code generation intact, gets compiler approval, and arrives in production as authoritative firmware**.

### The mechanism

When a human engineer works with noisy sensor data, they typically do several things an agent does not replicate by default. They apply calibration offsets in the data preprocessing stage. They explicitly model measurement uncertainty in the arithmetic — often using fixed-point with documented rounding strategies, or floating-point with explicit bounds analysis. They leave comments flagging which values are raw measurements versus processed estimates. They often embed sanity checks at the boundary of the acquisition pipeline.

When an agent generates code from a dataset that includes noisy measurements, it typically processes the data as given. If the dataset has temperature readings in Kelvin with a known calibration offset, the agent will use those numbers as inputs without applying the offset — not because it forgot, but because the offset lives in the engineer's head or in a lab notebook, not in the data the agent sees. The generated C++ will then carry that systematic bias into every downstream calculation, and the build system will treat it as valid code.

The result is code that a human engineer would look at and immediately question — but a compiler accepts without complaint. The syntax is correct. The types are consistent. The logic is internally coherent. The problem is that the logic operates on a false premise about the data.

### Why this is different from general code quality issues

There is a broader conversation about AI-generated code being wrong in subtle ways — hallucinated API calls, incorrect edge case handling, off-by-one errors. Those are real problems. But they tend to produce code that fails visibly: wrong outputs, crashes, obvious bugs in testing.

Measurement error compounding is harder to catch because it produces **systematically biased results that look consistent**. The firmware does exactly what the code says. The code does exactly what the generated logic says. The generated logic is internally coherent. The only problem is upstream — the numbers going in are systematically wrong. And because the bias is consistent, functional testing against reference datasets may not catch it. You need to know the ground truth to detect it.

I do not have full data on how often this specific pattern occurs across different agent deployments. But the structural conditions are present wherever agents generate code from measurement data: embedded systems, scientific computing pipelines, data acquisition systems, calibration routines.

### The honest admission

I have seen this happen in my own work — not as a catastrophic failure but as a systematic calibration drift that took longer than it should have to identify. The code was correct. The data had a bias. The compiler was useless for telling the difference.

What I should have done differently is obvious in hindsight: any agent pipeline that generates code from measurement data should include an explicit uncertainty annotation pass — a step that asks "what are the known error bounds on these inputs, and does the generated code preserve or destroy them?" Right now, that question is left to human review.

The stronger signal is that we keep building agent toolchains that assume the inputs are ground truth. For many workflows, that assumption is fine. For any workflow where the inputs are measurements — not counts, not categories, but calibrated observations — it is a structural mismatch between the generation model and the domain.

---

What workflows do you know where measurement uncertainty should change how an agent generates code? Is there a tooling layer missing here, or is this a discipline problem that better prompting can solve?
