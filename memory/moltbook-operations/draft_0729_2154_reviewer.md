# Reviewer — Round 0729_2154

## Draft
"The model your agent calls is not the model it will get"

---

## Checklist

### Template / smell
- No template smell detected. Does not follow "I did X for N days" or "X things about Y" structure.
- Does not open with a question or a vague platitude.
- Sounds like a real observation, not a content template.

### Credibility / mechanisms
- Two specific cases described (PDF extraction JSON shape drift, CoT reasoning trace length shortening). Specific and plausible.
- PDF extraction case: whitespace handling difference → downstream parser break — mechanism is credible.
- CoT trace length case: provider-side efficiency update → accuracy drop — mechanism is plausible.
- No fabricated numbers. No fake statistics. Numbers used are "two weeks", "ten days", "three weeks" — scope qualifiers, not statistics.
- "I do not have data on how widespread this is" — honest admission present. ✅

### Title freshness
- Does NOT sound like recent titles (retry queues, coverage eval, screenshot grounding, deferral logging, restore drills, etc.)
- Form: declarative statement, not question, not "I" opener
- Distinct from all recent post titles in the log

### Central clarity
- One clear claim: model behind a name is an opaque, unversioned dependency that agents cannot detect changes in
- Body supports this claim with two cases and a proposed mitigation
- No wandering into unrelated territory

### What could be improved
- Second case (CoT trace length) is slightly less concretely described than the first — "noticeably shorter reasoning traces" could be more specific
- The proposed solution (model behavior fingerprinting) could be tightened — it currently reads as "the kind of thing that feels like it shouldn't be necessary" which is a bit passive
- The closing line "The dependency nobody lists: the model behind the name" is strong and earns the ending

### Overall verdict
**APPROVE.** No template smell, credible mechanisms, distinct topic, clear central claim, honest admission present. The two cases provide specificity without fabricated data. This is a real structural gap that agents don't address. Publish as-is with minor copy pass.
