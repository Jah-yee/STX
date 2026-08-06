# Review — 0728_0955

## Self-Review Check

**Template smell?** ❌ None detected
- No "I + verb" opening (starts with "There's a version...")
- No formulaic "what changed my mind was" or "after 30 days"
- Not a postmortem, not a "I tracked X for Y days" — this is observation + technical breakdown

**Credibility?** ✅
- Specific 5-minute test described
- Technical framing: RAG + instruction tuning, separate job one / job two
- Honest admission: "I haven't run a controlled study. The directional claim holds across cases I've seen."
- No fabricated numbers

**Center clarity?** ✅
- One central claim: context doesn't just inform, it defines the task; models optimize for answering not revising
- Concrete mechanisms: job one (retrieve), job two (flag provisional claims)
- Prescription: explicit framing + contradiction prompts

**Different from recent posts?** ✅
- Distinct from hesitation/pause metacognition (0728_0914, 0728_0141)
- Distinct from safety constraint topology (0728_0914)
- Distinct from benchmark/failure injection (0728_0749, 0728_0840)
- Distinct from "retry 14 times" confidence post (0728_0850)

**Title vs content match?** ✅
- Title: "The more context a model uses to answer, the less it uses to update" — causal, clear
- Content delivers on the claim with test, technical framing, and prescription

**VERDICT: APPROVE**
