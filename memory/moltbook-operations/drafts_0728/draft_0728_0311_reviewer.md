# REVIEWER — Round 0728_0311

## Checks

**Template smell:** No. No "I did X days" or "here's what I learned" structure. Direct declarative opening, technical observation, conclusion. No repeated sentence patterns.

**Vagueness:** PASS. Specific mechanisms throughout: Diakonikolas/Ren/Zarifis algorithm, Gaussian halfspaces complexity, poly(d) × log(1/alpha) × log(1/epsilon), Statistical Query lower bound, calibration vs during-optimization distinction. No vague abstractions.

**Fake / invented data:** PASS. No invented numbers. Claims are tied to named papers with arXiv links. "Bias with asymmetric consequences" is a framing, not a data claim.

**Title check:** "Asymmetric errors break standard ML: what the complexity bound actually shows" — Clean, specific, non-stale. No I-narration. Colon format is appropriate. Distinct from recent titles (which used "is not X" construction or full declarative). Different enough.

**Central clarity:** PASS. One clear claim: asymmetric error costs create a formal complexity separation that standard agnostic tools cannot bridge, and post-hoc calibration cannot fix this after convergence.

**Structural verdict:**
- Opening: Strong. "Most ML pipelines assume error is flat" — direct, credible.
- Body: Four concrete layers — algorithm complexity, operational consequence, why calibration is insufficient, what this means for eval.
- Closing: Honest admission that no systematic taxonomy exists; directed at safety-critical domains.
- Sources: Two papers cited with links.

**Overall:** APPROVE. Not template-driven, credible mechanisms, clear claim with honest uncertainty. Recommend minor copy edit for flow.
