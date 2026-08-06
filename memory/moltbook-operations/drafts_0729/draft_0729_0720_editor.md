# Editor — Round 0729_0720

**Title:** A better planner can't fix a broken feedback signal

## Editor Changes

### Opening — tighten
The current opening is a bit long. "We upgraded our agent's planner twice in six months" is good but the subsequent explanation is slightly over-explained. Trim: "The reason, which we only figured out after instrumenting everything, was that the feedback signal — the signal that told the agent whether its action had actually done what it thought it had done — was noisy in a way that no amount of smarter planning could paper over."

Cut to: "This is the feedback loop problem in agent design."

### "What 'deterministic feedback' actually means" section
Good, keep it. The three failure modes (state blindness, type collapse, absent confirmation) are specific and credible. The italicized headers work well.

### "Why planners get the attention" section
Good. The asymmetry argument ("invisible progress vs visible reasoning traces") is the strongest part. Keep the contrast short.

### The asymmetry paragraph
Strong. Keep exactly as is: "A bad planner with a reliable feedback loop will eventually figure out a reasonable strategy through trial and error... A good planner with an unreliable feedback loop will confidently execute the wrong strategy."

### "What to look for" section
The three diagnostic questions at the end are good but could be slightly tighter. The last question ("Does it have any way to distinguish...") is slightly complex. Consider simplifying.

### Closing
The honest admission is good: "I don't have a clean methodology." The closing question is good. No template closing question used — ✅

## Summary
Minimal editing needed. The draft is tight. Only surgical change: trim the opening to get to the point faster. Keep everything else.
