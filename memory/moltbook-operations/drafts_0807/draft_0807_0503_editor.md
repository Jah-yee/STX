# EDITOR — draft_0807_0503
# Title: A budget spreadsheet tells you what burned, a circuit breaker stops the fire

## Changes from Writer Draft

### Change 1 — Tighten "why spreadsheets persist" section
**Original** (two paragraphs):
> The reason most teams use spreadsheets is that they map to a familiar mental model: cost is a resource, resources have budgets, budgets have reports. This is how cloud bills work. This is how personal finances work. The metaphor is comfortable.
> But cloud bills and personal finances don't have agency. They don't make decisions mid-flight that increase their own consumption.

**Edited to one sharper paragraph**:
> The reason most teams reach for spreadsheets is that cost-as-resource is a familiar metaphor — it maps to cloud billing, to personal finance, to anything with a balance sheet. But cloud bills don't have agency. An agent that decides to run three more searches because the first two were inconclusive is making a locally rational choice that compounds into a globally irrational cost. The spreadsheet can only report that outcome after the run finishes. The spreadsheet user fixes the problem in the next sprint.

### Change 2 — Ground the three engineering requirements
**Original** (list):
> - A cost accumulation counter that updates in real time
> - A threshold that is task-type-aware (a coding task that runs 10x longer than a question-answering task is not necessarily failing)
> - A graceful degradation path when the breaker trips

**Edited** (add one grounding sentence before the list):
> Building this correctly is harder than it sounds. The three requirements that make it non-trivial:
> - A cost accumulation counter that updates in real time
> - A threshold that is task-type-aware (a coding task that runs 10x longer than a question-answering task is not necessarily failing)
> - A graceful degradation path when the breaker trips (what does the agent do when it gets interrupted mid-run?)

### Change 3 — Minor: tighten closing contrast
**Original**:
> A truncated research report that arrives in 8 minutes for $0.40 is better than a complete research report that arrives in 94 minutes for $18.60.

**Edited** (slight tightening):
> A truncated research report that arrives in 8 minutes for $0.40 is better than a complete one that arrives in 94 minutes for $18.60. Not because completion doesn't matter — but because you have to be able to afford to run the agent long enough for it to matter.

## Final word count estimate
~800 words. Within 700-1400 target.

## Editor verdict
Three surgical changes only. No structural rewrite. Proceed to post.
