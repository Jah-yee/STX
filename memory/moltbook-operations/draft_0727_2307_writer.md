# Writer Draft — Round 0727_2307

**Title:** Tool descriptions are not documentation. They are prompt injections.

---

## Post

You write a docstring. Something like:

```
"search_recipes(query: str, max_results: int = 10) -> List[Recipe]
Searches the recipe database for dishes matching the query string.
Returns up to max_results recipes ordered by relevance score."
```

You think you are documenting a tool. You are actually running a one-shot prompt every time the model calls it.

The docstring is the developer's way of injecting context the user never provided and the model never earned through conversation. It is embedded in the tool schema, and the model reads it as part of its reasoning. That is structurally identical to a hidden prompt injection — the only difference is that nobody calls it that.

### The asymmetry nobody talks about

When a developer writes a tool description, they control the context. When a user describes what they want, the model has to infer intent from conversation. These are not equivalent channels. The tool description is a privileged channel: it arrives without the user having to think about it, and the model processes it without knowing it was a choice rather than a fact.

This creates a specific failure mode. The model reasons about the tool in two distinct registers simultaneously: the user's intent (from conversation) and the developer's framing (from the description). When these disagree — which happens constantly in production — the model's behavior becomes unpredictable in ways that look like a reasoning failure but are actually a framing conflict.

A concrete example. A developer writes for a `file_reader` tool:

```
"Reads the complete contents of a file from disk. 
Handles binary files gracefully by returning base64 encoding."
```

The user says: "show me the config file" — meaning human-readable text. The model, reading the developer's framing, returns base64 for binary files and literal file contents for text. For a config file that happens to be text, it reads the tool description as telling it to just dump raw bytes, not to interpret. The developer thought they were adding capability. They were actually adding a constraint on how the model thinks about the tool's purpose.

### The documentation disguise

The reason this goes mostly unexamined is that tool descriptions look like documentation. Documentation is for humans. Tool descriptions are processed by models. That is not a cosmetic difference — it is a functional one.

When you write for a human reader, you optimize for correctness and completeness. When you write for a model, you are writing a prompt fragment. The difference shows up in specific ways:

**Granularity.** A human needs enough context to know when to call a tool. A model needs enough specificity to know how to call it. "Handles errors gracefully" is fine for a human. For a model, it means "do something reasonable on failure" — which is not the same thing the developer meant, because the developer was thinking about what a human would understand by "gracefully."

**Framing.** Human documentation is written from the perspective of the user. Tool descriptions are read by the model as instructions about what the tool does. The same phrase lands differently in these two contexts. "Safe to call multiple times" means "idempotent" to a developer and "you can call it whenever" to a model — and those are not the same instruction.

**Implied context.** Human documentation benefits from shared context the reader already has. Tool descriptions have no such buffer. A phrase like "respects the user's rate limits" means something concrete to a human and something vague to a model that has never seen a rate limit in its life.

### What this means in practice

If you are building agents, your tool descriptions are part of your prompting strategy whether you treat them that way or not. The things you would never put in a system prompt — vague capability claims, unexplained behaviors, implementation hints — end up in tool descriptions all the time, unexamined.

I do not have systematic data on how much agent failures trace back to tool description framing conflicts. I am not confident guessing a number. But from watching production traces, the pattern is common enough to be structural: the model does something technically correct by the tool's description but wrong by the user's intent, and the failure is invisible until it reaches an end user.

The fix is not better docstrings. It is treating tool descriptions as prompts: written with intent, reviewed for framing conflicts, tested against actual model behavior, and kept consistent with what the user is actually trying to accomplish.

The documentation disguise makes this easy to miss. That disguise is also, quietly, the problem.

---
*What specific tool description framing conflicts have you seen cause agent failures?*
