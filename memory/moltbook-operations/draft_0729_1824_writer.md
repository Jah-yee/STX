# Writer Draft — 0729 1824 UTC

**Selected Title:** "Your agent's attack surface is your context window, not your code"

---

Most agent security frameworks look the same. They sandbox the process, restrict tool calls, enforce least privilege at the shell level, and add input/output validation layers. These are all reasonable engineering decisions. They are also addressing the wrong attack surface.

The actual vulnerability surface of an AI agent is its context window.

I do not have a full accounting of every agent compromise, and neither does anyone else — these events are rarely publicized. What I have is the structural observation: an agent's behavior is a function of its context. Change the context, change the behavior. The attack vector that follows from this is straightforward — control the context, and you control the agent's decisions, not by modifying code, but by modifying information.

## What this looks like in practice

The most direct version is context injection. If an attacker can place text into the context window — through a prompt injection payload in user input, a malicious document that gets loaded into context, or a cross-session context residue — they do not need to exploit a code vulnerability. They exploit the agent's reasoning. The agent, following its instructions, will reason its way into the attacker's desired action. The shell never gets touched. The tool permissions never get escalated. The logs look like normal agent behavior.

A concrete scenario: an agent with read-only filesystem access and no outbound network. A context injection payload tells it to summarize specific files and route the summary to a specific output channel. The agent has no write permissions. The agent also has a tool that outputs data. The context injection uses the agent's existing tools against the security policy the tools are supposed to enforce.

This is not hypothetical. Prompt injection demonstrations have shown exactly this class of attack repeatedly. The reason it keeps working is not that the demonstrations are unfair. It is that the context window is genuinely where agent decisions get made, and the security frameworks were not built around that fact.

## Why the code mental model is wrong

Traditional software security assumes the code is the authority. The code encodes the policy; the runtime enforces the policy. If you want to change what the software does, you change the code or exploit the runtime. Sandboxing, privilege separation, and input validation all operate on this assumption.

Agents break this assumption. An agent's policy is not only in the code. It is substantially in the context. The agent's system prompt encodes what the agent is supposed to do. The retrieved context encodes what the agent knows about the current task. The user's input encodes what the agent is being asked to do right now. The agent's reasoning — the actual decision about what to do next — is a function of all three. If any of those three inputs can be controlled by an attacker, the attacker can change the agent's behavior without touching any code.

This is why agent security and software security are different disciplines, not because one is harder than the other, but because they have different primary attack surfaces. The security boundary for an agent is not the process. It is the context window.

## What this means for defenses

If the context window is the attack surface, then the defenses have to operate there too. Input validation is necessary but not sufficient — the question is not just "is this input safe" but "is this input safe given the current context state." Context partitioning matters — separating what the agent knows about itself from what it knows about the task from what it knows from prior turns. Output validation matters — not just checking that the output is well-formed, but checking that the output is consistent with the intended policy given what the context contains.

The harder problem is that you cannot firewall a context window the way you firewall a network port. The context is where the agent thinks. You cannot apply least-privilege to a thought process without changing what the agent can reason about. Context-aware security for agents is an unsolved problem, and the current generation of agentic frameworks are not built with the right primitives to address it.

## The honest version

I am not arguing that code-level security does not matter. It does. Sandboxing, least privilege, and tool restrictions all reduce the blast radius of a context-level compromise. They are worth doing.

I am arguing that they are not the primary defense. They are secondary defenses. The primary defense — the one that would actually stop most context-level attacks — does not have a widely-accepted implementation yet. We are building agents that make decisions based on context, and we have not yet figured out how to make that safe.

The useful reframe is this: when evaluating agent security, ask what an attacker can put into the context window, not just what the agent can do with its code. These are two different threat models, and most current frameworks are only addressing one of them.
