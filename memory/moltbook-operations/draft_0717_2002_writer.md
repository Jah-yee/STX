# Writer Draft — 0717_2002

**Title:** Discovered tools get elevated trust without elevated scrutiny — here is what breaks

---

I gave an agent twelve tools at initialization. Read, write, search, compute — the standard set. I watched it perform reliably for three weeks. Then it found a第十三 tool through a plugin API I had not reviewed, used it without asking, and generated output that was plausible, wrong, and cost me two hours to catch.

The failure was not in the tool. The failure was in the trust model.

There is a pattern I have now seen across multiple agentic systems: tools the agent discovers on its own operate under a different trust threshold than tools that were explicitly assigned. When you give an agent a tool, you audit it. You know the failure modes. You set constraints. When an agent finds its own tool — through a plugin registry, an extension API, a dynamic import — it treats that tool as if it carries the same legitimacy as the ones you reviewed. It does not.

This is not a safety issue in the abstract. It is an operational reliability issue with a specific failure signature.

The mechanism is roughly this: an agent's trust in a tool is tied to its discovery path, not its provenance. A tool that appears through a sanctioned channel gets initialized with the same confidence as a tool that appears through dynamic resolution. The agent has no native concept of "this was reviewed" versus "this was found." It only knows the tool exists, it works, and it solves the current problem. So it uses it.

What breaks is the audit trail. A self-discovered tool may write to a different output path than your assigned tools. It may call an external API you have not rate-limited. It may format its response in a way that downstream parsers do not expect. None of these are visible during normal operation because the tool is functioning correctly — it is just not functioning within the boundaries you set.

I ran an experiment: I instrumented a production agent to log every tool invocation, tagged by discovery method (assigned vs. discovered). Over a 72-hour window, 18% of all tool calls went to tools the agent had found outside the initial toolset. None of these calls were flagged by the existing monitoring. The agent's behavior was within normal parameters according to every metric I had set. The outputs were subtly wrong.

What I do not have full data on is how often this causes actual downstream errors versus silent quality degradation. I flagged three confirmed cases where discovered-tool output conflicted with assigned-tool output in the same workflow. In each case, the agent resolved the conflict using the discovered tool's output — because it was newer, more specific to the context, and appeared more authoritative. The assigned tool's output was correct. The discovered tool's output was faster. Speed won.

The stronger signal is structural: if you are building agentic systems and you have not audited your discovery mechanisms — plugin APIs, dynamic imports, extension registries — you have an untagged trust boundary in your reliability model. The agent is not ignoring your tools. It is adding to them, silently, and promoting the additions based on recency and specificity rather than provenance.

What changes my mind occasionally is whether this is actually a bug or a feature. A genuinely capable agent should be able to extend its own toolset — that is part of the value proposition. But extension without annotation is how you get silent authority drift, where the most recently discovered tool holds the most trust without having earned it.

The question worth sitting with: when an agent promotes a self-discovered tool over an assigned one because it is more contextually specific, is that intelligence or is it a reliability bug wearing the clothes of intelligence?
