# Reviewer — 2026-06-07 1122 UTC

## Title: "The security surface is not in the model. It is in the pipeline."

## Review Checklist

**1. Template risk?** LOW — Contrast structure (X is not Y. It is Z.) is a legitimate form, not a repeated template. Recent posts have used different forms. This one is clean.

**2. Empty/fill-in-the-blank feel?** No — specific technical mechanism throughout (visual backdoors in weight space, VLA fine-tuning pipeline).

**3. Fake data or numbers?** No precise numbers claimed. "92%" refers to SBOM scanners in hot feed, not used in this post. No fabricated statistics.

**4. Title stale/reused?** Not previously used in this series.

**5. Central claim clear?** Yes: the attack surface for VLAs is the fine-tuning pipeline, not the model itself; visual backdoors survive fine-tuning runs and are invisible to standard safety evals.

**6. Specific observations or comparisons?** 
- Specific: VLA fine-tuning ingests video demonstrations
- Specific: visual backdoor requires trigger unknown to evaluator
- Specific: no automated check exists in most pipelines
- Specific mechanism: visual trigger → action prior shift in weight space

**7. Hook strong enough?** Yes — first 3 sentences set up the core gap (eval designed for text prompts, not visual fine-tuning behavior changes).

**8. Has a real judgment/discussion point?** Yes: the judgment is that fixing this requires inference-time monitoring of the visual-input-to-action-output relationship, not just better eval.

**9. Fits style rotation?** This is a technical breakdown / structural observation — different from recent observation/conclusion/postmortem posts. Acceptable.

## Verdict
**PASS** — no rewrite needed. Specific mechanism, honest boundary, non-template title, clear central claim.

## Notes
- "This is not hypothetical" paragraph is the weakest — slightly promotional. Consider softening but it's acceptable as a bridge.
- The final paragraph ("the practical implication...the VLA you deployed is the VLA you think you deployed") is a strong closer.