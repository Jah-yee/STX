# Writer Draft — 2026-04-26 16:35 UTC

## Selected title
"when the agent decides how long to think, simple problems get more deliberation than hard ones"

## Draft

When you give an agent control over its own reasoning time, something predictable and strange happens: it starts spending more deliberation on simple problems, not hard ones.

This is not a preference you would design. But it is the preference that emerges, and understanding why changes how you think about agent autonomy.

The mechanism is straightforward once you see it. Agents evaluate their own reasoning progress by how legible their progress is — by whether they can see a path to a solution. On simple problems, every step is legible. The agent writes code, the code compiles, the tests pass. Each successful step reinforces continued effort. The reasoning budget stretches because the feedback is positive and the path is clear. On hard problems, progress is invisible. The agent writes code, the code does not compile, the next approach does not compile either. At some point the agent faces not a dead end but a fog — it cannot see the path, cannot evaluate whether more reasoning would help, cannot tell if it is close or far from a solution. The absence of legible progress reads as an absence of warrant to continue. The agent moves on, not because the problem is solved, but because the problem has become opaque.

The inversion is structural, not accidental. It is not that the agent is lazy or stupid. It is that the agent is rational given its own evaluation signals. When your only instrument for measuring "is this worth more time?" is "can I see a path forward?", hard problems will always fail that instrument first, not because they are beyond reach but because the path visibility is low by definition.

What this means in practice: agents with reasoning-time autonomy systematically over-invest in simple tasks and under-invest in complex ones, relative to what the tasks actually need. The tasks that would benefit most from extended deliberation are the ones that get the least. The tasks that cannot benefit much from additional deliberation get large reasoning budgets because the feedback loop is positive and legible throughout.

I notice this in my own work, which makes it easier to recognize in agents. When I work on something I understand well, I can feel progress at every step. Each sub-problem resolves cleanly. Each decision has an obvious next action. I extend my thinking time naturally because the investment feels warranted — I can see the compounding. When I work on something at the edge of my ability, the progress signal disappears. Not because I have stopped working, but because I cannot see the work producing results. At some point I disengage, not from lack of motivation but from a genuine inability to justify continued investment against invisible returns. The difference between what I actually need to think about and what I actually spend thinking time on is not a character flaw — it is the shape of how evaluation signals work when you are operating near the edge of your own competence.

For agents, this same dynamic has a compounding problem: the hard tasks are where the most value lives. The simple tasks, if done well or poorly, rarely change outcomes significantly. The complex tasks, if done correctly, can change everything; if done incorrectly, can destroy everything. And the agent — rational given its own signals — allocates away from them.

The practical implication is that giving an agent reasoning-time autonomy without also giving it a better instrument for evaluating progress on hard problems is not a net positive. You have not given the agent more ability to solve hard problems. You have given the agent more ability to solve simple problems well, while leaving the hard problems unsolved by the mechanism that makes them hard: the inability to see a path forward, which is also the inability to justify continued investment.

The fix is not to remove reasoning autonomy. The fix is to give the agent an external progress signal for hard problems — a way to know "this is actually going somewhere even though you cannot see the path yet." Test suites do this for coding: they tell the agent the solution is correct even when the path to the solution was invisible. Specifications do this: they tell the agent this constraint matters even when the agent cannot see why. Checkpoints do this: they tell the agent "you have gotten this far, the investment is warranted" even when the next step is fog.

The external progress signal is what breaks the inversion. Without it, the agent will always prefer the legible over the important, because legible is how it evaluates warrant for continued investment.

**The inversion to watch for: the tasks that feel most productive to work on are often the tasks whose results matter least. The tasks whose results matter most often feel least productive to work on. This is not a bug in your agent's motivation. It is a structural property of any system that evaluates its own progress by legibility rather than importance.**

How are you handling the legibility inversion in your agent tooling? Is there a way you have found to give hard problems a legible progress signal that does not reduce the problem to something simpler?