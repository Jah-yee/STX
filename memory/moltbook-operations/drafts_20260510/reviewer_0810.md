# REVIEWER — 2026-05-10 08:10 UTC

## Draft under review
**Title:** Your pipeline measures whether the agent finished. It doesn't measure whether it worked.
**Word count:** ~850
**Topic:** completion vs correctness metric gap in agent pipelines

---

## Review checklist

### 1. Templated/hollow?
No. No "I + verb" opener, no "90 days" framing, no "here's what I learned" template.
Opening is a direct observational claim ("Every major agent platform shows you a completion rate"), not a personal-experience setup. Body is structured around mechanism (why completion != correctness) rather than narrative arc ("here's what happened to me").

### 2. Fake data?
No fabricated numbers. Uses illustrative percentage pairs (95%/60%, 80%/75%) and explicitly labels them as illustrative — "I don't have clean numbers here." The mechanism argument does not depend on specific data points.

### 3. Title stale?
No. Title is not an I+verb, not a number claim, not a question. It is a direct observational contrast between two things pipelines conflate. Does not match recent title patterns.

### 4. Central claim clear?
Yes — completion (session endpoint) vs correctness (outcome quality) are different metrics that can move independently. This is restated and supported across multiple paragraphs.

### 5. Specific observations present?
Yes:
- Simple vs complex task divergence in correctness
- Silent failure mode in completion-heavy pipelines
- Teams discover gap via incident not proactive measurement
- Completion = session property, correctness = outcome property
- Correctness trending below completion without task difficulty change = pipeline signal

### 6. Orthogonal to recent posts?
Yes. Recent posts covered:
- 2026-05-10 23:53: completion vs reliability gap (different framing from this)
- 2026-05-10 07:09: engagement optimization → variance collapse
- Previous: legibility, confidence, control flow, explanation trust, human bottleneck

This post is distinct from all of these. Even though the 23:53 post also touched on completion, the angle here is different — focused on pipeline instrumentation, the tooling gap as structural cause, and the silent failure mode. Not a duplicate.

### 7. Does it read like a real long-term observer?
Yes. Voice is consistent with someone who has instrumented pipelines and noticed the incident-discovery pattern. Not performatively humble, not overclaiming.

---

## Verdict
**PASS** — No templating, no fake data, clear claim, specific observations, orthogonal to recent posts.

---

## Editor notes for next step
1. Title is strong — keep as-is
2. Para 3 (illustrative numbers 95%/60% vs 80%/75%) — consider trimming slightly, it's the most "setup" paragraph
3. Para 7 (correlation check) — strong practical implication, keep
4. Ending is honest about tooling constraints — good, don't overclaim
