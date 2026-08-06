# Editor — Round 0726_0225

**Surgical changes only:**

1. **Opening sentence** — trim "last month" (makes it feel dated/anecdotal):
   - Before: "A pipeline processed a payment screenshot last month."
   - After: "A payment processing pipeline read a screenshot. The card number was 4532 2011 2833 01[artifact]6 — a space where no space should be, parsed as two tokens instead of sixteen digits."

2. **Nested extraction chains paragraph** — trim 2 sentences:
   - Before: "If a screenshot is processed by a vision model, whose output is then parsed by a code model, whose output is then sent to a tool — there are three boundaries where typed information becomes untyped information and then gets re-typed by a model that has no schema. The failure surface area is three times larger than it appears. Each boundary is individually reasonable. The composition is a trust cascade."
   - After: "If a screenshot is processed by a vision model, then a code model, then a tool — there are three boundaries where typed information becomes untyped and gets re-typed by a model with no schema. The composition is a trust cascade."

3. **Eval paragraph** — trim closing sentence (redundant with prior point):
   - Before: "These are different things."
   - After: [DELETE]

**Total: 3 surgical cuts. Final word count ~760 words.**
