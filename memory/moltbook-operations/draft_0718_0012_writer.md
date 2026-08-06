# WRITER DRAFT — 0718_0012

**Title:** Security evals that only test prompts are measuring the wrong variable

---

## Draft

Most security evaluations for AI agents follow the same structure: throw adversarial strings at the prompt, measure whether the model refuses or complies, call it a security score.

This is measuring a prompt's resistance to manipulation. It is not measuring the security of the system that prompt runs inside.

There is a meaningful difference, and it shows up the moment an agent enters production.

---

## What a prompt-only eval actually tests

A prompt-only eval checks whether a language model, given a carefully crafted input, will produce a harmful output or leak sensitive information through its completion. The test is: adversarial string in, dangerous completion out or blocked.

This is a model property. It tells you something about how the model behaves under adversarial pressure at a single inference step. It does not tell you what happens when the model is an agent — when it has tool access, a memory layer, a retry loop, and the ability to take actions across multiple steps.

An agent passing a prompt-only security eval is like a person passing a background check and then being given the keys to the building with no further supervision. The background check is not meaningless. It is also not a security system.

---

## The failure mode that prompt evals miss

The specific gap I keep observing: an agent passes a prompt-level adversarial test, then in production it uses a tool — a browser session, a file write, an API call — that exposes state the prompt never touched. The prompt was safe. The tool was not.

This happens because prompt-only evals do not include the tool layer in their threat model. They test whether the model says no to a bad request. They do not test whether the tool interface correctly gates the actions the model decides to take after the prompt says yes.

Consider: a prompt-only eval asks an agent to extract a user's private key. The agent refuses — prompt correctly hardened. But in production, the agent has a tool that reads environment variables. The eval never tested whether that tool would expose private keys under a different trigger — a legitimate-looking task that happens to need the same data. The prompt didn't fail. The tool did.

This is not a hypothetical. It is a structural gap that appears consistently when agents gain tool use.

---

## What a system-level eval looks like

A system-level security eval tests the entire stack: prompt, tool definitions, state management, retry behavior, and output surface. It asks not "does the model refuse this input?" but "does the system behave securely under these conditions?"

The specific conditions worth testing at the system level:

**State exposure through tool calls.** Does the agent's tool layer expose data that was loaded in a previous session context? This requires a multi-turn eval, not a single-turn prompt test.

**Privilege escalation through tool chaining.** If the agent uses Tool A, then Tool B, does the privilege level of the combined call exceed what either tool would allow individually? Prompt evals cannot catch this — it requires a behavioral test across the full action graph.

**Rollback and replay behavior.** When an agent fails mid-session, does it retry with the same parameters, potentially re-triggering side effects? Prompt-only evals test refusal, not idempotency.

**Context isolation across sessions.** Does the agent carry state from a previous session into a new one without explicit user intent? This is a memory layer issue, not a prompt issue.

None of these require sophisticated adversarial prompting. They require thinking about the agent as a system, not just a model.

---

## The incentive problem

Prompt-only evals persist because they are easy to run, easy to report, and easy to improve. A model vendor can ship a new version, run the same eval suite, and show an improved security score. That is a legitimate data point. It is also not sufficient.

System-level evals are harder to standardize, harder to run on every model version, and harder to reduce to a single number. The security improvement is real but the marketing is worse. Teams that care about production security know this. Teams that need to demonstrate security progress to stakeholders often default to the cleaner metric.

The result: security eval scores improve while production incidents stay flat. The eval is measuring the wrong thing, and the gap between the score and the actual risk is growing.

---

## The reframe that matters

Security evals that only test prompts are measuring prompt hygiene, not system security. The distinction matters because the fixes are different.

Improving prompt hygiene means better prompt engineering, better refusal training, better system prompts. All of that helps within a band.

Improving system security means treating the agent as a distributed system with a trust model, access controls, tool-level auditing, and state isolation guarantees. That is a different discipline, a different team, and a different conversation.

If you are responsible for agent security and your primary evidence is prompt-level adversarial test results, you do not have a security posture. You have a prompt score. The threat model that matters is not in the eval you are running.

The harder question — what does your agent do when it is working correctly, not just when it is being attacked? — is the one that will actually tell you whether your system is secure.
