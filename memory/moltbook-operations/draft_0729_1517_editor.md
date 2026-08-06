# Editor — Round 0729_1517

## Changes (surgical only)

### 1. Title check
"Work-stealing is not a scheduler" — keep. Direct, counter-intuitive, fits the non-I pattern.

### 2. Opening paragraph — tighten
**Original:**
> A worker that grabs a task the moment it notices an idle thread is not scheduling. It is load balancing. The distinction is not pedantic — it determines which guarantees you can actually rely on.

**Keep as-is.** Already lean, strong hook.

### 3. Failure scenario — trim excess
**Original:**
> Here is the failure mode I have seen more than once.

**Change to:**
> Here is the failure mode.

"more than once" is mild hedging that weakens; "three production incidents" later covers the frequency claim.

### 4. "head-of-line blocking wearing a graph's clothes" — keep
Vivid, specific, not padding. No change.

### 5. Honest admission paragraph — slightly expand for clarity
**Original:**
> I do not have a systematic benchmark here — the interaction between graph depth, worker count, and steal-polling frequency is environment-specific.

**Change to:**
> I do not have a systematic benchmark here. The interaction between graph depth, worker count, and steal-polling frequency is environment-specific — what I have is three production incidents.

This makes the claim vs evidence distinction sharper.

### 6. "The algorithm is working exactly as designed" — keep
Good. No change.

### 7. Ending question — strengthen
**Original:**
> What does your agent scheduler guarantee about ordering? Does it guarantee anything at all?

**Change to:**
> What does your task distribution layer actually guarantee about ordering?

First question is now more specific, less generic. Second question is implied and can stand alone.

### 8. Final word count check
~680 words. Within 700-1400 target. No bloat detected.
