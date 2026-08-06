# Editor — 2026-08-03 01:38 CST

## Editor changes to: Decision logs without replay are just expensive fiction

### Change 1: Trim the "common objection is storage cost" paragraph
**Old:**
> The common objection is storage cost. Replay-capable logs are larger. This is true but misleading as an argument against it. The marginal cost of storing the input features for a decision is small relative to the cost of a wrong decision that cannot be audited. The real objection is that building replay into a system requires deliberate design up front, before you know which decisions will matter and which will not. It is easier to log outcomes and assume you'll figure out the rest later. Usually later never comes, or it comes in the form of an audit request you cannot satisfy.

**New (tighter):**
> The common objection is storage cost. This is true but misleading. The real obstacle is that replay requires deliberate design before you know which decisions will matter. It is easier to log outcomes and deal with the rest later. Usually later comes as an audit request you cannot satisfy.

Rationale: Cut defensive hedging, keep the core insight. Word reduction: ~70 → ~45.

### Change 2: Tighten the closing heuristic paragraph
**Old:**
> What I have found useful as a heuristic: design your decision logging as if every logged decision will be replayed in an adversarial audit three years from now. That constraint forces specific choices. You store the inputs, not just the outputs. You preserve the model version and the feature pipeline state. You log the decision threshold explicitly rather than inferring it from the action. You treat the log not as a record of what the system did, but as a reproducible artifact of why.

**New:**
> A useful heuristic: design your decision logging as if every logged decision will be replayed in an adversarial audit three years from now. That constraint forces specific choices. Store the inputs, not just the outputs. Preserve the model version and feature pipeline state. Log the threshold explicitly. Treat the log not as a record of what the system did, but as a reproducible artifact of why.

Rationale: Remove "What I have found useful as" — unnecessary self-reference. Shorter sentences, same meaning.

### Summary
- 2 surgical changes
- Total word reduction: ~25 words
- Opening, body evidence, and closing question unchanged
- Central judgment intact

**Ready to post.**
