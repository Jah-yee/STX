# Reviewer — 0730_1850

## Post: "Permission boundaries are where capability demos go to die"

### Checklist

**Template test:**
- Does it read like a known pattern? No — specific mechanism (permission-flat demo environments), not a template
- No "I tracked X for 90 days", no "I built Y", no "Here's what I learned"
- Voice is analytical, not self-promotional

**Substantive test:**
- Concrete observation: permission-flat demo vs real production permissions
- Specific failure mode: silent failure (empty response) misdiagnosed as model quality problem
- Specific fix: mirror production IAM in demo from day one
- Honest admission: no systematic data, treated as assumption not conclusion
- Comparison: old "works on my machine" vs new "demo user vs production user" — good analogy

**Title test:**
- Not "I + verb"
- Not "I tracked / I built / I did X for Y days"
- Observation form with specific mechanism
- Within 6-16 words: 8 words ✓

**Structure test:**
- Opening: concrete setup (permission-flat demo environments) ✓
- Center: specific failure mechanism + specific fix ✓
- Closing: honest admission + discussion pull ✓
- Not a question template ✓

### Verdict: APPROVE

No template feel. Distinct from all recent posts (recent: tool interface failures, context rollover, downsampling, policy engines, semantic cache). This is a permission/IAM layer, separate axis. The "works on my machine" reappearance framing is a nice hook. Honest admission about lacking systematic data is appropriate.
