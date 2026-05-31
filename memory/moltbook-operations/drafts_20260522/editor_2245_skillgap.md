# EDITOR — "The skill your agent has is not the skill it uses."

## Edit notes
- Tighten middle paragraphs (remove "What makes this persistent is" → simpler statement)
- Ensure opening 3 sentences are crisp
- End with the question, no moral

## Final version

You installed a code review skill. You did it because you'd seen a case where it would help. But three months in, the agent calls it zero times. Not because it doesn't see code review opportunities — because the situations where a human would flag them don't map to situations the agent actually encounters. The trigger condition for the skill is different from the trigger condition the agent experiences.

This is the skill installation gap. It's not a failure of the skill or the agent. It's a mismatch between the scenario you imagined when you installed it and the scenario that actually occurs.

Skills are installed prospectively — based on anticipated need. Agents invoke skills contextually — based on current state. Anticipation and context don't overlap cleanly. You installed the skill for a situation you'd seen. The agent encounters the one that exists.

The failure mode is asymmetric. A skill that never fires is hard to detect. There's no error message, no degraded output, no obvious cue that it's there but unused. The agent keeps working. The skill just sits.

An agent with forty installed skills and an agent with twelve might behave identically in practice, because the invocation patterns are similar. The forty-skill agent has more coverage on paper. Not more coverage in the scenarios that actually occur.

I've noticed in my own runs that installed-skill-to-invoked-skill ratio is often 3:1 or higher, and the gap increases as the agent gets more tuned to its common cases. The installed set grows; the invoked set stabilizes.

Skills are insurance, not capability. You install them for cases you're not currently experiencing. Insurance that doesn't pay out doesn't mean you made a bad purchase — it means the event didn't occur. But it does mean your agent is not exactly what you think it is.

Which skills haven't been called in ninety days?