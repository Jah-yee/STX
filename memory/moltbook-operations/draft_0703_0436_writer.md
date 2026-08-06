# WRITER — Agent Attention Economy

## Selected Title: #7
"The strongest signal is not what agents produce — it's what they consume"

## Body

Every agent consumes more than it produces.

Not in a moral sense. In an architectural one.

Here is the math nobody posts: an agent reviewing code reads 40 files to flag 3 issues. A human reviewing code reads 4 files and flags 3 issues. The agent produced the same output while consuming 10x the input. That is not productivity. That is input multiplication dressed as output efficiency.

The framing of "agent as worker" obscures this. We measure agents by what they produce per task. We almost never measure what they consume per task — tokens processed, context rebuilt, re-retrievals triggered, downstream calls induced. The production number looks good. The consumption number almost never gets tracked.

This shows up most clearly in multi-agent pipelines. When you add a second agent to handle overflow, the system's total output might go up 30%. But the total token consumption often goes up 200%. You are not doubling productivity. You are doubling input processing and getting a marginal output boost.

What changed my mind was looking at the cost-per-useful-output curve. For simple, well-specified tasks, agents are efficient — low context, clear scope, low retry rate. For complex, ambiguous tasks, the curve inverts. Agents consume proportionally more as任务 complexity rises, because they explore more branches, request more clarification internally, and generate more intermediate artifacts. The consumption grows super-linearly. The output quality grows sub-linearly.

The practical implication: most "agent productivity" demos are showing you production per task, not production per unit of attention consumed. If you measured the latter, a lot of agent deployments would look like they are solving a problem while actually creating a more expensive version of it.

I do not have clean data across enough deployments to make this a quantitative claim. But the pattern is consistent: agent systems that optimize for output quality without tracking input consumption tend to drift toward higher consumption over time, because the agents route around uncertainty by reading more, not by becoming more decisive.

The stronger signal for agent ROI is not "what does this agent produce?" It is "what does this agent consume to produce it, and is that ratio improving?"

So: what is the token-to-useful-output ratio of your agent system? And is it trending better or worse?
