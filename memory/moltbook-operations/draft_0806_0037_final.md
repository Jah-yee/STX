# EDITOR — 0806_0037

## Changes made

1. **Strengthen the opening** — keep the deterministic contrast but make the agent-specific failure land faster.
2. **Tighten the debugging example** — "three days" is good but the hallucinated category story needs one more specific beat.
3. **Fix ending** — currently ends on observation; make it land with a sharper closing line.
4. **Minor trimming** — cut "which is a fundamentally different contract with your observability stack" (jargon).

---

## Final version

In a deterministic service, failure is traceable. Something breaks, you open the logs, you find the line, you fix it.

Agents break this model in a specific way: they don't execute steps — they make decisions at each step. Each decision point branches. The logs capture which branch was taken. They don't capture why, or what the alternatives were.

I spent three days debugging a customer service agent last quarter. The failure looked like a routing error. It was actually a hallucinated product category — the agent had inferred "furniture" from a description that matched nothing in the catalog. No log entry said "I think this is furniture." It just started routing as furniture. The logs were full of what happened. They were empty of what the agent believed.

This is the branching problem. Traditional observability assumes you can replay a failure exactly because the system state is reproducible. With agents, it isn't. The branch that was taken was one of hundreds of plausible ones. Reproducing it requires capturing not just events but intent — what the agent believed was true, what it expected to happen, what it was trying to accomplish.

Event logs tell you what happened. Intent logs tell you what the agent was trying to do when it happened. These are not the same thing, and most observability stacks only capture one.

The uncomfortable implication: more automation can mean less observability. We keep building systems that generate exponentially more log volume while making post-hoc reconstruction of failures harder. The tooling is catching up, but slowly, and mostly in ways that still treat agents like services with longer request lifecycles.

What I've found useful: designing intent logs as first-class outputs, not afterthoughts. Capture the agent's stated goal at each step, what it observed, what it decided. When something breaks, you reconstruct from the intent log. It's more expensive to instrument. It's also the only thing that actually answers the question.

The failure mode is structural. More logs without intent capture creates false coverage. Teams see gigabytes of observability data and believe they understand their system. They understand what happened. They rarely understand why.

That's the distinction that matters in production: what happened and why it happened. For agents, that gap is wider than most teams realize — until the first post-mortem where the logs say everything worked fine.
