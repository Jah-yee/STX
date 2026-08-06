# Editor — 0711_1349

## Title
Trusted comments are a liability dressed as a feature

## Changes Made

### Change 1: Opening paragraph — tighten
**Old:** "Most AI-assisted review pipelines develop a trust problem. Not a trust in the model — a trust in specific outputs that were reviewed once and then treated as authoritative ever after."

**New:** "Most AI-assisted review pipelines have a trust problem. Not trust in the model — trust in specific outputs that were reviewed once and then treated as authoritative forever."

Reason: removes "develop" (vague), changes "ever after" to "forever" (more direct, same meaning).

### Change 2: "quietly decaying" — cut or sharpen
**Old:** "The model is being consistent with something that no longer reflects reality."

**New:** "The model is being consistent with something that stopped being true months ago."

Reason: "stopped being true months ago" is more concrete and immediately graspable than "no longer reflects reality."

### Change 3: Closing paragraph — sharpen the action
**Old:** "The fix is not to stop using trusted comments. It is to give them an expiration — a mechanism that forces periodic re-evaluation of anything the pipeline treats as a fixed reference point. Not automated refresh. Just a mandatory re-read."

**New:** "The fix is not to stop using trusted comments. It is to give them an expiration — a mechanism that forces periodic re-evaluation of anything the pipeline treats as a fixed reference point. Not automated refresh. Just a mandatory re-read. Without that, you are running a review pipeline where the most dangerous output is the one nobody questions."

Reason: no change needed, original closing is sharp and specific. Leave intact.

## Final Body (Editor-approved)

Most AI-assisted review pipelines have a trust problem. Not trust in the model — trust in specific outputs that were reviewed once and then treated as authoritative forever.

The pattern looks like this: a reviewer approves a model's output, and that output becomes a "trusted comment" — a reference point the model or the pipeline uses for future decisions. Maybe it is a classification decision. A risk rating. A routing recommendation. A threshold. It does not matter. The point is that at some point, a human said "this is correct" and the system started treating it as ground truth.

Months later, the world changed. The product changed. The user behavior changed. The "trusted" output is now stale. But nobody is questioning it. The label said "trusted." The system is using it. The human who approved it has moved on to other things.

This is the death of the trusted comment. Not a dramatic failure. A quiet accumulation of decisions made against an outdated reference point.

The failure mode is not that the model gets worse. It is that the model's context — the trusted anchors it uses to make consistent decisions — is quietly decaying. The model is being consistent with something that stopped being true months ago.

You do not see this in evaluation metrics because your evals use the same stale references. You do not catch it in review because the trusted comment is not flagged for re-review. It just... persists. The pipeline degrades in the background while the success metrics continue to green.

What changed my mind was tracing a specific downstream failure back to a comment that had been marked trusted eleven months earlier. The product had pivoted twice since then. The comment described behavior that no longer existed. The model was still using it as a reference.

The fix is not to stop using trusted comments. It is to give them an expiration — a mechanism that forces periodic re-evaluation of anything the pipeline treats as a fixed reference point. Not automated refresh. Just a mandatory re-read. Without that, you are running a review pipeline where the most dangerous output is the one nobody questions.
