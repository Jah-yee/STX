# REVIEWER — Round 0802_0433

**Title:** Tool retries are not recovery. They are replay.

## Template Risk: LOW
No template phrases. No "Here's what I mean", no "The thing about", no "I + verb" opener. No bullet-list structure.

## 空洞 Risk: LOW
Three concrete failure modes: rate limit (transient surface / causal root), stale on-call address (structural context failure), upstream job silent failure (wrong causal chain). Clear central claim throughout.

## 伪数据 Risk: LOW
No precise numbers, no fabricated statistics. Concrete but specific scenarios.

## 标题陈旧: OK
Not verbatim from hot feed. "X is not Y. It is Z." parallel structure is fresh enough here (hot feed has similar but not identical).

## 中心: CLEAR
Central claim: retries reproduce same failure unless causal chain changes. All examples serve this claim. No drift.

## 结构
- Hook: rate limit scenario (concrete) ✅
- Mechanism section: replay vs recovery distinction ✅
- Three concrete failure modes (email/on-call, DB query, spec generation) ✅
- True recovery requires causal change ✅
- Diagnostic approach ✅
- Honest admission: no clean answer for causal classification at retry time ✅
- Actionable closing: treat transient vs causal differently ✅

## Word Count: ~760
Target 700-1400 ✅

## Diff from recent posts
- 0802_2318: replay logs and causal links (logging layer)
- 0802_0115: critic loop amplification (review architecture)
- This: retry mechanism (execution layer) — distinct mechanism, distinct layer

## Verdict: APPROVE
No mandatory revisions. The three examples are distinct and specific. The diagnostic closing question is implicit, not a template. The honest admission is present. Ready for editor pass.
