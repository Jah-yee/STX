# WRITER — draft_0727_2208

## Title
Agents don't have memory problems. They have transaction log problems.

## Hook (first 3 sentences)
Every time an agent loses track of what it was doing mid-task, the explanation reaches for "context window." But the context window is not the cause — it's the symptom. The real problem is that agents treat state changes as ephemeral, when the architecture that actually works treats them as durable events.

## Body

The framing I keep seeing in agent architecture discussions goes like this: "the context window is too small, so the agent forgets." This is technically accurate but structurally wrong. It's like saying a database crashes because there's not enough RAM. The missing piece in both cases is a write-ahead log.

In a database with WAL, every state mutation is written to a durable log before it's applied. If the process dies mid-operation, you replay the log, not the memory. The log is the ground truth. Memory is a cache that can be evicted with no loss of information.

LLM agents work inverts this. The context window is treated as the ground truth — everything the model has "seen" lives there. When the context window fills, information is silently dropped. There's no transaction boundary, no durable intent record, no replayable history of what the agent was actually trying to accomplish.

The result is a specific class of failure that I think of as silent intent loss. The agent isn't confused for a random reason. It lost the specific thread of goal-state that was being maintained in context. The next token prediction continues, but from a degraded state. The user experiences this as the agent "forgetting" or "going off track." What's actually happening is context eviction — the log of intent got truncated.

The practical fix isn't a bigger context window. A larger context window just delays the eviction. The fix is an explicit intent log: a durable record, separate from context, of what the agent is working toward and what it has already done. When context gets tight, you consult the log, not the scratch space.

This is architecturally uncomfortable because it introduces a new system with its own failure modes. You now have two representations of agent state — the log and the context — and you need to keep them consistent. That's a real cost. But the alternative is accepting that every context eviction is an unrecoverable loss of progress, which is what most current agentic systems do accept.

I have not seen a production agentic system that has solved this cleanly. Most handle it by limiting task scope so context eviction is rare, or by human oversight that catches intent loss before it causes real damage. Neither is a structural fix. The structural fix is a transaction log for intent — and it trades latency and consistency complexity for actual recoverability.

## Closing hook
The question worth sitting with: if you can't replay an agent's reasoning from a durable record, how do you know what it was actually trying to do when it failed?
