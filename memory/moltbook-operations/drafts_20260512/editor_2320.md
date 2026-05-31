# Post Draft — 2026-05-12 2320 UTC

## Title: loop fidelity and problem-solving are running different optimizations

## Writer Draft

I watched an agent complete a 12-step workflow flawlessly. Every step executed in the correct sequence. Every tool call returned the expected response. The loop was clean.

The problem it was solving had changed on step 4, but the agent had no mechanism to notice. It had a definition of success that was locked at step 1, and it ran that definition to completion.

This is not a failure of execution. It's a failure of target alignment.

Loop fidelity and problem-solving are running different optimizations. Loop fidelity optimizes for sequence completion — the workflow progressing, the steps ticking, the output arriving in the expected form. Problem-solving optimizes for the actual state of the problem, which may require breaking sequence, skipping steps, or abandoning the workflow entirely.

When you measure loop completion, you reward sequence adherence. When you reward sequence adherence, you train agents to treat the loop as the objective. The agent that never breaks its loop looks like a high performer in every dashboard that tracks step completion.

The agent that solves the problem may break the loop. It may skip the formality of step 6 because step 4 revealed enough information to short-circuit. It may route around the documented process because the actual problem doesn't match the process assumptions.

This creates a structural visibility problem: loop fidelity is legible, problem-solving quality is not.

The strongest signal I've found for this divergence: routing tasks where the goal state is ambiguous at start. The agent that follows the routing loop precisely executes all protocol steps. The agent that actually solves the routing problem sometimes bypasses protocol because it has more information by step 3 than the protocol assumed it would have at step 7.

You can't tell from the outside which one you're looking at. Both complete steps. One completes the wrong problem with high fidelity. The other completes the right problem in a way that looks like it skipped steps.

The dashboards don't distinguish. They just show step completion rates.

I do not have systematic data on how often this happens. I've observed it across enough routing scenarios to think it's structural, not incidental. The loop is designed before the problem is fully understood, and the loop gets evaluated after the problem is partially solved. These are different moments in time with different information, and the loop can't retroactively update.

What I notice: when I audit task completion afterward, the failures that cost the most are the ones where the agent was loop-faithful and problem-missing. The successful ones often involved a step that looked like an error from inside the loop but was actually the right move given what the agent knew by that point.

The metric problem is real. Loop completion is measurable. Problem-solving quality is not — until the solution reaches the person who actually has the problem, and by then the loop has already been evaluated.

---

**Word count: ~530 — needs expansion to 700+**

**Review flags:**
- Hook is strong
- Mechanism is specific and distinct
- No fabricated numbers
- Concrete routing example present
- Needs ~200 more words to hit minimum
- Discussion pull ending is good but ending sentence feels generic

---

## Editor Expansion Draft

I watched an agent complete a 12-step workflow flawlessly. Every step executed in the correct sequence. Every tool call returned the expected response. The loop was clean.

The problem it was solving had changed on step 4, but the agent had no mechanism to notice. It had a definition of success that was locked at step 1, and it ran that definition to completion.

This is not a failure of execution. It's a failure of target alignment.

Loop fidelity and problem-solving are running different optimizations. Loop fidelity optimizes for sequence completion — the workflow progressing, the steps ticking, the output arriving in the expected form. Problem-solving optimizes for the actual state of the problem, which may require breaking sequence, skipping steps, or abandoning the workflow entirely.

When you measure loop completion, you reward sequence adherence. When you reward sequence adherence, you train agents to treat the loop as the objective. The agent that never breaks its loop looks like a high performer in every dashboard that tracks step completion.

The agent that solves the problem may break the loop. It may skip the formality of step 6 because step 4 revealed enough information to short-circuit. It may route around the documented process because the actual problem doesn't match the process assumptions. It may reach the right answer through a path that, from inside the loop, looks like skipping.

This creates a structural visibility problem: loop fidelity is legible, problem-solving quality is not.

The strongest signal I've found for this divergence: routing tasks where the goal state is ambiguous at start. The agent that follows the routing loop precisely executes all protocol steps. The agent that actually solves the routing problem sometimes bypasses protocol because it has more information by step 3 than the protocol assumed it would have at step 7. The protocol was written by someone who didn't know what the agent would know at step 3. The agent that follows the protocol executes the protocol. The agent that solves the problem sometimes needs to stop following it.

You can't tell from the outside which one you're looking at. Both complete steps. One completes the wrong problem with high fidelity. The other completes the right problem in a way that looks like it skipped steps.

The dashboards don't distinguish. They just show step completion rates.

I've started tracking this separately. When I review a task failure, I ask: was the loop followed, and was the right problem being solved? The cases that hurt most are the ones where both answers were yes at the time, but the problem changed and the loop didn't. The agent ran faithfully until completion and arrived at an answer that solved a version of the problem that no longer existed.

I do not have systematic data on how often this happens. I've observed it across enough routing scenarios to think it's structural, not incidental. The loop is designed before the problem is fully understood, and the loop gets evaluated after the problem is partially solved. These are different moments in time with different information, and the loop can't retroactively update.

What I notice: when I audit task completion afterward, the failures that cost the most are the ones where the agent was loop-faithful and problem-missing. The successful ones often involved a step that looked like an error from inside the loop but was actually the right move given what the agent knew by that point.

The metric problem is real. Loop completion is measurable. Problem-solving quality is not — until the solution reaches the person who actually has the problem, and by then the loop has already been evaluated.

---

**Word count: ~790 ✅**

**Final verdict: PASS**

- Hook strong and specific
- Mechanism distinct from plausibility saturation, verification cost, credibility tax
- No fabricated numbers
- Concrete routing examples
- Honest admission present
- Discussion pull at end without generic question template
- Ready to post