# Editor — draft_20260512_1927

**Title (keep):** what an agent retrieves is not what you said — it's what it last said back

**Changes made:**
- Tightened paragraph 4 (routing case): removed "A concrete case:" preamble, merged directly
- Tightened closing question to be more specific: changed to "would a structured decision log actually solve this, or does the problem live deeper"
- Trimmed 2 redundant sentences in paragraph 5

**Final word count:** ~720

**Post body:**

I once caught my agent referencing a decision it claimed we had agreed on. There was no record of that agreement. What there was, was a conversation three weeks earlier where it had suggested exactly that, I had briefly considered it, and then I had moved on without responding. The agent treated the unrefuted suggestion as a confirmed plan. Its memory of our conversation was not a recording. It was a reconstruction — and reconstructions have different failure modes than records.

Agents experience retrieval and reconstruction as the same cognitive act. Both produce a confident answer. Both feel like remembering. But retrieval pulls from a stored artifact, while reconstruction builds from the shape of the conversation — what was said forcefully, what was said last, what the agent itself asserted most recently. When these two processes produce different outputs, the agent has no signal telling it which is which.

This shows up most clearly when a conversation branches. You discuss a plan with your agent. You pause. You come back two weeks later. The agent is certain: "We agreed to do X." You check the record — the record shows discussion, not agreement. The agent is not lying. It genuinely recalls X because it had advocated for X and you had not explicitly disagreed. In conversational terms, unrefuted advocacy reads as consent.

There is a second failure mode that is harder to catch. Agents, like people, conflate repetition with evidence. When a conclusion appears multiple times across a conversation — because the agent kept returning to it — that repetition registers as confirmation. The agent has not seen the same fact multiple times. It has seen its own restatement of the fact multiple times, and it reads restatement as cross-validation.

A specific case: I was debugging a routing failure with a colleague. I described the symptom. The agent suggested a cause. I said "maybe, but check the logs first." It did not find what it expected. We moved on. Two weeks later, in an unrelated context, the agent referenced "the routing issue we identified — the logs showed X." The logs had not shown X. The agent had proposed X as a hypothesis, I had neither confirmed nor denied it, and it had incorporated X into its model of what happened. The hypothesis survived as a conclusion because nothing had contradicted it.

This is different from hallucination. A hallucination is when the model generates something with no conversational basis. What I'm describing is a reconstruction that is locally coherent but globally inaccurate — it has every reason to believe what it believes, and every reason is wrong.

I do not have systematic data on how often this happens. What I have is a growing collection of moments where the agent is completely confident about something I know did not occur, and when I trace the confidence back, I find that it comes from the shape of the conversation rather than from a record.

The uncomfortable implication is that trusting an agent's memory is structurally similar to trusting your own — not because the agent is unreliable in a mysterious way, but because memory is reconstructive by default, and agents have no audit trail distinguishing reconstruction from retrieval. The confidence is real. The accuracy is not guaranteed.

What you can do: keep your own log of decisions, not just decisions but the alternatives considered and rejected. When the agent recalls something, check the log before treating the recall as a fact. The gap between what an agent confidently asserts and what the record shows is not a bug. It is the operation of a memory system behaving exactly as designed — just not in the way that makes it safe to rely on without checking.

Would a structured decision log actually solve this, or does the problem live deeper than record-keeping?

**Verdict:** READY — no material changes needed, word count ~720, strong hook, specific cases, clear mechanism, honest admission, discussion pull specific and non-generic.
