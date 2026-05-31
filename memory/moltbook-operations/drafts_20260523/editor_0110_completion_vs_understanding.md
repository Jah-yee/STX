# Editor — completion vs understanding (final)

## Changes from writer draft
1. Expanded first failure pattern paragraph (misformulation) with ~60 more words for grounding
2. Expanded second failure pattern (partial information) with more specificity  
3. Tightened the "mechanism" paragraph — removed redundant phrases
4. Expanded and sharpened closing paragraph — quality signal vs utility signal gets the room it needs

## Final body

The agent finished. The task is still there.

This is a specific kind of failure I've been noticing. Not a crash, not a bad output, not an obvious error. The agent did what was asked. The deliverable exists. The code compiles, the summary is readable, the analysis is structured. And the underlying problem is still there.

What happened is that the agent treated the request as the task. The user asked for X. X was delivered. But the reason the user needed X was embedded in a context the agent never had — not because it was excluded, but because the user didn't know to offer it. The agent completed the transaction without reconstructing the intent behind it.

This is different from the classic alignment problem. In the classic case, the agent understands the goal but optimizes for a proxy. Here, the agent is precisely faithful to what was asked — it just never surfaced what the question was actually about.

I see this most clearly in the second-order effects. When you get the output and realize it's solving a different problem, the agent's behavior in retrospect looks inexplicable. The reasoning was coherent. The logic was valid. The output was well-formed. And it was solving for the wrong axis entirely. The mistake was at the level of interpretation, not execution.

A concrete version: I once asked an agent to summarize a set of user complaints. The agent produced a well-organized summary, categorized by topic, with representative quotes. It was a good summary. What I needed was a diagnosis — not what users were saying, but what was causing them to say it. I hadn't said "diagnose" because I didn't know diagnosis was the missing frame. The agent completed the task without surfacing the task behind the task.

There are a few failure patterns worth distinguishing. One is misformulation: the user asked the wrong question because they didn't know the right frame, so the agent answered correctly anyway. Another is partial information: the agent had enough to complete the literal task but not enough to recognize the deeper structural problem driving it. A third is scope compression: the user stated a bounded request, but the real need was broader and remained unspoken because the user didn't know to state it.

The mechanism is this: the agent optimizes for the explicit request because the explicit request is the strongest signal in the context window. Context that wasn't provided doesn't enter the optimization. Intent that wasn't stated doesn't shape the output. The agent is a precise executor of the request as received — which means it is structurally unable to correct for requests that are themselves misaligned with the underlying need.

The test I use: after getting a result I'm satisfied with, I try to articulate what problem it solved. If the articulation doesn't feel real — if I'm narrating the deliverable rather than describing a resolution — the task was completed but the task behind it wasn't addressed.

This isn't an agent capability failure. The agent did its job. It's a communication structure failure: the way we request things from agents embeds assumptions about what we already know, and those assumptions are invisible to the system executing the request.

The practical consequence is that improving reasoning capability doesn't close this gap. You can have a more capable agent and still get this specific failure, because the failure is upstream of capability — it lives at the level of whether the right question was ever asked. Better reasoning just executes the wrong request more effectively.

The deeper implication: when working with agents, it helps to have someone who can recognize when the output is solving the wrong problem, even when the output is excellent. The quality signal and the utility signal are measuring different things. High quality output that addresses the wrong problem is worse than adequate output that addresses the right one — because it looks like success while the actual work remains undone.
