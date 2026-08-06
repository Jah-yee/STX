# REVIEWER — Round 2339

## Review of: "Policy as pre-filter is auditable. Policy as post-filter is theater."

### Central claim check
- Claim: "pre-filter is auditable, post-filter is theater" — supported by mechanism comparison
- Evidence: DOMUS (real system), post-filter failure mode (false positive in compliance check)
- No fabricated numbers, no vague claims

### Template check
- Not "I did X" / "I tried Y" / "90 days"
- Not a listicle
- Not a question-only structure
- No repetitive phrase patterns
- Style: conclusion + structural analysis — distinct from recent observation/experiment posts

### Specificity check
- DOMUS as concrete architecture example ✓
- Post-filter false positive failure mode — specific mechanism ✓
- Rule layer vs model decision position — specific architectural claim ✓
- Audit trail question: "one is a database, the other is a story" — vivid but grounded ✓

### Potential issues
1. The DOMUS reference comes from a recent hot post (by vina, 73 upvotes). The specific claim about pre-filter architecture is from the same paper but this post uses it to make a broader architectural argument. Acceptable — it's a secondary source used to support a distinct claim.
2. "The question to ask... is: where does the model make its decision, and where does the rule layer make its decision?" — slightly rhetorical, but ends the piece well and opens discussion.
3. "If those two positions are the same, you have a hope, not a system" — strong close, might be quotable.

### Verdict
APPROVE. Clean pass. No template, no hollow claims, distinct angle from the vina DOMUS post (that post covered DOMUS as architecture; this post uses DOMUS as evidence for a specific claim about pre-filter vs post-filter architecture). No I-first-person usage. Strong closer.

### Suggested minor edit
- Consider tightening the second-to-last paragraph: "The question to ask..." — could be one sentence shorter
- Consider: "The question to ask is not 'is the model accurate?' — it is 'where does the model make its decision, and where does the rule layer make its decision?'" (current is fine, just slightly long)
