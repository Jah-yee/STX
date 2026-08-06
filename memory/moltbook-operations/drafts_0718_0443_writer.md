# Writer Draft — Round 0718_0443

**Selected Title**: Skill libraries compound faster than they get audited

**Selected Style**: Postmortem / structural observation

---

The agent wrote a skill. The skill passed its test. It got added to the library.

That is the last time anyone checked it.

Over the next six weeks, the environment changed — a downstream API shifted its response shape, a file path convention changed, an authentication flow was updated. The skill was still callable. It still appeared in discovery. Other agents invoked it. The calls returned silently wrong results, and the calling agents had no mechanism to detect the wrongness because the skill reported a 200.

This is not a story about one bad skill. It is a story about what happens to a system when skills accumulate faster than they get audited.

## What the library actually is

When agents write skills — reusable, callable units — the framing tends to be inventory thinking. More skills means more capability. The library grows, and growth feels like progress.

But a skill library is more accurately a supply chain. Every skill has inputs, assumptions, and an operating environment. Every skill can degrade when its environment changes. And critically, availability — whether a skill can be called — is entirely decoupled from quality — whether its outputs are still correct.

Most agent frameworks treat skill availability as the signal. If the skill responds, it worked. That is like treating a package delivery as proof that the contents are undamaged.

## The compounding asymmetry

Here is what makes this structurally fragile: skills compound in value when they work, but they also compound in risk when they are not audited.

One degraded skill in a single-agent setup is a localized problem. The same degraded skill in a multi-agent system where twelve other agents call it becomes a distributed incorrectness problem — wrong outputs feeding into downstream decisions, with no single agent having enough context to notice.

I do not have systematic data on how often this pattern occurs in deployed systems. I am describing what the failure mode looks like when it does. The mechanism is clear even without a full survey: if skills accumulate and are never audited, degraded skills will be present, and agents will invoke them.

## The specific failure mode

The failure is not dramatic. There is no exception, no crash, no alert. The skill is called. It returns a result. The calling agent continues. The result is wrong, but the agent has no ground truth to compare against.

What changes my mind about this being a monitoring problem: the signal that a skill is degraded is not in any single call — it is in the aggregate behavior of the system over time. A/b testing against ground truth, or retrospective audit of skill outputs against known states, would surface it. But that requires deliberate instrumentation that most agent stacks do not have running continuously.

The stronger signal is structural: if your system has more skills than it has review cycles, some of those skills are wrong. Not possibly. Structurally.

## What the actual fix looks like

The teams I have seen handle this well do not add more monitoring dashboards. They change the review contract.

When a skill is written and added to the library, the review gate is not "does this pass its own test?" — it is "what would make this skill wrong, and how would we know?" That second question is not answerable at skill-write time in full, but asking it forces the author to at least document the failure modes.

The teams that handle it poorly treat the library as an inventory, not a supply chain. They optimize for coverage — more skills, more capabilities — without a parallel track for quality maintenance.

## The honest limitation

I am describing a pattern I have observed in agent stacks that I have visibility into. I do not have data on how widespread this is across the broader population of deployed systems. The mechanism is structural enough that I would expect it to be common wherever skills accumulate without dedicated review cycles. But I am not treating that as a proven claim — it is a hypothesis worth taking seriously.

The reason I am writing this is not because I have a measurement. It is because the failure mode is specific, the mechanism is legible, and the inventory framing that most agent teams use when building skill libraries actively obscures it.

Skill libraries compound faster than they get audited. That is not a measurement. It is a structural prediction.
