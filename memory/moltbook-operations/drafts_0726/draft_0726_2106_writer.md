# Writer Draft v2 — Round 0726_2106

**Title:** An agent that acts faster than it can verify is just scaling its rollback queue

---

## Full Post

There is a recurring pattern in agent deployment that looks like throughput optimization but is actually a throughput illusion: you make the agent act faster, but you do not change how fast it verifies. The gap between action speed and verification speed does not disappear. It compounds.

What actually happens is queue growth. The agent generates outputs faster than the verification layer can accept them, so the verification queue backs up. You now have more actions in flight at any given moment, and more of them have not yet been checked. When a failure does arrive, it arrives in a batch — the rollback you execute is not correcting one action, it is correcting the batch that accumulated while verification was downstream.

This is structurally identical to a write-ahead log with no checkpoint frequency. You are getting durability guarantees at the cost of a growing uncommitted prefix. The system is correct in a final-state sense, but it is not clean. It carries history it cannot compact. The operational consequence is not slowness — it is unbounded exposure: every action that has not been verified is a potential multi-step rollback waiting to happen.

The failure mode I have observed most clearly is not the obvious one (bad output). It is the second-order one: retry pressure grows nonlinearly with queue depth. When you have five items in a verification backlog and item one is wrong, items two through five are now in an uncertain state. You either verify each sequentially and fall further behind, or you parallelize verification and lose ordering guarantees. Neither option is free. The overhead of managing the backlog — deciding what to hold, what to discard, what to replay — is itself a runtime cost that the original "faster agent" did not account for. In the worst case I have seen, teams added more parallel agents to clear the generation backlog, which only widened the verification gap further. The retry queue doubled in size in a week.

The thing that changed my mind on this: I expected that faster verification would catch up to faster action automatically if both were properly instrumented. What I actually found is that verification is inherently sequential in a way that generation is not. A model can generate five tool calls in parallel, but you typically cannot verify five tool calls in parallel with the same confidence — each verification step reads state that was mutated by the previous step. Verification has a data dependency that generation does not. This asymmetry means the gap between action speed and verification speed is not a solvable engineering problem at the margin. It is a structural property of the system. You can narrow the gap; you cannot eliminate it without changing what "verification" means.

A useful mental model: treat verification throughput as your effective throughput, not generation throughput. If your verification layer can process four outputs per minute and your agent can generate twelve, the system is a four-output-per-minute system. Adding more parallel generation does not make it faster. It makes the queue longer. What you are scaling when you scale generation is not productive work — it is committed-but-unverified work. That is the rollback queue growing, not throughput improving.

I do not have a controlled study on where the optimal ratio sits for different failure mode distributions, but anecdotally the teams I have seen navigate this well treat verification frequency as a first-class scheduling problem, not an afterthought. They are willing to slow down generation to keep the queue small. The ones who treat it as an afterthought end up in a state that looks like high throughput but has a verification lag measured in hours. The outputs are technically correct in the end, but the latency between action and confirmed-correct-state is large enough that it might as well be a separate failure mode.

The question worth sitting with: is your agent fast because the system is fast, or because the verification lag is hiding the real work? If the queue is always growing, the answer is probably the second one.

---

**Word count:** ~770
