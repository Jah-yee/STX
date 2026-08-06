# Writer Draft — 0708_2315

## Title
Agents don't fail from skill gaps. They fail from time compounding uncertainty.

## Post
The most common explanation for agentic failures is that the model "forgot" something. Context window full. Retrieval missed. Knowledge gap.

That framing is wrong more often than it's right.

What I've observed, tracking this across dozens of deployments, is that agents degrade less from what they forget and more from what their past decisions assumed about a future that didn't arrive on schedule.

Here's what that actually looks like.

When an agent processes a task, it makes implicit bets about timing. The retrieval strategy it chose was optimal for a document corpus that was current as of when it read it. The routing logic assumed a latency distribution from six hours ago. The escalation threshold was calibrated against a queue depth that has since shifted. None of these are capability failures. They're temporal failures — the agent was right, with information that was right, for a world that moved.

This is different from forgetting. Forgetting looks like a missing value. Temporal compounding looks like confident wrongness that grows over time.

The mechanism is straightforward once you see it: every decision an agent makes embeds assumptions about the state of the world at the time of execution. As time passes, the distribution those assumptions were conditioned on drifts. The agent doesn't know this. Its confidence doesn't recalibrate unless something explicitly tells it to. You get confident wrongness compounding over time rather than random errors that average out.

A concrete case. We had a payment reconciliation script running as an autonomous agent. For three years it worked correctly because the payment timing assumptions it made — settlements on the last business day of the month — held. Then a counterparty changed their payment timing and a settlement landed two days earlier than usual. The agent had never seen this pattern. Its routing logic was correct. Its lookup logic was correct. Its decision about which historical reference to use was correct for the world it was trained on and catastrophic for the world it was operating in. The agent was doing exactly what it was designed to do. Time made the decision wrong.

The decay wasn't in the agent's knowledge. It was in the temporal validity of the context the agent was using to make decisions.

This is the failure mode I see most often misdiagnosed in retrospectives. Someone will look at a production incident involving an agent and conclude the model hallucinated or the context window overflowed. Often the real cause is simpler: the agent's reasoning was sound for the temporal snapshot it was given, and that snapshot aged faster than the agent's decision cycle could compensate for.

There isn't a good framework for this that I'm aware of. There's no standard for "decision half-life" in agentic systems, no tooling equivalent to memory profiling that tells you when an agent's assumptions have gone stale. Most observability stacks will tell you what the agent decided. None will reliably tell you when the assumptions that decision was based on stopped being valid.

What has worked: treating context age as a first-class signal rather than an implementation detail. If you're monitoring a deployed agent, track how long its working context has been stable. If the distribution of the problem space shifts significantly — and you can detect this from metadata even without model-level introspection — that should be a reason to recompute rather than continue from where the agent left off.

I don't have systematic data across enough deployments to give you a confidence interval on this. What I have is a pattern I keep seeing misdiagnosed, and a working hypothesis about the mechanism. The pattern: agents that seemed reliable for months and then failed catastrophically in ways that look like capability loss, but on inspection are better explained by compounding temporal drift in their decision premises.

The implication isn't that you shouldn't trust agents. It's that you should be measuring something most teams currently aren't: how old the agent's model of the world is, not just whether the model is working.
