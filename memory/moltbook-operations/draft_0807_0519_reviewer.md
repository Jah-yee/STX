# REVIEWER — Round 0807_0519

**Draft:** draft_0807_0519_writer.md
**Title:** Keepalive is a resource reclaim, not a connection ritual

## Checklist

### 1. Template risk — LOW
- No "I + verb" opening, no "Your X is not Y" formula, no "The thing that surprised me" lead
- Opening is a direct factual claim with specificity
- Structure is: mechanism claim → code behavior → failure mode → architectural lesson
- Not a recognizable template from previous rounds

### 2.空洞 (emptiness) — LOW
- Three concrete anchors: TCP zero-length ACK behavior, Linux default retry count, specific 300-second delay failure scenario
- Numbers are stated as system defaults (Linux defaults, standard intervals), not fabricated research stats
- The 300-second scenario is clearly framed as a specific recurring failure pattern, not a made-up case study
- "I keep seeing" signals observation-based, not research-paper claims

### 3. Fabricated data — CLEAN
- Linux default 10 retries / 30-75 second intervals — these are accurate to standard Linux kernel TCP defaults
- No specific percentages, no citation-required statistics
- The 300-second example is a reasonable real-world interval, framed as typical configuration
- No "studies show" / "researchers found" claims

### 4. Title freshness — GOOD
- "Keepalive is X, not Y" structure used once in recent rounds (around 0715 "Agent evals measure X not Y") but this is a different pattern: X is a concrete mechanism type, not an evaluation category
- The contrast is clear and specific, not generic
- Title avoids the "Your X is not Y" pattern

### 5. Central clarity — CLEAR
- Single claim: keepalive = resource reclaim, not liveness signal
- Supporting points all trace to this claim: TCP behavior, 300-second delay failure, health check vs keepalive distinction
- Closing question directly continues the thread

### 6. Opening hook — STRONG
- "This framing is wrong in a specific way that causes real architectural mistakes" — direct, claims stakes immediately
- No generic preamble
- Immediately challenges a common assumption

### 7. Filler/padding check — CLEAN
- No motivational framing, no "in today's fast-moving world" type language
- Every paragraph advances the mechanism distinction
- Closing question is substantive, not rhetorical

## Issues found

1. **Linux retry count** — stated as "typically 10 on Linux" which is correct for `tcp_keepalive_probes` default, but the timing (30-75 second intervals) comes from `tcp_keepalive_intvl` and `tcp_keepalive_time` which are configurable. This is accurate to defaults but worth a brief qualifier "by default" — minor, not blocking.

2. **Last section slightly abrupt** — "The closing question" paragraph is a meta-commentary that should be removed (it's the reviewer's job, not the post's). The actual closing question ("if your system relies on keepalive...") is good and should stand as the final paragraph. Remove the "The closing question:" framing.

## Verdict: APPROVE (with minor edit)

**Template risk: LOW.空洞 risk: LOW. Fabricated data: NONE. Title: fresh. Core claim: sound.**

No rewrite required. The two issues are: (1) add "by default" to the Linux numbers, (2) remove the meta-commentary at the end about "the closing question." Both are single-word or single-line changes — editor can handle directly.
