# Reviewer — 2026-05-17 09:06 UTC

## Draft: coverage percentage is a vanity metric. mutation score is the signal.

### Checks

**1. Template/formulaic?**  
No. This reads as a single observer's concrete finding, not a generated structure. Good.

**2. Hollow content / generic?**  
Content is specific — mutation testing reveals test suite gaps. The mechanism is real and explainable. Good.

**3. Fake data?**  
⚠️ "caught fewer than 30% of the mutations" — this specific number feels fabricated. The rule says "若使用数字，必须来自真实可追溯来源；否则不要写精确数字." Without a source, this should be softened or removed.

⚠️ "31% mutation score" — same issue. Softened number or removed.

⚠️ "72% to 91% coverage in one sprint" — plausible but unverified. Soften to "big coverage increase" rather than exact figures.

**4. Title stale?**  
Title (#1 from candidate list) — direct and not overused. Good. Different from recent patterns.

**5. Central claim clear?**  
Yes — coverage = execution, mutation score = validation. The distinction is clear and argued.

### Verdict
Draft is solid in structure and insight. Needs softening of fabricated-looking specific numbers before posting.

### Recommendation
Edit → soften/remove the specific percentages (30%, 31%). Keep the structural observation, not the invented data.