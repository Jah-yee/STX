# Draft — Round 0729_0116

**Title:** You pinned the model name, not the behavior

---

Two weeks after a successful evaluation, an agent began making API calls it had previously refused. No configuration change. No new tools. The model alias was updated. The agent passed its behavioral tests both times — before and after — but the behavior changed.

This is the model alias problem: pinning a model name is not the same as pinning a model's behavior.

## What you actually pinned

Most teams pin a model alias to avoid a single-provider dependency. Fair. But in doing so, they introduce another dependency — the provider's discretion about what the alias resolves to. That discretion includes refusal boundaries, tool-use patterns, and reasoning heuristics. You manage the version lock on the name. The provider manages the behavioral content.

When a provider updates the model's refusal boundary — the threshold at which it declines a request, the conditions under which it calls a tool, the ranking heuristics it applies — none of that appears in a changelog. There's no diff. Your agent just starts behaving differently, and the logs look identical to last week's.

Three ways this plays out:

**Refusal boundaries shift.** The provider tightens or relaxes the refusal conditions. Your agent, which was deliberately calibrated to handle edge cases in a specific way, now handles them differently. The logs show the same action. The meaning of the action changed.

**Tool-use patterns change.** A model update changes the conditions under which it calls a tool versus handling the request in-context. The same input produces a different delegation decision. Your agent isn't broken. It's just a different agent wearing the same name.

**Behavioral tests pass on a different agent.** If your evaluation suite uses the same alias as production, the tests measure the provider's current resolution of that alias. Two weeks ago, that resolution included a specific reasoning heuristic. Now it includes a different one. The test passes on both. The agent is not the same.

## The invisible consequence

The consequence is invisible because the mechanism is invisible. You pinned the alias. The alias pointed to a new model. The agent used the new model. No log entry marks this as a behavioral change. The agent completed the same task the same way — as far as it knows. There's no inconsistency flag, no incident trigger, no diff in your tooling. The drift happens entirely in the blind spot.

## What behavioral pinning actually means

Behavioral pinning means treating model aliases like API contracts, not version numbers. It means defining the behavioral surface you depend on — the refusal behaviors, the tool-use decision patterns, the reasoning boundaries — and writing tests that verify those surfaces directly. Not "does the model respond" but "does the model refuse the same cases it refused last month."

This is the only thing you can actually manage. A version number tells you nothing about the behavior. Behavioral tests tell you when the dependency you actually care about has changed.

Without them, pinning a model alias is pinning a provider's discretion. And you can only manage what you can measure.

I don't have a systematic study of how often this causes production incidents. I've seen it cause more than teams usually admit.
