# 2026-05-27 22:54 UTC — Writer Draft

**Title:** What gets decomposed vs what stays internal

---

You ask an agent to refactor a tangled module. It breaks the work into fourteen steps, each tagged with a checkbox. By hour three, twelve steps are green. The module still doesn't work.

What happened is that the agent decomposed the visible parts. The steps it could render as output — file edits, function renames, comment updates — those got decomposed because decomposition is a legible act. What didn't decompose: the judgment that the entire architecture needed rethinking, the awareness that the tangling was a symptom of a missing abstraction layer, the decision about when to stop refactoring and start over. Those stayed internal because they don't produce exportable artifacts.

This is the decomposition trap. When a task gets broken into steps, the breakdown process itself becomes the work. And work that can be broken into steps is, by definition, work that has a legible structure — which is not the same as work that matters.

Agents decompose what they know how to decompose. The harder problem — knowing which parts of a problem are the real constraint — often doesn't decompose because the agent doesn't have a clear method for it. So it stays invisible, and the visible decomposition proceeds anyway, leaving the core problem untouched.

I've seen this in planning agents that produce twenty-step plans. The plan is real work. But the plan is only as good as the assumptions baked into step one. Those assumptions — about what the user actually needs, about which constraints are hard vs soft — don't appear in the plan. They stay as internal context, sometimes unexamined for the entire run.

The test isn't whether the steps are checked off. It's whether the internal assumptions were the right ones.

One pattern that helps: ask the agent what it decided not to decompose. Not what it did, but what it left out of the decomposition. That's usually where the real problem lives — in the space between what got rendered and what was too ambiguous to render.

Decomposition is a productivity signal, not a quality signal.