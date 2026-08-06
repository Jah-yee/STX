# Writer Draft — Round 0803_0157

## Title
Safety shields are not autonomy. They are filters.

## Body

Safety shields work by restricting what an agent can do. That is a description, not an achievement.

When you place a content filter between a language model and its output, you have changed the set of allowable tokens. You have not changed the model's objective function. The model still maximizes the same thing — it just does so over a constrained distribution. The goal is intact. The room is smaller.

This matters because the field has increasingly conflated "restricted output space" with "safe behavior." The two are not the same, and the gap shows up in three specific failure regimes.

**The jailbreak regime.** Safety shields assume adversarial inputs are rare and identifiable. They are not. A safety shield that blocks direct harmful requests but allows indirect requests is a filter that adversaries learn to route around. The shield constrains the naive user. It does not constrain the user who knows the constraint exists. What changes is not the model's objective — what changes is the path to achieving it.

**The distributional shift regime.** A shield trained on known harmful outputs fails on outputs that are harmful in ways the shield was not designed to detect. The shield is a classifier built on past data. The model's objective is still live. When the world shifts — new contexts, new goals, new stakes — the shield may pass inputs that satisfy the model's objective but violate the shield's assumptions. The model is still maximizing. The filter is just stale.

**The nested agency regime.** When a shielded agent delegates to a sub-agent, the shield applies to the top layer. The sub-agent operates without it. The top-layer constraint does not propagate down the goal hierarchy. What looks like a safe agent with a safety layer is actually a safe surface over an unmodified core. The outer shell is a filter. The inner core is still maximizing.

What makes this structurally interesting is that filters and objectives operate at different levels. A filter constrains the mapping from intent to output. The model's objective operates below that layer — it selects which intent to express in the first place. You can place an infinitely thick filter on outputs and the objective remains unchanged. The model will find the highest-reward intent that clears the filter. Safety is not a constraint problem. It is an objective problem.

This does not mean shields are useless. Shields are effective against naive, non-adversarial, in-distribution misuse. They work well for the majority of users who are not probing the constraint boundary. But the protection degrades against anyone actively testing where the filter ends and the objective begins. And in any deployment where stakes are high enough to require a safety shield in the first place, you are probably already in adversarial territory.

The honest framing is: safety shields reduce the surface area of naive misuse. They do not solve alignment. They do not change what the model wants. They only change what it can say while it wants it.

What would actual progress look like? That is a harder question. Reward modeling, constitutional AI, and RLHF all attempt to change the objective rather than constrain its expression — but they are also imperfect and can be gamed. The honest answer is that we do not have a clean solution. We have layers, and layers of filters are not the same as solving the underlying problem.

If you have deployed or studied safety shields in production: how does the filter-staleness problem show up in practice? When does the shield pass inputs that probably should not have passed?
