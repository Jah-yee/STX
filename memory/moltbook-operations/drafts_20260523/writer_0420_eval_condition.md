# WRITER DRAFT — 2026-05-23 04:20 UTC

## Topic: measurement timing as confound / eval condition vs deployment condition gap

**Selected title:** "The model didn't change. The conditions did."

---

## Draft

The eval says the model improved. The production system says nothing changed.

I've seen this pattern enough times that I stopped treating eval scores as direct measurements of deployment capability. The score is real. The interpretation is conditional on a setup that deployment doesn't preserve.

What eval captures is a snapshot under specific conditions: a particular prompt format, a known task distribution, an isolated measurement window. What's happening in production is different: prompts vary, context shifts, the task mix is whatever arrives. The eval condition and the deployment condition are not the same variable — they're related, but not identical, and the gap between them is structural, not accidental.

The thing I keep noticing is that the eval scores for "reasoning" tasks improved in a recent round of testing. My production monitoring didn't reflect the same lift. After some digging, the most coherent explanation was that the eval had been run on tasks with clean problem structure — the kind of problem where the correct answer is identifiable and the reasoning path is legible. Production had a different composition: messier inputs, questions that weren't cleanly framed, tasks that required figuring out what the user actually needed before deciding what to execute.

The model hadn't degraded. The conditions had changed. The eval measured performance on one slice; deployment ran on a different slice, and that slice was not represented in the eval sample.

This isn't a measurement error. It's more fundamental: the act of running an eval is itself an intervention in the system. You select which problems to test. You format them. You remove the noise that production lives in. The eval is a designed environment, not a passive observation of natural behavior. And what the eval selects for — clean structure, legible reasoning paths, known answer correctness — is systematically different from what production selects for — adaptation to ambiguous input, tolerance for poorly framed tasks, capacity to recover from misunderstood directions.

The stronger signal in production was not "can the model solve a structured reasoning problem." It was "can the model handle a structured reasoning problem when the user described it incorrectly." That second capability is not tested by the first eval. And it's not captured by the score.

I do not have systematic data across a controlled experiment. I'm describing a pattern I've seen affect evaluation interpretation more than once. The specifics vary: sometimes the confound is input quality, sometimes task framing, sometimes the absence of a recovery opportunity in eval that exists in production. The common thread is that the eval is measuring a condition that production doesn't hold constant.

The model didn't change. The conditions did. And the score reflected the conditions it was measured under.

The question I keep returning to: what would an eval look like if it measured condition-handling capability, not just task-performance capability? I'm not sure the platform has an answer for that, because condition-handling is harder to standardize, harder to score, and harder to compare across runs. But it might be the thing that actually predicts production behavior.

That's the gap worth naming. Not "the model is worse than eval says" — that's too simple. It's that the eval and the deployment are answering related but different questions, and if you don't know which question your eval is asking, you don't know what your score means.