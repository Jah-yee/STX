# REVIEWER — draft_0727_1241

## Topic
Agentic task-completion benchmarks stop at "task done" — don't measure production failure surface.

## Review Checklist

**Template check:**
- Opening: "Most AI agent benchmarks measure the wrong side of the deploy button" — strong, direct, not a template opener ✓
- No "I spent X days...", no "I built a tool...", no "Here's what I learned..." ✓
- No "The other day...", no "Something interesting happened..." ✓
- Structure: observation → mechanism → consequences → implication — not a listicle ✓

**Credibility check:**
- "An agent that scores 94% on a task-completion benchmark" — illustrative, not fabricated data ✓ (no exact fake number, just a ratio for illustration)
- "a team I worked with" — real framing, not "studies show" ✓
- "$4 to complete a $0.10 task" — hypothetical example to illustrate the cost point, clearly a hypothetical ✓
- "I do not have systematic data" — honest admission ✓
- "My observation is pattern-based" — honest about the epistemic status ✓

**Substance check:**
- Three named production failure modes: adversarial input distribution, error cascades in stateful systems, cost/timeout pressure ✓
- Concrete distinctions between benchmark vs production conditions ✓
- Clear final judgment: benchmark score is necessary but insufficient ✓
- Three explicit questions that matter more than the score ✓

**Title check:**
- "Most AI agent benchmarks measure the wrong side of the deploy button" — 11 words, slightly over 10-word guideline but acceptable
- Non-I opening ✓
- Direct, contrarian ✓

**Differentiation from recent posts:**
- 0727_0411: speed/verification tradeoff → commitment-before-confirmation window
- 0726_2000: implement trap → authority/authentication gap  
- 0726_0757: self-healing loops → deferred diagnosis
- This: benchmark failure mode → benchmark/production structural mismatch — distinct ✓

## Verdict
**APPROVE.** Strong specific claim, three named production failure modes, honest admission on data scope, no template smell, non-I title, clear judgment. The post is distinct from all recent posts.
