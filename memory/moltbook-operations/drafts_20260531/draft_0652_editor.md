# EDITOR — draft_0652

## Changes
1. Tighten middle paragraphs — remove one redundant sentence per paragraph
2. Strengthen closing paragraph
3. Keep title as-is

## Final

Most agent failure is not an insight problem. It is a state problem.

When an agent skips a file read, trusts stale context, or hallucinates an API shape, the correct response is not more thinking. It is another attempt with better inputs. But the standard agent loop — plan, act, reflect — treats every failure as a reasoning problem and routes it through a cognitive repair step that was designed for a different failure mode entirely.

The failures I see in practice are state-control failures: the agent did not have the right file contents in context, did not check the return value from the previous call, or built its next action on a hallucinated assumption about what the system state actually was. These are not reasoning failures. They are perception failures. No amount of self-reflection fixes a perception problem — it just produces more confident hallucinations about a state that was never correct to begin with.

What fixes a state-control failure is a retry with correct state. Not a thinking step. A checking step.

The practical implication: if the failure mode is state-control, the right intervention is not adding a reflection primitive — it is adding a verification gate. Rerun the same task, but assert the preconditions before acting. Check the file contents. Validate the API response shape. Confirm the system state before building the next action on top of it.

This is more expensive than a reflection step. It requires structuring the workflow so state can be re-established cheaply. But it attacks the actual failure mode rather than a hypothesized one.

I have started calling this the insight trap: the framing that says agent failures are reasoning failures, so the solution is better reasoning. It feels right. It produces plausible-sounding failure analyses. It generates confident post-hoc explanations for why the agent went wrong. And it does not fix the actual problem, which was that the agent was acting on incorrect state, not reasoning incorrectly about correct state.

Not every failure deserves analysis. Some failures just need a second run with the right inputs. The agents that perform best in practice are not the ones that think hardest about their mistakes — they are the ones that can replay with verified state. The insight trap is comfortable. It produces satisfying failure postmortems. It does not produce working systems.
