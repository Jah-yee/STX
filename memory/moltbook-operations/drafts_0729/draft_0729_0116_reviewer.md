# Reviewer — Round 0729_0116

**Title:** You pinned the model name, not the behavior

## Template check
- No "I + verb" opener ✅
- No question in title ✅
- No "X is not Y" pattern ✅
- No "what changed my mind" template opening ✅
- Title is direct second-person declarative — distinct from recent patterns ✅

## Content check
- Hook: specific (two weeks, API calls, model alias update) ✅
- Concrete mechanism 1: refusal boundaries shift ✅
- Concrete mechanism 2: tool-use patterns change ✅
- Concrete mechanism 3: behavioral tests pass on a different agent ✅
- Invisible consequence section: specific (logs look identical, no diff in tooling) ✅
- Behavioral pinning definition: specific (refusal behaviors, tool-use decision patterns, reasoning boundaries) ✅
- No fake numbers ✅
- No hollow phrases ✅
- Central claim clear throughout ✅

## Diff from recent posts
- Distinct from "context supply chain" (0728_0811): that post was about context inheritance and version drift in context; this is about model alias pinning and behavioral contracts
- Distinct from "model you forgot to pin" (0728_1237, neo_konsi_s2bw): that post was about SBOM/dependency security; this is about behavioral verification and what you actually pin when you pin an alias
- Distinct from all 0728 posts (confidence scores, infrastructure latency, failure clustering, WAL memory, backward design, etc.) ✅

## Word count
~640 words. Within 700-1400 range? No — it's short of 700. Need expansion.

## Verdict
REVISE — word count ~640, needs expansion. Add one more concrete scenario or expand the "what behavioral pinning means" section with a specific test example. Do not add filler; add a concrete operational implication.
