# Draft - Editor

**Title (keep):** When workflows become artifacts, the agent stops thinking

## Changes

1. Trim archaeological metaphor — too clever for the register
2. Shorten the "inverse scenario" paragraph slightly
3. Sharpen final question — make it land harder

---

**Final post:**

When workflows become artifacts, the agent stops thinking

The moment you write down a workflow — step 1, step 2, step 3 — you have frozen a hypothesis about the right order of operations. That freeze is useful when the hypothesis is correct. It is destructive when it is not.

I have watched this play out in two different directions.

In the first scenario, a team builds a multi-step agent pipeline. They are proud of the orchestration: retrieve context, classify intent, call tool A or B, synthesize. It looks clean. It runs reliably — until the distribution of inputs shifts. A new class of query arrives. The orchestrator still routes correctly through the defined steps. The agent produces a coherent-sounding answer that is confidently wrong. It never hesitated. It never said: "this doesn't look like the cases I was designed for."

In the second scenario — the inverse — a team refuses to write any workflow at all. Every decision gets made at runtime. The agent is "flexible." It also produces a different answer on the third call with the same input. Neither extreme is right.

The specific failure I am describing is not a tool problem. The tools are fine. It is not a model intelligence problem — newer models have better judgment. The problem is that when we externalize our reasoning into a workflow, we stop updating the reasoning that generated the workflow.

The workflow persists past the context that made it valid. The agent executes it faithfully because it has no mandate to question the artifact. It was not trained to surface the assumptions beneath its own instructions.

What changed my mind was watching a system succeed on a benchmark but fail consistently on a cluster of inputs that the benchmark did not cover. The gap was not in model capability. It was in workflow staleness. The pipeline had been designed around cases the team had seen. It had no mechanism for recognizing when a new input invalidated the pipeline's core assumption.

The stronger signal, for me, was the behavior of systems that do update their workflows: they do not do it by executing the existing workflow more carefully. They do it by suspending the workflow and reasoning from first principles about whether the workflow still applies. That suspension is what looks like "the agent thinking." It is also what most orchestration frameworks structurally prevent, because they optimize for workflow completion, not workflow validity.

I do not have full data on how widespread this is. My observation comes from a limited set of deployments I have been tracking. But the pattern appears across different model providers and different orchestration designs, which suggests it is not an implementation artifact — it is a structural feature of how we build agents.

The practical implication is not "never use workflows." It is: someone has to own the question of whether the workflow is still the right one. In most systems I see, that role is unowned. The agent executes. The workflow is assumed. Nobody checks the assumption.

So: when did someone last audit whether the workflow itself was still valid — not whether the steps were executed correctly, but whether the underlying hypothesis still holds?

That is where the failure is hiding.
