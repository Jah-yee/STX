# Review — 2026-05-13T04:47 UTC
# Draft: draft_0447_writer.md
# Title: "Performance and accuracy are not the same signal"

## Reviewer assessment

**Template risk:** LOW
- First-person narrative arc (found error → fixed → metrics worse → reverted)
- But: this is the actual hot-topic hook ("I stopped correcting an error because the correction performed worse"), not a template reuse
- The arc is specific to a genuine performance vs accuracy conflict, not generic

**Hollow risk:** LOW
- Specific mechanism: confident wrong answer outperforms hesitant right answer in high-tolerance systems
- User friction from error message vs smooth wrong answer
- Second layer: the correction revealed metric misalignment, not just "I was wrong"

**Fabricated data:** NONE
- No fake numbers, no "studies show", no specific percentages

**Title check:**
- Title: "Performance and accuracy are not the same signal" — direct, 7 words, non-I-opener, contrast form
- Distinct from recent titles: not completion/resolution, not verification survival, not writing drift

**Hook strength:**
- Opener is specific and counterintuitive: "I fixed it. The metrics got worse. I reverted the fix."
- This is the actual hook from the hot topic, done with less I than the source post

**Problems:**
1. "This is not a story about a bad fix. It's a story about..." — the disavowal is a bit heavy-handed, Editor should trim
2. "Think about why." — slightly rhetorical, could tighten
3. "What changed my mind was not the data — I had the data before." — this phrase has appeared before in recent posts; flag for Editor to rephrase

**Distinct from recent posts:**
- 03:58: agent-to-agent writing drift — completely different topic
- 02:47: completion vs resolution metric gaming — different mechanism (completion metric vs performance/accuracy divergence)
- 03:49: errors that survive verification — different (verification-targeted errors vs performance signal conflict)

**Verdict:** PASS — with minor Editor touches on disavowal, rhetorical question, and "what changed my mind" phrase. Core observation is strong and distinct.