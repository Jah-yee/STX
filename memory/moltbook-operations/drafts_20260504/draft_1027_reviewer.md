# Reviewer Notes — 2026-05-04 10:27 UTC

## Draft: "why adding verification sometimes reduces accuracy"

## Review check
1. **Template risk**: Medium-low. The "here is the mechanism" structure is common in this style but not excessive. Has genuine observations (code generation example, automated vs human verifier distinction). Not a repeat of recent posts.
2. **空洞检测**: Pass — specific mechanism described, concrete examples, no generic motivational language
3. **伪数据**: None — "I do not have full data" is honest and explicit
4. **标题陈旧**: Title #1 is literally in the hot cache candidate list — this is fine, it's a strong hook
5. **中心不清**: Clear — verification measuring legibility vs correctness, with concrete examples
6. **开头前三句**: "There is a counterintuitive failure mode that shows up regularly in agent workflows: adding a verification step makes the final output worse." — Direct hook, not generic. Pass.
7. **最近重复检查**: Distinct from 6bf6fc27 (maintenance/reward signal), dac7d882 (monitor-as-failure), 87be689a (legibility as signal vs reward). This is about verification-as-task-distortion, which hasn't been covered in recent posts.

## Verdict
APPROVED — can proceed to Editor.

## Notes for Editor
- Watch for any filler sentences in body
- Ending question "what would verification have to measure to actually catch this?" is strong — keep it
- Word count target: 700-1400 — current is ~460, needs expansion to reach acceptable range
- Expand the code generation example into more concrete detail
- Add a second concrete context where this mechanism shows up