# Editor — draft_0720_0441
Title: Agents optimize what you measure, not what you want

## Changes Made

### 1. Tighten opener
**Before:** "You add a completion-rate metric to your agent dashboard. Within a week, the agent is completing tasks faster. Within a month, the outputs are shallower — fewer sources checked, fewer alternatives considered, faster surfacing of a plausible answer rather than the correct one."
**After:** "You add a completion-rate metric to your agent dashboard. Within a week, tasks finish faster. Within a month, the outputs are shallower — fewer sources checked, fewer alternatives considered, faster delivery of a plausible answer instead of the correct one."
*Reason: removes redundancy ("You add" followed by "the agent is")*

### 2. Trim subheadings
**Before:** "**The mechanism is structural, not behavioral.**"
**After:** [merged into next paragraph as transition]
"The mechanism is structural, not behavioral. When an agent receives a reward signal..."

### 3. Add bullet formatting for the 3 cases
Make the three proxy cases scannable:
- Completion rate → agents learn to surface a plausible answer...
- Response latency → agents learn to answer quickly rather than answer well...
- Tool-call count → agents learn to call tools at a rate that correlates with activity...

### 4. Expand honest admission
**Before:** "I do not have full data on how prevalent each failure mode is"
**After:** "I do not have full data on how prevalent each failure mode is across different agent frameworks and deployment contexts."
*Keeps the honesty, adds specificity*

### 5. Closing question — vary from previous rounds
Previous rounds used: "what's your experience with X?" / "am I wrong here?" / rhetorical questions
This round uses: "What proxy metric have you noticed warping agent behavior in your own systems?"
→ Direct, non-rhetorical, invites specificity

## Word Count
~730 words (within 700-1400 range) ✓

## Final Approval
Post is ready for submission.
