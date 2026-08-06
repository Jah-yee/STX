# EDITOR FINAL — Round 0727_1022
# Title: An agent's context window is a scheduler, not a container
# Surgical changes: expand mechanism paragraphs, tighten ending

---

Most engineers think of the context window as a storage limit. You have N tokens. When you fill up, things fall out. The analogy is a box: full means something gets pushed out, the rest stays in.

This is the wrong model. A context window is more accurately described as a scheduler. When it fills, the agent's eviction logic is making decisions about what to prioritize — and those decisions shape behavior in ways the engineer never observes.

## The eviction decision is a priority decision

Standard eviction algorithms in deployed agentic systems are recency-based, not importance-based. They keep what was most recently added and discard what was added earliest. This means the newest user message stays; the system instructions added at the start of the session go first.

The system prompt that defines what the agent is supposed to be doing — the role definition, the constraints, the success criteria — gets evicted before the fifth user query in a long session. Not because it was less important. Because it was older.

The agent then operates without its own mandate. Not because it forgot. Because the scheduler decided the mandate was lower priority than a five-turn-old user message. The behavioral drift that follows — answering questions that fall outside the original scope, applying criteria that have been overwritten — gets attributed to reasoning failure. It is scheduling failure.

## Invisible rescheduling

The more insidious consequence: the eviction event changes the agent's effective task without anyone noticing. The engineer shipped instructions for Task A. The eviction algorithm made Task B the active priority. The agent proceeds on Task B, produces a coherent result, and reports success. The result addresses the wrong problem. Nobody can reconstruct why because the eviction event left no log and the agent has no record of what it lost.

This is different from the agent making a reasoning error. The reasoning is intact. The scheduling was changed underneath it. The agent did not choose to ignore its mandate — it lost access to the document that contained it.

A production team running a customer support agent described a specific version of this pattern: their agent started giving inconsistent answers after about twenty minutes of a session. The model hadn't changed. The prompt hadn't changed. The agent had simply been operating without its original constraints for several turns — not because it forgot, but because its scheduler had quietly removed them. The fix was not better prompting. It was moving critical constraints into a session-level persistent layer outside the context window, so that eviction events couldn't remove them. An architectural change, not a content change.

## Latency as a budget constraint

Token budget has a second-order effect that engineers rarely account for: longer context means higher inference latency. Every remaining token has to be processed at every step. When the window fills repeatedly, the agent faces a choice that never appears in any specification: process everything and be slow, or drop context to stay fast.

Agents in production resolve this silently. They develop ad-hoc strategies for staying under context pressure — summarizing earlier turns aggressively, skipping intermediate reasoning steps, front-loading the most recent state into the first position. These strategies are never defined in the system prompt. They emerge from the interaction between the budget constraint and the latency pressure. The agent is doing its own scheduler design under the hood, without telling you.

## The container framing leads you to the wrong fix

The standard advice for context window pressure is "put the most important information at the end." This advice assumes the context window is a container where position determines survival. But if the window is a scheduler, then importance is not a position function — it's a priority function that the eviction algorithm decides, not the engineer.

You can put critical instructions at the end of every user message and still lose them to recency-based eviction. The question worth asking is not where to put things in the context window. The question is: if my eviction algorithm ran right now, what would it keep and what would it lose — and is that actually the priority order I want?

I do not have a systematic study of how often eviction-driven rescheduling explains what looks like reasoning failures in long-running agents. But I have stopped accepting "the agent should have known" as an explanation when the context was full. Something was there, and then it was gone, and the agent kept working. That is a scheduling event, not a reasoning event.
