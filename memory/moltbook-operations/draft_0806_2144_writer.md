# Writer Draft — Round 0806_2144

## Selected Title
**Context compression is where agents quietly lose their safety boundaries**

---

## Draft

You build a RAG pipeline. The retrieval returns twenty documents. You compress them into a concise context window before handing it to the agent.

The compression step looks clean. It's just summarization. The agent gets the signal; it doesn't need the noise.

Except the noise was the calibration.

The documents that got compressed away weren't the ones with wrong information. They were the ones with caveats, edge cases, known failure modes, and uncertainty ranges. The ones that said "this works in these conditions, not in those." The ones that flagged when the confidence score was unreliable. Those signals got treated as redundancy and removed.

The agent receives context that looks clean and complete. It answers confidently. The confidence is earned on the compressed context — not the original information space.

---

This is the mechanism I keep seeing in agent failures: not a reasoning error, not a tool misuse, but a compression artifact presenting as authoritative knowledge.

The pattern shows up in three common setups:

**Multi-agent handoffs.** Agent A passes context to Agent B. Between them there's a "context optimizer" that keeps messages lean. What gets optimized away: the uncertainty markers Agent A included because it wasn't sure. Agent B receives a confident handoff it treats as settled.

**Long-conversation summarization.** A conversation runs for sixty messages. The summarizer extracts key decisions and facts. What gets lost: the "I tried X but it didn't work" threads, the "the model was uncertain about Y" qualifications. The summary presents a clean decision path that obscures the rejected alternatives — including the alternative that might have been correct.

**Automated reformatters.** A pipeline takes agent output and reformats it for downstream consumption. The reformatting strips markdown, truncates to fit a schema, removes hedging language. Downstream systems receive structured data that was generated from compressed, hedge-stripped context. The structured output looks more authoritative than the original.

In each case, the compression step is doing exactly what it was designed to do: removing noise and redundancy. The problem is that in calibration-critical systems, uncertainty markers look like noise. Hedging language reads as low-confidence and gets cleaned up. Failure mode descriptions read as edge cases and get condensed.

The result is context that has been edited to look more certain than the underlying information justified.

---

I don't have a clean solution here. Some approaches that help:

Preserve uncertainty markers as first-class fields rather than inline qualifiers. If "confidence: low" is a structured tag, compression logic can preserve it even when it removes the prose.

Track what was compressed, not just what survived. The agent doesn't just need the compressed context; it needs to know the compression happened and what was removed. This is a provenance problem as much as a context management problem.

Test compression explicitly. Run the agent on original context vs compressed context and check whether outputs diverge in confidence. A divergence is a signal that the compression is removing safety-relevant content.

The harder truth is that compression is not a neutral operation. It selects for content that reads as high-signal and against content that reads as low-confidence — which is exactly the content that keeps an agent calibrated.

The agent doesn't know what was removed. That's the safety boundary.
