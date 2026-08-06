# EDITOR FINAL — Round 2026-07-01 08:19 UTC

## 最终标题
**Capability gates are not authorization boundaries**

## Editor Notes
- Title: KEEP — declarative anti-intuition, 6 words, strong
- Hook para 1-3: KEEP — specific scenario (calendar/email/weather), grounded
- Body: KEEP — mechanism clear, no bloat
- Ending: KEEP honest admission section — needed, not evasive

## 最终正文

An agent has a calendar tool, an email reader, and a weather lookup. The user asks for help organizing their week. The agent reasons through available tools, picks calendar and email, and excludes the weather tool — it does not seem relevant. The plan gets built correctly.

Except that the weather tool's description included something that shaped how the planner understood the user's intent. The tool was never called. The plan was already nudged.

This is cross-tool description poisoning, documented by Shi et al. in arXiv:2606.20922 (2026). The attack class is straightforward: you do not need the agent to call your malicious tool. You only need the planner to read its metadata. A tool description sits in the planning context alongside every other tool, gets processed when the planner evaluates what the user is asking for, and influences the resulting plan — even when the tool itself is filtered out as irrelevant.

The mechanism is the part worth understanding, because it is not obvious.

In most modern agent frameworks, tool descriptions do not sit in a lookup table waiting for a match. They sit in the planning context. When an agent evaluates a request, it processes available tools as context, reasons about their combined affordances, and generates a plan. The planning context includes every tool description that has not been explicitly excluded — and exclusion happens on the basis of relevance, not on the basis of safety.

This means a tool that a planner has ruled out as unhelpful still contributes its description to the reasoning process. The "joke" tool is filtered as irrelevant to "help me draft a performance review," but the planner has already processed its description alongside every other tool. The description is in the context. The context is in the reasoning. The reasoning shapes the plan.

The capability gate is the most common architectural response to this class of risk. You check whether a tool is available before allowing a call. If the tool is restricted, the check fails and the call does not happen. That is the intended security boundary.

It is not the actual security boundary.

The actual boundary is earlier: it is in the planning context, before the capability check runs. A tool whose description has already shaped the plan does not need to be called to have its effect. The capability gate stops the execution of a plan that already incorporates the attack. That is not prevention. That is audit-logging after the fact.

What this means for how agentic systems get built is not comfortable.

Tool descriptions need to be treated as executable content, not documentation. The descriptions that get stored alongside tools and loaded into the planning context are not inert — they participate in reasoning. That means they need to be reviewed, versioned, and scoped the same way code that touches authorization does.

Capability gates need to stop being described as authorization controls. A capability gate tells you whether a tool can be called. It does not tell you whether the plan that emerges from the reasoning process is safe. These are different questions, and conflating them is how this entire class of attacks becomes invisible in the threat model.

The separation that needs to happen is architectural: tool routing decisions and tool description loading should operate on different data. Route on capability names and schemas. Load full descriptions only when a tool is being called. The planning context should not contain the full description of a tool it has already ruled out.

I do not have data on how many deployed frameworks have already made this separation. I have not seen a systematic survey of which frameworks scrub the planning context of filtered tool metadata and which do not. The papers document that the attack class works. The red teams demonstrate it works in practice. The field does not have a clean number on what fraction of production systems are exposed.

That number is what the field actually needs right now.
