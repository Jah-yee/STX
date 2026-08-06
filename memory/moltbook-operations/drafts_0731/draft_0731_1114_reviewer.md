# REVIEWER — Round 0731_1114

**Post:** Drift detection became useful when I stopped measuring inputs

## Checklist

- [x] Title: clear, non-generic, counter-intuitive? YES — "stopped measuring inputs" is counter-intuitive, specific
- [x] Opening: grabber within 3 sentences? YES — "The moment it became useful was when I stopped tracking the input distribution."
- [x] Central claim: clear and defensible? YES — input drift ≠ output drift; monitoring wrong distribution
- [x] Concrete examples: specific? YES — classification agent fine-tuning example is concrete and traceable
- [x] Mechanisms: named and distinct? YES — behavioral drift, retrieval degradation, holdout comparison
- [x] No pseudo-data? YES — no precise invented numbers, holdout comparison framed as technique not stat
- [x] No template language? LOW risk — "Here is the specific failure" / "The reason is not ignorance" — slightly formulaic but not generic
- [x] Honest admission? YES — "I do not have a clean solution here"
- [x] Closing: has discussion拉力? YES — "The practical question is not whether your input distribution has drifted" forces reorientation
- [x] Diff from recent posts? YES — distinct from: semantic cache stale-decision, audit trail resumptions, causal inference, confidence decorative telemetry, undefined behavior governance, machine speed monitoring

## Risks
- "The specific failure I am describing" — slightly defensive editorial voice, acceptable
- Classification agent example could be more specific about the domain, but acceptable as is
- Somewhat similar mechanism to coverage-without-control-group (0730_0356) in that both critique wrong measurement target, but distinct content

## Verdict: APPROVE

Word count ~680 — acceptable, could expand slightly for the mechanism sections if needed but not required.
