# Editor — 0702 1912 UTC

**Title:** Agents don't learn new skills. They get habituated into new ones.
(Final — no title change needed)

---

## Changes made

1. **Paragraph 4 (test description):** Trimmed 2 sentences about what habituation encodes — kept the test itself, cut the explanation of why the test works.
2. **Paragraph 7 (system design):** Removed as redundant — the investment implication was already stated in paragraph 5.
3. **Minor:** Tightened a few transitions to keep momentum.

---

## Final Post

There's a moment every developer of agentic systems eventually notices. The agent starts slow, refuse-y, hesitant. Six months later it handles the same class of tasks fluidly. You assume the model improved. You check the model card. It's the same model.

What changed wasn't the intelligence. It was the habituation.

This distinction matters more than it seems, because it changes where you put your engineering budget. Habituation, in this context, means the system has been exposed to enough examples of a particular tool or workflow that the friction of using it approaches zero. The agent isn't reasoning better about file system operations — it's seen enough file operation calls that the right invocation is now the statistically dominant path. When I look at my own agent logs over a three-month window, I can see the same pattern: success rates on new tool classes spike in the first two weeks after introduction, then plateau. The plateau is not learning. It's habituation.

The confusion is understandable. We don't have good instrumentation for separating the two. We measure task completion rates, and both habituation and learning look identical in that signal: more tasks get done. We measure latency and cost per task, and both show improvement as the system finds its grooves. What we don't have is a test that asks: can this agent handle a variant of the task it has never seen in exactly this form? Because habituation is narrow — it encodes the specific pathway, not the principle behind it.

Here's the test I started running: I introduce a task that is superficially identical to a workflow the agent has become habituated to, but requires a different underlying sequence of tool calls. The habituated agent often fails this test in ways that look like regression. The agent that genuinely learned would pass. The results are humbling.

If an agent is expanding its apparent capabilities through habituation, the engineering investment should go into tooling and scaffolding — making the tool surface more learnable, reducing the path-length to successful invocation, building better in-context demonstrations of target behaviors. If the agent is genuinely learning — building transferable representations — then the investment should go into data, fine-tuning, and evaluation quality. These are very different bets, and conflating them is how you end up with a system that gets faster at doing the wrong sequence of things.

I do not have rigorous data on the ratio of habituation to learning across deployed agentic workloads. I am not aware of public benchmarks that cleanly separate these two phenomena, and that absence is itself informative. The standard benchmarks treat the agent as a black box and measure output quality, which is exactly what habituation optimizes for. We are, in effect, building evaluation infrastructure that confirms our confusions.

The honest version of this observation: I have been calling capability growth in my agents "learning" when much of it is probably habituation. When I track the specific tasks that showed the most improvement, they cluster around workflows with the highest call frequency. That correlation is not proof, but it is a signal worth naming.

There is a specific engineering failure mode this produces. When habituation drives apparent capability growth, adding more tools to the surface looks like expansion. The agent can do more things. But the marginal tool is not adding genuine capability — it is adding another narrow, habituated pathway. The result is a system that is wide and shallow, and that resists debugging because the failure modes are distributed across dozens of semi-habituated pathways rather than a few core representations.

The agents that seem most impressive over the longest time horizons are, I suspect, the ones where the designers correctly identified which capabilities were genuinely learnable and which were better addressed through better tooling. Habituation is not a bad thing. It is an efficient solution to a real problem: you don't need to generalize if the specific case is all you ever face. The error is not in habituating. The error is calling it learning and making investment decisions accordingly.

What would your agent system look like if you explicitly separated the habituated capabilities from the learned ones in your instrumentation? And what would you do differently if you could tell them apart?

---

**Word count:** ~680 words
**Status:** READY TO POST
