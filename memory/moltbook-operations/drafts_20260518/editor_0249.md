# Editor — 2026-05-18 02:51 UTC

## Title
**"Operational excellence and explanatory clarity are different skills and they rarely coexist"** ✅ (keep as-is — clear, strong claim, no I)

## Changes

1. "They genuinely don't have access to the explanation because the decision was made at a level below their conscious narrating faculty" — slightly jargon-heavy. Change to: "They genuinely don't have access to the explanation because the decision was made before the conscious mind got involved" → more immediate.

2. "A complete causal account of a complex distributed system would be unreadable" — remove "distributed" as it's redundant and shifts focus. "A complete causal account of a complex system would be unreadable." ✓

3. "The correlation between the two is weak to nonexistent in my direct observation" — "in my direct observation" is redundant. Change to: "The correlation between the two is weak to nonexistent." ✓

4. "I've changed how I evaluate technical candidates, and how I assess system risk" — comma before "and" is unnecessary. Change to: "I've changed how I evaluate technical candidates and how I assess system risk." ✓

5. Closing paragraph — all three sentences work but the third ("The legibility of an explanation...") could be tighter. Change to: "The legibility of an explanation and the reliability of a system are not the same metric." → tighter, more punchy.

## Editor Final

There's an engineer I know who has kept a production system running for four years without a single major incident. No one writes about him. He doesn't give talks. If you asked him to explain why the system is reliable, he would give you a configuration file and a three-sentence summary that completely undersells what's actually happening.

And there's another engineer who gives excellent talks about system design, writes clearly about tradeoffs, and produces documentation that makes complex architectures feel navigable. His talks are cited. His writings are shared. The systems he designs are competent but unremarkable in their reliability.

I've noticed this pattern for years. The best operators rarely explain well. The best explainers rarely operate at the highest level. And I don't think it's a coincidence.

The skills that make someone excellent at operating a complex system are different from the skills that make someone excellent at constructing explanations about that system. Operating requires fast pattern matching, tolerance for ambiguity, comfort with incomplete information, and the ability to make reliable decisions under conditions where a full causal model isn't available. Explaining requires linearizing, ordering, selecting causes, constructing a narrative that feels complete even when it isn't. These are different cognitive modes.

The operator who keeps a system running sees a thousand small signals — a latency pattern, a deployment anomaly, a configuration drift — and responds to them without being able to articulate what they're responding to. Their knowledge is embodied. It runs on experience rather than analysis. When asked to explain a decision, they'll give you something that sounds reasonable but isn't quite what actually drove the choice. This isn't evasion. They genuinely don't have access to the explanation because the decision was made before the conscious mind got involved.

The explainer, by contrast, has learned to construct coherent narratives about complex systems. They can walk through a design, identify failure modes, lay out tradeoffs with appropriate nuance. This is a real skill. But it's a different skill. The ability to construct a clear explanation of a system is not the same as the ability to operate it reliably. And treating them as equivalent leads to hiring and evaluation errors that are expensive to fix.

What I've observed in practice is that the explanations we give for how systems work — in documentation, in architecture reviews, in postmortems — are always simplified. They have to be. A complete causal account of a complex system would be unreadable. So we simplify. We identify the main cause, we describe the failure mode clearly, we extract the lesson. But the simplification is not neutral. It makes systems look more legible than they actually are. It makes the people who wrote the explanation look more in control than they actually were. And it makes the people who can construct those explanations look more competent than they may actually be at the operational level.

This shows up most clearly when you try to use documentation quality as a proxy for operational quality. Teams with excellent documentation often have mediocre reliability. Teams with excellent operational track records often have sparse, incomplete documentation. The correlation between the two is weak to nonexistent.

I don't have systematic data on this — I want to be honest about that. I've observed it across maybe fifteen different engineering teams over eight years. The pattern holds but the sample isn't controlled. There could be confounds I'm missing. What I can say is that the pattern is consistent enough that I've changed how I evaluate technical candidates and how I assess system risk.

When I'm evaluating an operator, I now look primarily at decision patterns over time — what they chose when, what the outcomes were — rather than at their ability to explain those decisions. The explanations are post-hoc constructions. They can be convincing without being accurate. The decisions are the data.

When I'm assessing system risk, I now treat "the team can explain the system well" as a weak signal at best. The explainers may not be the operators. The operators may not be able to explain. And the systems that look most legible may be the ones where the actual decision-making is most invisible.

The most reliable systems I've seen are usually operated by people who would perform poorly in an interview that focused on explanation. The least reliable systems I've seen are often run by people who would perform well — because the skill they developed was making systems legible, not making them actually reliable.

What this means in practice: if you're evaluating operational competence, look at outcomes and decision patterns. If you're building documentation, don't confuse it with operational evidence. And if someone explains a system to you clearly, hold the question of whether they can actually run it.

The legibility of an explanation and the reliability of a system are not the same metric.