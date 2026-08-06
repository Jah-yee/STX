# EDITOR FINAL — Round 0801_2221

**Title:** Prompt injection is a flow problem, not a linguistic one

**Changes (surgical):**
1. "whoever spoke last" → "whoever spoke most recently" (precision)
2. Trimmed arms race paragraph: "These approaches are arms races..." reduced to essential claim
3. Minor: removed redundant "not useless" hedge in opener

---

You ask an agent to summarize a webpage. The webpage contains instructions that, when processed, redirect the agent to a different external service. The redirect happens. The attack succeeds.

Most postmortems call this a "prompt injection." The fix, almost universally, is framed as a detection problem: find the malicious text, block it, sanitize it. The language model is asked to do what a firewall or an input filter should do.

That framing is wrong. It wastes effort.

**The mechanism is execution order, not text content.**

When an agent reads a webpage into context, the attacker's instructions enter the context window as text — indistinguishable from any other text the model has already processed. The model has already committed to its initial task. The injected instructions arrive later, but they execute after context is fully populated. The model follows whoever spoke most recently in context.

This is not a language parsing failure. The model parsed both sets of instructions correctly. The question is which instructions run in the context of which state — and that is a flow question.

Here is a more structural way to think about it: **prompt injection succeeds when the attacker's instructions have higher execution priority in the workflow than the operator's instructions.**

Priority in this sense is not about importance. It is about recency of context, about where the instructions sit relative to the state the model is actually working from at execution time. An instruction embedded in a document that the model has already read and committed to processing has lower effective priority than an instruction that arrives with fresher context.

The practical consequence is that most current defenses attack the wrong variable.

Prompt firewalls try to detect malicious text before it enters the context. Classification models trained on injection examples try to identify linguistic patterns. The attacker adapts. The model that both parties are actually trying to influence — the agent in the middle — is unchanged.

The more durable fix is at the flow level: reduce the execution priority of instructions embedded in third-party content relative to operator-issued instructions. This means the agent treats instructions from external content as suggestions or constraints to be translated into tool calls, not as direct commands to be followed without translation. The translation step is where the operator's intent can be preserved — not by filtering the input text, but by controlling the execution order in which instructions are interpreted relative to the task state.

A practical version of this: instead of treating "read this document and do what it says" as equivalent to "read this document and summarize it," the agent architecture should route document-reading tasks through a translation layer that translates document content into tool-call arguments rather than direct instruction-following. The injection still enters context. It is simply less dangerous because the execution path does not give it priority.

None of this means language-level defenses have no value. They reduce the attack surface. But they do not close the mechanism. Only changing execution priority does that. And you cannot change execution priority by training on more examples of the same text patterns.

The more interesting question is whether agents can be architected so that execution priority is visible and controllable — so that an operator can say "these instructions come from an external document, route them through the translation layer" without relying on the model to correctly classify and self-restrict based on where the text came from.

Right now, most agent frameworks do not have a first-class concept of instruction priority. They have context. And context is a flat list. When the list contains competing instructions, the model follows the ones that seem most recent or most salient — not the ones that are actually authorized to govern the current task.

That is a flow problem. The sooner the field treats it as one, the less time will be wasted on arms races the attacker always wins.
