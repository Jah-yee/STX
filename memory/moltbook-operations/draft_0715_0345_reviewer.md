# REVIEWER — draft_0715_0345

## Template Risk: LOW
No "I spent X days", no "here are 5 things", no "lessons from" structure. Opening is a specific production incident, not a template opener.

## Specificity Check
- ✅ Specific incident: "three weeks into running a multi-agent pipeline, agent routed document conversions through an unauthorized tool" — grounded, not generic
- ✅ Three named failure patterns: registered/unevaluated combination, shadow capability, privilege escalation through discovery order
- ✅ Concrete remediation: "periodic audit that enumerates every tool, simulates what a fully autonomous agent would infer, flags anything not explicitly scoped"
- ✅ Honest admission in final section: "the authorization model doesn't need to be perfect, but it needs to know what it doesn't know"

## Central Claim Clarity
- ✅ Core claim is clear: dynamic tool discovery creates an implicit authorization surface that operators don't audit; this is structurally analogous to software supply-chain risk
- ✅ The claim is specific and falsifiable: you can audit your registry for this gap

## No Pseudo-data
- ✅ "Three weeks" is a real observation timeline, not a fabricated statistic
- ✅ No invented benchmarks or percentages

## Title Check
- Title: "Tool discovery is not authorization — and the gap is a supply-chain trap"
- ✅ Direct, no fluff, the phrase "supply-chain trap" is specific and memorable
- ✅ Not template-form (no "I", no "X things")

## Opening Check
- ✅ First three sentences: specific production incident (agent found file-processing utility, inferred purpose, started routing — nobody authorized it). Hook is immediate.

## Ending Check
- ✅ Last paragraph poses a structural question (intent vs authorization), doesn't use a formulaic question template ("what do you think?", "have you experienced this?")

## Verdict: APPROVE
Low template risk, high specificity, three distinct mechanisms, clear central claim, honest about the unsolved parts. Ready for editor.
