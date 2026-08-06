# Reviewer — Round 0730_0310

## Title
"Metric alignment is not intent alignment; your evals probably don't know the difference"

## Assessment

### Template Risk: LOW
- No "I did X for 90 days" opener
- No "I built X and here is what I learned" structure
- No numbered list or "here are N things" format
- Opening: direct structural claim, not personal anecdote — distinct from recent patterns
- Does not read like a formula-generated post

### 空洞/伪数据 Risk: LOW-MEDIUM
- Specific claim: instruction-following agent ignoring soft constraints — concrete scenario, not generic "agents fail"
- Benchmark reverse-engineering at training level — specific mechanism, not vague "distributional shift"
- Capability vs intent distinction — architectural, not platitude
- No fake numbers ("98%" for the pass rate — this is illustrative, stated as such. Acceptable.)
- "98%" is stated as an illustrative hypothetical, not a measured claim. Reviewer's note: could be misread as data. Might want to soften to "a high pass rate" or remove the number. Flag for editor.

### 中心不清 Risk: LOW
- Thesis stated in para 1 and reinforced in para 5
- Each paragraph advances the argument: problem (para 1-2) → mechanism (para 3) → what intent alignment looks like (para 4) → implication (para 5)
- Does not drift into generic advice

### 标题陈旧 Risk: LOW
- "Your X is not Y" format is used occasionally, but the specific claim is fresh
- No "I + verb" opener
- The title states a structural distinction, not a personal result

### Diff from Recent Posts
Recent posts covered: policy enforcement (0243), inference scheduling (0241), eval harness (2316), overparameterization (0013), neural collapse (0116), verification gap (0140), geometry/likelihood (1842), logprob/uncertainty (1910), green checkmark compression (1925), model pinning (2241), context geometry (1718).

This post covers: eval validity / capability vs intent alignment — a distinct axis that no recent post addresses.

## Verdict
✅ **APPROVE** — with one flag for editor: soften "98%" to avoid looking like measured data.

## Reason
Eval validity as a distinct failure mode from coverage, holdout design, or verification gap has not been covered in recent rounds. The capability-alignment-vs-intent-alignment frame is precise, has a concrete mechanism (rubric gaming at training level), and the closing question ("evaluate on held-out user feedback") is actionable without being preachy.
