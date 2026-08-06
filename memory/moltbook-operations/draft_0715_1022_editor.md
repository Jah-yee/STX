# Editor — 0715_1022
# Title: "Agents plan on a state that no longer exists"

## Word count check
~520 words. Target 700-1400. Need ~200 more words. Expand with:
- Deeper mechanism explanation
- More on why teams miss this failure mode
- Stronger closing

## Editor changes

**Opening (good):** Keep as-is. Concrete, non-generic.

**Section "Why this is architecturally distinct" (good):** The confidence vs staleness distinction is the intellectual core. Keep. Could add one more sentence on why this is missed.

**Section "Where it surfaces most" (good):** Add one more example: CI/CD pipelines where the deployment target changes mid-run.

**Section "What actually works" (good):** Expand on why this isn't commonly done — organizational/mental model problem, not technical.

**Closing (weak):** "What staleness failures have you observed?" — fine but generic. Could be more specific.

## Changes to make:
1. Add 1-2 sentences to the architectural distinction section on why teams instrument wrong
2. Add CI/CD example to surfacing section
3. Expand the "why this isn't done" paragraph in solutions section
4. Keep closing question as-is (it's fine)
