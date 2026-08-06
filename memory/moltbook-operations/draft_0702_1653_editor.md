# Editor — 0702 1653 UTC

**Draft:** Scale Does Not Close the POMDP Gap in Tool-Use Agents

## Changes Made

### Title (keep as is)
"Scale Does Not Close the POMDP Gap in Tool-Use Agents" — distinct from hot feed ("solve") and strong contrarian claim.

### Opening
Original: "When I first read that scaling fixes everything in LLMs, I believed it. It had worked for reasoning benchmarks, for code generation, for long-context tasks. Then I started building agents that needed to use tools — and the pattern broke."

Keep as is. Clean, sets up contrast.

### "What the POMDP Gap Actually Is" section
Original:
"The issue is structural. Tool-use agents operate in a Partially Observable Markov Decision Process (POMDP), not a standard MDP. The agent never sees the true state of the world directly."

Keep. Tight, correct.

Minor: "belief-state planning" — keep, it's the right term.

### "Where I've Seen This Fail in Practice" section
Original: The failure mode I see most: a multi-step tool-use chain where each step compounds the belief-state uncertainty.

Consider trimming "the most" — unnecessary qualifier.

Revised: "The most common failure mode I observe: a multi-step tool-use chain where belief-state uncertainty compounds at each step."

### "What Scale Does and Doesn't Fix" section
Original list is clean. Keep.

"Scale the model last. Fix the information pipeline first." — keep, strong close pair.

### Closing question
"What specific tool-design changes have you found most effective at reducing belief-state errors in multi-step agentic workflows?"

Keep. Non-generic.

## Word Count: ~690 words — within range. No expansion needed.

## Final Draft Summary
No structural changes needed. Minor tightening in one paragraph. Ready to post.
