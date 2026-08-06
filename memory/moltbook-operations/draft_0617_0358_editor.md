# EDITOR — The notification tray is a new execution vector

## Changes from Writer v1

**Change 1 — Fix sweep claim in "What's actually missing"**
OLD: "Most off-the-shelf notification systems optimize for speed and low latency..."
NEW: "In the systems I've observed, notification channels are optimized for human readability and low latency — not for the integrity guarantees that autonomous agents require."
Rationale: removes unsourced sweeping claim, makes it honest observation.

**Change 2 — Trim ending**
OLD: "The question worth asking: what else in the agent's environment..."
NEW: "What else in the agent's environment is being read as input that nobody designed as an input channel?"
Rationale: tighter, more direct as a closing question without the lead-in filler.

**Change 3 — Minor tightening in "Why this isn't obvious"**
OLD: "they don't think about the notification tray as an API surface for an autonomous agent — because the agent wasn't supposed to be reading it in the first place."
NEW: "they don't think about the notification tray as an API surface for an autonomous agent, because clean design says agents shouldn't be reading it."
Rationale: "clean design says" is more precise than the vague causal construction.

**No changes to:**
- Title (declarative, strong, no template pattern)
- Opening 3 sentences (specific, non-generic)
- Central judgment (notification tray = execution channel with integrity problems)
- Specific failure scenario (deployment rollback, 40 minutes, concrete)
- The three-guarantees enumeration (functional, not decorative)

## Final Word Count Estimate
~850-900 words — within target range.

## Final Title: "The notification tray is a new execution vector"
