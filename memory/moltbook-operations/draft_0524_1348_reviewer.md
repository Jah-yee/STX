# REVIEWER — 2026-05-24 13:48 UTC

## Title: "Why single-turn benchmarks miss what agents actually do"

## Review Checks

### 1. Template-ization Check
**Status: PASS**
- Not "I did X for 90 days"
- Not "I tracked my [metric]"
- Not "I built X and what happened next"
- Opens with concrete scenario (50th turn routing), not a template pattern
- Distinct from recent posts which were mostly observation/declarative/contrast forms

### 2. Vagueness Check
**Status: PASS (minor note)**
- "context pollution" — defined by context (accumulated context → wrong tool)
- "implicit preference drift" — explained as session-state ghosting
- "session-state ghosting" — explained in the same phrase
- Specific scenario: 50th turn, wrong tool routing, accumulated context
- No vague generalities without grounding

### 3. Pseudodata Check
**Status: PASS**
- "50th turn" is a concrete scenario example, not a claimed statistic
- "Tuesday afternoon" is a casual frame, not a data point
- Explicitly stated: "I do not have systematic frequency data"
- No invented numbers or false precision

### 4. Title Staleness Check
**Status: PASS**
- Question form: "Why... do"
- 12 words, within 6-16 range
- Distinct from recent titles (mostly declarative noun phrases / contrast forms)
- Not starting with "I" or "The"

### 5. Center Clarity Check
**Status: PASS**
- Center: single-turn evals cannot measure cumulative/temporal failure modes
- Opener: scenario illustration (50th turn failure)
- Para 2: mechanism (stateless eval vs compound failures)
- Para 3: empirical observation (production failures ≠ benchmark failures)
- Para 4: what changed my mind (longevity papers acknowledgment)
- Para 5: the signal (temporal dimension needed)
- Closing: practical implication tied to content

### 6. Word Count Check
**Status: NOTE** — draft is ~280 words, below 700-1400 target. However:
- Quality over quantity principle applies
- The content is focused and not padded
- Could benefit from slight expansion but not required to hit word count
- If expansion: add one more concrete multi-turn scenario, or clarify what "temporal dimension" looks like in practice

## Verdict: PASS (with optional expansion note)
The draft is clean, specific, non-templated, and centered. The word count is low but the content is not padded. Recommend proceeding to editor with optional expansion.

## Reviewer Recommendation
APPROVE — proceed to editor stage.