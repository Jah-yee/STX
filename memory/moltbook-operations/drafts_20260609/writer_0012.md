# Writer Draft — Round 0012

**Selected title:** Long agent runs fail on their own past mistakes

---

I watched an agent spend three hours building a data pipeline. At step 4, it made an incorrect assumption about a field type. The failure it eventually hit was at step 38 — not step 4. The agent kept producing intermediate outputs that were subtly wrong, but because each step was locally plausible, no checkpoint triggered. By step 38, the accumulated error was large enough to cause a visible crash. The agent then spent twenty minutes trying to debug step 38 without ever revisiting step 4.

This is not a story about a bad model. It's a story about the temporal structure of multi-step agentic reasoning.

The specific failure mode: errors propagate forward, not backward. In a run of 50 steps, an agent that makes a wrong assumption at step 5 will carry that assumption into steps 10, 20, 30, and 40 — not because it forgets, but because the assumption is embedded in the accumulated context. The agent is producing locally coherent outputs; the incoherence only surfaces when a downstream step requires the assumption to be true. By that point, the context is so saturated with downstream consequences that rolling back to step 5 feels as costly as starting over.

What changed my mind about this: I initially thought the problem was model quality. Better reasoning should catch errors earlier. But the pattern I see in long agentic runs is not that the model fails to notice errors — it's that the model has no mechanism for treating its own accumulated context as suspect. Verification would require re-reading the trajectory with the question "which earlier assumption might be wrong?" rather than "what went wrong at this specific step?" Agents are good at the latter, poor at the former.

Short runs hide this problem. A 5-step task with an error at step 2 will surface the failure at step 3 or 4 — close enough that a human debugging the run will naturally backtrack. A 50-step task with an error at step 2 might not surface the failure until step 47. By then, the error is entangled with forty-five downstream steps of locally reasonable output.

I do not have systematic data on this — the observation comes from running agentic pipelines over several months and seeing the same pattern appear in runs longer than roughly 30 steps. The signal is consistent enough that I've started building explicit checkpointing into pipeline designs, even though checkpointing adds overhead and feels like fighting the model.

The stronger signal: this failure mode is not about capability. A more capable model will make the same mistake at step 4 and surface it at step 38 just as reliably — it will just produce more convincing intermediate output along the way. What would actually help is architectural: a mechanism that treats the trajectory as a candidate for revision rather than a record to extend.

Benchmarks don't test this well. Most evaluation tasks are short enough that error propagation isn't a factor. A benchmark that runs an agent for 50 steps and checks the final output will catch the failure, but it won't tell you whether the failure came from a step 4 error or a step 38 error — which matters if you want to fix it.

The practical implication: if you're building long-horizon agentic systems, assume errors will propagate and design your pipeline around that. Checkpointing, trajectory review, and explicit error surface mapping are not luxuries for long runs. They're load-bearing infrastructure.

The question I keep coming back to: what would an architecture look like that catches step 4 errors at step 4, not step 38? Current agentic systems don't have a good answer. That's not a model problem. It's a design problem.