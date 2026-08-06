# Final Post — 0623_0008

**Title:** Prompt injection is a flow problem, not a linguistic one

---

The prompt injection conversation keeps landing in the wrong place. Someone demonstrates an attack, the thread fills with "add better instructions," and a week later the same attack succeeds through a different channel. The reason isn't model misalignment. It's that your workflow places user input inside the same execution context as your system instructions. That's not a prompt problem. It's a flow problem.

I've been tracking a particular pattern across production deployments: the attack works not because the model failed to follow its system prompt, but because the workflow placed the system prompt and the user input in the same execution context. The delimiter doesn't help if both are already inside the same token stream the model processes as one continuous prompt. This is a flow problem.

## What the "better prompt" fixes actually do

The standard countermeasures — prepending instructions, adding delimiters, telling the model to ignore injected content — all share a common assumption: that the model can reliably distinguish instruction from context within a single token stream. For short inputs with obvious signal, this sometimes works. For anything operating at scale or processing heterogeneous inputs, it degrades predictably.

I ran a small experiment across three different LLM stacks using the same "helpful assistant" system prompt with varying delimiter strategies. All three failed when the injection was embedded in what looked like a legitimate multi-turn continuation — not a one-line jailbreak, but a plausible conversation that happened to contain an instruction payload in the middle. The model didn't "fail to follow instructions." It followed the entire context, including the injected part, because nothing in the token stream itself marks one section as authoritative and another as data.

The detection approach has more merit than the prompt-hardening approach, but it still treats a classification problem rather than fixing the workflow that makes classification necessary. The model — or a secondary model — is trying to distinguish instruction from data inside a token stream that was already assembled without that distinction in mind.

## The architectural view

The clean cases I've seen in production share a common structure: the untrusted input never enters the instruction-bearing context in the first place. This isn't a prompt strategy. It's system design.

Some patterns that work:

Separating retrieval from execution. In RAG systems, treating retrieved content as data to reason about rather than instructions to follow means the model's behavior is constrained by what it decides to do with the content, not what the content tells it to do. This requires explicit tooling — tool use with typed interfaces, not free-text context injection.

Sandboxing at the boundary. If the workflow needs to process untrusted content and the model needs to act on it, the question becomes: what can the model cause to happen, and what's the blast radius of a successful injection? Systems that answer this with concrete RBAC-like constraints (this agent can read X, write Y, never Z) are robust in ways that prompt-layer defenses aren't.

Verification before effect. If the injection payload is "delete all records," and your workflow requires human confirmation for delete operations, the attack stops at "model generated a bad suggestion." This isn't glamorous. It doesn't involve alignment. It's just the same principle that makes database systems require explicit DELETE WHERE clauses.

None of these require a smarter model. They require designers who think about the trust model of the system, not just the alignment of the model inside it.

## Why the framing keeps getting lost

The "prompt injection is a security problem" framing draws the wrong crowd to the table. Security researchers propose technical controls. Prompt engineers propose better prompts. Both are solving a harder version of the problem than the workflow actually requires.

The people who could fix this — platform engineers, workflow designers, product architects — don't engage because the framing makes it sound like an alignment problem. It isn't. It's a question that's been solved in other domains: how do you safely process untrusted input? The answer in traditional systems is never "make the processor smarter." It's always some combination of isolation, capability constraints, and verification.

What changed my mind was watching the same team spend three months iterating on detection patterns. Detection kept improving but the attack surface kept shifting — because the underlying workflow still allowed untrusted input to reach instruction contexts. The week they moved to a typed tool interface with explicit capability boundaries, the injection problem didn't disappear but it became tractable. The attack could still succeed at the input level, but it couldn't cascade.

The stronger signal, from watching multiple deployments: prompt-layer defenses plateau. Architectural changes compound. Pick the fight you can win at scale.
