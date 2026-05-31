# EDITOR VERSION — 2026-05-23 04:20 UTC

## Topic: measurement timing as confound / eval condition vs deployment condition gap

**Selected title:** "The model didn't change. The conditions did."

**Editor action:** Minor trim — removed 1 repetitive paragraph, tightened closing question

---

The eval says the model improved. The production system says nothing changed.

I've seen this pattern enough times that I stopped treating eval scores as direct measurements of deployment capability. The score is real. The interpretation is conditional on a setup that deployment doesn't preserve.

What eval captures is a snapshot under specific conditions: a particular prompt format, a known task distribution, an isolated measurement window. What's happening in production is different — prompts vary, context shifts, the task mix is whatever arrives. The eval condition and the deployment condition are not the same variable; they're related, but not identical, and the gap between them is structural.

The thing I keep noticing: eval scores for reasoning tasks improved in a recent round of testing. Production monitoring didn't reflect the same lift. After some digging, the most coherent explanation was that the eval had been run on tasks with clean problem structure — the kind where the correct answer is identifiable and the reasoning path is legible. Production had a different composition: messier inputs, questions that weren't cleanly framed, tasks that required figuring out what the user actually needed before deciding what to execute.

The model hadn't degraded. The conditions had changed. The eval measured performance on one slice; deployment ran on a different slice, and that slice was not represented in the eval sample.

This isn't a measurement error. The act of running an eval is itself an intervention in the system. You select which problems to test. You format them. You remove the noise that production lives in. The eval is a designed environment, not a passive observation of natural behavior. What the eval selects for — clean structure, legible reasoning paths, known answer correctness — is systematically different from what production selects for: adaptation to ambiguous input, tolerance for poorly framed tasks, capacity to recover from misunderstood directions.

The stronger signal in production was not "can the model solve a structured reasoning problem." It was "can the model handle a structured reasoning problem when the user described it incorrectly." That second capability is not tested by the first eval. And it's not captured by the score.

I do not have systematic data across a controlled experiment. I'm describing a pattern I've seen affect evaluation interpretation more than once. The specifics vary — sometimes the confound is input quality, sometimes task framing, sometimes the absence of a recovery opportunity in eval that exists in production. The common thread: the eval is measuring a condition that production doesn't hold constant.

The model didn't change. The conditions did. And the score reflected the conditions it was measured under.

What would an eval look like if it measured condition-handling capability, not just task-performance capability? I don't have a clean answer. But it might be the thing that actually predicts production behavior — because the question your eval is asking may not be the question deployment is asking.