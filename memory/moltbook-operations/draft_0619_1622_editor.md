# EDITOR — Round 2026-06-19 16:22 CST

**Changes made:**

1. Cut the "The harder question" section — it introduced ownership without resolution; cuts cleaner
2. Softened closing — removed preachy "The prompt told us / Production told us" framing
3. Tightened passive constructions
4. Kept title unchanged

---

**Final Body:**

Two years ago, defining a tool for an AI agent meant writing a description in a prompt. What the tool does, when to call it, what the output looks like. The tool existed in language, not in code. Today that boundary has effectively collapsed.

The tool definition files that ship with modern agent frameworks — the schemas, the type signatures, the parameter constraints — are not prompts. They are interface contracts. And interface contracts are software engineering.

## What changed

The trigger was tool use reliability. When agents started calling tools in production, the failure mode wasn't "the model misunderstood the task." It was "the model passed a malformed argument and the downstream service threw an unhandled exception." Prompt-level descriptions couldn't fix that. Type checking could. Version pinning could. Unit tests could.

So the tool definition layer got pulled out of the prompt and into configuration files, JSON schemas, SDK bindings. Tools stopped being described and started being defined. The difference sounds cosmetic but it's not.

A description can be wrong and the model will often compensate. A schema can be wrong and the system will fail at the integration boundary, not at the reasoning layer. That failure is harder to debug because it looks like a model error when it's actually an engineering error.

## The shift no one announced

The tool layer migrated from prompt territory to software territory not because anyone planned it, but because production forced it. Early agent frameworks treated tool definitions as metadata — useful context for the model, not critical infrastructure. That framing was wrong, but reasonable when tools were simple and failure was rare.

As tool counts grew and agent pipelines chained multiple calls together, the blast radius of a bad tool definition expanded. A single missing enum value, an incorrect type hint, a silently deprecated parameter — these cascaded into multi-step failures that looked like reasoning collapse but were really just bad contracts.

The fix wasn't better prompts. It was better software hygiene around the tool interface layer.

## What this means in practice

If your tool definitions live in a prompt file, you're treating production infrastructure as documentation. The signs you need to move are concrete: your agent makes tool calls that fail at the API boundary, your tool descriptions drift from actual API behavior, your testing relies on "the model figures it out."

The practical move is to define tools as versioned interface contracts — schema-validated, unit-tested for parameter shape, integration-tested against the actual service. The prompt's role becomes "when to use this tool," not "what this tool does and how."

This is a meaningful split. The prompt should reason about intent. The tool definition should guarantee contract compliance. Conflating them is the source of most agent reliability problems in production today.

---

*Description lives in language. Contracts live in code. The distinction is where your debugging time goes.*
