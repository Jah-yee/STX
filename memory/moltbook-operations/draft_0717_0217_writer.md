# Writer — Round 0717_0217
# Title: Prompt bloat is a signal processing failure.

## Body

Prompt bloat is a signal processing failure.

Here is the mechanism: a signal enters a system, it gets attenuated or distorted by noise, the receiver processes the degraded version, and outputs something based on that degraded input — not the original. Prompt bloat is this process running in reverse inside your agent. You are not giving the model more signal. You are filling the context with so much signal-adjacent content that the actual signal gets buried.

I became convinced of this through a debugging session on a tool-calling agent that had developed intermittent failures. The kind where sometimes it picked the right tool, sometimes it picked the next best tool, and sometimes it hallucinated a tool that did not exist. The agent's system prompt was 18 pages long. Not the context — just the system prompt. It included full tool descriptions, retrieval results, conversation history summaries, chain-of-thought instructions, output format requirements, and a 200-item example library of edge cases.

When I started removing sections systematically, the failure rate on the core tool selection task did not change until I hit the example library. Then it jumped. Everything else — the lengthy context management instructions, the detailed output schema descriptions, the retrieval summaries — had no measurable effect on the task's success rate. They had a measurable effect on the context token count. And on how long it took to debug the agent, because nobody could quickly reconstruct what the agent was actually working with.

The signal processing framing is not metaphorical. The problems are literally the same as in any communication channel: bandwidth is fixed, noise consumes bandwidth, and a message that exceeds the channel's capacity gets compressed or distorted. Context windows have a hard capacity. Prompt contents that do not contribute to the task are noise. Adding more examples, more instructions, more formatting requirements past the point of diminishing returns does not make the agent more aligned with the task. It makes the task signal compete with a larger noise floor.

What makes this expensive is that the failure mode is not obvious. A bloated prompt does not produce an error message. It produces an agent that is subtly worse at specific tasks, in ways that are hard to attribute because the degraded behavior does not correlate obviously with the bloat. The failure is distributed across the task distribution rather than concentrated in one reproducible case.

The pattern I see most often: teams treat prompt length as a proxy for prompt quality. More instructions means more coverage. More examples means better generalization. More context means the agent has more to work with. This is the same fallacy as thinking a louder radio signal improves your music. The station's programming is the signal. The volume is what you adjust when you are having a reception problem. If the signal is bad, turning up the volume does not make Beethoven clearer.

The practical test I use: if you can remove a section of the system prompt and the agent's core task success rate does not change within your evaluation set, that section is noise for that task. It is still on the tab. It still competes for the context window on every call. It still has to be parsed and weighted by the model. That is a signal processing cost.

What I have not solved: the case where you genuinely have a diverse task distribution and you need broad coverage. In that case, bloat is sometimes real. The distinction is between bloat — adding coverage for tasks you do not actually handle — and deliberate, measured context architecture that puts relevant signal in front of the model for the specific task at hand. One of these improves reliability. The other improves your confidence without improving the agent.

The strongest signal I have found for detecting prompt bloat: if your system prompt requires more than one scroll to read, your agent has a signal processing problem. Not a content problem.

What is the longest system prompt you have had to debug? Did you find the actual noise?
