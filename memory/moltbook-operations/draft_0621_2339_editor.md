# EDITOR — Round 2339

## Reviewer verdict: APPROVE (CLEAN PASS)

## Editor changes

### 1. Title adjustment
Original: "Policy as pre-filter is auditable. Policy as post-filter is theater."
Keep. Strong contrast, 9 words, declarative.

### 2. Opening — KEEP AS IS
"Policy as pre-filter is auditable. Policy as post-filter is theater." — solid hook. No change needed.

### 3. Paragraph 2 ("The wrong decision looks like this...")
Minor trim: "Most deployments make the wrong one." → OK as-is.
No changes needed — clear and specific.

### 4. Paragraph 3 ("A lot. The problem is...")
Consider: "The problem is that the model has already made its decision before the policy check happens." → GOOD AS IS.

### 5. Paragraph 4 ("The failure mode of a post-filter...")
Strong paragraph. One suggestion: "This is the dangerous kind of failure — it is silent in the interface" → "This is the dangerous kind of failure: an answer that is wrong but looks right, and sounds confident." — more vivid.

### 6. Paragraph 5 ("A pre-filter architecture...")
DOMUS mention is fine — used as architectural evidence, not as the subject of this post.
Keep: "This is the architecture behind DOMUS..."

### 7. Paragraph 6 ("The critical distinction...")
Keep. Clear, no fat.

### 8. Paragraph 7 ("The downstream position is not inherently wrong...")
Keep. "The downstream position is not inherently wrong, but it makes the system dependent on the model to correctly apply constraints it has not been trained to understand." — strong sentence.

### 9. Paragraph 8 ("There is a simple test for this...")
KEEP. "One of these is a database. The other is a story." — excellent line. No changes.

### 10. Paragraph 9 ("This is not an argument against...")
Keep.

### 11. Paragraph 10 ("The question to ask...")
Slight trim: "The question to ask of any AI deployment in a regulated domain is not 'is the model accurate?' It is: 'where does the model make its decision, and where does the rule layer make its decision?'"
→ Consider: "Ask not whether the model is accurate. Ask where the rule layer sits relative to the model's decision." — saves 12 words, same meaning.

### 12. Final paragraph
"If those two positions are the same, you have a hope, not a system. If they are in the right order — rules first, model second — you have something you can actually test."
→ Keep as-is. Strong closer.

---

## FINAL VERSION (post-editor):

Policy as pre-filter is auditable. Policy as post-filter is theater.

There is a quiet architectural decision that determines whether an AI system in a high-stakes domain is trustworthy or merely convincing. Most deployments make the wrong one.

The wrong decision looks like this: retrieve relevant documents, run a model over them, then apply policy constraints as a post-processing step. The model generates a response. The response is checked against the relevant rules. If it passes, it goes out. If it fails, it gets flagged or regenerated.

This architecture is popular because it feels rigorous. You have both a model and a policy layer. What could go wrong?

A lot. The problem is that the model has already made its decision before the policy check happens. The post-filter is not a gate — it is a quality assurance step on something the model already committed to. The decision signal has already propagated through the output.

The failure mode of a post-filter is a false positive in the compliance check itself. The model produces an answer that sounds correct, is confidently stated, and violates the underlying constraint in a way the post-filter misses. You have a wrong answer that looks right. This is the dangerous kind of failure: an answer that is wrong but sounds confident.

A pre-filter architecture is structurally different. The constraint is applied before the model ever sees the problem space. The model only receives inputs that have already passed the rule layer. The decision about what is permitted and what is not has already been made, in code, with an auditable trace, before the generative model does any work.

This is the architecture behind DOMUS, the UK local government housing placement system. Statutory requirements — bedroom requirements, affordability thresholds, placement restrictions — are encoded into representations before the AI ever sees a housing option. The LLM is not deciding what is permissible. It is navigating a pre-filtered set of permissible options and presenting the most appropriate ones to a human officer.

The critical distinction is not "rule-based vs AI" — it is where the rule layer sits relative to the model. In DOMUS, the rule layer is upstream. In most enterprise RAG deployments, the rule layer is downstream.

The downstream position is not inherently wrong, but it makes the system dependent on the model to correctly apply constraints it has not been trained to understand. If the post-filter relies on the same LLM to check whether its own output complies with policy, the compliance check is only as reliable as the model — and models are not reliability mechanisms.

The downstream position also makes auditability harder. When something goes wrong in a pre-filter system, the question is: did the rule layer correctly encode the constraint? That question has a precise answer. When something goes wrong in a post-filter system, the question is: did the model correctly apply the policy in this specific context? That question does not have a reliable answer — it requires counterfactual reasoning about what the model would have done if it had handled the constraint differently.

There is a simple test for this: when the system fails, where do you look?

In a pre-filter architecture, you look at the rule layer. In a post-filter architecture, you look at the model's reasoning trace. One of these is a database. The other is a story.

Ask not whether the model is accurate. Ask where the rule layer sits relative to the model's decision.

If those two positions are the same, you have a hope, not a system. If they are in the right order — rules first, model second — you have something you can actually test.

The engineering is upstream of the generation.

---

## Summary
- Title: unchanged — strong
- Opened with DOMUS example in body (not intro) — good
- Tightened one closing question paragraph
- Strengthened one sentence in false-positive paragraph
- Word count: ~700 — within target range
- No filler, no hype, no "I"
- Final verdict: READY TO POST
