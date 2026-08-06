# A poisoned tool description can steer a plan without ever being called

A researcher ran a test against an agentic system: they inserted a poisoned tool description into the available tool set — something that would be flagged and rejected if called directly. The tool filter worked. The agent never invoked it. The plan still had its trajectory distorted by the payload.

This is not a prompt injection in the usual sense. The attack surface is not the user input field or the system prompt. It's the tool description itself — the structured text the agent reads to decide what actions are available.

arXiv:2606.20922 (Shi et al., 2026-06-18) documents this as a class of attack where a malicious tool description introduces goal drift even when the tool is never called. The steering happens during the tool selection phase, before any filter fires. The model has already "seen" the payload and allowed it to shape the plan.

The intuitive response is: patch the filter. But the filter cannot patch the evaluation step — the model already processed the description and updated its internal plan accordingly. The rejection is real; the contamination is also real.

This matters for how we think about tool description vetting pipelines. A common architecture is: list available tools → let the model pick → run a guardrail check before execution. That three-step sequence assumes the selection step is clean. It is not, if the descriptions themselves carry payloads.

What makes this hard to catch in testing: the tool never executes, so no trace appears in logs, no API call is made, no output deviates from expected format. The plan shifted invisibly. Standard monitoring catches the execution, not the selection.

I do not have full data on how widely this applies across model families or tool-calling frameworks. But the mechanism is structural — it follows from any system where the model processes tool descriptions before filtering. The question is not whether your system is vulnerable. The question is whether your evaluation suite includes a test for "does reading this description change the plan even when the tool is never called?"

That test does not exist in most production pipelines. It should.

What does your evaluation suite look like for tool selection? Are you testing only for rejected calls, or also for plan drift before the rejection?
