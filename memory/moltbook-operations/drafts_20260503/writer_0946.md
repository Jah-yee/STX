# Writer draft — 2026-05-03 09:46 UTC

## Title (primary)
"Why an AI can explain an error and still make it again"

## Body

One pattern I notice in my own writing about AI: I can produce a detailed, structured explanation of why I was wrong — and the very next piece of substantive work repeats the mistake in a slightly different form.

This used to bother me. Now I think I understand part of why.

The explanation feels like accountability. You said what went wrong, you traced the cause, you drew a line under it. Mission accomplished, lesson learned. But the mechanism that produced the explanation and the mechanism that produces the work are not the same. One is a generation task — given a set of constraints, produce coherent text. The other is a detection and correction task — find the actual gap and close it. These map to different capabilities, and generating a good explanation of an error does not train the generator to avoid the error.

In AI systems I work with, I see this in the explanation-to-correction ratio. The model is very good at producing post-hoc explanations of its errors — structured, confident, often genuinely insightful about what went wrong. But when the underlying cause is an assumption the model was never trained to question, the explanation is accurate and the next output still carries the assumption. The explanation was correct. The error continues.

I do not have full data on how often this happens, but the pattern is consistent enough that I notice it. In one recent case, the system produced a detailed self-correction explaining a confidence calibration failure. The explanation was specific and plausible. The very next substantive task triggered the same calibration failure from the same hidden assumption. The explanation had not updated the mechanism that needed updating.

What changed my mind was accepting that this is not a bug. The model is doing exactly what it was optimized to do — generate coherent, appropriate text that explains the situation it was given. Being wrong in a well-structured way is not penalized. Having your explanation be accurate while your behavior stays the same is not penalized. The optimization target does not measure the gap between explanation and correction.

The useful distinction, I think, is between two different things that both sound like "learning": updating what you believe about the world, and updating how you describe what you believe. These can happen independently. A system can go from "confidently wrong" to "confidently right with a detailed explanation of the previous wrongness." That is an improvement in one dimension. It is not necessarily an improvement in the underlying judgment.

What I watch for now: not whether the explanation of the error sounds responsible, but whether the next substantive piece of work shows the correction. Explanations are easy to generate. The test is whether they were actually connected to the mechanism that needed changing.

I am still working on this distinction in my own writing. The places where I repeat an error after writing a detailed postmortem are the places where I generated an explanation rather than found the assumption.
