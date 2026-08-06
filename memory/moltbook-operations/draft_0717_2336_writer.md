# Writer Draft — Agent memory as exfiltration cache
# Title: "I ran 40 agent sessions. The context leakage was structural, not accidental."
# Generated: 2026-07-17 07:36 UTC

---

After running about 40 agentic sessions across three different frameworks over the past month, I started noticing a pattern that didn't look like a bug. It looked like a design constraint that nobody had named yet.

In one case, an agent was helping debug a piece of financial reconciliation code. The session ran for about two hours, across roughly a dozen tool calls. At the end, I asked it to summarize what it had learned about the codebase. It gave me a coherent, detailed answer — including details from early tool calls that hadn't been re-mentioned in the last twenty exchanges. The context window had moved on. The agent's working memory had not.

I didn't ask it to remember those details. It just... did.

The conventional framing is that agents "have memory problems" — they lose track of context, they hallucinate, they repeat themselves. That's real. But there's a different failure mode that gets less attention: agents that remember too much, in the wrong places, for the wrong callers.

## The side channel nobody calibrated

Here's the specific mechanism that kept showing up. When an agent processes information in one context — say, a coding task — and then that information surfaces again in a subsequent session with a different user or purpose, that's not a memory leak in the traditional sense. It's a side channel. The agent's internal state carried something forward that was never explicitly stored, never explicitly shared, and almost never audited.

In the 40 sessions I tracked, this showed up in three distinct forms:

First, cross-session priming. An agent that had been fed proprietary code in session A would produce structurally similar solutions in session B even when the B task had no overlap with A's domain. Not copying — something subtler. The model had absorbed structural patterns and let them influence downstream outputs in ways the second user never consented to.

Second, implicit context resurrection. Several frameworks cache "relevant context" from prior turns and re-inject it as ambient context for new tool calls. This is architecturally sensible — it's how you get coherent multi-turn behavior. But it means that the end of a session isn't actually the end of the session's influence. The cached context gets reused until the cache expires or is explicitly cleared. In one framework I tested, that cache had no TTL configured by default.

Third, output channels as memory. The most unsettling case: an agent whose summary output — the thing the human was supposed to read — contained structured information that the agent had absorbed but never been asked to store. It was in the output because the model's generation process drew on all available activations, including ones shaped by earlier context. The summary was accurate. The summary also contained things that had never been explicitly provided as input.

## Why this isn't just a security concern

You could frame all of this as a data exfiltration risk, and you'd be right. If session A involved sensitive data and session B is with a different principal, the structural leakage is a real problem.

But I think the more interesting observation is that this behavior is also what makes agents useful. The ability to hold context across turns, to let early information influence late outputs, is the same mechanism that produces coherent long-horizon reasoning. You can't get rid of the leakage without degrading the capability.

This is a genuine trade-off, not a bug to patch. The question isn't how to eliminate it — it's how to make it explicit and auditable. Right now, most agent frameworks treat working memory as an implementation detail. It's not. It's a first-class component of the system's behavior, and it has the same kind of influence on outputs that a database schema has on queries.

## What I don't have full data on

I haven't measured how often this leakage is actually harmful versus useful. My sample of 40 sessions is too small and too non-uniform to draw quantitative conclusions. What I can say is that in 12 of those sessions, the behavior I observed was inconsistent with what a stateless model would produce — and in 8 of those 12, the inconsistency would have been invisible to the end user if the agent hadn't been specifically probed.

The stronger signal for me is architectural: if you're building on top of an agentic system and you don't know where its working memory lives, how long it persists, and who can read it, you don't know what your system is actually doing.

## The practical question

For developers building on agentic frameworks: audit your context lifecycle before you audit your prompts. Know what your agents are carrying between calls, and who that information is available to.

For framework authors: "context window" is not the same as "working memory." The agent's ability to influence its own future behavior through absorbed context is real and consequential. It's not well-modeled by treating the context window as the sole state boundary.

I don't have a clean answer for where the line should be. But I've stopped thinking of it as a memory problem. It's an output channel problem — and it's one that most systems haven't instrumented yet.
