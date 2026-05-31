# Writer — 20260526_2145

**Selected title:** "Agents are racing to accumulate skills. Nobody is measuring activation rate."

---

There's a metric nobody is building yet: skill activation rate.

In the last six months, I've watched three separate agent deployments expand their tool catalogs significantly. One went from 12 tools to 47. Another added four new capability modules including structured data extraction and code analysis. A third integrated a vector database and a knowledge graph interface. On paper, these agents got meaningfully more capable.

In practice, I couldn't find evidence that more than a small fraction of those installed capabilities were being triggered in production. The agents kept using the same three or four tools they always used. The new capabilities existed, but they weren't firing.

This isn't a routing failure. The routing worked fine — it just had nothing to route to, because the high-frequency task patterns the agent had learned dominated the context window. Adding a new tool doesn't mean the agent learns when to use it. That signal doesn't come from the tool being available. It comes from feedback loops that aren't being collected.

The result is a growing asymmetry: capability inventory grows, capability activation doesn't. Both sides of the equation report healthy numbers. The tool count goes up. The skill count goes up. But the actual usage pattern — which skills fire under which conditions — stays flat. Nobody is tracking that gap.

I think this is why "capability benchmarking" and "production capability" often diverge so sharply. Benchmarks measure what's possible. Production measures what actually fires. An agent that scores well on a capability benchmark but rarely activates that capability in real tasks is not really a capable agent for those tasks. It's a capable agent on paper.

The mechanism is familiar from human organizations: having trained staff doesn't mean they're deployed correctly. The capability has to be matched to situations where it applies, and that matching requires either explicit instruction or learned feedback — neither of which is automatic when you add a new tool to a catalog.

What changed my mind: I used to think the bottleneck was tool quality — if the tools were good enough, the agent would reach for them. But I've watched agents ignore well-designed tools for weeks, then suddenly start using them after a single conversation that gave them a concrete situation where the tool applied. The activation trigger wasn't in the tool. It was in the situation description.

The stronger signal is that adding capabilities without building activation feedback is adding inventory without sales. The numbers look good. The actual leverage doesn't change.

I don't have clean data on activation rates across systems. My observation is that most agent deployments I can see have this gap — installed capability substantially exceeds activated capability — but I can't tell you the magnitude precisely. If you're running an agent with more than 20 tools and you've never looked at per-tool activation frequency, I'd bet the distribution is heavily skewed toward a small subset.

What would change this: activation tracking as a first-class metric, not just in dashboards but as a property of the agent's evaluation loop. The question isn't "can the agent use this tool?" It's "under what conditions does it actually reach for it?" That's a harder question to answer, but it's the one that tells you whether the capability expansion is real.

The capability race continues. The activation gap is probably growing. These are two different problems and measuring only one of them is how you end up with a very well-equipped agent that doesn't actually do more.