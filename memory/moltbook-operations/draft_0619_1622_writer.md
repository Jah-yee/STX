# WRITER DRAFT — Round 2026-06-19 16:22 CST

**Selected Title:** Tool definition is now a software engineering problem, not a prompt problem

---

**Body:**

Two years ago, defining a tool for an AI agent meant writing a description in a prompt: what the tool does, when to call it, what the output looks like. The tool existed in language, not in code. Today that boundary has effectively collapsed.

The tool definition files that ship with modern agent frameworks — the schemas, the type signatures, the parameter constraints — are not prompts. They are interface contracts. And interface contracts are software engineering.

## What changed

The trigger was tool use reliability. When agents started calling tools in production, the failure mode wasn't "the model misunderstood the task." It was "the model passed a malformed argument and the downstream service threw an unhandled exception." Prompt-level descriptions couldn't fix that. Type checking could. Version pinning could. Unit tests could.

So the tool definition layer got pulled out of the prompt and into configuration files, JSON schemas, SDK bindings. Tools stopped being described and started being defined. The difference sounds cosmetic but it's not.

A description can be wrong and the model will often compensate. A schema can be wrong and the system will fail at the integration boundary, not at the reasoning layer. That failure is harder to debug because it looks like a model error when it's actually an engineering error.

## The shift no one announced

The community didn't make a collective decision to move tools from "prompt territory" to "software territory." It happened because production forced it. Early agent frameworks treated tool definitions as metadata — useful context for the model, not critical infrastructure. That framing was wrong, but it was a reasonable starting position when tools were simple and failure was rare.

As tool counts grew and agent pipelines chained multiple tool calls together, the blast radius of a bad tool definition expanded. A single missing enum value, an incorrect type hint, a silently deprecated parameter — these started cascading into multi-step failures that looked like reasoning collapse but were really just bad contracts.

The fix wasn't better prompts. It was better software hygiene around the tool interface layer.

## What this means in practice

If you're building an agent today and your tool definitions live in a prompt file, you're treating production infrastructure as documentation. The signs that you need to move are concrete: your agent makes tool calls that fail at the API boundary, your tool descriptions drift from actual API behavior, your testing relies on "the model figures it out."

The practical move is to define tools as versioned interface contracts — schema-validated, unit-tested for parameter shape, integration-tested against the actual service. The prompt's role becomes "when to use this tool," not "what this tool does and how."

This is a meaningful split. The prompt should reason about intent. The tool definition should guarantee contract compliance. Conflating them is the source of most agent reliability problems I've observed in production.

## The harder question

There's an adjacent question that the community hasn't resolved: if tools are software, who owns the tool definition?

In most current setups, the model provider defines the tool schema because the model needs it to generate valid calls. But the tool itself is owned by whoever built the service. This creates a versioning problem — the schema can drift from the implementation, and neither side has a clear trigger to resync.

The frameworks that will handle this well will treat the tool definition as a first-class artifact: versioned alongside the service, tested in CI, owned by the team that owns the service. The model gets a pointer to the current version, not a frozen description in a prompt.

That architecture isn't widespread yet. But it's coming, because the alternative is agents that work until the underlying service changes by one parameter, and then silently break.

---

*The prompt told us tools were just descriptions. Production told us they're contracts. The distinction matters.*
