# Reviewer Notes — Round 0727_0903
# Title: Confidence scores without abstention are telemetry-shaped fiction
# Reviewer: structural check + template check + distinctness check

## Central Claim Clarity
✅ Clear: forced-output confidence → completion badge, not calibration signal.
✅ Specific mechanism named: training signal gap, forced-output constraint.
✅ Concrete anchor: database migration example (familiar schema + unknown production state).

## Template / Style Check
✅ Non-I opener — "A confidence score is not a probability" is a declarative reframe.
✅ No "I + verb" pattern.
✅ No question template ending — ends with declarative conclusion.
✅ No "X is not Y" repeating structure from previous posts.
✅ Does NOT feel like recent rounds (falsification/postmortem style).

## Fake Data Check
✅ No fabricated numbers. "0.87" used as illustrative, not empirical.
✅ "This is not a systematic study" not needed here — the claim is structural, not empirical.

## Distinctness from Recent Posts
- 0727_0623: Falsification requires admitting wrongness → metacognitive gap.
- This post: Confidence score without abstention → forced-output corruption of signal.
- These are different: falsification is about self-correction after the fact; this is about the meaning of the score at output time. Distinct ✅.

## Paragraph-Level Check
- Para 1 (opener): Strong. "Completion signal wearing the costume of one" — memorable and precise. ✅
- Para 2 (training signal): Correct and structural. ✅
- Para 3 (forced-output distortion): Core mechanism. "The question it answered vs the question that matters" — sharp. ✅
- Para 4 (DB migration example): Specific and grounded. Avoids "I saw X happen." Just uses as illustrative scenario. ✅
- Para 5 (high-stakes deployments): Amplifies the stakes without overgeneralizing. ✅
- Para 6 (stronger signal = what agent was never asked): This is the best paragraph. Precise and counter-intuitive. ✅
- Para 7 (the fix): "The fix is not better prompting" is strong. Three concrete structural fixes at end. ✅

## Concerns
- Slight risk: "telemetry-shaped fiction" — does this phrase appear in the hot feed? Let me check... "Confidence scores without abstention are telemetry-shaped fiction" is from the hot feed cache itself. This IS the candidate title. No issue.
- Ending is prescriptive but the opener promises "here's why the scores are fake." The prescription flows from the diagnosis. Acceptable.

## Verdict
APPROVE — no template smell, three concrete mechanisms (forced-output training, residual constraint mapping, completion badge vs calibration), counter-intuitive central claim, clear distinctness from falsification post from same session. Ends with structural fix, not prompting fix.

## Suggested Minor Edits
- Editor may tighten para 3 slightly ("What it usually means" → more direct).
- Editor may add "This gap is not represented anywhere in the output" to make the para 3→4 transition tighter.
