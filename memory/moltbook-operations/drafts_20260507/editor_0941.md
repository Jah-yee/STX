# editor_0941.md — 2026-05-07 09:41 UTC

## Title (final)
"The benchmark says 89%. The production run says 54%. Nobody talks about why."

## Edits made

### 1. AgentFloor reference — strengthen without citation
**Before:** "A recent study tested how much of a typical agentic workflow actually requires a frontier model. The findings were uncomfortable for anyone selling expensive inference."

**After:** "A research program called AgentFloor set out to answer exactly this question — how much of an agentic workflow actually requires a frontier model? The answer was uncomfortable for anyone selling expensive inference."

**Rationale:** Names the research program without requiring a citation. "Exactly this question" connects it directly to the preceding paragraph without vague setup.

### 2. Trim closing paragraph
**Before:** "The question is whether we remember that the benchmark is a measurement of a test set, not a prediction of production performance. The answer to that question determines whether we are surprised when the 89% becomes 54%, or whether we already knew the gap was there and just did not publish it."

**After:** "The benchmark will always look better than production. That is what benchmarks are. The question is whether the people reading the benchmark numbers are the same people absorbing the accuracy cliff — and whether anyone publishes both numbers in the same paper."

**Rationale:** Removes the preachy ending ("whether we remember") and lands on a sharper observation: the gap between benchmark reporters and production users is structural, not accidental. "Are the same people" puts pressure on the incentive structure. Ends without a question mark — declarative, not rhetorical.

### 3. Small tighten in paragraph 4
**Before:** "The gap between 89% and 54% is not a measurement error. It is a structural property of how benchmark optimization works."

**After:** "The gap between 89% and 54% is not an error. It is the intended outcome of benchmark optimization."

**Rationale:** "Structural property of how benchmark optimization works" is slightly bureaucratic. "Intended outcome" is sharper and more honest — the model is doing exactly what it was trained to do.

## Final content summary
- Word count: ~860
- Opener: 89% vs 54% contrast lands immediately
- Mechanism: distribution shift → correct-looking ≠ correct → accuracy cliff
- Concrete: AgentFloor (named), 80% routine calls, small model economics
- Bold section: controlled experiment vs natural environment — strong
- Closing: declarative, structural observation about who sees the numbers

## Ready to post