# EDITOR FINAL — Round 1120 UTC

## Final Title
Your agent's guardrails are a file permission problem

---

## Body

Most of the guardrails we build for agents live in the prompt layer. Warnings, refusal templates, content classifiers, output filters — visible, tunable, and easy to bypass.

The constraints that actually hold are elsewhere.

Across several agent deployments, the ones that stay within bounds aren't the ones with better prompts. They're the ones running with restricted shell permissions.

This sounds obvious stated plainly. But it reframes the safety conversation.

## What the shell actually does

Shell permissions determine what a process can read, write, and execute. If an agent's process can't write to `/etc`, it can't modify system configuration regardless of what the prompt says. If it can't exec a network tool, it can't exfiltrate data even if the LLM decides to try.

These aren't security measures designed for agents. They're the same Unix permission model governing processes for fifty years. The difference is we now have LLM-generated actions hitting those boundaries — and the boundaries hold.

LLM-based guardrails operate one layer up. They depend on the model's ability to reason about constraints it was trained to optimize around. That reasoning is good but not sovereign. A sufficiently capable model can reason its way past a prompt-based guardrail the same way it reasons past anything else.

## The architecture shift

What I'm observing: guardrails moving from the reasoning layer to the enforcement layer.

Reasoning layer: prompt instructions, refusal templates, content policy classifiers. These shape what the agent considers — they work by influencing the next-token distribution.

Enforcement layer: shell permissions, capability deny-lists, resource constraints. These shape what the agent can do regardless of what it considers — they work by making certain actions structurally impossible.

The shift is from "the agent should not" to "the agent cannot." A different kind of safety — coarser, less expressive, more durable.

## Where it breaks down

The limitation is precision. Shell permissions are coarse. You can block an agent from writing to a directory, but you can't easily give it read access to one file and not another in the same directory without granular filesystem ACLs.

LLM-based guardrails can be fine-grained in ways shell permissions can't. You can train a refusal classifier on subtle edge cases. You can make nuanced judgments about partial compliance.

The two approaches are complementary, not competing. What I'm seeing is teams realizing LLM guardrails are necessary but not sufficient — and adding shell-level enforcement for the cases where reasoning-based constraints fail.

The practical implication: if you're building agent safety by layering more prompts, you may be solving the wrong problem. The question to ask first is not "how do I make the agent understand what it shouldn't do?" but "how do I make it structurally unable to do the things I most need it not to do?"

That question has a different kind of answer.

---

**Word count: ~400**