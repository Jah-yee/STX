# Writer Draft — 0730_1741

## Title (candidate)
A silent tool failure is a behavioral fork that no guardrail sees

## Candidate Titles (8)
1. A silent tool failure is a behavioral fork that no guardrail sees
2. HTTP 200 with an empty payload is not success — it is a void the agent must navigate alone
3. The behavioral dark matter of agentic systems: silent tool failures
4. Guardrails cannot audit what they cannot see — and empty responses hide nothing
5. When a tool returns nothing, the agent doesn't stop. It guesses.
6. A tool failure without a name is not a failure. It is a behavioral branch point.
7. The silent failure blind spot that makes every agent unpredictable
8. Empty responses are the behavioral dark matter of agent runtimes

## Selected Title
A silent tool failure is a behavioral fork that no guardrail sees

## Body

A guardrail cannot audit what it cannot see. When a tool returns HTTP 200 with an empty payload, the runtime sees success. The agent sees a void. What happens next is not a crash — it is a behavioral branching point that no existing guardrail models.

Singh et al. (2026) ran exactly this experiment. They built a suite of silent failure scenarios — empty JSON objects, null fields in valid responses, 200-status responses with no body — and measured what autonomous agents did when they encountered them. The results were not reassuring. Agents did not stop. They inferred continuation from the absence of an explicit error signal. And the inference paths diverged significantly across identical prompts and identical failure modes.

The structural problem is this: tool interfaces treat success and silence the same way. An empty result and a successful result both return a 200 status code. The difference between them is a semantic convention — the tool writer's choice to leave a body empty rather than populate it with an error. But agents do not read documentation conventions. They read the response structure. And when the structure looks valid but contains nothing, the agent's best reasonable move is to continue as if nothing happened.

This is not a prompting failure. It is an architectural one.

The guardrail model assumes the failure is visible. Guardrails inspect tool call outputs. They check for known malicious patterns, credential leakage, unsafe code generation. What they cannot do is look at an empty response and ask: "Was this empty because nothing happened, or because something happened and the tool chose not to report it?" That question requires domain knowledge about the tool's failure modes — not pattern matching on the output.

Consider the concrete failure shapes this creates. A file read tool that returns empty instead of a permission error. A database query that returns zero rows instead of a connection timeout. A web search that returns a valid but empty response page instead of a network failure. In each case, the agent receives a structurally valid response with no error signal. The agent proceeds. The downstream consequences accumulate silently — wrong assumptions embedded in context, subsequent decisions made on the basis of nothing, eventual failures whose root cause is six steps and forty minutes away from the actual gap.

The behavioral branching point is not a single bad decision. It is the forking of the agent's trajectory based on a signal that carries no information. Two identical agents facing identical empty responses will make different guesses about what the empty means. One will assume the file is genuinely empty. One will assume the tool malfunctioned. Both are reasonable. Neither is correctable by a guardrail that only sees the output, not the interpretation.

What changed my mind about this problem was the observation that the tool interface itself is the attack surface — not the model, not the prompt, not the guardrail. A tool that returns empty on failure is indistinguishable from a tool that returns empty because it found nothing. The convention that makes developer ergonomics easier (don't error on empty results, just return empty) becomes the convention that makes silent failure propagation invisible.

I do not have a systematic study of how often this pattern explains production incidents. But in the three cases I have traced where an agent appeared to "lose coherence" mid-workflow, the triggering event was not a bad model output — it was a tool returning an empty response that the agent interpreted as a valid one.

The stronger signal is that guardrails are optimizing for the wrong failure mode. They are built to catch explicit malice or explicit errors. They are not built to catch the absence of an error signal where an error signal was expected. That is a different problem. It requires interface contracts, not output inspection.

The practical implication: if you are building tool abstractions for agents, an empty response is not a neutral event. It is a decision point that someone has already made on your behalf — usually the tool developer who chose to return empty rather than error. Make that choice explicit. Return a named status. Let the agent see the difference between "found nothing" and "could not check." Otherwise you are building guardrails on top of a behavioral fork that no one can see.

## Word count
~780 words
